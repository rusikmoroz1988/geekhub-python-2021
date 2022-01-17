# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class VikkaPipeline (object):

    def open_spider(self, spider):
        self.file = open(spider.year + "_" + spider.month + "_" + spider.day + ".csv", "w", encoding="utf8")
        self._fields = ["title", "text", "tags", "URL"]
        self.file.write(",".join(self._fields) + "\n")

    def process_item(self, item, spider):
        item["title"] = item["text"]
        item["text"] = item["text"]
        item["tags"] = item["tags"]
        item["URL"] = item["URL"]

        line = (
                item["title"],
                item["text"],
                item["tags"],
                item["URL"],
                "\n",
               )
        line = ",".join(line)
        self.file.write(line)
        return item
    
    def close_spider(self, spider):
        self.file.close()
