#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: getLogger.py
# @time: 2018/8/2 13:42
# @desc: 获取logger对象通用方法
import logging.handlers

# 日志文件路径
LOG_FILE = '..\\resources\\log\\myLog.txt'


def get_log():

    # 实例化handler
    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
    # 设置输出格式
    fmt = '%(asctime)s - %(levelname)s - %(message)s'
    # 实例化formatter
    formatter = logging.Formatter(fmt)
    # 为handler添加formatter
    handler.setFormatter(formatter)
    # 获取名为tst的logger
    logger = logging.getLogger('tst')
    # 为logger添加handler
    logger.addHandler(handler)
    # 设置bug等级
    logger.setLevel(logging.DEBUG)
    return logger
