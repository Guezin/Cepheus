import json
import requests

from common.config import API_SPACEX

def handler(event, context):
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

    return {
        "statusCode": 200,
        "body": json.dumps(upcoming_launches, ensure_ascii=False).encode('utf8'),
    }
