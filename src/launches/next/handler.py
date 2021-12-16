import requests
from http import HTTPStatus

from common.config import API_SPACEX
from common.handlerbase import Handler, Result
from common.translator import translate_word_if_exists

class NextLaunch(Handler):
  def handler(self):
    response = requests.get(f'{API_SPACEX}/v4/launches/next')

    if response.status_code != 200:
      raise Exception(f'Error - Status API(/launches/next) SpaceX: {response.status_code}')

    next_launch_data = response.json()

    rocket_id = next_launch_data['rocket']
    rocket_data = requests.get(f'{API_SPACEX}/v4/rockets/{rocket_id}')

    if rocket_data.status_code != 200:
      raise Exception(f'Error - Status API(/rockets/{rocket_id}) SpaceX: {rocket_data.status_code}')

    rocket = rocket_data.json()

    next_launch = {
      'mission': next_launch_data.get('name', ''),
      'details': translate_word_if_exists(next_launch_data.get('details')),
      'date_utc': next_launch_data.get('date_utc', ''),
      'rocket': {
        'name': rocket.get('name', ''),
        'cost_per_launch': rocket.get('cost_per_launch', ''),
        'description': translate_word_if_exists(rocket.get('description'))
      }
    }

    return Result(HTTPStatus.OK, next_launch)

def handler(event, context):
  return NextLaunch(event, context).run()
