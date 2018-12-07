# -*- coding: utf-8 -*-

import scrapy

# 生成器语法
# 带有yield 关键字的函数在python中称之为generator 生成器


class QuotesSpider(scrapy.Spider):
    name = "catchImg"
    start_urls = [
        'https://mp.weixin.qq.com/s/Gw5g1RXoUvjVU7aSeLsNsQ',
    ]

    def parse(self, response):
        for img in response.css('img'):
            yield {
                'src': img.css('img::attr(src)').extract_first(),
            }

        # next_page = response.css('li.next a::attr("href")').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)