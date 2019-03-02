# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import datetime
import re

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join, Identity
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags


def date_convert(value):
    try:
        value = re.search(r'\d{4}/\d{1,2}/\d{1,2}', value).group()
        create_date = datetime.datetime.strptime(value, '%Y/%m/%d').date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date


def check_numbers(value):
    if re.match(r'(\d+)', value):
        num = int(re.match(r'(\d+)', value).group(1))
    else:
        num = 0
    return num


def remove_comment_tags(value):
    if '评论' in value:
        return ""
    else:
        return value


# 重载ItemLoader
class ArticleItemLoader(ItemLoader):
    # let the default output value of all items get the first one.
    default_output_processor = TakeFirst()


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()

    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert)
        # output_processor = TakeFirst()
    )

    praise_nums = scrapy.Field(
        input_processor=MapCompose(check_numbers)
    )

    fav_nums = scrapy.Field(
        input_processor=MapCompose(check_numbers)
    )

    comment_nums = scrapy.Field(
        input_processor=MapCompose(check_numbers)
    )

    front_image_url = scrapy.Field(
        output_processor=Identity()
    )

    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join('--')
    )

    url = scrapy.Field()

    url_object_id = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = '''
            insert into article_spider3(title, url, create_date, fav_nums, url_object_id, front_image_url, comment_nums, praise_nums, tags)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 

        '''
        params = (self['title'], self['url'], self['create_date'], self['fav_nums'], self['url_object_id'],
                  self['front_image_url'], self['comment_nums'], self['praise_nums'],
                  self['tags'])
        return insert_sql, params


class LagouJobItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


def strip_work_years(value):
    value = value.replace('/', '').rstrip()
    return value


def strip_salary(value):
    value = value.strip()
    return value


def strip_job_city(value):
    value = value.replace('/', '').strip()
    return value


def strip_degree_need(value):
    value = value.replace('/', '').strip()
    return value


def deal_with_job_addr(value):
    if '查看地图' in value:
        return ''
    return value


def handle_tags(value):
    try:
        value = ''.join(value)
        return value
    except Exception:
        return 'Null'


class LagouJobItem(scrapy.Item):
    title = scrapy.Field(

    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    salary = scrapy.Field(
        input_processor=MapCompose(strip_salary)
    )
    job_city = scrapy.Field(
        input_processor=MapCompose(strip_job_city)
    )
    work_years = scrapy.Field(
        input_processor=MapCompose(strip_work_years)
    )
    degree_need = scrapy.Field(
        input_processor=MapCompose(strip_degree_need)
    )
    job_type = scrapy.Field()
    publish_time = scrapy.Field()
    job_advantage = scrapy.Field()
    job_addr = scrapy.Field(
        input_processor=MapCompose(deal_with_job_addr),
        output_processor=Join()
    )
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    tags = scrapy.Field(

        output_processor=Join(',')
    )
    crawl_time = scrapy.Field()
    job_desc = scrapy.Field(
        output_processor=Join()
    )
    crawl_update_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = '''
                    insert into lagou_spider(
                    title, url, url_object_id, salary, job_city, 
                    work_years, degree_need, job_type, publish_time, 
                    job_advantage, job_addr, company_name, company_url, tags, 
                    crawl_time, job_desc)
                    
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE salary=VALUES(salary), job_desc=VALUES(job_desc)

                '''
        params = (
            self['title'], self['url'], self['url_object_id'], self['salary'], self['job_city'],
            self['work_years'], self['degree_need'], self['job_type'], self['publish_time'],
            self['job_advantage'], self['job_addr'], self['company_name'], self['company_url'], self['tags'],
            self['crawl_time'], self['job_desc']

        )
        return insert_sql, params


class TourongjieItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


def remove_space(value):
    value = remove_tags(value.strip())
    return value.rstrip()


class TourongjieItem(scrapy.Item):
    project_need = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    location = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    financing_entity = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    industry = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    industry_nature = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    financing_use = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    financing_funds = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    total_funds = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    financing_method = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    information = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    stage = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    capital_account_persent = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    financing_exit_method = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    min_exit_period = scrapy.Field(
        input_processor=MapCompose(remove_space),

    )
    company_url = scrapy.Field()
    url_object_id = scrapy.Field()
    commapy_profile = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = '''
                    insert into tourongjie_spider(
                    project_need, location, financing_entity, industry, industry_nature,
                    financing_use, financing_funds, total_funds, financing_method,
                    information, stage, capital_account_persent, financing_exit_method, min_exit_period,
                    company_url, company_profile, url_object_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)
                    

                '''
        params = (
            self['project_need'], self['location'], self['financing_entity'], self['industry'], self['industry_nature'],
            self['financing_use'], self['financing_funds'], self['total_funds'], self['financing_method'],
            self['information'], self['stage'], self['capital_account_persent'], self['financing_exit_method'],
            self['min_exit_period'],
            self['company_url'], self['company_profile'], self['url_object_id']

        )
        return insert_sql, params
# ON DUPLICATE KEY UPDATE project_need=VALUES(project_need), financing_funds=VALUES(financing_funds)
