import scrapy
from ..items import QuotesItem


class QuotesHwSpider(scrapy.Spider):
    name = 'quotes_hw'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response, **kwargs):
        data_quote = QuotesItem()
        for quote in response.xpath("/html//div[@class='quote']"):
            find_quote = quote.xpath("span[@class='text']/text()").get()
            data_quote['author'] = quote.xpath("span/small/text()").extract()
            data_quote['tags'] = quote.xpath("div[@class='tags']/a/text()").extract()
            data_quote['quote'] = find_quote.replace('”', '').replace('“', '').strip()
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)
        return data_quote
