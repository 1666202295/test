#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: crawler.py
# @time: 2018/8/2 16:33
# @desc: 爬虫案例 爬取妹子图


import requests
import os
from bs4 import BeautifulSoup
import time


# 用于下载页面
def download_page(url):
    print("下载界面:{}".format(url))
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    r.encoding = 'gb2312'
    return r.text


def get_pic_list(html):
    # 获取每个页面的套图列表,之后循环调用get_pic函数获取图片
    print("获取图片列表")
    soup = BeautifulSoup(html, 'html.parser')
    div_page = soup.find("div", class_="picnew clearfix")
    pic_list = div_page.find("ul").find_all("li")
    for i in pic_list:
        a_tag = i.find('a')
        link = a_tag.get('href')
        get_pic(link)


# 获取当前页面的图片,并保存
def get_pic(link):
    print("下载图片")
    html = download_page(link)  # 下载界面
    soup = BeautifulSoup(html, "html.parser")
    div_page = soup.find("div", class_="postContent")
    pic_list = div_page.find_all("img")  # 找到界面所有图片
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    for i in pic_list:
        pic_link = i.get('src')  # 拿到图片的具体 url
        print("开始下载:{}".format(pic_link))
        try:
            r = requests.get(pic_link, headers=headers, timeout=20)  # 下载图片，之后保存到文件
            # 判断后缀名,只有png和jpg的文件才下载
            file_name = str(pic_link.split('/')[-1])
            suffix_name = file_name.split(".")[-1]
            if suffix_name == "png" or suffix_name == "jpg":
                with open('pic/{}'.format(str((time.time()))) + file_name, 'wb') as f:
                    f.write(r.content)
                    print("下载成功:{}".format(pic_link))
                    time.sleep(1)  # 休息一下，不要给网站太大压力，避免被封
        except Exception:
            print("{}下载出错了".format(pic_link))


def create_dir(name):
    # 创建文件目录
    if not os.path.exists(name):
        os.makedirs(name)


def execute(url):
    page_html = download_page(url)
    get_pic_list(page_html)


def main():
    create_dir('pic')
    queue = [i for i in range(0, 72)]  # 构造 url 链接 页码。
    while len(queue) > 0:
        cur_page = queue.pop(0)
        if cur_page == 0:
            print("正在下载首页")
            url = "http://meizitu.com"
            execute(url)
            print("首页下载完成".format(cur_page))
            print()
        else:
            print('正在下载{}页'.format(cur_page))
            url = 'http://meizitu.com/a/more_{}.html'.format(cur_page)
            execute(url)
            print("第{}页下载完成".format(cur_page))
            print()

    print("爬取完成了")


if __name__ == '__main__':
    main()
