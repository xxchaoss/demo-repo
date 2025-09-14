import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = base_url + "pokemon/" + name
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return(pokemon_data)
    else:
        print(f"failed: {response.status_code}")

pokemon_name = input("Enter pokemon name: ")
pokemon_info = get_pokemon(pokemon_name)

if pokemon_info:
    print(f"Pokemon name: {pokemon_info['name']}")
    print(f"Pokemon ID: {pokemon_info['id']}")
    print(f"Pokemon height: {pokemon_info['height']}")
    print(f"Pokemon weight: {pokemon_info['weight']}")



