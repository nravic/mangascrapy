import scrapy
import zipfile
import os
import zipfile
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from mangascraper.settings import *
from shutil import make_archive
import subprocess

input_url = str(input('Enter page 1 of mangastream url: '))
manga_info = input('Enter comma seperated values for manga and chapter: ')
manga_info = manga_info.split(',')

#extract manga name and chapter no.

from mangascraper.spiders.mangastream_spider import MangaStreamSpider
spider = MangaStreamSpider
spider.start_urls = [input_url]

if __name__ == "__main__":
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(MangaStreamSpider)
    process.start() 

make_archive('/home/scire/to-read/'+manga_info[0]+'_'+manga_info[1], 'zip', root_dir='/home/scire/to-read', base_dir='downloads')

subprocess.Popen(["rm", "-r", "/home/scire/to-read/downloads/"], stdout=subprocess.PIPE)


