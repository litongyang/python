# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from lxml import etree
import requests

# options = webdriver.ChromeOptions()
# options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# driver = webdriver.Chrome(chrome_options=options)
# driver.get("https://www.baidu.com/?tn=21002492_25_hao_pg")
# element = driver.find_element_by_id('kw')
# element.send_keys(u'人生苦短，我学Python')# 输入字符串到这个输入框里
# driver.find_element_by_id('su').click()


# import logging
#
# # 设置日志等级和输出日志格式
# logging.basicConfig(level=logging.DEBUG,
#
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
#
# logging.debug('这是一个debug级别的日志信息')
# logging.info('这是一个info级别的日志信息')
# logging.warning('这是一个warning级别的日志信息')
# logging.error('这是一个error级别的日志信息')
# logging.critical('这是一个critical级别的日志信息')
import logging
from datetime import datetime
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # 设置打印级别
formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s')

# 设置屏幕打印的格式
sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)
log_name =str(datetime.now().strftime('%Y%m%d%H')) +'.log'
# 设置log保存
fh = logging.FileHandler(log_name, encoding='utf8')
fh.setFormatter(formatter)
logger.addHandler(fh)
try:
    x=0
    for i in range(1, x):
        print i
    logging.info('Start print log......'+ str(x))
except Exception,e:
    logging.error(Exception, e)
    pass
