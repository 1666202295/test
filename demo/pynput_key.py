#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: pythonItChat.py
# @time: 2018/8/3 14:58
# @desc:监控键盘的输入
from pynput import keyboard


# 键盘处理逻辑
def press(key):
    print("点击按键", key)


# 键盘监听事件 具体逻辑交给press处理
with keyboard.Listener(on_press=press) as listener:
    listener.join()
