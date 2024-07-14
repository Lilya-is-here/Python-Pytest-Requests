import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8caf9dc769408d81d490da6b2e57726b'
HEADER = {'Content-Type':'application/json', 
          'trainer_token': TOKEN}
TRAINER_ID = '5344'


def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response.status_code == 200


def test_part_of_response():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response.json()['data'][0]['trainer_name'] =='NewLily'  
