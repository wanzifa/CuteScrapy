# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
"""
我们一般的步骤就是，爬取数据，写入item对象，然后对item对对象做一些处理
pipeline文件就是做最后一件事情的
利用pipeline文件，我们可以进行数据去重，存入数据库等等很多事情
这里 我们做一个比较常见的存入数据库操作
"""
import pymongo
from scrapy import log

class MongoDBPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    # 这个方法很厉害
    # crawler不仅可以提供settings中的数据 还可以触及许多其它的主要组成部分
    # 比如signal等等
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB', 'items')
        )
    
    #spider被开启时，调用这个方法
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    
    #spider被关闭时 调用这个方法
    def close_spider(self, spider):
        self.client.close()    
            
    # 必须实现的方法
    # 每个pipeline组件都需要调用这个方法
    # 它必须返回一个Item或它的继承类对象
    # 否则 抛出DropItem异常
    def process_item(self, item, spider):
        collection_name = self.__class__.__name__
        self.db[collection_name].insert(dict(item))
        return item
