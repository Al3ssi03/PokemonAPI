import ExtractPokemon as Pokemon
import TransformDataPokemon as Elaborate
import CreateAndLoadIntoDB
import RunQueries
import pandas as pd

def process_damage_relations(pokemon_data):
    """Elabora le relazioni di danno dai dati dei Pokémon."""
    damage_relations = []
    for pokemon in pokemon_data:
        if 'type_details' in pokemon:
            for type_info in pokemon['type_details']:
                type_name = type_info.get('type_name')

                for damage_to in type_info.get('double_damage_to', []):
                    damage_relations.append({
                        'type_id': type_name,
                        'relation_type_id': damage_to,
                        'damage_relation': 'double_damage_to'
                    })

                for damage_from in type_info.get('double_damage_from', []):
                    damage_relations.append({
                        'type_id': type_name,
                        'relation_type_id': damage_from,
                        'damage_relation': 'double_damage_from'
                    })
    return pd.DataFrame(damage_relations)

def expand_relations(df, id_col, list_col):
    """Espandi colonne con liste in righe separate."""
    expanded_rows = [
        {id_col: row[id_col], list_col: related_id}
        for _, row in df.iterrows()
        for related_id in row[list_col]
    ]
    return pd.DataFrame(expanded_rows)

def process_dataframes(pokemon_data, PokeData):
    """Crea e trasforma tutti i DataFrame necessari."""
    # Pokémon
    df_pokemon = PokeData[['id', 'name', 'height', 'weight', 'base_experience']]
    df_pokemon.columns = ['id', 'name', 'height', 'weight', 'base_experience']
    df_pokemon = Elaborate.CleanDF(df_pokemon)

    # Tipi
    types_expanded = PokeData[['id', 'type_details']].explode('type_details')
    types_expanded['type_name'] = types_expanded['type_details'].apply(
        lambda x: x.get('type_name') if isinstance(x, dict) else None
    )

    # Mantieni solo le colonne necessarie e rimuovi duplicati
    df_types = types_expanded[['id', 'type_name']].dropna(subset=['type_name']).drop_duplicates()

    # Rinomina le colonne
    df_types.columns = ['type_id', 'type_name']
    df_types = Elaborate.CleanDF(df_types)

    # Abilità
    abilities_expanded = PokeData[['id', 'ability_details']].explode('ability_details')
    abilities_expanded['ability_name'] = abilities_expanded['ability_details'].apply(
        lambda x: x.get('ability_name') if isinstance(x, dict) else None
    )
    abilities_expanded['effect'] = abilities_expanded['ability_details'].apply(
        lambda x: x.get('effect') if isinstance(x, dict) else None
    )

    # Rimuovi la colonna 'ability_details' per evitare problemi con i dizionari
    abilities_expanded = abilities_expanded.drop(columns=['ability_details'], errors='ignore')

    # Rimuovi eventuali righe con valori nulli e duplicati
    df_abilities = abilities_expanded.dropna(subset=['ability_name', 'effect']).drop_duplicates()

    # Rinomina le colonne
    df_abilities.columns = ['ability_id', 'ability_name', 'effect']


    # Relazioni Pokémon-Tipi
    df_pokemon_types = PokeData[['id', 'type_id']].rename(columns={'id': 'pokemon_id'})
    df_pokemon_types = Elaborate.CleanDF(expand_relations(df_pokemon_types, 'pokemon_id', 'type_id'))

    # Aggiungi la colonna 'id' autoincrementale
    df_pokemon_types.insert(0, 'id', range(1, len(df_pokemon_types) + 1))

    # Relazioni Pokémon-Abilità
    df_pokemon_abilities = PokeData[['id', 'ability_id']].rename(columns={'id': 'pokemon_id'})
    df_pokemon_abilities = Elaborate.CleanDF(expand_relations(df_pokemon_abilities, 'pokemon_id', 'ability_id'))

    # Aggiungi la colonna 'id' autoincrementale
    df_pokemon_abilities.insert(0, 'id', range(1, len(df_pokemon_abilities) + 1))

    # Relazioni di Danno
    df_types_damage = process_damage_relations(pokemon_data)
    df_types_damage.columns = ['type_id', 'relation_type_id', 'damage_relation']
    df_types_damage = Elaborate.CleanDF(df_types_damage)

    return df_pokemon, df_types, df_abilities, df_pokemon_types, df_pokemon_abilities, df_types_damage

if __name__ == "__main__":
    # Estrai i dati dei Pokémon
    pokemon_data = Pokemon.fetch_first_gen_pokemon()
    PokeData = Elaborate.GetCleanData(pokemon_data)

    # Crea i DataFrame
    df_pokemon, df_types, df_abilities, df_pokemon_types, df_pokemon_abilities, df_types_damage = process_dataframes(pokemon_data, PokeData)

    # Inserisci i dati nel database
    if CreateAndLoadIntoDB.CreateAndInsertDB(df_pokemon, df_types, df_abilities, df_pokemon_abilities, df_pokemon_types, df_types_damage):
        print("Operazione completata con successo!")