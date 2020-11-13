import scrapy
import os


class NewsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['haiwainet.cn']
    start_urls = ['https://www.cnki.net/']
    custom_settings = {'LOG_LEVEL': 'WARNING',
                       'LOG_FILE': '../logs/'+name+'.log'}

    # def start_requests(self):
    #     yield scrapy.Request(self.start_urls[0])

    def parse(self, response):
        print(response.text)


if __name__ == '__main__':
    os.system('scrapy crawl news')
