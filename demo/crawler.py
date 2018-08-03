#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: crawler.py
# @time: 2018/8/2 16:33
# @desc: 爬虫案例 爬取煎蛋妹子图

# 爬取地址:http://jandan.net/ooxx


from urllib import request
from bs4 import BeautifulSoup


url = "http://jandan.net/ooxx"
html = request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html)
print(soup.prettify())
for link in soup.find_all("img"):
    print(link.get('href'))

