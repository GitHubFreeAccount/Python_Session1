# -*- coding: utf-8 -*-

from scrapy import cmdline

cmdline.execute("scrapy crawl catchImg -o quotes.json".split())
# cmdline.execute("scrapy crawl Demo1 -o quotes-humor.json -a tag=humor".split())
