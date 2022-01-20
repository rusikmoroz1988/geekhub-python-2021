# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from dataclasses import replace
from itemadapter import ItemAdapter
import sqlite3

class VikkaDbPipeline:

    def open_spider(self, spider):
        base_name = spider.date.replace('/', '_') + '.db'
        self.connection = sqlite3.connect(base_name)
        self.cursor = self.connection.cursor()    
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS news(
            title TEXT,
            text TEXT,
            tags TEXT,
            URL TEXT);
            """)   
        self.cursor.execute("SELECT * FROM news")
        result = self.cursor.fetchall()
        if len(result)!=0:
            self.cursor.execute('DELETE FROM news')

    def process_item(self, item, spider):
        sql = "INSERT INTO news VALUES (?, ?, ?, ?)"
        self.cursor.execute(sql, (item['title'], item['text'], item['tags'], item['URL']))
        return item
    
    def close_spider(self, spider):
        self.connection.commit()
        self.connection.close()
