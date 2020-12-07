import scrapy
import os

from scrapy import Request

from crawler.items import ExampleItem
# from selenium import webdriver
import json


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.finnair.com']
    start_urls = ['https://api.finnair.com/c/flightapp/flight-core-proxy/flightlist', ]
    # https://www.finnair.com/cn/cn/information-services/flights/flightslist
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'X-API-Key': 'Dg4baijHYq9BLH7YR40Ki9CymRXRLAbBVT7exvzb'
    }

    def start_requests(self):
        return [Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)]

    def parse(self, response):

        # print(response.text)
        data = json.loads(response.body_as_unicode())
        # print(data['last_updated'])
        # print(data['flights'][0]['airline'])
        items = []
        # {
        #     "id": "e7a1a3c0-8f6a-422f-b6c5-d75876043a1d",
        #     "airline": "AY",
        #     "flight_number": "AY1332",
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
        # 航线 = scrapy.Field()
        # 航班号 = scrapy.Field()
        # 预定出发日期 = scrapy.Field()
        # 预定出发时间 = scrapy.Field()
        # 起点 = scrapy.Field()
        # 终点 = scrapy.Field()
        # 出发时间 = scrapy.Field()
        # 到达时间 = scrapy.Field()
        # 服务类型 = scrapy.Field()
        # 状态 = scrapy.Field()
        # 注册号 = scrapy.Field()
        time_update = data['last_updated']
        for flight in data['flights']:
            item = ExampleItem()
            item['更新时间'] = time_update
            item['航线'] = flight['airline']
            item['航班号'] = flight['flight_number']
            item['预定出发日期'] = flight['scheduled_departure_date']
            item['预定出发时间'] = flight['scheduled_departure_time']
            item['起点'] = flight['origin_name']
            item['终点'] = flight['destination_name']
            item['出发时间'] = flight['departure_time']
            item['到达时间'] = flight['arrival_time']
            item['服务类型'] = flight['serviceType']
            item['状态'] = flight['status']
            item['注册号'] = flight['registration']
            items.append(item)
            yield item
            # print(flight['id'])
        return items
        pass
