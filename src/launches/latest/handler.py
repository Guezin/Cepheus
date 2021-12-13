import json
import requests

from common import config

def handler(event, context):
    response = requests.get(f'https://api.spacexdata.com/v4/launches/latest')

    if response.status_code is not 200:
      raise Exception(f'Error - Status API SpaceX: {response.status_code}')

    latest_launch_data = response.json()

    latest_launch = {
      'name': latest_launch_data['name'],
      'date_utc': latest_launch_data['date_utc'],
      'date_local': latest_launch_data['date_local'],
    }

    return {
        "statusCode": 200,
        "body": json.dumps(latest_launch, ensure_ascii=False).encode('utf8'),
    }
