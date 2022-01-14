# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    quote = scrapy.Field()


class AuthorsItem(scrapy.Item):
    name = scrapy.Field()
    born = scrapy.Field()
    description = scrapy.Field()
