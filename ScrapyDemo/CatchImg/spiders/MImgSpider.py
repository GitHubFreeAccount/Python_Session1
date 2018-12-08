# -*- coding utf-8 -*-


import scrapy



class MImgSpider(scrapy.Spider):
    name = 'MImg'
    allowed_domains = ['mmjpg.com']
    start_url = "http://www.mmjpg.com/"

    urls=[]


    def start_requests(self):
        url = self.start_url;
        tag = getattr(self, 'tag', None)
        if (tag is not None):
            url = "/" + tag

        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        arraytags = response.css('a[target="_blank"]')
        print  len(arraytags)
        for quotes in arraytags:
            if len(quotes.css('img')) > 0:
                self.urls.append(quotes.css('a::attr(href)').extract_first())
                yield {
                    'urltitle': quotes.css('img::attr(alt)').extract_first(),
                    'url': quotes.css('a::attr(href)').extract_first(),
                }


        for item_url in self.urls:
            if item_url is not None:
                yield scrapy.Request(item_url, self.parse)
