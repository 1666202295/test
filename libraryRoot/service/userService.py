#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: userService.py
# @time: 2018/10/12 15:41
# @desc: 用户服务接口

import libraryRoot.dao.userDao as userdb
from libraryRoot import getLogger

logger = getLogger.get_log()


# 用户根据手机号码和密码登录
def user_login(user_phone, user_password):
    if user_phone and user_password:
        data = userdb.get_user_phone(user_phone)
        logger.info(data)
        if len(data) > 1:
            return "数据不唯一"
        else:
            result = data[0]
            db_phone = result["phone"]
            db_password = result["password"]
            if user_phone == db_phone:
                if user_password == db_password:
                    return "success"
                else:
                    return "password is error"
            else:
                return "user_phone is error"

