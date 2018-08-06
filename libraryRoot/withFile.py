#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: withFile.py
# @time: 2018/8/6 9:48
# @desc: 文件操作


# 通过with 打开文件
# mode="a" 表示追加写操作
def with_file_a(write_params, file_path):
    # 以urf-8格式打开文件,不然写入中文时会出现乱码情况
    with open(file_path, mode="a", encoding="utf-8") as heine:
        # write 为写操作
        heine.write("\n" + write_params)


# 复制文件
# 二进制读取文件,写入另外的文件,相当于实现复制功能
# 二进制读取文件方式适合于读取非文本的文件 如图片,音频
def copy_file(source_path, target_path):
    with open(source_path, "rb") as rf:
        # rb表示以二进制字节方式写考拉2.jpg文件
        with open(target_path, "wb") as wf:
            # 以1kb大小作为缓存传输,即每次读取1kb
            chunk_size = 1024
            # 读取源文件
            rf_chunk = rf.read(chunk_size)
            # 如果读取的内容长度大于0,即未到文件结尾
            while len(rf_chunk) > 0:
                # 写入到目标文件
                wf.write(rf_chunk)
                # 继续读源文件 直到结束
                rf_chunk = rf.read(chunk_size)
