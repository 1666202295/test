#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: python_closePackage.py
# @time: 2018/9/7 20:00
# @desc: python 中的闭包
# python 中的闭包是指在函数中有声明了函数,并把这个函数当做返回值返回


def test(x):
    # 声明了一个test1函数
    def test1(params):
        print(params)

    # 将test1返回
    return test1


# 调用test函数获取返回值test1 并用result接收
test1 = test()
test1(123)

