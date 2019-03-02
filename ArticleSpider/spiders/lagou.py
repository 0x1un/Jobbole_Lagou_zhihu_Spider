from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider, Rule
from .mytools import Mytools
from ..items import LagouJobItemLoader, LagouJobItem
import datetime


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']

    rules = (
        Rule(LinkExtractor(allow=r"zhaopin/.*"), follow=True),
        Rule(LinkExtractor(allow=r"gongsi/j\d+.html"), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True)
    )


    custom_settings = {
        'COOKIES_ENABLED': False,
        "DOWNLOAD_DELAY": 0.5,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'www.lagou.com',
            'Upgrade-Insecure-Requests': '1',
            'Cookie': 'JSESSIONID=ABAAABAAADEAAFIBCD44E138F7B16FC70E4AA46B109801F; _ga=GA1.2.948320197.1534851127; user_trace_token=20180821193209-d7564b6c-a535-11e8-ab1f-5254005c3644; LGUID=20180821193209-d7564f40-a535-11e8-ab1f-5254005c3644; index_location_city=%E6%88%90%E9%83%BD; _gid=GA1.2.180925300.1536590785; TG-TRACK-CODE=hpage_code; X_HTTP_TOKEN=c935a49c0e8f02628c7ea7eb3acdadce; SEARCH_ID=b370a10d410d4b99bcb384ae52c15057; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1534851129,1535022796,1536594353; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536594353; LGRID=20180910234553-9989d7fa-b510-11e8-8d59-525400f775ce'
        },
        'DOWNLOADER_MIDDLEWARES': {
            # user-agent代理
            'ArticleSpider.middlewares.RandomUserAgentMiddleware': 2,
            # ip代理
            # 'ArticleSpider.middlewares.RandomIpProxyMiddleware': 3,
            # 'ArticleSpider.middlewares.JSPageMiddleware': 3,
        }
    }

    def parse_job(self, response):
        date = datetime.datetime.now().date()
        item_loader = LagouJobItemLoader(item=LagouJobItem(), response=response)
        item_loader.add_xpath('title', '//*[@class="job-name"]/@title')
        item_loader.add_value('url', response.url)
        item_loader.add_value('url_object_id', Mytools.get_md5(response.url))
        item_loader.add_xpath('salary', '//*[@class="job_request"]/p/span[1]/text()')
        item_loader.add_xpath('job_city', '//*[@class="job_request"]/p/span[2]/text()')
        item_loader.add_xpath('work_years', '//*[@class="job_request"]/p/span[3]/text()')
        item_loader.add_xpath('degree_need', '//*[@class="job_request"]/p/span[4]/text()')
        item_loader.add_xpath('job_type', '//*[@class="job_request"]/p/span[5]/text()')
        item_loader.add_xpath('publish_time', '//*[@class="publish_time"]/text()')
        item_loader.add_xpath('job_advantage', '//*[@class="job-advantage"]/p/text()')
        item_loader.add_xpath('job_addr', '//*[@class="work_addr"]/a/text()')
        item_loader.add_xpath('company_url', '//*[@id="job_company"]/dt/a/@href')
        item_loader.add_xpath('company_name', '//*[@id="job_company"]/dt/a/img/@alt')
        item_loader.add_xpath('tags', '//*[contains(@class,"position-label")]/li/text()')
        item_loader.add_value('crawl_time', date)
        item_loader.add_xpath('job_desc', '//*[@class="job_bt"]/div/p/text()')
        # item_loader.add_value('crawl_update_time', date)
        job_item = item_loader.load_item()

        return job_item
