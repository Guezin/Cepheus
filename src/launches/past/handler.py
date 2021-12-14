import requests
from http import HTTPStatus

from common.config import API_SPACEX
from common.handlerbase import Handler, Result
from common.translator import translate_word

class PastLaunches(Handler):
  def handler(self):
    response = requests.get(f'{API_SPACEX}/v4/launches/past')

    if response.status_code != 200:
      raise Exception(f'Error - Status API SpaceX: {response.status_code}')

    past_launches_data = response.json()
    
    past_launches = [
      { 
        'mission': launch.get('name'),
        'success': launch.get('success'),
        'failures': launch.get('failures'),
        'details': launch.get('details'),
        'date_utc': launch.get('date_utc'),
        'date_local': launch.get('date_local'),
        'rocket_id': launch.get('rocket')
      }
      for launch in past_launches_data
    ]

    return Result(HTTPStatus.OK, past_launches)


def handler(event, context):
  return PastLaunches(event, context).run()
