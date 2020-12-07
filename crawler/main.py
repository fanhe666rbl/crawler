from scrapy.cmdline import execute

execute(["scrapy", "crawl", "example", "-o", "items.json"])