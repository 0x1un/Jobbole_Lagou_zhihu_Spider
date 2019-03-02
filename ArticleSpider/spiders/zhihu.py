# # -*- coding: utf-8 -*-
# import time
#
# import scrapy
# from selenium import webdriver
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.common.by import By
#
#
# class ZhihuSpider(scrapy.Spider):
#     name = 'zhihu'
#     allowed_domains = ['www.zhihu.com']
#     start_urls = ['http://www.zhihu.com/']
#
#     def parse(self, response):
#         pass
#
#     def start_requests(self):
#         browser = webdriver.Chrome('/usr/bin/chromedriver')
#         browser.get('https://www.zhihu.com/')
#         time.sleep(3)
#         browser.find_element_by_xpath(
#             '//*[@id="root"]/div/main/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/button[1]').click()
#         browser.find_element_by_xpath(
#             '/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys(
#             '18782909054')
#         browser.find_element_by_xpath(
#             '/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(
#             'qingfing__')
#         browser.find_element_by_xpath(
#             '/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/button').click()
#         cookies = browser.get_cookies()
#         if cookies:
#             cookie_dict = {}
#             for cookie in cookies:
#                 cookie_dict[cookie['name']] = cookie['value']
#             browser.close()
#             print(cookie_dict)
#         return [scrapy.Request(url=self.start_urls[0], dont_filter=True, cookies=cookie_dict, callback=self.parse)]
#
