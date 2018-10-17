#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: mysql.py
# @time: 2018/10/12 18:47
# @desc: 连接数据库

# 驱动包
import pymysql
# 连接池包
from DBUtils.PooledDB import PooledDB
# 日志对象
from libraryRoot import getLogger

# 连接数据库
pool = PooledDB(pymysql, 5, host='172.16.10.22', user='wzd-prod', passwd='(6Fl3WI1162JwUx', db='wzd', port=3306)

# 获取连接对象
conn = pool.connection()

logger = getLogger.get_log()


def execute_sql(sql):
    logger.info(sql)
    # 获取游标
    cursor = conn.cursor()

    # 使用execute()执行sql语句
    cursor.execute(sql)

    index = cursor.description

    # 结果集
    result = []
    # 使用fetall()获取全部数据
    for res in cursor.fetchall():
        row = {}
        for i in range(len(index) - 1):
            row[index[i][0]] = res[i]
        result.append(row)

    logger.info(sql + ",result = " + str(result))

    # 关闭游标和数据库的连接
    cursor.close()
    return result

