#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: crawlerDemo.py
# @time: 2018/8/7 16:25
# @desc: 爬取煎蛋网

import os
import requests
from bs4 import BeautifulSoup


# 创建文件
def create_dir(name):
    # 创建文件目录
    if not os.path.exists(name):
        os.makedirs(name)


# 打开网页
def execute(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    return r.text


# 初始化方法
def main():
    # 创建文件目录
    # create_dir("煎蛋")
    # 网页页码
    # 循环打开网页
    for page in range(1, 2):
        print("正在访问第{}页....".format(page))
        url = "http://jandan.net/ooxx/page-{}".format(page)
        print(url)
        page_html = execute(url)
        soup = BeautifulSoup(page_html, 'html.parser')
        pic_list = soup.find_all('li', class_='wp-item')
        print(pic_list)
        page += 1


# 程序入口
if __name__ == "__main__":
    main()
