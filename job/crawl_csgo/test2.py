# -*- coding: utf-8 -*-
import requests
data = {'k':'v'}
url = "https://www.lexico.com/list/0/2?locale=en"
headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               'ContentType':'application/json',
               # 'Host':'zhannei.baidu.com',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
response = requests.post('https://api.youpin898.com/api/homepage/es/template/GetCsGoPagedList', headers=headers, data=data)
print response.content




