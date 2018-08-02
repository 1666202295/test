#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: python_exception.py
# @time: 2018/8/2 12:46
# @desc:  python中的异常

"""
打印图形框 如下:
xxxxxx
x    x
xxxxxx

********
*      *
*      *
********

"""

# 可以通过logging.CRITICAL 关闭所有日志的输出
# logging.disable(logging.CRITICAL)

import getLogger

logger = getLogger.get_log()


def box_print(symbol, width, height):
    # 我们发现,width 和 height 必须为大于2的值, symbol 必须为一个字符,才能打印出一个完整的箱子

    # 增加判定,如果width 和 height 不大于2,则抛出异常,symbol 长度不等于 1 则抛出异常
    if len(symbol) != 1:
        logger.debug("symbol 的长度不为1")
        raise Exception("symbol 的长度必须为1")
    if width <= 2:
        logger.debug("width 不大于2")
        raise Exception("width 必须大于2")
    if height <= 2:
        logger.debug("height 不大于2")
        raise Exception("height 必须大于2")

    # 第一行打印 width 个 标识符
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)

    print(symbol * width)


# 使用 try except 来捕捉可能出现的异常
for sys, w, h in (("*", 4, 4), ("#", 1, 2), ("II", 1, 2)):
    try:
        box_print(sys, w, h)
        print("程序没有抛出异常")
    except Exception:
        print("出错了")
    finally:
        print("程序运行完成")




