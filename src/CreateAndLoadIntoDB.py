import sqlite3
from sqlalchemy import create_engine
import RunQueries

def create_table(cursor, table_name, table_definition):
    """Crea una tabella nel database."""
    try:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({table_definition});")
        print(f"Tabella {table_name} creata con successo.")
    except sqlite3.Error as e:
        print(f"Errore nella creazione della tabella {table_name}: {e}")

def insert_data(engine, df_dict):
    """Inserisci i dati nei DataFrame forniti."""
    with engine.connect() as connection:
        for table_name, dataframe in df_dict.items():
            dataframe.to_sql(table_name, con=connection, if_exists='replace', index=False)
    print("Inserimento completato con successo.")

def CreateAndInsertDB(df_pokemon, df_types, df_abilities, df_pokemon_abilities, df_pokemon_types, df_types_damage):
    """Crea e popola il database."""
    try:
        # Connessione al database
        connection = sqlite3.connect('pokemon.db')
        cursor = connection.cursor()

        # Definizione delle tabelle
        tables = {
            'pokemon': """
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                height DECIMAL,
                weight DECIMAL,
                base_experience INTEGER
            """,
            'types': """
                type_id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_name TEXT NOT NULL
            """,
            'abilities': """
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ability_name TEXT NOT NULL,
                effect TEXT NOT NULL
            """,
            'pokemon_abilities_relations': """
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pokemon_id INTEGER NOT NULL,
                ability_id INTEGER NOT NULL,
                FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
                FOREIGN KEY (ability_id) REFERENCES abilities(id)
            """,
            'pokemon_types_relations': """
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pokemon_id INTEGER NOT NULL,
                type_id INTEGER NOT NULL,
                FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
                FOREIGN KEY (type_id) REFERENCES types(type_id)
            """,
            'types_damage_relations': """
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_id INTEGER NOT NULL,
                relation_type_id INTEGER NOT NULL,
                damage_relation TEXT NOT NULL,
                FOREIGN KEY (type_id) REFERENCES types(type_id),
                FOREIGN KEY (relation_type_id) REFERENCES types(type_id)
            """
        }

        # Creazione delle tabelle
        for table_name, table_definition in tables.items():
            create_table(cursor, table_name, table_definition)
        connection.commit()
        # Configura SQLAlchemy
        engine = create_engine('sqlite:///pokemon.db')
        df_dict = {
            'pokemon': df_pokemon,
            'types': df_types,
            'abilities': df_abilities,
            'pokemon_abilities_relations': df_pokemon_abilities,
            'pokemon_types_relations': df_pokemon_types,
            'types_damage_relations': df_types_damage
        }

        # Inserimento dei dati
        insert_data(engine, df_dict)

        cursor.execute("PRAGMA table_info(pokemon_types_relations);")
        print("Struttura della tabella pokemon_types_relations:", cursor.fetchall())
        # Commit delle modifiche
        connection.commit()

        # Esegui le query
       # RunQueries.Run(engine)

    except sqlite3.Error as e:
        print(f"Errore durante la gestione del database: {e}")
    finally:
        if connection:
            connection.close()
            print("Connessione al database chiusa.")
