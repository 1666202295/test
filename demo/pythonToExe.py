#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: pythonToExe.py
# @time: 2018/8/1 15:34
# @desc: 将pthon脚本生成exe格式文件 双击运行
# 程序内容实现如下: 在F盘下生成一个新文件,写入内容:运行成功
# 程序编程完成后需要打包python为exe文件,步骤如下
# 黑窗口运行 pip install pyinstaller 安装PyInstaller 如果已经安装则不需要重复安装
# 使用 pyinstaller 打包 如: pyinstaller -F F:\test\demo\pythonToExe.py
# 运行后在脚本文件上级目录生成 dist 和 build 两个文件夹 如与demo同级生成dist和build文件夹
# 其中，build 目录是 pyinstaller 存储临时文件的目录，可以安全删除
# 最终的打包程序在 dist 内部的 dpython 目录中
# -w可以命令运行exe文件不会出现黑窗口如: pyinstaller -F -w D:\project\test.py
# -i命令可以更换程序图标如: pyinstaller -F -w -i D:\project\test.ico D:\project\test.py

strEnter = "运行成功"
fileName = "pythonToExeDemo.txt"
path = "F:\\" + fileName


# 通过with 打开文件
# mode="a" 表示追加写操作
def with_file_a(write_params, file_path):
    # 以urf-8格式打开文件,不然写入中文时会出现乱码情况
    with open(file_path, mode="a", encoding="utf-8") as heine:
        # write 为写操作
        heine.write("\n" + write_params)


with_file_a(strEnter, path)
# exec(open(path, encoding='utf-8').read()) 函数表示执行path指向的文件
exec(open("F:\\test\\demo\\isPrime.py", encoding='utf-8').read())

