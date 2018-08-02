#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: operationPDF.py
# @time: 2018/8/2 19:42
# @desc: 将多个PDF文件生成成一个PDF

import PyPDF2


# 将两个PDF文件合并
def connection():
    path = "..\\resources\\demoFile\\pdf\\"
    file_names = ["找一个频率相同的人.pdf", "每天给你一颗糖.pdf"]
    merger = PyPDF2.PdfFileMerger()
    for file_name in file_names:
        merger.append(PyPDF2.PdfFileReader(path + file_name))

    merger.write(path + "connection.pdf")


connection()




