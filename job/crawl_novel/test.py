# coding=utf-8
import requests
from lxml import etree
import re
import io
from fontTools.ttLib import TTFont


# def get_html_woff():
#     # 保存html文档
# url = "https://book.qidian.com/info/1011705052"
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
# }
# response = requests.get(url, headers=headers).text


def new_html(old_html):
    print type(old_html)
    font = {}
    font[100506] = 'three'
    font[100499] = 'seven'
    font[100507] = 'period'
    font[100504] = 'one'
    font[100501] = 'four'
    font[100498] = 'five'
    font[100500] = 'nine'
    font[100501] = 'four'
    new_value = {}
    d = {}

    woff_dict = {'.notdef': ' ', 'period': '.', 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                 'six': 6,
                 'seven': 7, 'eight': 8, 'nine': 9}
    # 键和值反转
    for key, value in font.items():
        d[value] = key

    # 组成新的字典
    for i in woff_dict:
        for j in d:
            if i == j:
                new_value.update({"&#" + str(d[j]) + ";": woff_dict[i]})
    for k,v in new_value.items():
        print k,v
    # txt = io.open("aa.html", "r", encoding="utf-8").read()

    for ch in new_value.items():
        # print str(ch[0])
        # print str(ch[1])
        response = old_html.replace(str(ch[0]), str(ch[1]))

    new_html = io.open("new.html", 'w', encoding='utf-8')
    new_html.write(response)


if __name__ == '__main__':
    url = "https://book.qidian.com/info/1011705052"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    }
    response = requests.get(url, headers=headers).text
    print("[***]正在解析...")
    new_html(response)
    print("[***]解析成功...")
