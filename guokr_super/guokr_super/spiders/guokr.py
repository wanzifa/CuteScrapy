#coding:utf-8

import scrapy
from scrapy.spiders import Spider
from scrapy.http.request import Request
from scrapy.selector import Selector
from guokr_super.items import GuokrSuperItem


class GuoKeSpider(Spider):
    # 爬虫的名字
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = [
        'http://www.guokr.com'
    ]

    def parse(self, response):
        self.log('Hi, this is the main page! %s' % response.url)
        sel = Selector(text=response.body)
        site_tech = sel.xpath("//div[@class='contents-l'][2]/div[1]/ul[1]/li[1]/a/@href").extract()[0]
        title  = sel.xpath("//div[@class='contents-l'][2]/div[1]/ul[1]/li[1]/div[@class='cont'][1]/h3[1]/a/text()").extract()
        # 这个Request引用自http模块
        # request的第一个参数会被传递给downloader中间件 
        # 然后中间件会返回一个response对象 这个响应被传递到第二个参数的函数里
        # meta里面是定义处理函数里面会用到的一些参数
        return Request(url=site_tech, callback=self.parse_item, meta={'title':title})

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        sel = Selector(text=response.body)
        guoke_tech = GuokrSuperItem()
        guoke_tech['title'] = response.meta.get('title')
        guoke_tech['author'] = sel.xpath("//a[@id='articleAuthor'][1]/text()").extract()
        guoke_tech['time'] = sel.xpath("//p[@class='gfr'][1]/text()").extract()
        guoke_tech['author_url'] = sel.xpath("//a[@id='articleAuthor'][1]/@href").extract()
        guoke_tech['content'] = sel.xpath("//div[@id='articleContent'][1]").extract()
        return guoke_tech


