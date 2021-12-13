import json
import requests

def handler(event, context):
    response = requests.get('https://api.spacexdata.com/v4/launches/past')

    if response.status_code != 200:
      raise Exception(f'Error - Status API SpaceX: {response.status_code}')

    past_launches_data = response.json()

    past_launches = [
      { 
        'name': launch['name'], 
        'date_utc': launch['date_utc'], 
        'date_local': launch['date_local']
      }
      for launch in past_launches_data
    ]

    return {
        "statusCode": 200,
        "body": json.dumps(past_launches, ensure_ascii=False).encode('utf8'),
    }
