#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: python_web.py
# @time: 2018/10/12 13:58
# @desc: web 接口 启动后访问 http://127.0.0.1:9090/index/

# 导入bottle包和beaker包的指定模块
# bottle文档 http://www.bottlepy.org/docs/dev/tutorial.html
from bottle import default_app, get, run
from beaker.middleware import SessionMiddleware

# 设置session参数
'''
创建一个session配置的字典，用来存储session的存储类型为文件类型，session过期时间为3600秒，
session文件存放路径为/tmp/sessions/simple （存放在linux系统tmp目录下的文件，系统定期会自动清理）
'''
session_opts = {
     'session.type': 'file',
     'session.cookie_expires': 3600,
     'session.data_dir': '/tmp/sessions/simple',
     'session.auto': True
 }


@get('/index/')
def callback():
    return 'Hello World!'


# 函数主入口
if __name__ == '__main__':
    app_argv = SessionMiddleware(default_app(), session_opts)
    # run方法配置端口监听
    run(app=app_argv, host='0.0.0.0', port=9090, debug=True, reloader=True)