#coding:utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

#from scrapyclass.items import MeneameItem


# CrawlSpider区别于Spider最显著的就是一个rule元组
class MeneameSpider(CrawlSpider):
    name = 'meneame'
    start_urls = ['http://meneame.net']
    
    # rules元组里是你在这个页面（start_urls列表里面那个)希望提取到的url对应的
    # 正则表达式匹配 
    # 如果你设置了follow＝False，那么爬虫不会跟进，也就是只爬完当前页面就结束了
    # 如果你设置了follow=True 那么爬虫就会跟进 举个例子
    # 你从第一页里找到了第二三四五六的链接 爬虫会在这些页面重新寻找page链接
    # 然后继续爬下去 以此类推
    # 注意 现在的发现是 Rule是按次序匹配爬取的 第二个不爬完 第一个不会循环跟进
    # 这个是猜测 具体是不是这样 待我看完源码再来检验
    # （源码看完来更新)确实是这样的哈哈哈
    # 注意 如果你设置了回调函数 那么follow默认为false 否则为true
    rules = (
        # 参数一设需要提取的url的正则表达式
        Rule(LinkExtractor(allow='\?page=\d+')),
        Rule(LinkExtractor(allow='meneame.net/story'), callback='parse_article'),
    )

    def parse_article(self, response):
        # item = MeneameItem()
        #item['title'] = response.css('.news-body h1 a::text').extract()[0]
       
       #item['description'] = response.css('.news-body::text').extract()[4]

        #return item
        print 'hehehe'
