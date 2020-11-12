import scrapy
import os


class NewsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['haiwainet.cn']
    start_urls = ['http://finance.haiwainet.cn/yw/']
    custom_settings = {'LOG_LEVEL': 'WARNING',
                       'LOG_FILE': '../logs/'+name+'.log'}


    # def start_requests(self):
    #     yield scrapy.Request(self.start_urls[0])

    def parse(self, response):
        ls = response.xpath('//ul[@class="ul04 ub01 pt10 upton"]')
        item = {}
        for l in ls:
            url = l.xpath('./li/a/@href').extract_first()
            item['detail'] = url
            break
        pass
        yield item


if __name__ == '__main__':
    os.system('scrapy crawl news')
