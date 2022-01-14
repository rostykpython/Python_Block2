from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:49046126w@localhost:5432/quotes_db')


def db_connect():
    """
    Creates database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine('postgresql+psycopg2://postgres:49046126w@localhost:5432/quotes_db')


def create_items_table(engine):
    """
    Create the Items table
    """
    Base.metadata.create_all(engine)


class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_author = Column(String, primary_key=True, unique=True)
    born = Column(String)
    description = Column(String)

    def __init__(self, name_author, born, description):
        self.name_author = name_author
        self.born = born
        self.description = description


class Quotes(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    author = Column(String)
    tags = Column(ARRAY(String))
    quote = Column(String)

    def __init__(self, author, tags, quote):
        self.author = author
        self.tags = tags
        self.quote = quote


Base.metadata.create_all(engine)