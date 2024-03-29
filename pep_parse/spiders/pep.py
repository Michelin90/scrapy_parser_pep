from typing import Iterator

import scrapy
from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response: HtmlResponse) -> Iterator[Request]:
        table_section = response.css('section[id^=numerical-index] tbody tr')
        for table_row in table_section:
            pep_link = table_row.css('a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response: HtmlResponse) -> Iterator[PepParseItem]:
        data = {
            'number': response.css('h1.page-title::text').get().split()[1],
            'name': response.css('h1.page-title::text').get().split(' – ')[1],
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)
