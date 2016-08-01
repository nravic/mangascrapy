# -*- coding: utf-8 -*-

# Scrapy settings for mangascraper project

BOT_NAME = 'mangascraper'

SPIDER_MODULES = ['mangascraper.spiders']
NEWSPIDER_MODULE = 'mangascraper.spiders'


# Configure item pipelines
ITEM_PIPELINES = {
    'mangascraper.pipelines.CustomFilesPipeline': 1,
}
FILES_STORE = '/home/scire/to-read'
    
