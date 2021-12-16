import requests
from http import HTTPStatus

from common.config import API_SPACEX
from common.handlerbase import Handler, Result
from common.translator import translate_word_if_exists

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
    
    latest_launch = {
      'mission': latest_launch_data.get('name', ''),
      'success': latest_launch_data.get('success', ''),
      'details': translate_word_if_exists(latest_launch_data.get('details')),
      'date_utc': latest_launch_data.get('date_utc', ''),
      'rocket': {
        'name': rocket.get('name', ''),
        'cost_per_launch': rocket.get('cost_per_launch', ''),
        'description': translate_word_if_exists(rocket.get('description')),
      },
    }

    return Result(HTTPStatus.OK, latest_launch)

def handler(event, context):
    return LatestLaunch(event, context).run()
