from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


database_url = 'postgresql+psycopg2://postgres:49046126w@localhost:5432/aiohttp_task'


engine = create_engine(database_url)
DBSession = sessionmaker(bind=engine)
Base = declarative_base()
