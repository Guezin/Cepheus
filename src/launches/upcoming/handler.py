import requests
from http import HTTPStatus

from common.config import API_SPACEX
from common.handlerbase import Handler, Result

class UpcomingLaunches(Handler):
  def handler(self):
    response = requests.get(f'{API_SPACEX}/v4/launches/upcoming')

    if response.status_code != 200:
      raise Exception(f'Error - Status API SpaceX: {response.status_code}')

    upcoming_launches_data = response.json()

    upcoming_launches = [
      { 
        'name': launch['name'], 
        'date_utc': launch['date_utc'], 
        'date_local': launch['date_local']
      }
      for launch in upcoming_launches_data
    ]

    return Result(HTTPStatus.OK, upcoming_launches)

def handler(event, context):
  return UpcomingLaunches(event, context).run()
