# coding=utf-8
import requests
from lxml import etree
from datetime import datetime

txt_name = 'data_woman_' + '.txt'
file_handle = open(txt_name, mode='w')


class CrawlNovel:
    def __init__(self):
        self.urlListW = ['https://www.jjwxc.net/topten.php?orderstr=7&t=2']  # 女性小说url
        self.header = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
                       'Accept - Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
                       # 'Connection': 'keep-alive',
                       # 'Host': 'www.buu.edu.cn',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
        self.novelUrlW = []  # 女性小说urlist
        self.novelWordsNumW = []  # 女性小说字数list
        self.supportW = []  # 女性小说点赞list

    def get_url_w(self):
        """
        获取女性小说的url和小说字数
        :return:
        """
        for url in self.urlListW:
            print url
            response = requests.get(url, headers=self.header, timeout=3)
            response.encoding = response.apparent_encoding
            html = etree.HTML(response.text)
            # /html/body/table[3]/tbody/tr[2]/td[3]/a
            # /html/body/table[3]/tbody/
            # /html/body/table[3]/tbody/tr[2]/td[7]
            novel_list_xpath = '/html/body/table[3]/tbody'
            novel_list = html.xpath(novel_list_xpath)
            if len(novel_list) > 0:
                for i in range(2, len(novel_list[0]) + 1):
                    novel_xpath_head = '/html/body/table[3]/tbody/tr['
                    novel_url_xpath = novel_xpath_head + str(i) + ']/td[3]/a/@href'
                    novel_wordsNum_xpah = novel_xpath_head + str(i) + ']/td[7]/text()'
                    novel_url = html.xpath(novel_url_xpath)
                    novel_wordsNum = html.xpath(novel_wordsNum_xpah)
                    novel_url_w = 'https://www.jjwxc.net/' + novel_url[0]
                    self.novelUrlW.append(novel_url_w)
                    self.novelWordsNumW.append(novel_wordsNum[0].replace(u'\xa0', ''))
        # print len(self.novelUrlW)
        print self.novelUrlW
        # print len(self.novelWordsNumW)
        print self.novelWordsNumW

    def get_support_w(self):
        """
        获取女性小说的点赞数
        :return:
        """
        urltest = ['https://www.jjwxc.net/onebook.php?novelid=3419133']
        # for url in urltest:
        for url in self.novelUrlW:
            print url
            response = requests.get(url, headers=self.header, timeout=5)
            response.encoding = response.apparent_encoding
            html = etree.HTML(response.text)
            # //*[@id="oneboolt"]/tbody/tr[176]/td/div/span[3]
            # //*[@id="oneboolt"]/tbody
            body_list = html.xpath('//*[@id="oneboolt"]/tbody')
            max_num = len(body_list[0])
            xpath = '//*[@id="oneboolt"]/tbody/tr[' + str(max_num - 1) + ']/td/div/span[3]/text()'
            support_list = html.xpath(xpath)
            self.supportW.append(support_list[0])
        print self.supportW


if __name__ == '__main__':
    crawlNovel = CrawlNovel()
    crawlNovel.get_url_w()
    for i in range(0, len(crawlNovel.novelWordsNumW)):
        file_handle.write(str(crawlNovel.novelWordsNumW[i]))
        file_handle.write('\t')
    file_handle.write('\n')
    crawlNovel.get_support_w()
    for i in range(0, len(crawlNovel.supportW)):
        file_handle.write(str(crawlNovel.supportW[i]))
        file_handle.write('\t')
    file_handle.write('\n')
