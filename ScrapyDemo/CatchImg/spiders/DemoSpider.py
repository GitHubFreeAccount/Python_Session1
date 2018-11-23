# -*- coding: utf-8 -*-
import scrapy

'''
启动爬虫命令是添加参数，本势力主要测试，在spider中如何使用argument 参数
'''


class DemoSpider(scrapy.Spider):
    name = "Demo1"

    def start_requests(self):
        url = "http://quotes.toscrape.com/"
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            # 字典 相当于map数据
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
