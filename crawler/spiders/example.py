import scrapy
import os

from scrapy import Request

from crawler.items import ExampleItem
# from selenium import webdriver
import time


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.finnair.com']
    start_urls = ['https://api.finnair.com/c/flightapp/flight-core-proxy/flightlist', ]
    # http://shike.gaotie.cn/zhan.asp?l=0&zhan=%B1%B1%BE%A9
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'X-API-Key': 'Dg4baijHYq9BLH7YR40Ki9CymRXRLAbBVT7exvzb'
    }

    def start_requests(self):
        return [Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)]
    # def __init__(self):
    #     self.browser = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")
    #     # D:/chromedriver_win32
    #     # F:/Environment/SeleniumWebDriver/chromedriver_win32
    #
    # def __del__(self):
    #     self.browser.close()

    def parse(self, response):
        # node_list = response.xpath('/html/body/div[2]/div/div/div[3]/div/div/div[3]/table/tr[2]')
        # print(response.xpath('/html/body/div[1]/div/div/div[3]/div/div/div[3]/ta/tr[2]').extract())
        print(response.text)
        # self.browser.get(response.url)
        time.sleep(15)
        # print(self.browser.page_source.xpath('/html/body/div[1]/div/div/div[3]/div/div/div[3]/ta/tr[2]'))
        # item = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div/div[3]/table/tbody/tr[2]')
        # print(item)
        # /html/body/div[2]/div/div/div[3]/div/div/div[3]/table/tr[2]
        # items = []
        # for node in node_list:
        #     item = ExampleItem()
        #     # item['text'] = node.extract()
        #     num = node.xpath('./td[1]/a/text()').extract()
        #     start = node.xpath('./td[3]/a[1]/text()').extract()
        #     end = node.xpath('./td[3]/a[2]/text()').extract()
        #     start_time = node.xpath('./td[6]/text()').extract()
        #     end_time = node.xpath('./td[4]/text()').extract()
        #     length = node.xpath('./td[7]/text()').extract()
        #     print(num)
        #     if len(num):
        #         item['车次'] = num[0]
        #         # print(num[0])
        #     if len(start):
        #         item['始发站'] = start[0]
        #     if len(end):
        #         item['终点站'] = end[0]
        #     if len(start_time):
        #         item['开车时间'] = start_time[0]
        #     if len(end_time):
        #         item['到站时间'] = end_time[0]
        #     if len(length):
        #         item['全程_时间'] = length[0]
        #         items.append(item)
        # item['url'] = response.text
        # return items
        pass
