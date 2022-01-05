import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re
from main import Base, DBSession, engine
from models import Product

Base.metadata.create_all(engine)
Base.metadata.bind = engine
db_session = DBSession()


async def get_all(links, session):
    tasks = []
    for link in links:
        task = asyncio.create_task(info(link, session))
        tasks.append(task)

    return await asyncio.gather(*tasks)


async def info(link, session):
    response = await session.get(link)
    text = await response.text()
    return text


async def main(links):
    async with aiohttp.ClientSession() as session:
        data = await get_all(links, session)
        return data


def parse_product(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    data = soup.find_all('span')
    product_name = soup.find('title').text.strip().split('—')[0]
    product_info = {
        'name': product_name.strip(),
    }
    for item in data:
        for pattern in ['жиры', 'белки', 'углеводы']:
            if re.search(pattern, item.text):
                feature, value = item.text.strip()[:-1].split('—')
                product_info[feature.strip()] = value.strip()
        if len(product_info) == 4:
            return product_info


def save_to_db(db_session, product):
    product_info = parse_product(product)
    db_session.add(Product(*product_info.values()))
    db_session.commit()


if __name__ == '__main__':
    urls = [
        'https://fitaudit.ru/food/114512',
        'https://fitaudit.ru/food/115520',
        'https://fitaudit.ru/food/114427',
        'https://fitaudit.ru/food/114885',
        'https://fitaudit.ru/food/114909'
    ]
    results = asyncio.get_event_loop().run_until_complete(main(urls))

    for result in results:
        save_to_db(db_session, result)
