# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.files import FilesPipeline

class CustomFilesPipeline(FilesPipeline):

    def file_key(self, url):
        file_guid = url.split('/')[-1]
        return 'download/%s' % (file_guid)
