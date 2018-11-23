# -*- coding: utf-8 -*-

import scrapy

# 生成器语法
# 带有yield 关键字的函数在python中称之为generator 生成器


class QuotesSpider(scrapy.Spider):
    name = "catchImg"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)