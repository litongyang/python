# -*- coding: utf-8 -*-
# import json
#
# import requests
#
# headers = {'accept': 'application/json, text/plain, */*',
#            'accept - Encoding': 'gzip, deflate, br',
#            'accept-Language': 'zh-CN,zh;q=0.9',
#            'origin':'https://www.youpin898.com',
#            'referer':'https://www.youpin898.com/',
#            # 'Connection': 'Keep-Alive',
#            # 'Host': 'zhannei.baidu.com',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
#            'Content-Type': 'application/json;charset=UTF-8'
#            }
# url = 'https://www.youpin898.com/market/csgo?gameId=730&weapon=weapon_knife_karambit'
# params = {"listType":"30","gameId":"730","weapon":"weapon_knife_falchion","pageIndex":1,"pageSize":20,"sortType":"0","listSortType":"2"}
# r = requests.post(url, headers=headers, params=json.dumps(params))
# print r.text
# print r.json()
import requests

headers = {
    'authority': 'api.youpin898.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
    'apptype': '1',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.youpin898.com',
    'pragma': 'no-cache',
    'referer': 'https://www.youpin898.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
}
max_page = 10

for i in range(max_page):
    data = '{"listType":"30","gameId":"730","weapon":"weapon_scar20","pageIndex":'+str(i)+',"pageSize":20,"sortType":"0","listSortType":"2"}'
    lists = []
    response = requests.post('https://api.youpin898.com/api/homepage/es/template/GetCsGoPagedList', headers=headers,
                             data=data).json()
    # print len(response['Data'])
    print data
    for i in response['Data']:
        print(i['CommodityName'])
        # print(i['Id'])
        # print(i['LeaseDeposit'])
