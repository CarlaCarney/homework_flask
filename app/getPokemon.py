import requests as r

def getPokemon(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}'
    response = r.get(url)
    if not response.ok:
        raise Exception("Error. Please enter a valid Pokemon name.")

    data = response.json()
    pokedex = {}
    pokedex = {
            'name': data['name'],
            'type': data['types'][0]['type']['name'],
            'exp': data['base_experience'],
            'img': data['sprites']['front_shiny'],
            'abilities': data['abilities'][0]['ability'],
            'stats': {i['stat']['name']: i['base_stat'] for i in data['stats']}
        }
    return pokedex
