import requests
import pandas as pd

# Função para pegar todos os pokémons
def get_all_pokemons():
    pokemons = []
    url = "https://pokeapi.co/api/v2/pokemon"
    
    while url:
        response = requests.get(url)
        data = response.json()
        pokemons.extend([{"id": pokemon["url"].split("/")[-2], "name": pokemon["name"]} for pokemon in data["results"]])
        
        # Verifica se há uma próxima página de resultados
        url = data.get("next")
    
    return pokemons

# Recolher todos os Pokémon
pokemons = get_all_pokemons()

# Criar DataFrame com os dados
df_bronze = pd.DataFrame(pokemons)

# Salvar como arquivo CSV para representar a camada Bronze
df_bronze.to_csv('bronze_pokemon_data.csv', index=False)

print(f"{len(df_bronze)} Pokémons foram salvos no arquivo CSV.")
