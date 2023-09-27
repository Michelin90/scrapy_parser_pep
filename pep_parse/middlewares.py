from __future__ import annotations

from typing import Iterator

from scrapy import Spider, crawler, exceptions, signals
from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse


class PepParseSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: crawler) -> PepParseSpiderMiddleware:
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(
        self,
        response: HtmlResponse,
        spider: Spider
    ) -> None:
        return None

    def process_spider_output(
        self,
        response: HtmlResponse,
        result: Request,
        spider: Spider
    ) -> Iterator:
        for i in result:
            yield i

    def process_spider_exception(
        self,
        response: HtmlResponse, exception: exceptions, spider: Spider
    ) -> None:
        pass

    def process_start_requests(
        self,
        start_requests: Request,
        spider: Spider
    ) -> Iterator:
        for r in start_requests:
            yield r

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: crawler) -> PepParseDownloaderMiddleware:
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(
        self,
        request: Request,
        spider: Spider
    ) -> None:
        return None

    def process_response(
        self,
        request: Request,
        response: HtmlResponse,
        spider: Spider
    ) -> HtmlResponse:
        return response

    def process_exception(
        self,
        request: Request,
        exception: exceptions,
        spider: Spider
    ) -> None:
        pass

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)
