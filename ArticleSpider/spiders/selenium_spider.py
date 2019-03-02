# import time
#
# import selenium.webdriver.support.wait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
#
# # browser.get('http://zhihu.com')
# # time.sleep(5)
# # login_button = browser.find_element_by_xpath(
# #     '//*[@id="root"]/div/main/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/button[1]')
# # login_button.click()
# # browser.find_element_by_xpath(
# #     '/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys(
# #     '18782909054')
# # browser.find_element_by_xpath(
# #     '/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(
# #     'qingfing__')
# # login = browser.find_element_by_xpath('/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/button').click()
# # cookies = browser.get_cookies()
# browser = webdriver.Chrome('/usr/bin/chromedriver')
# browser.get('https://www.zhihu.com/')
# time.sleep(3)
# browser.find_element_by_xpath(
#     '//*[@id="root"]/div/main/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/button[1]').click()
# browser.find_element_by_xpath(
#     '/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys(
#     '18782909054')
# browser.find_element_by_xpath(
#     '/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(
#     'qingfing__')
# browser.find_element_by_xpath(
#     '/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/button').click()
# cookies = browser.get_cookies()
# if cookies:
#     print(cookies)
#     cookie_dict = {}
#     for cookie in cookies:
#         cookie_dict[cookie['name']] = cookie['value']
#     browser.close()
# print(cookie_dict)
#
s = [{'domain': '.zhihu.com', 'value': 'db1c80452286452d852fedbb144e7370|1532430952000|1532430952000', 'secure': False,
  'expiry': 1627038952.126841, 'name': 'q_c1', 'path': '/', 'httpOnly': False},
 {'domain': 'www.zhihu.com', 'value': '1c2b7f9548c57cd7d5a535ac4812e20e', 'secure': False, 'expiry': 1532431852.12654,
  'name': 'tgw_l7_route', 'path': '/', 'httpOnly': False},
 {'domain': '.zhihu.com', 'value': '"ALDlCdUT8w2PTu6X7OtH6EJvIT_c6JewZec=|1532430952"', 'secure': False,
  'expiry': 1627038952.126786, 'name': 'd_c0', 'path': '/', 'httpOnly': False}, {'domain': '.zhihu.com',
                                                                                 'value': '"2|1:0|10:1532430957|14:capsion_ticket|44:YWNhZDk1ZTZmMDcwNDI0NWI1MjUzY2RhYWZiODljY2Q=|6c5f221558e6a7d94141a012d91139381aad05efcbd81a193c598232f860e15a"',
                                                                                 'secure': False,
                                                                                 'expiry': 1535022956.97836,
                                                                                 'name': 'capsion_ticket', 'path': '/',
                                                                                 'httpOnly': True},
 {'domain': '.zhihu.com', 'value': '8cec7e91-290a-441a-81bc-d516411f63a8', 'secure': False, 'name': '_xsrf',
  'path': '/', 'httpOnly': False},
 {'domain': '.zhihu.com', 'value': 'e62802e4-381d-45c5-9b2d-dd2a70a87a1e', 'secure': False, 'expiry': 1595502952.126656,
  'name': '_zap', 'path': '/', 'httpOnly': False}]
