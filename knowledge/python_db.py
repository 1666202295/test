#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: python_db.py
# @time: 2018/8/9 15:08
# @desc: python 连接数据库
import pymysql

# 数据库地址
host = "localhost"
# 用户名
user = "admin"
# 密码
password = "admin"
# 数据库
db = "python"
# 端口号
port = 3306
# 编码格式
charset = "utf8"


# 获取数据库连接和游标
def get_conn():
    # 获取数据库连接
    conn = pymysql.connect(host=host, user=user, db=db, passwd=password, port=port, charset=charset)
    # 获取游标
    cur = conn.cursor()
    return conn, cur


# 执行语句
def execute_sql(execute_sql):
    conn, cur = get_conn()
    # 执行查询
    cur.execute(execute_sql)
    # 获取查询结果
    data = cur.fetchall()
    for i in range(len(data)):
        print(data[i])


def close(conn, cur):
    # 提交事务
    conn.commit()
    # 关闭游标
    cur.close()
    # 释放数据库资源
    conn.close()


sql = "select * from base_info"
execute_sql(sql)

