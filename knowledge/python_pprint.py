#!/usr/bin/env python
# encoding: utf-8
'''
@author: 曹会金
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: python_pprint.py
@time: 2018/7/27 10:34
@desc: 在本地生成py文件来存储信息
'''

import pprint

cats = [{"name": "Garfield", "desc": "chubby"}, {"name": "Tom", "desc": "naughty"}]

s = pprint.pformat(cats)

with open("../content/myCats.py", "w") as filedObj:
    filedObj.write("cats = " + s + "\n")
