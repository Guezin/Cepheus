import requests
from http import HTTPStatus

from common.config import API_SPACEX_GRAPHQL
from common.handlerbase import Handler, Result
from common.translator import translate_word_if_exists
from common.queries import past_launches_query

class PastLaunches(Handler):
  def handler(self):
    response = requests.post(API_SPACEX_GRAPHQL, json={'query': past_launches_query})

    if response.status_code != 200:
      raise Exception(f'Error - Status API SpaceX: {response.status_code}')

    past_launches_data = response.json()['data']['launchesPast']

    past_launches = [
      { 
        'mission': launch.get('mission_name', ''),
        'success': launch.get('launch_success', False),
        'details': translate_word_if_exists(launch.get('details')),
        'date_utc': launch.get('launch_date_utc', ''),
        'rocket': {
          'name': launch.get('rocket', {}).get('rocket', {}).get('name', ''),
          'cost_per_launch': launch.get('rocket', {}).get('rocket', {}).get('cost_per_launch', ''),
          'description': translate_word_if_exists(launch.get('rocket', {}).get('rocket', {}).get('description', ''))
        }
      }
      for launch in past_launches_data
    ]

    return Result(HTTPStatus.OK, past_launches)


def handler(event, context):
  return PastLaunches(event, context).run()
