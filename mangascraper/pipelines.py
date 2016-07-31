# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
class CustomFilesPipeline(FilesPipeline):
    
    
    def file_key(self, url):
        file_guid = url.split('/')[-1]
        return 'downloads/%s' % (file_guid)
    
    
#ALTERNATIVE IMAGES PIPELINE. Doesn't download images currently due to some bug. 
# class MyImagesPipeline(ImagesPipeline):

#     #Name download version
#     def file_path(self, request, response=None, info=None):
#         image_guid = request.meta['fileno'][0]
#         log.msg(image_guid, level=log.DEBUG)
#         return 'downloads/%s' % (image_guid)

    
#     def get_media_requests(self, item, info):
#         for image_url in item['image_urls']:
#             yield Request(image_url)
