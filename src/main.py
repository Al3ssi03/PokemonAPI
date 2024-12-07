import ExtractPokemon as Pokemon, TransformDataPokemon as Elaborate
import CreateAndLoadIntoDB

if __name__ == "__main__":
    #Extract Data and Insert it into a DataFrame
    pokemon_data = Pokemon.fetch_first_gen_pokemon()
    #Transoform the DataFrame so Elaborate It
    PokeData = Elaborate.GetCleanData(pokemon_data)
    
    df_pokemon = PokeData[['pokemon_id', 'name', 'height', 'weight', 'base_experience']]
    df_pokemon.columns = ['id', 'name', 'height', 'weight', 'base_experience']
    
    df_types = PokeData[['type_id', 'type_name']]
    df_types.columns = ['id', 'type_name']
    
    df_abilities = PokeData[['ability_id', 'ability_name', 'effect']]
    df_abilities.columns = ['id', 'ability_name', 'effect']

    df_pokemon_types = PokeData[['pokemon_id', 'type_id']]
    df_pokemon_types.columns = ['pokemon_id', 'type_id']

    df_pokemon_abilities = PokeData[['pokemon_id', 'ability_id']]
    df_pokemon_abilities.columns = ['pokemon_id', 'ability_id']

    df_types_damage = pokemon_data[['type_id', 'relation_type_id', 'damage_relation']]
    df_types_damage.columns = ['type_id', 'relation_type_id', 'damage_relation']
    CreateAndLoadIntoDB.Run

    #Load dataFrame into a DataBase SQLLite
    