import scrapy
import os
from crawler.items import ExampleItem
from selenium import webdriver
import time


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.finnair.com']
    start_urls = ['https://www.finnair.com/cn/cn/information-services/flights/flightslist', ]
    # http://shike.gaotie.cn/zhan.asp?l=0&zhan=%B1%B1%BE%A9

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="F:/Environment/SeleniumWebDriver/chromedriver_win32/chromedriver.exe")

    def __del__(self):
        self.browser.close()

    def parse(self, response):
        # node_list = response.xpath('/html/body/div[2]/div/div/div[3]/div/div/div[3]/table/tr[2]')
        # print(response.xpath('/html/body/div[1]/div/div/div[3]/div/div/div[3]/ta/tr[2]').extract())
        print(response)
        self.browser.get(response.url)
        time.sleep(15)
        print(self.browser.page_source)
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
