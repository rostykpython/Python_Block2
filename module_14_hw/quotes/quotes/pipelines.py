# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from .models import db_connect, Quotes, Authors


class QuotesPipeline:

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        engine = db_connect()
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item).asdict()
        session = self.Session()

        if 'keywords' in adapter.keys():
            tags = adapter['keywords']
            author = adapter['author']
            quote = adapter['quote']
            print('Check data')
            print(tags)
            print(author)
            print(quote)
            session.add(
                    Quotes(
                        author=author[0],
                        tags=tags,
                        quote=quote
                    )
                )

        elif 'born' in adapter.keys():
            print(adapter['name'])
            print(adapter['born'])

            session.add(
                Authors(
                    name_author=adapter['name'],
                    born=adapter['born'],
                    description=adapter['description']
                )
            )
        session.commit()
        session.close()
        return item
