# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field()
    车次 = scrapy.Field()
    始发站 = scrapy.Field()
    终点站 = scrapy.Field()
    开车时间 = scrapy.Field()
    到站时间 = scrapy.Field()
    全程_时间 = scrapy.Field()
    pass
