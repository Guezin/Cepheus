import requests
from http import HTTPStatus

from common.config import API_SPACEX
from common.handlerbase import Handler, Result
from common.translator import translate_word

class LatestLaunch(Handler):
  def pre_process(self):
    pass

  def handler(self):
    response = requests.get(f'{API_SPACEX}/v4/launches/latest')

    if response.status_code != 200:
      raise Exception(f'Error - Status API(/launches/latest) SpaceX: {response.status_code}')

    latest_launch_data = response.json()
    
    rocket_id = latest_launch_data['rocket']
    rocket_data = requests.get(f'{API_SPACEX}/v4/rockets/{rocket_id}')

    if rocket_data.status_code != 200:
      raise Exception(f'Error - Status API(/rockets/{rocket_id}) SpaceX: {rocket_data.status_code}')

    rocket = rocket_data.json()

    failures = len(latest_launch_data['failures']) > 0 and [{ 'reason': translate_word(failure['reason']) } for failure in latest_launch_data['failures']] or []
    details = latest_launch_data.get('details')
    
    latest_launch = {
      'mission': latest_launch_data.get('name', ''),
      'success': latest_launch_data.get('success', ''),
      'failures': failures,
      'details': details is not None and translate_word(details) or None,
      'date_utc': latest_launch_data.get('date_utc', ''),
      'date_local': latest_launch_data.get('date_local', ''),
      'rocket': {
        'name': rocket.get('name', ''),
        'cost_per_launch': rocket.get('cost_per_launch', ''),
        'description': translate_word(rocket.get('description', '')),
      },
    }

    return Result(HTTPStatus.OK, latest_launch)

def handler(event, context):
    return LatestLaunch(event, context).run()
