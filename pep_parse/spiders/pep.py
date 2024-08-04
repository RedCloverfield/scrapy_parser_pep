import scrapy

from constants import PEP_URL
from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [PEP_URL, ]

    def parse(self, response):
        links = response.css('#numerical-index table tbody tr a[href^="pep"]')
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, title = ''.join(
            response.css('h1.page-title ::text').getall()
        ).split(' – ')
        data = {
            'number': number[4:],
            'name': title,
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)
