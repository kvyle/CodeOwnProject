import requests

def get_pokemon_info(pokemon_name):

# Construct the URL for the PokeAPI with the provided Pokemon name
  url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
# Send a GET request to the PokeAPI
  response = requests.get(url)
    
# Check if the request was successful
  if response.status_code == 200:
# Parse the response JSON
    pokemon_data = response.json()
        
# Extract the relevant information from the response
    name = pokemon_data['name']
    types = [type_data['type']['name'] for type_data in pokemon_data['types']]
    abilities = [ability_data['ability']['name'] for ability_data in pokemon_data['abilities']]
        
# Display the Pokemon information
    print("Name:", name)
    print("Types:", ', '.join(types))
    print("Abilities:", ', '.join(abilities))
  else:
# Display an error message if the request was not successful
    print("Error:", response.status_code)

# Ask the user for a Pokemon name
pokemon_name = input("Enter a Pokemon name: ")

# Call the function to retrieve and display Pokemon information
get_pokemon_info(pokemon_name)