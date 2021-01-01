import scrapy


class HiydSpider(scrapy.Spider):
    name = 'hiyd'
    allowed_domains = ['food.hiyd.com']
    start_urls = ['http://food.hiyd.com/']

    def parse(self, response):
        pass
