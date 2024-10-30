import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd6ae0d847c76575fa798cf548a375e71'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "PikaPika",
    "photo_id": 678
}


response_create = requests.post(url = f'{URL}/pokemons', headers= HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_change = {
    "pokemon_id": pokemon_id,
    "name": "Pikaashu",
    "photo_id": 678
}

response_change = requests.put(url = f'{URL}/pokemons', headers= HEADER, json = body_change)
print(response_create.text)

message = response_change.json()['message']
print(message)

body_add = {
    "pokemon_id": pokemon_id
}

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_add)
print(response_create.text)

message = response_add.json()['message']
print(message)