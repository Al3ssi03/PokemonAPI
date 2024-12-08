from sqlalchemy import create_engine
import RunQueries

engine = create_engine('sqlite:///pokemon.db')

RunQueries.Run(engine)