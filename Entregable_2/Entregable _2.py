import requests
import pandas as pd

url = 'https://www.balldontlie.io/api/v1/'
endpoint = 'games'


def main_request(url, endpoint):
    response = requests.get(url + endpoint)
    return response.json()


def get_pages(response):
    return response['meta']['per_page']


def parse_json_games(response):
    gameslist = []
    for e in response['data']:
        char = {
            'id': e['id'],
            'date': e['date'],
            'home_team_score': e['home_team_score'],
            'visitor_team_score': e['visitor_team_score'],
            'season': e['season'],
            'period': e['period'],
            'status': e['status'],
            'home_team_id': e['home_team']['id'],
            'visitor_team_id': e['visitor_team']['id']
        }
        gameslist.append(char)
    return gameslist


def parse_json_home_team(response):
    home_team_list = []
    for e in response['data']:
        char = {
            'id': e['home_team']['id'],
            'abbreviation': e['home_team']['abbreviation'],
            'city': e['home_team']['city'],
            'conference': e['home_team']['conference'],
            'division': e['home_team']['division'],
            'full_name': e['home_team']['full_name'],
            'name': e['home_team']['name']
        }
        home_team_list.append(char)
    return home_team_list


def parse_json_visitor_team(response):
    visitor_team_list = []
    for e in response['data']:
        char = {
            'id': e['visitor_team']['id'],
            'abbreviation': e['visitor_team']['abbreviation'],
            'city': e['visitor_team']['city'],
            'conference': e['visitor_team']['conference'],
            'division': e['visitor_team']['division'],
            'full_name': e['visitor_team']['full_name'],
            'name': e['visitor_team']['name']
        }
        visitor_team_list.append(char)
    return visitor_team_list


data = main_request(url, endpoint)

df_games = pd.DataFrame(parse_json_games(data))

df_home_team = pd.DataFrame(parse_json_home_team(data))

df_visitor_team = pd.DataFrame(parse_json_visitor_team(data))

from sqlalchemy import create_engine

conn = create_engine(
    'postgresql://pagustinamato_coderhouse:7kxDU66Urk@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database')
df_games.to_sql('games_nba', conn, index=False, schema='pagustinamato_coderhouse', if_exists='replace', method=None)
df_home_team.to_sql('home_teams_nba', conn, index=False, schema='pagustinamato_coderhouse', if_exists='replace', method=None)
df_visitor_team.to_sql('visitors_teams_nba', conn, index=False, schema='pagustinamato_coderhouse', if_exists='replace', method=None)
