import requests
import pandas as pd

url = 'https://www.balldontlie.io/api/v1/'
endpoint = 'teams'


def main_request(url, endpoint):
    response = requests.get(url + endpoint)
    return response.json()


def get_pages(response):
    return response['meta']['per_page']


def parse_json(response):
    teamlist = []
    for e in response['data']:
        char = {
            'id': e['id'],
            'full_name': e['full_name'],
            'name': e['name'],
            'abbreviation': e['abbreviation'],
            'city': e['city'],
            'conference': e['conference'],
            'division': e['division']
        }
        teamlist.append(char)
    return teamlist


data = main_request(url, endpoint)

df = pd.DataFrame(parse_json(data))

from sqlalchemy import create_engine
conn = create_engine('postgresql://pagustinamato_coderhouse:7kxDU66Urk@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database')
df.to_sql('teams_nba', conn, index=False, schema='pagustinamato_coderhouse', if_exists='replace')

