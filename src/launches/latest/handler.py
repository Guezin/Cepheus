import requests
from http import HTTPStatus

from common.config import API_SPACEX
from common.handlerbase import Handler, Result

class LatestLaunch(Handler):
  def pre_process(self):
    pass

  def handler(self):
    response = requests.get(f'{API_SPACEX}/v4/launches/latest')

    if response.status_code != 200:
      raise Exception(f'Error - Status API SpaceX: {response.status_code}')

    latest_launch_data = response.json()

    latest_launch = {
      'name': latest_launch_data['name'],
      'date_utc': latest_launch_data['date_utc'],
      'date_local': latest_launch_data['date_local'],
    }

    return Result(HTTPStatus.OK, latest_launch)

def handler(event, context):
    return LatestLaunch(event, context).run()
