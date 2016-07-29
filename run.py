import scrapy
import zipfile
import os
import zipfile
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from mangascraper.settings import *
from shutil import make_archive

input_url = str(input('Enter page 1 of mangastream url: '))
#manga_info = input('Enter comma seperated values for the manga and the chapter no. (in list form ([]): ')

#extract manga name and chapter no.

from mangascraper.spiders.mangastream_spider import MangaStreamSpider
spider = MangaStreamSpider
spider.start_urls = [input_url]
process = CrawlerProcess(get_project_settings()) #load settings 

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(MangaStreamSpider)
    process.start() 

#make_archive('/home/scire/to-read/'+manga_info[0]+'_'+manga_info[1], 'zip', root_dir=None, base_dir=None)

