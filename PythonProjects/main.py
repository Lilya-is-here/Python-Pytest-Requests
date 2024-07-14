import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8caf9dc769408d81d490da6b2e57726b'
HEADER = {'Content-Type':'application/json', 
          'trainer_token': TOKEN}

body_create_pokemon = {
    "name": "By_request",
    "photo_id": 1
}

body_change_name = {
    "pokemon_id": "43329",
    "name": "New Name",
    "photo_id": 1
}

body_catch_in_pokeball = {
    "pokemon_id": "43329"
}

''' response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create_pokemon)
print(response.text) '''

''' response = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change_name)
print(response.text) '''

response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_catch_in_pokeball)
print(response.text)
