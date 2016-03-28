#coding:utf-8
from scrapy.spiders import Spider
from scrapy.selector import Selector

#from guokr.items import GuokrItem, BaiduItem

class GuokeSpder(Spider):
    #爬虫的名字
    name='mutiple'
    # 允许爬取的域名
    # 实践证明，这一行无法限制是否真的爬取它限制的域名
    # 我猜，是为了增强程序的可读性而已
    allowed_domains = ['guokr.com']
    # 爬取的页面
    # 其实我们可以爬很多个，毕竟它是列表形式
    # 爬取的时候，不以你列表的顺序为顺序，不信，爬爬看！
    start_urls = [
        'http://www.guokr.com',
        'http://www.baidu.com'
    ]
    
    # 这个response参数是scrapy类的一个downloader中间件实现的，我们后面会讲
    def parse(self, response):
        # Selector可以为我们实例化一个选择器对象
        # 选择器对象可以通过xpath语句选择页面中的内容
        url = response.url
        print "我正在爬取{0}".format(url)

