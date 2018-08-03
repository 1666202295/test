#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: pythonItChat.py
# @time: 2018/8/3 14:58
# @desc:itchat 微信模块初探 文档参考 http://itchat.readthedocs.io/zh/latest/

import itchat

# 登录
itchat.auto_login()

# 文件助手userName
fileUser = "filehelper"


# 主动给文件助手发送一条消息
itchat.send("Hello", toUserName=fileUser)


fileName = "YourWeChatData.txt"
path = "F:\\" + fileName
strEnter = """
    我和你的文件助手打了个招呼,并且知道了你的好友都有谁\n
"""

# 打印好友列表
friends = itchat.get_friends(update=True)[0:]
for friend in friends:
    strEnter = strEnter + str(friend)


# 通过with 打开文件
# mode="a" 表示追加写操作
def with_file_a(write_params, file_path):
    # 以urf-8格式打开文件,不然写入中文时会出现乱码情况
    with open(file_path, mode="a", encoding="utf-8") as heine:
        # write 为写操作
        heine.write("\n" + write_params)


with_file_a(strEnter, path)


messagePath = "F:\\message.txt"


# 监听信息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # 打印收到的消息
    print(msg.User.NickName)
    nick_name = msg.User.NickName
    text = msg.Text
    message = str(nick_name) + ":" + str(text)
    with_file_a(message, messagePath)
    # 回复信息
    return "我收到消息了"


# 启动监听
itchat.run()
