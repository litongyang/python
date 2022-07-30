# coding=utf-8
import requests
from lxml import etree
import chardet
from datetime import datetime

txt_name = 'data_man' + '.txt'
file_handle = open(txt_name, mode='w')


class CrawlNovel:
    def __init__(self):
        self.urlListW = ['http://www.zongheng.com/rank/details.html?rt=5&d=0&r=&i=0&c=0&p=1',
                         'http://www.zongheng.com/rank/details.html?rt=5&d=0&r=&i=0&c=0&p=2',
                         'http://www.zongheng.com/rank/details.html?rt=5&d=0&r=&i=0&c=0&p=3',
                         'http://www.zongheng.com/rank/details.html?rt=5&d=0&r=&i=0&c=0&p=4',
                         'http://www.zongheng.com/rank/details.html?rt=5&d=0&r=&i=0&c=0&p=5',
                         'http://www.zongheng.com/rank/details.html?rt=5&d=0&r=&i=0&c=0&p=6',
                         'http://www.zongheng.com/rank/details.html?rt=5&d=0&r=&i=0&c=0&p=7',
                         ]  # 男性小说url
        self.header = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
                       'Accept - Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
                       'Connection': 'keep-alive',
                       'Host': 'www.qidian.com',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
        self.novelUrlM = []  # 男性小说urlist
        self.novelWordsNumM = []  # 男性小说字数list
        self.supportM = []  # 男性小说点赞list

    def get_data_m(self):
        """
        获取男性小说的字数和点击数
        :return:
        """
        for url in self.urlListW:
            print url
            response = requests.get(url, headers=self.header, timeout=3)
            response.encoding = response.apparent_encoding
            html = etree.HTML(response.text)
            # /html/body/div[2]/div[4]/div[2]/div[3]/ul
            novel_list_xpath = '/html/body/div[2]/div[4]/div[2]/div[3]/ul'
            novel_list = html.xpath(novel_list_xpath)

            if len(novel_list) > 0:
                for i in range(1, len(novel_list[0])+1):
                    # /html/body/div[2]/div[4]/div[2]/div[3]/ul/li[1]/span[5]
                    # /html/body/div[2]/div[4]/div[2]/div[3]/ul/li[1]/span[6]
                    novel_xpath_head = '/html/body/div[2]/div[4]/div[2]/div[3]/ul/li['
                    novel_wordsNum_xpath = novel_xpath_head + str(i) + ']/span[5]/text()'
                    novel_surpportNum_xpah = novel_xpath_head + str(i) + ']/span[6]/text()'
                    novel_wordsNum = html.xpath(novel_wordsNum_xpath)
                    novel_surpportNum = html.xpath(novel_surpportNum_xpah)
                    wordsNum = ''
                    for i in range(0, len(novel_wordsNum[0])-1):
                        wordsNum += novel_wordsNum[0][i]
                    self.novelWordsNumM.append(int(wordsNum)*10000)
                    self.supportM.append(int(novel_surpportNum[0]))


        print len(self.novelWordsNumM)
        print "男性小说字数：",self.novelWordsNumM
        print len(self.supportM)
        print "男性小说点击率：",self.supportM



if __name__ == '__main__':
    crawlNovel = CrawlNovel()
    crawlNovel.get_data_m()
    for i in range(0, len(crawlNovel.novelWordsNumM)):
        file_handle.write(str(crawlNovel.novelWordsNumM[i]))
        file_handle.write('\t')
    file_handle.write('\n')
    for i in range(0, len(crawlNovel.supportM)):
        file_handle.write(str(crawlNovel.supportM[i]))
        file_handle.write('\t')
    file_handle.write('\n')
