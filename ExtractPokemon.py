import requests
import json

BASE_URL = 'https://pokeapi.co/api/v2'

def fetch_pokemon(pokemon_id):
    url = f"{BASE_URL}/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "id": pokemon_id,
            "name": data['name'],
            "height": data['height'],
            "weight": data['weight'],
            "base_experience": data['base_experience'],
            "types": [t['type']['name'] for t in data['types']],
            "abilities": [a['ability']['name'] for a in data['abilities']],
        }
    else:
        print(f"Errore per Pokémon ID {pokemon_id}: {response.status_code}")
        return None
    

def fetch_type_info(type_name):
    url = f"{BASE_URL}/type/{type_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "type_name": type_name,
            "double_damage_to": [relation['name'] for relation in data['damage_relations']['double_damage_to']],
            "double_damage_from": [relation['name'] for relation in data['damage_relations']['double_damage_from']],
        }
    else:
        print(f"Errore per Tipo {type_name}: {response.status_code}")
        return None
    
def fetch_ability_info(ability_name):
    url = f"{BASE_URL}/ability/{ability_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "ability_name": ability_name,
            "effect": data['effect_entries'][0]['effect'] if data['effect_entries'] else "No description available",
        }
    else:
        print(f"Errore per Abilità {ability_name}: {response.status_code}")
        return None



def fetch_first_gen_pokemon():
    all_pokemon = []
    for pokemon_id in range(1, 151):  # Prima generazione 151
        pokemon = fetch_pokemon(pokemon_id)
        if pokemon:
            # Ottieni informazioni aggiuntive sui tipi e abilità richiamando gli altri endpoints
            pokemon['type_details'] = [fetch_type_info(t) for t in pokemon['types']]
            pokemon['ability_details'] = [fetch_ability_info(a) for a in pokemon['abilities']]
            all_pokemon.append(pokemon)
    return all_pokemon



