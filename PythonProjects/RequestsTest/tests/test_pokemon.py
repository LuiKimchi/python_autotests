import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd6ae0d847c76575fa798cf548a375e71'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '7173'
def test_status_code():
    response = requests.get(url=f'{URL}/pokemons',params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response ():
        response_get = requests.get(url=f'{URL}/pokemons',params = {'trainer_id':TRAINER_ID})
        assert response_get.json()['data'][0]['name'] == 'Pikaashu'