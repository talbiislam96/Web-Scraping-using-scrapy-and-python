# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import dns

class PimPipeline(object):
    def __init__(self):
        
        client = pymongo.MongoClient("mongodb+srv://MaherBen:MaherBen@cluster0-untz6.mongodb.net/test?retryWrites=true&w=majority")
        db = client.test
        
        self.collection = db['jobs']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
