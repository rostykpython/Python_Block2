import scrapy
from ..items import AuthorsItem


class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response, **kwargs):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()
        author = AuthorsItem()
        author['name'] = extract_with_css('h3.author-title::text')
        author['born'] = extract_with_css('.author-born-date::text')
        author['description'] = extract_with_css('.author-description::text')
        # yield {
        #     'name': extract_with_css('h3.author-title::text'),
        #     'birthdate': extract_with_css('.author-born-date::text'),
        #     'bio': extract_with_css('.author-description::text'),
        # }
        return author
