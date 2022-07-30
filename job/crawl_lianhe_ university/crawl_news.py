# coding=utf-8
import requests
from selenium import webdriver
from lxml import etree
import re
from zhon.hanzi import punctuation
import jieba
import wordcloud
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# reqs = requests.get(url,header=headers)
# html = etree.HTML(reqs.text)



class CrawlNews:
    def __init__(self):
        self.url = 'https://www.buu.edu.cn/'
        self.header = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
                       'Accept - Encoding':'gzip, deflate',
                       'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
                       'Connection':'keep-alive',
                       'Host':'www.buu.edu.cn',
                       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
        self.options = webdriver.ChromeOptions()
        self.chrome_dir = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Chrome驱动安装本地地址
        self.content = ''
        self.news_list = []

    def get_news_url(self):
        """
        获取新闻urllist
        :return:
        """
        response = requests.get(self.url, headers=self.header, timeout=3)
        response.encoding = response.apparent_encoding
        # print response.text
        html = etree.HTML(response.text)
        # // *[ @ id = "barrierfree_container"] / div[4] / div / div[3] / ul / li[1] / a
        news_list_xpath = '//*[@id="barrierfree_container"]/div[2]/div/div[3]/ul'
        news_list = html.xpath(news_list_xpath)
        news_url_list = []
        print len(news_list[0])
        # // *[ @ id = "barrierfree_container"] / div[2] / div / div[3] / ul / li[1] / a
        news_xpath_head = '//*[@id="barrierfree_container"]/div[2]/div/div[3]/ul/li['
        for i in range(0, len(news_list[0])):
            news_xpath = news_xpath_head + str(i+1) + ']/a/@href'
            news_url = html.xpath(news_xpath)
            print news_url[0]
            self.news_list.append(news_url[0])
        print "新闻数量：", len(self.news_list)

    def get_content(self):
        """
        获取新闻所以文本
        :return:
        """
        # url_test = ['https://news.buu.edu.cn/art/2022/5/10/art_13588_676916.html']  # 测试
        file_handle = open('test.txt', 'a')
        for news_url in self.news_list:
            print news_url

            self.options = webdriver.ChromeOptions()
            self.options.binary_location = self.chrome_dir
            driver = webdriver.Chrome(chrome_options=self.options)
            driver.get(news_url)
            news_xpath = '//*[@id="barrierfree_container"]/table[6]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td/table[1]/tbody/tr[3]'
            news = driver.find_element_by_xpath(news_xpath,)
            file_handle.write(news.text)

    def data_clean(self):
        """
        数据清洗，构造纯中文本
        :return:
        """
        f = open('test.txt', 'r')
        self.content = f.read()
        """去除中文标点"""
        for i in punctuation:
            self.content = self.content.replace(i, '')
        """去除英文字母"""
        self.content = re.sub('[a-zA-Z]', '', self.content)
        """去除数字"""
        self.content = re.sub('[0-9]', '', self.content)
        """去除英文标点"""
        punc = u'!"#$%&’()*+,-./:;<=>?@[]^_`{|}~'
        self.content = re.sub(r"[{}]+".format(punc), '', self.content)
        """去除特殊字符"""
        self.content =  self.content.replace('/', '').replace('.', '').replace('\n','').replace(':', '').replace('-', '')
        print self.content

    def text_minning(self, text):
        """
        文本挖掘，求词频
        :return:
        """
        result = jieba.lcut(text)
        extend_list = ['的', '和', '在','是', '了','与']  #  删除一些连接词
        text_train = ret = [ i for i in result if i not in extend_list ]
        # print text_train
        # 输出结果：<class 'list'>
        wordcount = Counter(text_train)
        # print dict(wordcount)
        # pandas 数据分析
        df = pd.DataFrame.from_dict(wordcount,orient='index').reset_index()
        df.columns = ['a', 'b']
        pandas_data = df.sort_values('b', ascending=False).head(10)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'
        plt.bar(pandas_data['a'], pandas_data['b'], color='#87CEFA')
        plt.title("Top 10 words")
        plt.show()
        for i in range(len(wordcount.most_common(10))):
            print"词频第%d名："%(i+1), wordcount.most_common(10)[i][0]

        # txt = " ".join(text_train)
        # cloud = wordcloud.WordCloud(width=2000, height=1400, font_path="msyh.ttc")  # 设置图片宽度、高度、字体
        # cloud.generate(txt)
        # cloud.to_file(r'wordcloud.png')  # 词云图片



    def data_analysis(self):
        pass



if __name__ == '__main__':
    crawlNews = CrawlNews()
    # crawlNews.get_news_url()
    # crawlNews.get_content()
    crawlNews.data_clean()
    crawlNews.text_minning(crawlNews.content)
