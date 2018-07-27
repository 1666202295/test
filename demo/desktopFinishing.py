#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: desktopFinishing.py
# @time: 2018/7/27 15:14
# @desc: 桌面整理,检查桌面的文件,同类型的文件放到同类型的文件夹中,如果没有则创建文件夹

import os
import copyFile

root_path = "C:\\Users\\user\\Desktop"
file_list = os.listdir(root_path)
for i in range(0, len(file_list)):
    path = os.path.join(root_path, file_list[i])
    if os.path.isfile(path):
        suffix = file_list[i].split(".")[-1]
        targetPath = os.path.join(root_path, suffix)
        # 判断文件夹是否存在
        if os.path.exists(targetPath) is False:
            os.makedirs(targetPath)
        targetPath = os.path.join(targetPath, file_list[i])
        copyFile.copy_file(path, targetPath)
        os.remove(path)

