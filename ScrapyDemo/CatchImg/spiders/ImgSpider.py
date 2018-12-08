# -*- coding: utf-8 -*-

import scrapy


# 生成器语法
# 带有yield 关键字的函数在python中称之为generator 生成器


class QuotesSpider(scrapy.Spider):
    name = "catchImg"
<<<<<<< HEAD

    allowed_domains = ['quantuwang.com']

    start_url = 'http://www.quantuwang.com'

    def start_requests(self):

        tag = getattr(self, 'tag', None)
        if (tag is not None):
            url = self.start_url + "/" + tag

        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # 判断是不是子页面的resposne，获取子页面的资源
        if response.css('div.c_img') is not None:
            for quote in response.css('div.c_img'):
                yield {
                    'liname': quote.css('img::attr(alt)').extract_first().encode('utf-8').rsplit()[-1],
                    'imgurl': quote.css('img::attr(src)').extract_first(),
                }

        sub_page = self.start_url + response.css('div.box div  li a::attr("href")').extract_first()
        print sub_page
        if sub_page is not None:
            yield response.follow(sub_page, self.parse)
=======
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
>>>>>>> bd686529204361622897c9003e5d0aeef4d5bac9
