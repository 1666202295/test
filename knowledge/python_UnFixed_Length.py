#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: python_UnFixed_Length.py
# @time: 2018/9/23 12:03
# @desc: 不定长传参


# *表示传递过来的参数会被包装成一个元组使用
def get_sum(*params):
    print(params, type(params))
    result = 0
    for i in params:
        print(i)
        result += i
    print(result)


# ** 表示传递过来的参数会被包装成一个字典使用
def create_user(**params):
    print(params, type(params))
    print(params["name"])


get_sum(1, 2, 3, 4)
create_user(name="joker", sex="男")
