#coding:utf-8
from scrapy.spiders import Spider
from scrapy.selector import Selector

from guokr.items import GuokrItem

class GuokeSpder(Spider):
    #爬虫的名字
    name='guokr'
    #允许爬取的域名
    allowed_domains = ['guokr.com']
    #爬取的页面
    start_urls = ['http://www.guokr.com']
    
    # 这个response参数是scrapy类的一个downloader中间件实现的，我们后面会讲
    def parse(self, response):
        # Selector可以为我们实例化一个选择器对象
        # 选择器对象可以通过xpath语句选择页面中的内容
        sel = Selector(response)
        title = sel.xpath("//li[@class='content-article'][1]/a[1]/img/@alt").extract()
        item = GuokrItem()
        item['title'] = title
        return item

