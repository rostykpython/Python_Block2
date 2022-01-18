import asyncio
import aiohttp
import datetime
from models import NewsApiModel, create_engine_db, create_table
from sqlalchemy.orm import sessionmaker

engine = create_engine_db()
create_table(engine)
Session = sessionmaker(engine)
session_db = Session()


async def parse_first_news_api(session, news_topic):
    async with session.get(
        f"https://newsdata.io/api/1/news?apikey=pub_3708634089d2961206f438f82ea62034028a&q={news_topic}"
    ) as response:

        articles = await response.json()
        for article in articles["results"]:
            session_db.add(
                NewsApiModel(
                    topic=news_topic,
                    article_name=article["title"],
                    url=article["link"],
                    source="newsdata",
                    date_added=datetime.date.today(),
                )
            )
        session_db.commit()


async def parse_second_news_api(session, news_topic):
    async with session.get(
        f"https://newsapi.org/v2/everything?q={news_topic}&from={datetime.date.today()}&sortBy=popularity&apiKey=726cf17c455f48a9a794e0b0fbeae9c5"
    ) as response:

        articles = await response.json()
        for article in articles["articles"]:
            session_db.add(
                NewsApiModel(
                    topic=news_topic,
                    article_name=article["title"],
                    url=article["url"],
                    source="newsapi",
                    date_added=datetime.date.today(),
                )
            )
        session_db.commit()


async def gathering_articles(news_topic):

    tasks = []
    async with aiohttp.ClientSession() as session:
        for news in news_topic:
            task = asyncio.create_task(parse_first_news_api(session, news))
            task2 = asyncio.create_task(parse_second_news_api(session, news))
            tasks.append(task)
            tasks.append(task2)

        return await asyncio.gather(*tasks)


if __name__ == "__main__":
    news_topics = ["Ukraine", "computer", "Kiev"]

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    f = asyncio.run(gathering_articles(news_topics))
