import sqlite3

# Connessione a un database (se non esiste, verrà creato)
connection = sqlite3.connect('pokemon.db')
print(connection.total_changes)
if connection :
    
    #TODO -INSERIRE PARTE DI INSERIMENTO IN TABELLA
    # Creazione di una tabella
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            height INTEGER,
            weight INTEGER,
            types TEXT
        );
    ''')

    # Inserimento di un esempio
    cursor.execute('''
        INSERT INTO pokemon (name, height, weight, types)
        VALUES ('Pikachu', 4, 60, 'Electric');
    ''')






# Salva le modifiche e chiudi la connessione
connection.commit()
connection.close()




def insert_data_to_db(pokemon_table, type_table, pokemon_types_table, ability_table, pokemon_abilities_table):
    conn = sqlite3.connect("pokemon.db")
    cursor = conn.cursor()

    # Inserisci Pokémon
    cursor.executemany("""
    INSERT INTO pokemon (id, name, height, weight, base_experience)
    VALUES (?, ?, ?, ?, ?)
    """, pokemon_table)

    # Inserisci tipi
    cursor.executemany("""
    INSERT INTO types (id, type_name)
    VALUES (?, ?)
    """, [(id, name) for name, id in type_table.items()])

    # Inserisci relazioni Pokémon-Tipi
    cursor.executemany("""
    INSERT INTO pokemon_types (pokemon_id, type_id)
    VALUES (?, ?)
    """, pokemon_types_table)

    # Inserisci abilità
    cursor.executemany("""
    INSERT INTO abilities (id, ability_name)
    VALUES (?, ?)
    """, [(id, name) for name, id in ability_table.items()])

    # Inserisci relazioni Pokémon-Abilità
    cursor.executemany("""
    INSERT INTO pokemon_abilities (pokemon_id, ability_id)
    VALUES (?, ?)
    """, pokemon_abilities_table)

    conn.commit()
