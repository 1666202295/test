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
def connection(path, file_names, new_pdf_name):
    # 创建pdf操作对象
    merger = PyPDF2.PdfFileMerger()
    # 循环文件
    for file_name in file_names:
        # 将pdf文件添加到pdf操作对象
        merger.append(PyPDF2.PdfFileReader(path + file_name))
    # 输出新生成的问题件
    merger.write(path + new_pdf_name)


# 给pdf指定页添加水印
def add_wager_mark(page_num, pdf_path, water_path, new_pdf_path):
    # 读入原始pdf文件
    with open(pdf_path, "rb") as pdfFile:
        pdf_reader = PyPDF2.PdfFileReader(pdfFile)
        # 获取指定页
        page = pdf_reader.getPage(page_num)
        # 读入水印文件
        with open(water_path, "rb") as markFile:
            water_reader = PyPDF2.PdfFileReader(markFile)
            # 水印文件只有一页,所以直接获取0
            water_page = water_reader.getPage(0)
            # 合并两页对象
            page.mergePage(water_page)
            # 新PDF文件对象
            new_pdf_file_writer = PyPDF2.PdfFileWriter()
            # 将生成后的第一页文件加入到新PDF文件对象
            new_pdf_file_writer.addPage(page)
            # page_num已经手动添加,所以从page_num + 1页开始循环添加到新PDF对象
            for num in range(page_num + 1, pdf_reader.numPages):
                page_obj = pdf_reader.getPage(num)
                new_pdf_file_writer.addPage(page_obj)
            # 写出到新文件
            with open(new_pdf_path, "wb") as newPDFFile:
                new_pdf_file_writer.write(newPDFFile)


resourcesPath = "..\\resources\\demoFile\\pdf\\"

pdfFileNames = ["找一个频率相同的人.pdf", "每天给你一颗糖.pdf"]
newPdfName = "connection.pdf"
connection(resourcesPath, pdfFileNames, newPdfName)

pafPath = resourcesPath + "找一个频率相同的人.pdf"
pageNum = 0
wagerPath = resourcesPath + "watermark.pdf"
newPdfName = resourcesPath + "addWaterMark.pdf"
add_wager_mark(pageNum, pafPath, wagerPath, newPdfName)




