import requests
from http import HTTPStatus

from common.config import API_SPACEX
from common.handlerbase import Handler, Result

class NextLaunch(Handler):
  def handler(self):
    response = requests.get(f'{API_SPACEX}/v4/launches/next')

    if response.status_code != 200:
      raise Exception(f'Error - Status API SpaceX: {response.status_code}')

    next_launch_data = response.json()

    next_launch = {
      'name': next_launch_data['name'],
      'date_utc': next_launch_data['date_utc'],
      'date_local': next_launch_data['date_local'],
    }

    return Result(HTTPStatus.OK, next_launch)

def handler(event, context):
  return NextLaunch(event, context).run()
