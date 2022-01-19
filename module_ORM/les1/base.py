from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine_address_book = create_engine('postgresql+psycopg2://postgres:49046126w@localhost:5432/address_book')
Session_address_book = sessionmaker(bind=engine_address_book)

engine_note_book = create_engine('postgresql+psycopg2://postgres:49046126w@localhost:5432/note_book')
Session_note_book = sessionmaker(bind=engine_note_book)

Base = declarative_base()

print('Connected to source database')
