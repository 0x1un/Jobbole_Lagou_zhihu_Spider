# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import ArticlespiderItem
from .mytools import Mytools
from ..items import ArticleItemLoader

# from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


# from pyvirtualdisplay import Display
class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts']
    handle_httpstatus_list = [404, 403]
    # def __init__(self):
    #     # 集成selenium
    #     self.display = Display(visible=0, size=(800, 600)) # 使用pyvirtualdisplay让chrome隐式启动
    #     self.display.start()
    #
    #     self.browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    #     super().__init__()
    #     # 连接信号，当信号被触发时执行关闭chrome的函数
    #     dispatcher.connect(receiver=self.spider_closed, signal=signals.spider_closed)
    #
    # def spider_closed(self, spider):
    #     try:
    #         self.browser.quit()
    #     except Exception:
    #         print('chrome退出异常..')
    #     else:
    #         print('chrome已正常关闭..')

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            # user-agent代理
            'ArticleSpider.middlewares.RandomUserAgentMiddleware': 2,
            # ip代理
            # 'ArticleSpider.middlewares.RandomIpProxyMiddleware': 3,
            # 'ArticleSpider.middlewares.JSPageMiddleware': 3,
        }
    }

    def __init__(self):
        self.fail_urls = []

        dispatcher.connect(self.handle_spider_closed, signals.spider_closed)

    def handle_spider_closed(self, spider, reason):
        self.crawler.stats.set_value('Failed_urls', ','.join(self.fail_urls))

    def parse(self, response):
        if response.status in [404, 403]:
            self.fail_urls.append(response.url)
            self.crawler.stats.inc_value('Failed url')

        post_nodes = response.xpath('//*[@id="archive"]/div/div/a')
        for post_node in post_nodes:
            post_url = post_node.xpath('@href').extract_first()
            img_url = post_node.xpath('img/@src').extract_first()
            yield Request(url=response.urljoin(post_url), meta={'front_image_url': img_url}, callback=self.parse_detail)

        # get next page
        next_page_url = response.xpath('//*[@class="next page-numbers"]/@href').extract()[0]
        if next_page_url:
            yield Request(url=response.urljoin(next_page_url), callback=self.parse)
            ...

    def parse_detail(self, response):
        """

        :param response:
        :return:
        """
        front_image_url = response.meta.get('front_image_url', '')
        # load item via item-loader 引入items中自定义ItemLoader
        item_loader = ArticleItemLoader(item=ArticlespiderItem(), response=response)

        item_loader.add_xpath('title', '//*[@class="entry-header"]/h1/text()')
        item_loader.add_xpath('create_date', '//*[@class="entry-meta-hide-on-mobile"]/text()')
        item_loader.add_xpath('praise_nums', '//*[@class="post-adds"]/span/h10/text()')
        item_loader.add_xpath('fav_nums', '//*[contains(@class,"bookmark-btn")]/text()')
        item_loader.add_xpath('comment_nums', '//*[contains(@class,"href-style hide-on-480")]/text()')
        item_loader.add_value('front_image_url', [front_image_url])
        item_loader.add_xpath('tags', '//*[@class="entry-meta-hide-on-mobile"]/a/text()')
        item_loader.add_value('url', response.url)
        item_loader.add_value('url_object_id', Mytools.get_md5(response.url))
        article_item = item_loader.load_item()

        yield article_item
