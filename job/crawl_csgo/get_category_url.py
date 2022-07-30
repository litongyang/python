# -*- coding: utf-8 -*-
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
"""
获取游戏商品细分品类url
"""


class GetGoodsCategoryUrl:
    def __init__(self):
        self.url = "https://api.youpin898.com/api/v2/commodity/Tag/GetCsGoWeaponList"
        self.headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
                        'Accept - Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
                        'Connection': 'Keep-Alive',
                        'Host': 'zhannei.baidu.com',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
        self.json_data = ''
        self.category_url = []
        self.goods_category_url = []
        self.url_head = 'https://www.youpin898.com/market/csgo?gameId=730&'
        self.goods_query_list = []


    def get_goods_category_url(self):
        self.json_data = json.loads(requests.get(self.url).text)
        # print self.json_data
        for key, category_name in self.json_data.items():
            if key == 'Data':
                for category_item in category_name:
                    for key1, query in category_item.items():
                        if key1 == 'Name':
                            if query == '其他' or query == '印花':
                                break
                        if key1 == 'Children':
                            for child in query:
                                for key2, goods_query in child.items():
                                    if key2 == 'Name':
                                        if goods_query == '不限':
                                            break
                                    if key2 == 'QueryString':
                                        if len(goods_query) > 0:
                                            goods_query = goods_query[0].lower() + goods_query[1:]  # 首字母变小写
                                            self.goods_query_list.append(goods_query.replace('weapon=', ''))
                                            self.goods_category_url.append(str(self.url_head) + str(goods_query))
        # return self.goods_category_url
        return self.goods_query_list



if __name__ == '__main__':
    getGoodsUrl = GetGoodsCategoryUrl()
    getGoodsUrl.get_goods_category_url()
    print len(getGoodsUrl.goods_category_url)
    print getGoodsUrl.goods_category_url
    print getGoodsUrl.goods_query_list