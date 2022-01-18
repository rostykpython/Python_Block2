import datetime
from fastapi import FastAPI, Query, Path
from typing import Optional
from news_parsing import gathering_articles
from models import NewsApiModel, create_engine_db
from sqlalchemy.orm import sessionmaker


app = FastAPI()


def create_db_api():
    engine = create_engine_db()
    Session = sessionmaker(engine)
    return Session()


@app.get("/get-news/{source}")
def get_news(
        source: str = Path(None, description="Choose the source from which you want to get the info"),
        topic: str = Query(None),
        time: Optional[str] = Query(str(datetime.date.today()))):

    articles_data = []
    session = create_db_api()

    articles = session.query(NewsApiModel).filter(
        NewsApiModel.source == source,
        NewsApiModel.topic == topic,
        NewsApiModel.date_added >= time
    )

    for item in articles:
        article_data = {
            'topic': item.topic,
            'title': item.article_name,
            'url': item.url,
            'source': item.source
        }
        articles_data.append(article_data)

    return articles_data


@app.get("/add-news/{topic}")
async def add_news(topic: str):
    await gathering_articles([topic])
    return {
        'Data': 'successfully add'
    }
