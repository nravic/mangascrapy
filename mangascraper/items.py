# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MangaStreamItem(scrapy.Item):
    name = "MangaStreamItem"
    file_urls = scrapy.Field()
    files = scrapy.Field()

class MangaFoxItem(scrapy.Item):
    name = "MangaFoxItem"
    file_urls = scrapy.Field()
    files = scrapy.Field()
