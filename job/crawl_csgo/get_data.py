# -*- coding: utf-8 -*-

from os import times
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from lxml import etree
import get_category_url as get_category_url_class
import re
import chardet
import create_table as create_table
import pandas as pd
from datetime import datetime
import sys
reload(sys)
import os
sys.setdefaultencoding('utf8')
""" log日志文件设置 """
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


class GetData:
    def __init__(self):
        self.mysql = create_table.CreateTable()
        self.category_url_list = get_category_url_class.GetGoodsCategoryUrl().get_goods_category_url()
        self.category_url_list_test = ['https://www.youpin898.com/market/csgo?gameId=730&weapon=weapon_knife_survival_bowie',
                                       'https://www.youpin898.com/market/csgo?gameId=730&weapon=crate_sticker_pack_london2018_legends_collection']
        self.options = webdriver.ChromeOptions()
        self.chrome_dir = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Chrome驱动安装本地地址
        self.items_url_list = []  # 商品内容url
        self.id_url_dict = {}  # id和url对应的字典
        self.attribute_all_list = []  # 一个商品所以属性list
        # self.sale_all_list = []  # 商品属性售卖list
        # self.sale_list = []  # 一个商品单一属性出售list


    def get_category_info_url(self):
        logging.info('主页面共有：'+str(len(self.category_url_list)))
        # print len(self.category_url_list)
        for one_category_url in self.category_url_list:
            logging.info("当前url："+ str(one_category_url))
            # print "当前url：", one_category_url
            try:
                self.options.binary_location = str(self.chrome_dir)
                driver = webdriver.Chrome(chrome_options=self.options)
                driver.get(one_category_url)
                driver.execute_script(js)
                time.sleep(10)
                onegoods_category_lease_html = etree.HTML(
                    BeautifulSoup(driver.page_source, "html.parser").decode('utf-8'))  # 一类商品属性的租赁html
                """获取商品的数量 """
                goods_lease_cnt = 1
                try:
                    goods_lease_cnt = len(
                        onegoods_category_lease_html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div/div[2]/div[4]/div[2]/div[1]')[0])
                except Exception, e:
                    logging.info(str(Exception) + str(e))
                    # print Exception, e
                logging.info("获取商品的数量:"+ str(goods_lease_cnt))
                # print "获取商品的数量:",goods_lease_cnt
                name_id_dict = {}
                if goods_lease_cnt == 0:
                    continue
                else:
                    for i in range(1, goods_lease_cnt):
                        try:
                            xpath = '//*[@id="__layout"]/div/div[3]/div[1]/div/div[2]/div[4]/div[2]/div[1]/div['+ str(i) +']/span/div[2]/div[1]/text()'
                            one_name_str = onegoods_category_lease_html.xpath(xpath)  # 单品名称
                            one_name = one_name_str[0].replace(' ', '').replace('\n', '')
                            pattern = re.compile(ur'(?<=\|).*?(?=(\(|$))')
                            one_name = (pattern.search(one_name)).group()
                            name_id_dict[one_name] = i
                        except Exception, e:
                            logging.info(str(Exception) + str(e))
                            # print Exception, e
                    logging.info("商品url的数量："+ str(len(name_id_dict)))
                    # print "商品url的数量：",len(name_id_dict)
                    """ 打开商品细节页面 """
                    # goods_lease_cnt_test = 4
                    url_index_list = []
                    for k, v in name_id_dict.items():
                        url_index_list.append(v)
                    url_index_list = sorted(url_index_list)
                    for v in url_index_list:
                        # driver = webdriver.Chrome(chrome_options=self.options)
                        xpath = '//*[@id="__layout"]/div/div[3]/div[1]/div/div[2]/div[4]/div[2]/div[1]/div[' + str(v) + ']'
                        try:
                            ac = ActionChains(driver)
                            # ac.move_to_element(driver.find_element_by_xpath(xpath)).perform()
                            ac.click(driver.find_element_by_xpath(xpath)).perform()
                            # time.sleep(0.5)
                            # driver.find_element_by_xpath(xpath).click()

                        except Exception, e:
                            logging.info(str(Exception) + str(e))
                            # print Exception, e

                    try:
                        for i in range(1, len(driver.window_handles)):
                            driver.switch_to.window(driver.window_handles[i])
                            # print driver.current_url
                            """ 构造ID-url的字典"""
                            id = driver.current_url.replace('https://www.youpin898.com/goodInfo?id=', '')
                            self.id_url_dict[id] = driver.current_url
                            self.items_url_list.append(str(driver.current_url))
                    except Exception, e:
                        logging.info(str(Exception) + str(e))
                        # print Exception, e
                    logging.info("获取的一个页面的url："+ str(self.items_url_list))
                    logging.info("获取的url总数量："+str(len(self.items_url_list)))
                    logging.info("获取的总url："+ str(self.items_url_list))
                    logging.info("-------------------------------")
                    # print "获取的一个页面的url：",self.items_url_list
                    # print "获取的url总数量：", len(self.items_url_list)
                    # print "获取的总url：", self.items_url_list
                    # print "-------------------------------"
                    driver.close()
            except Exception, e:
                logging.info(str(Exception) + str(e))
                # print Exception, e

    def save_url(self):
        file_handle = open('url_all.txt', mode='w+')
        self.items_url_list = list(set(self.items_url_list))  # 去重
        for url in self.items_url_list:
            file_handle.write(url)
            file_handle.write('\t')
        file_handle.close()


    def get_data(self):
        # 读存入txt的url
        f = open("url_all_test.txt", 'r')
        items_url_list = f.read().split('\t')
        # 'https://www.youpin898.com/goodInfo?id=46363‘
        url_test = ['https://www.youpin898.com/goodInfo?id=46695','https://www.youpin898.com/goodInfo?id=46363']  # 测试
        # for url in self.items_url_list:
        num_page = 0  # 爬取网页计数器
        for url in items_url_list:
            num_page += 1
            logging.info("爬取网页数："+ str(num_page))
            # print "爬取网页数：", num_page
            try:
                self.options = webdriver.ChromeOptions()
                self.options.binary_location = self.chrome_dir
                driver = webdriver.Chrome(chrome_options=self.options)
                logging.info("当前爬取网页url："+ str(url))
                # print "当前爬取网页url：",url
                driver.get(url)
                time.sleep(1)
                html = etree.HTML(
                    BeautifulSoup(driver.page_source, "html.parser").encode('UTF-8'))
                """获取每一个属性的数据"""
                label_list = html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div')  # 属性分类
                xpath_head = '//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div/label['
                # print logging.info("商品属性个数：" + str(len(label_list[0])))
                # print len(label_list[0])
                for i in range(0, len(label_list[0])-1):
                    time.sleep(1)
                    attribute_one_list = []
                    xpath_temp = xpath_head + str(i+1) + ']'
                    logging.info(str(xpath_temp))
                    # print xpath_temp
                    ac = ActionChains(driver)
                    # ac.move_to_element(driver.find_element_by_xpath(xpath_temp)).perform()
                    ac.click(driver.find_element_by_xpath(xpath_temp)).perform()
                    time.sleep(1)
                    # driver.find_element_by_xpath(xpath_temp).click()
                    # time.sleep(1)
                    goods_items_html = etree.HTML(BeautifulSoup(driver.page_source, "html.parser").decode('utf-8'))
                    """获取商品名称"""
                    goods_name = goods_items_html.xpath(
                         '//*[ @id ="__layout"]/ div / div[3] / div[1] / div[2] / div / div[2] / div[1] / h1/text()')
                    goods_name_name = goods_name[0].replace(' ', '').replace('\n', '')
                    attribute_one_list.append(goods_name_name)
                    logging.info('name:'+ str(goods_name_name))
                    # print 'name:', goods_name_name
                    """获取军规级"""
                    level = goods_items_html.xpath(
                        '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div/div[2]/div[2]/span[2]/span/text()')
                    value = unicode(level[0]).replace(' ', '').replace('/n', '').encode('utf8')
                    level_name = level[0].replace(' ', '').replace('\n', '')
                    attribute_one_list.append(level_name)
                    logging.info('level:'+ str(level_name))
                    # print 'level:', level_name
                    """获取属性名称"""
                    attribute = goods_items_html.xpath(
                        '//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div/label[' + str(i+1) + ']/span[2]/text()')
                    attribute_name = attribute[0].replace(' ', '').replace('\n', '')
                    attribute_one_list.append(attribute_name)
                    logging.info('attribute:'+ str(attribute_name))
                    # print 'attribute:', attribute_name
                    """获取一属性的在租赁总数"""
                    lease_cnt_str = goods_items_html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[1]/text()')
                    num = re.findall("\d+", lease_cnt_str[0])
                    if len(num) > 0:
                        lease_cnt = [int(x) for x in num][0]  # 将str格式的数字转换成int
                    else:
                        lease_cnt = 0
                    attribute_one_list.append(lease_cnt)
                    logging.info('lease_cnt:'+ str(lease_cnt))
                    # print 'lease_cnt:', lease_cnt
                    """获取一属性的在出售总数"""
                    sale_cnt_str = goods_items_html.xpath(
                        '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/text()')
                    num = re.findall("\d+", sale_cnt_str[0])
                    if len(num) > 0:
                        sale_cnt = [int(x) for x in num][0]  # 将str格式的数字转换成int
                    else:
                        sale_cnt = 0
                    attribute_one_list.append(sale_cnt)
                    logging.info('sale_cnt:'+ str(sale_cnt))
                    # print 'sale_cnt:', sale_cnt
                    """获取长短租最低价"""
                    lease_price_s_min = None  # 最小短租价格
                    lease_price_l_min = None  # 最小长租价格
                    if lease_cnt > 0:
                        ac = ActionChains(driver)
                        # ac.move_to_element(driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[1]/div/div/div/div/div[1]/div[1]')).perform()
                        ac.click(driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[1]/div/div/div/div/div[1]/div[1]')).perform()
                        # driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[1]/div/div/div/div/div[1]/div[1]').click()
                        if lease_cnt >= 15:
                            driver.execute_script(js)
                            time.sleep(5)
                        else: # 数量过少不用下滑
                            time.sleep(2)
                        goods_items_html = etree.HTML(BeautifulSoup(driver.page_source, "html.parser").decode('utf-8'))
                        leasesale_div_list = goods_items_html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[9]/ul[1]')
                        leasesale_xpath_head = '//*[ @ id = "__layout"]/div/div[3]/div[1]/div[9]/ul[1]/li['
                        lease_price_s_list = []
                        lease_price_l_list = []
                        logging.info("leasesale_div_list[0]"+ str(len(leasesale_div_list[0])))
                        # print "leasesale_div_list[0]", len(leasesale_div_list[0])
                        if len(leasesale_div_list[0]) > 1:
                            try:
                                for i in range(1, len(leasesale_div_list[0])+1):
                                    try:
                                        lease_xpath_s = leasesale_xpath_head + str(i) + ']/div[6]/div/div[1]/strong/text()'  # 短租价格小path
                                        lease_xpath_l = leasesale_xpath_head + str(i) + ']/div[6]/div/div[2]/strong/text()'  # 长租价格小path
                                        lease_price_s_str = goods_items_html.xpath(lease_xpath_s)
                                        lease_price_l_str = goods_items_html.xpath(lease_xpath_l)

                                        if len(lease_price_s_str) > 0 :
                                            lease_price_s = float(lease_price_s_str[0].replace('\n', '').replace(' ', ''))
                                            lease_price_s_list.append(lease_price_s)
                                        if len(lease_price_l_str) > 0:
                                            lease_price_l = float(lease_price_l_str[0].replace('\n', '').replace(' ', ''))
                                            lease_price_l_list.append(lease_price_l)
                                    except:
                                        pass
                                if len(lease_price_s_list):
                                    lease_price_s_min = min(lease_price_s_list)
                                else:
                                    lease_price_s_min = None
                                if len(lease_price_l_list):
                                    lease_price_l_min = min(lease_price_l_list)
                                else:
                                    lease_price_s_min = None
                            except:
                                pass
                    attribute_one_list.append(lease_price_s_min)
                    attribute_one_list.append(lease_price_l_min)
                    logging.info("lease_price_s_min"+ str(lease_price_s_min ))  # 最小短租价格
                    logging.info("lease_price_l_min"+ str(lease_price_l_min ))  # 最小长租价格
                    # print "lease_price_s_min", lease_price_s_min # 最小短租价格
                    # print "lease_price_l_min", lease_price_l_min # 最小短租价格
                    """获取出售最低价"""
                    sale_price_min = None  # 最小短租价格
                    if sale_cnt > 0:
                        time.sleep(2)
                        ac = ActionChains(driver)
                        # ac.move_to_element(
                        #     driver.find_element_by_xpath(
                        #         '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[2]')).perform()
                        ac.click(driver.find_element_by_xpath(
                            '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[2]')).perform()
                        # driver.find_element_by_xpath(
                        #     '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[2]').click()
                        if sale_cnt >= 15:
                            driver.execute_script(js)
                            time.sleep(5)
                        else:  # 数量过少不用下滑
                            time.sleep(2)
                        goods_items_html = etree.HTML(BeautifulSoup(driver.page_source, "html.parser").decode('utf-8'))
                        sale_div_list = goods_items_html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[9]/ul[1]')
                        leasesale_xpath_head = '//*[ @ id = "__layout"]/div/div[3]/div[1]/div[9]/ul[1]/li['
                        # sale_price_min = 10000000  # 最小短租价格
                        sale_price_list = []
                        logging.info("sale_div_list:" + str(len(sale_div_list[0])))
                        if len(sale_div_list[0]) > 1:
                            try:
                                for i in range(0, len(sale_div_list[0]) + 1):
                                    try:
                                        sale_xpath = leasesale_xpath_head + str(i + 1) + ']/div[5]/span/span/text()'
                                        sale_price_s_str = goods_items_html.xpath(sale_xpath)
                                        if len(sale_price_s_str) > 0:
                                            sale_price = float(sale_price_s_str[0].replace('\n', '').replace(' ', ''))
                                            sale_price_list.append(sale_price)
                                    except:
                                        pass
                                if len(sale_price_list) > 0:
                                    sale_price_min = min(sale_price_list)
                            except Exception, e:
                                logging.info(str(Exception) + str(e))
                                # print Exception, e
                    attribute_one_list.append(sale_price_min)
                    logging.info("sale_price_s_min"+ str(sale_price_min))
                    # print "sale_price_s_min", sale_price_min  # 出售最低价格
                    """获取成交记录总数"""
                    time.sleep(1)
                    if lease_cnt > 0 or lease_cnt > 0:
                        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[1]/div/div/div/div/div[1]/div[4]').click()
                        saled_div_list = goods_items_html.xpath(
                            '// *[ @ id = "__layout"] / div / div[3] / div[1] / div[7] / div / div[1] / div[3] / div[1] / ul')
                        attribute_one_list.append(len(saled_div_list[0])-1)  # 获取成交总量
                        logging.info("saled_cnt"+ str(len(saled_div_list[0])-1))
                        # print "saled_cnt", len(saled_div_list[0])-1
                    else:
                        attribute_one_list.append(0)
                        logging.info("saled_cnt:"+ str(0))
                        # print "saled_cnt:", 0
                    self.attribute_all_list.append(attribute_one_list)
                    logging.info("###############")
                    # print "##########"


                # """点statTrak属性"""
                time.sleep(1)
                xpath_star = xpath_head + str(len(label_list[0])) + ']'
                ac = ActionChains(driver)
                # ac.move_to_element(driver.find_element_by_xpath(xpath_star)).perform()
                ac.click(driver.find_element_by_xpath(xpath_star)).perform()

                # driver.find_element_by_xpath(xpath_star).click()
                time.sleep(1)
                html = etree.HTML(
                    BeautifulSoup(driver.page_source, "html.parser").encode('utf-8'))
                label_list = html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div')  # 属性分类
                for i in range(0, len(label_list[0]) - 1):
                    time.sleep(1)
                    attribute_one_list = []
                    xpath_temp = xpath_head + str(i + 1) + ']'
                    logging.info(str(xpath_temp))
                    # print xpath_temp
                    ac = ActionChains(driver)
                    # ac.move_to_element(driver.find_element_by_xpath(xpath_temp)).perform()
                    ac.click(driver.find_element_by_xpath(xpath_temp)).perform()
                    time.sleep(1)
                    # driver.find_element_by_xpath(xpath_temp).click()
                    # time.sleep(1)
                    goods_items_html = etree.HTML(BeautifulSoup(driver.page_source, "html.parser").decode('utf-8'))
                    """获取商品名称"""
                    goods_name = goods_items_html.xpath(
                        '//*[ @id ="__layout"]/ div / div[3] / div[1] / div[2] / div / div[2] / div[1] / h1/text()')
                    goods_name_name = goods_name[0].replace(' ', '').replace('\n', '')
                    attribute_one_list.append(goods_name_name)
                    logging.info('name:'+ str(goods_name_name))
                    # print 'name:', goods_name_name
                    """获取军规级"""
                    level = goods_items_html.xpath(
                        '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div/div[2]/div[2]/span[2]/span/text()')
                    value = unicode(level[0]).replace(' ', '').replace('/n', '').encode('utf8')
                    level_name = level[0].replace(' ', '').replace('\n', '')
                    attribute_one_list.append(level_name)
                    logging.info('level:'+ str(level_name))
                    # print 'level:', level_name
                    """获取属性名称"""
                    attribute = goods_items_html.xpath(
                        '//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div/label[' + str(i + 1) + ']/span[2]/text()')
                    attribute_name = attribute[0].replace(' ', '').replace('\n', '')
                    attribute_one_list.append(attribute_name)
                    logging.info('attribute:'+ str(attribute_name))
                    # print 'attribute:', attribute_name
                    """获取一属性的在租赁总数"""
                    lease_cnt_str = goods_items_html.xpath(
                        '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[1]/text()')
                    num = re.findall("\d+", lease_cnt_str[0])
                    if len(num) > 0:
                        lease_cnt = [int(x) for x in num][0]  # 将str格式的数字转换成int
                    else:
                        lease_cnt = 0
                    attribute_one_list.append(lease_cnt)
                    logging.info('lease_cnt:'+ str(lease_cnt))
                    # print 'lease_cnt:', lease_cnt
                    """获取一属性的在出售总数"""
                    sale_cnt_str = goods_items_html.xpath(
                        '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/text()')
                    num = re.findall("\d+", sale_cnt_str[0])
                    if len(num) > 0:
                        sale_cnt = [int(x) for x in num][0]  # 将str格式的数字转换成int
                    else:
                        sale_cnt = 0
                    attribute_one_list.append(sale_cnt)
                    logging.info('sale_cnt:'+ str(sale_cnt))
                    # print 'sale_cnt:', sale_cnt
                    """获取长短租最低价"""
                    lease_price_s_min = None  # 最小短租价格
                    lease_price_l_min = None  # 最小长租价格
                    if lease_cnt > 0:
                        ac = ActionChains(driver)
                        # ac.move_to_element(driver.find_element_by_xpath(
                        #     '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[1]/div/div/div/div/div[1]/div[1]')).perform()
                        ac.click(driver.find_element_by_xpath(
                            '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[1]/div/div/div/div/div[1]/div[1]')).perform()
                        # driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[1]/div/div/div/div/div[1]/div[1]').click()
                        if lease_cnt >= 15:
                            driver.execute_script(js)
                            time.sleep(5)
                        else:  # 数量过少不用下滑
                            time.sleep(2)
                        goods_items_html = etree.HTML(BeautifulSoup(driver.page_source, "html.parser").decode('utf-8'))
                        leasesale_div_list = goods_items_html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[9]/ul[1]')
                        leasesale_xpath_head = '//*[ @ id = "__layout"]/div/div[3]/div[1]/div[9]/ul[1]/li['
                        lease_price_s_list = []
                        lease_price_l_list = []
                        logging.info("leasesale_div_list[0]"+ str(len(leasesale_div_list[0])))
                        # print "leasesale_div_list[0]", len(leasesale_div_list[0])
                        if len(leasesale_div_list[0]) > 1:
                            try:
                                for i in range(1, len(leasesale_div_list[0]) + 1):
                                    try:
                                        lease_xpath_s = leasesale_xpath_head + str(
                                            i) + ']/div[6]/div/div[1]/strong/text()'  # 短租价格小path
                                        lease_xpath_l = leasesale_xpath_head + str(
                                            i) + ']/div[6]/div/div[2]/strong/text()'  # 长租价格小path
                                        lease_price_s_str = goods_items_html.xpath(lease_xpath_s)
                                        lease_price_l_str = goods_items_html.xpath(lease_xpath_l)

                                        if len(lease_price_s_str) > 0:
                                            lease_price_s = float(
                                                lease_price_s_str[0].replace('\n', '').replace(' ', ''))
                                            lease_price_s_list.append(lease_price_s)
                                        if len(lease_price_l_str) > 0:
                                            lease_price_l = float(
                                                lease_price_l_str[0].replace('\n', '').replace(' ', ''))
                                            lease_price_l_list.append(lease_price_l)
                                    except:
                                        pass
                                if len(lease_price_s_list):
                                    lease_price_s_min = min(lease_price_s_list)
                                else:
                                    lease_price_s_min = None
                                if len(lease_price_l_list):
                                    lease_price_l_min = min(lease_price_l_list)
                                else:
                                    lease_price_s_min = None
                            except:
                                pass
                    attribute_one_list.append(lease_price_s_min)
                    attribute_one_list.append(lease_price_l_min)
                    logging.info("lease_price_s_min" + str(lease_price_s_min))  # 最小短租价格
                    logging.info("lease_price_l_min" + str(lease_price_l_min))  # 最小长租价格
                    # print "lease_price_s_min", lease_price_s_min  # 最小短租价格
                    # print "lease_price_l_min", lease_price_l_min  # 最小短租价格
                    """获取出售最低价"""
                    sale_price_min = None # 最小短租价格
                    if sale_cnt > 0:
                        time.sleep(2)
                        ac = ActionChains(driver)
                        # ac.move_to_element(
                        #     driver.find_element_by_xpath(
                        #         '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[2]')).perform()
                        ac.click(driver.find_element_by_xpath(
                            '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[2]')).perform()
                        # driver.find_element_by_xpath(
                        #     '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[2]').click()
                        if sale_cnt >= 15:
                            driver.execute_script(js)
                            time.sleep(5)
                        else:  # 数量过少不用下滑
                            time.sleep(2)
                        goods_items_html = etree.HTML(BeautifulSoup(driver.page_source, "html.parser").decode('utf-8'))
                        sale_div_list = goods_items_html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[9]/ul[1]')
                        leasesale_xpath_head = '//*[ @ id = "__layout"]/div/div[3]/div[1]/div[9]/ul[1]/li['
                        sale_price_list = []
                        logging.info("sale_div_list:"+ str(len(sale_div_list[0])))
                        # print "sale_div_list:", len(sale_div_list[0])
                        if len(sale_div_list[0]) > 1:
                            try:
                                for i in range(0, len(sale_div_list[0]) + 1):
                                    try:
                                        sale_xpath = leasesale_xpath_head + str(i + 1) + ']/div[5]/span/span/text()'
                                        sale_price_s_str = goods_items_html.xpath(sale_xpath)
                                        if len(sale_price_s_str) > 0:
                                            sale_price = float(sale_price_s_str[0].replace('\n', '').replace(' ', ''))
                                            sale_price_list.append(sale_price)
                                    except:
                                        pass
                                if len(sale_price_list) > 0:
                                    sale_price_min = min(sale_price_list)
                            except Exception, e:
                                logging.info(str(Exception) + str(e))
                                # print Exception, e
                    attribute_one_list.append(sale_price_min)
                    logging.info("sale_price_s_min"+ str(sale_price_min))
                    # print "sale_price_s_min", sale_price_min  # 出售最低价格
                    """获取成交记录总数"""
                    time.sleep(1)
                    if lease_cnt > 0 or lease_cnt > 0:
                        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[1]/div/div/div/div/div[1]/div[4]').click()
                        saled_div_list = goods_items_html.xpath(
                            '// *[ @ id = "__layout"] / div / div[3] / div[1] / div[7] / div / div[1] / div[3] / div[1] / ul')
                        attribute_one_list.append(len(saled_div_list[0])-1)  # 获取成交总量
                        logging.info("saled_cnt"+ str(len(saled_div_list[0])-1))
                        # print "saled_cnt", len(saled_div_list[0])-1
                    else:
                        attribute_one_list.append(0)
                        logging.info("saled_cnt"+ str(0))
                        # print "saled_cnt", 0
                    self.attribute_all_list.append(attribute_one_list)
                    logging.info("#################")
                    # print "##########"

                logging.info("attribute_all_list:"+ str(self.attribute_all_list))
                # print "attribute_all_list:", self.attribute_all_list
                # mysql操作
                # insert_sql = ''
                # insert_sql += '\'' + level[0].replace(' ','').replace('\n','') + '\'' + ','
                # insert_sql = insert_sql[0:-1]
                # self.mysql.insert_data('test', insert_sql)
                # for i in self.attribute_all_list:
                #     insert_sql = ''
                #     for j in i:
                #         for k in j:
                #             insert_sql += '\'' + k + '\'' + ','
                #         insert_sql = insert_sql[0:-1]
                #     print insert_sql
                #     # self.mysql.insert_data('csgo_info', insert_sql)

            except Exception,e:
                print Exception,e

    def save_data_excel(self):
        excel_name = str(datetime.now().strftime('%Y%m%d%H')) +'.xlsx'
        df = pd.DataFrame(self.attribute_all_list)
        # print "pandas", df
        writer = pd.ExcelWriter(excel_name)
        df.to_excel(writer, encoding='utf_8')
        writer.save()


if __name__ == '__main__':
    getData = GetData()
    # getData.get_category_info_url()
    # getData.save_url()
    getData.get_data()
    getData.save_data_excel()
    # os.system('shutdown -s -t 1')
