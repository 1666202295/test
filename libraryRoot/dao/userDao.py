#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: userDao.py
# @time: 2018/10/12 19:08
# @desc: 用户数据库接口

import libraryRoot.dao.mysql as db


# 主键查询
def get_user(id):
    uid = int(id)
    sql = "select * from user_info WHERE id = " + uid
    return db.execute_sql(sql)


# 手机号查询
def get_user_phone(phone):
    sql = "select * from user_info where phone = '" + phone + "'"
    return db.execute_sql(sql)
