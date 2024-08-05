import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for link in response.css(
            '#numerical-index table tbody tr a[href^="pep"]'
        ):
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, title = ''.join(
            response.css('h1.page-title ::text').getall()
        ).split(' – ')
        yield PepParseItem(
            number=number[4:],
            name=title,
            status=response.css('dt:contains("Status") + dd abbr::text').get()
            )
