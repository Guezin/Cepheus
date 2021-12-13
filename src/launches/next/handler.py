import json
import requests

from common.config import API_SPACEX

def handler(event, context):
    response = requests.get(f'{API_SPACEX}/v4/launches/next')

    if response.status_code != 200:
      raise Exception(f'Error - Status API SpaceX: {response.status_code}')

    next_launch_data = response.json()

    next_launch = {
      'name': next_launch_data['name'],
      'date_utc': next_launch_data['date_utc'],
      'date_local': next_launch_data['date_local'],
    }

    return {
        "statusCode": 200,
        "body": json.dumps(next_launch, ensure_ascii=False).encode('utf8'),
    }
