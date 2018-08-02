#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: python_assert.py
# @time: 2018/8/2 19:17
# @desc: assert为断言判断 表示必须满足某些条件
# 程序实现: 输入RGB 并分别赋值打印 而程序中参数并没有传递R,运行后会报错找不到红色

wood_hill = {"G": "122", "B": "100"}


def switch_lights(stoplight):
    assert "R" in stoplight.keys(), "没有找到红色" + str(stoplight)
    for key in stoplight.keys():
        if stoplight[key] == "G":
            green = stoplight[key]
        elif stoplight[key] == "B":
            blue = stoplight[key]
        elif stoplight[key] == "R":
            red = stoplight[key]
        print(green, blue, red)


# 如果 assert 没有通过校验,则会报错
# AssertionError: 没有找到红色{'G': 'green', 'B': 'blue'}
switch_lights(wood_hill)
