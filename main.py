import ExtractPokemon as Pokemon, TransformDataPokemon as Elaborate
from tabulate import tabulate

if __name__ == "__main__":
    #Extract Data and Insert it into a DataFrame
    pokemon_data = Pokemon.fetch_first_gen_pokemon()
    #Transoform the DataFrame so Elaborate It
    PokeData = Elaborate.GetCleanData(pokemon_data)
    #Load dataFrame into a DataBase SQLLite
    
    # print(tabulate(PokeData, headers='keys', tablefmt='grid')) per test