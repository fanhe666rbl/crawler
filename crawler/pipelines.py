# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import codecs
import os


class CrawlerPipeline:
    def __init__(self):
        base_dir = os.getcwd()
        filename = base_dir + '/items.json'

        if not os.path.getsize(filename):
            # ����ǿ��ļ��������[
            f = codecs.open(filename, 'a')
            f.write('[\n')
            f.close()
        else:
            # ȥ������]
            f = codecs.open(filename, 'rb+')
            f.seek(-1, 2)
            f.truncate()
            f.close()
            # ȥ��\n
            f = codecs.open(filename, 'rb+')
            f.seek(-2, 2)
            f.truncate()
            f.close()
            # ��Ӷ���
            f = codecs.open(filename, 'a')
            f.write(',\n')
            f.close()

    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/items.json'
        with codecs.open(filename, 'a') as f:
            # �������
            line = '\t' + json.dumps(dict(item), ensure_ascii=False) + ',\n'
            f.write(line)
        return item

    def close_spider(self, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/items.json'
        # ȥ�����һ�еĶ���
        f = codecs.open(filename, 'rb+')
        f.seek(-2, 2)
        f.truncate()
        f.close()
        # ���]
        f = codecs.open(filename, 'a')
        f.write('\n]')
        f.close()

