# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    更新时间 = scrapy.Field()
    # {
    #     "id": "e7a1a3c0-8f6a-422f-b6c5-d75876043a1d",
    #     "airline": "AY", "flight_number": "AY1332",
    #     "scheduled_departure_date": "07.12.2020",
    #     "scheduled_departure_time": "10:20",
    #     "origin_name": "London Heathrow Apt",
    #     "destination_name": "Helsinki-Vantaa",
    #     "departure_time": "10:22 (Departed)",
    #     "arrival_time": "15:01 (Landed)",
    #     "serviceType": "J",
    #     "status": "ARR",
    #     "registration": "OHLVI"
    # }
    航线 = scrapy.Field()
    航班号 = scrapy.Field()
    预定出发日期 = scrapy.Field()
    预定出发时间 = scrapy.Field()
    起点 = scrapy.Field()
    终点 = scrapy.Field()
    出发时间 = scrapy.Field()
    到达时间 = scrapy.Field()
    服务类型 = scrapy.Field()
    状态 = scrapy.Field()
    注册号 = scrapy.Field()
    pass
