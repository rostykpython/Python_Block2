from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

w_engine = create_engine('postgresql+psycopg2://postgres:49046126w@localhost:5432/weather_db')
Session = sessionmaker(bind=w_engine)

Base = declarative_base()
