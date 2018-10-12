#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: get_log.py
# @time: 2018/9/25 11:15
# @desc: 处理日志
import withFile

# 文件的操作是用os
root_dir = 'C:\\Users\\user\\Desktop\\'
log_path = "paymentcenterweb_26.log"

with open(root_dir + log_path, mode="r", encoding='UTF-8') as heine:
    num = 0
    line = heine.readline()
    content = ""
    while line:
        num += 1
        content += line
        line = heine.readline()
        if num % 10000 == 0:
            # 每万条日志,生成一个文件
            path = root_dir + "26_web\\web_26_1_" + str(num/10000) + ".txt"
            withFile.with_file_a(content, path)
            content = ""

    if len(content) > 0:
        # 最后还有文件不足100000条没有写入,则写入最后一个文件中
        path = root_dir + "26_web\\web_26_1_" + str(num / 10000) + ".txt"
        withFile.with_file_a(content, path)



