import sqlite3
import pandas as pd

# Connessione a un database (se non esiste, verrà creato)
def CreateAndInsertDB(df_pokemon,df_types,df_abilities,df_pokemon_abilities,df_pokemon_types,df_types_damage):
    connection = sqlite3.connect('pokemon.db')
    print(connection.total_changes)
    if connection :
    # Creazione di una tabella
        cursor = connection.cursor()
    # Creazione di una pokemon
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            height DECIMAL,
            weight DECIMAL,
            base_experience INTEGER
        );
    ''')
    
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS types (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_name TEXT NOT NULL
        );
    ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS abilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ability_name TEXT NOT NULL,
            effect TEXT NOT NULL
        );
    ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokemon_abilities_relations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pokemon_id TEXT NOT NULL,
            ability_id TEXT NOT NULL,
            FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
            FOREIGN KEY (ability_id) REFERENCES abilities(id)
        );
    ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokemon_types_relations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pokemon_id TEXT NOT NULL,
            type_id TEXT NOT NULL,
            FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
            FOREIGN KEY (type_id) REFERENCES types(id)
        );
    ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS types_damage_relations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_id TEXT NOT NULL,
            relation_type_id TEXT NOT NULL,
            damage_relation ENUM('double_damage_to','double_damage_from'),
            FOREIGN KEY (relation_type_id) REFERENCES types(id),
            FOREIGN KEY (type_id) REFERENCES types(id)
        );
    ''')
    #inserimento in DB
        insert_from_dataframe(cursor, 'pokemon', df_pokemon)
        insert_from_dataframe(cursor, 'types', df_types)
        insert_from_dataframe(cursor, 'abilities', df_abilities)
        insert_from_dataframe(cursor, 'pokemon_abilities_relations', df_pokemon_abilities)
        insert_from_dataframe(cursor, 'pokemon_types_relations', df_pokemon_types)
        insert_from_dataframe(cursor, 'types_damage_relations', df_types_damage)

    # Commit delle modifiche
        connection.commit()

    # Chiusura della connessione
        connection.close()
    return connection


def insert_from_dataframe(cursor, table_name, dataframe):
    """
    Inserisce i dati da un DataFrame in una tabella SQLite.

    :param cursor: Oggetto del cursore SQLite.
    :param table_name: Nome della tabella in cui inserire i dati.
    :param dataframe: pandas.DataFrame con i dati da inserire.
    """
    columns = ", ".join(dataframe.columns)
    placeholders = ", ".join(["?"] * len(dataframe.columns))
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    
    # Convertiamo il DataFrame in una lista di tuple
    data = dataframe.to_records(index=False)
    cursor.executemany(sql, data)
