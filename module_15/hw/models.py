import datetime
from sqlalchemy import Column, String, Date, Integer, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.engine import create_engine

Base = declarative_base()


class NewsApiModel(Base):
    __tablename__ = 'news_api_data'

    id = Column(Integer, primary_key=True)
    topic = Column(String)
    article_name = Column(String)
    url = Column(String)
    source = Column(String)
    date_added = Column(Date, default=datetime.date.today())

    def __init__(self, topic, article_name, url, source, date_added):
        self.topic = topic
        self.article_name = article_name
        self.url = url
        self.source = source
        self.date_added = date_added


def create_table(engine):
    Base.metadata.create_all(engine)


def create_engine_db():
    return create_engine('postgresql+psycopg2://postgres:49046126w@localhost:5432/news_api_db')
