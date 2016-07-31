import scrapy
from mangascraper.items import MangaStreamItem
from scrapy.exceptions import CloseSpider
from scrapy.http import Request

class MangaStreamSpider(scrapy.Spider):
    name = 'mangastream'
    allowed_domains = ['mangastream.com']

    def parse(self, response):
        img = response.css('img').xpath('@src').extract()
        imageURL = img[0]
        current_page_no = response.url.split('/')[-1]
            
        yield MangaStreamItem(fileno=current_page_no, file_urls=[imageURL])
        next_page = response.css('.next').xpath('a/@href').extract()
        if next_page:
            yield scrapy.Request(next_page[0], self.parse)
            if int(next_page[0].split('/')[-1])==1:
                raise CloseSpider('Im out!')
            

