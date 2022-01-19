from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_engine = 'postgresql+psycopg2://postgres:49046126w@localhost:5432//weather_db'
Session = sessionmaker(bind=db_engine)
Base = declarative_base()
