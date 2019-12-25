# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class ZaobaoPipeline(object):
    def __init__(self):
        self.file = codecs.open("zb_item.json", "wb", encoding="utf-8")

    def process_item(self, item, spider):
        i = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(i)
        self.file.write('\n')
        return item

    def close_spider(self, spider):
        self.file.close()

