#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: connectionPDF.py
# @time: 2018/8/2 19:42
# @desc: 将多个PDF文件生成成一个PDF

import PyPDF2


path = "C:\\Users\\user\\Desktop\\pdf"
fileNames = ["债权系统文档V1.0.pdf", "债权接口_3.1.pdf"]

merger = PyPDF2.PdfFileMerger()
for file_name in fileNames:
    merger.append(PyPDF2.PdfFileReader(path + "\\" + file_name))

merger.write(path + "\\Demo.pdf")
