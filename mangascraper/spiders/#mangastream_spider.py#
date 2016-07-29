import scrapy
from mangascraper.items import MangaStreamItem
from scrapy.exceptions import CloseSpider

class MangaStreamSpider(scrapy.Spider):
    name = 'mangastream'
    allowed_domains = ['mangastream.com']
    start_urls = ['http://mangastream.com/r/the_seven_deadly_sins/185/3560/1']
    def parse(self, response):
        img = response.css('img').xpath('@src').extract()
        imageURL = img[0]

        yield MangaStreamItem(file_urls=[imageURL])
        next_page = response.css('.next').xpath('a/@href').extract()
        if next_page:
            yield scrapy.Request(next_page[0], self.parse)
        if int(next_page[0].split('/')[-1])==1:
            raise CloseSpider('Im out!')
        

