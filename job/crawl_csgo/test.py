
# -*- coding: utf-8 -*-
from os import times
from bs4 import BeautifulSoup
# import urllib.error
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from lxml import etree
import requests



options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.youpin898.com/market/csgo?gameId=730&weapon=weapon_knife_survival_bowie")
js = '''
            let height = 0
    let interval = setInterval(() => {
        window.scrollTo({
            top: height,
            behavior: "smooth"
        });
        height += 500
    }, 500);
    setTimeout(() => {
        clearInterval(interval)
    }, 7000);
'''
driver.execute_script(js)
time.sleep(8)
# 点击出售按钮
# driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/div/div[2]/div[2]/div[1]/label[2]/span[2]').click()
# driver.execute_script(js)
# time.sleep(8)
bs = BeautifulSoup(driver.page_source, "html.parser")
bs = bs.encode('utf-8')
# print bs
html = etree.HTML(bs)
"""获取出租商品的数量 """
goods_lease_cnt = len(html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div/div[2]/div[4]/div[2]/div[1]')[0])
# print goods_lease_cnt


""" 打开商品细节页面 """
xpath = ''
for i in range(1, 4):
    xpath = '//*[@id="__layout"]/div/div[3]/div[1]/div/div[2]/div[4]/div[2]/div[1]/div[' + str(i) + ']'
    driver.find_element_by_xpath(xpath).click()
url_list = []
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    url_list.append(str(driver.current_url))
    driver.close()
print url_list

for url in url_list[1:]:
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div/label[4]').click()
    except :
        pass
# driver.switch_to.window(windows[1])
# print driver.window_handles



# driver.close()

# x = html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div/div[2]/div[4]/div[2]/div[1]/div[1]')
# y = html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div/div[2]/div[4]/div[2]/div[1]')
# print x[0].text
# print y[0].text



# html = etree.HTML(bs.text)
# data = html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div/div[2]/div[4]/div[2]/div[1]')
# print type(data)
# print len(data)

# url = "https://www.youpin898.com/market/csgo?gameId=730&weapon=weapon_knife_falchion"
# headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
#                'Accept - Encoding':'gzip, deflate',
#                'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
#                'Connection':'Keep-Alive',
#                'Host':'zhannei.baidu.com',
#                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
# r = requests.get('http://zhannei.baidu.com/cse/search', headers=headers, timeout=3)
# reqs = requests.get(url)
# print reqs.text
# html = etree.HTML(reqs.text)
# data = html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div/div[2]/div[4]/div[2]/div[1]/div[1]')
# print type(data)
# print len(data)
# for i in data:
#     print i.text


