from sqlalchemy import create_engine, text
import os

def Run(engine):
    sqlFolder = 'Queries'
    for filename in os.listdir(sqlFolder):
        if filename.endswith('.sql'):
            file_path = os.path.join(sqlFolder, filename)
        
            with open(file_path, 'r') as file:
                sql_query = file.read()

        # Esegui la query
            with engine.connect() as connection:
                result = connection.execute(text(sql_query)).fetchall()

        # Stampa i risultati
            for row in result:
                print(row)


