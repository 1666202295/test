#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: getSubtitle.py
# @time: 2018/11/30 13:21
# @desc: 从视频源中获取字幕
import os
import cv2
from PIL import Image

last_text = ""
video_path = ""
video_path = "d:\\video\\demo6.mp4"


# 视频地址
def get_video_path():
    video_path = input("请输入视频文件地址:(如:D:\\video.MP4)")
    if video_path:
        return video_path
    else:
        video_path = input("请输入视频文件地址:(如:D:\\video.MP4)")
        return video_path


# 创建图片临时文件夹
def create_dir(video_path):
    # 根据.拆分
    img_path = video_path.split(".")[0]
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    return img_path


# 视频拆分
def save_img(video_path_save_img):
    # D:\video\demo.png
    img_path_save_img = create_dir(video_path_save_img)
    vc = cv2.VideoCapture(video_path_save_img)  # 读入视频文件
    c = 1
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
    global last_text
    while rval:  # 循环读取视频帧
        rval, frame = vc.read()
        if (c % 20 == 0):
            cv2.imwrite(img_path_save_img + "\\" + str(c/20) + ".jpg", frame)
            img_tailoring(img_path_save_img + "\\" + str(c/20) + ".jpg")
        c = c + 1
        cv2.waitKey(1)
    vc.release()
    return img_path_save_img


# 图片裁剪
def img_tailoring(img_path):
    im = Image.open(img_path)
    # 图片的宽度和高度
    img_size = im.size
    img_width = img_size[0]
    img_height = img_size[1]
    '''
    裁剪：传入一个元组作为参数
    元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
    '''
    # 以图片左上角为准 x,y 为开始截取点的坐标 w,h为结束截取点的坐标
    # 截取图片中一块宽和高都是250的
    x = 0
    y = img_height * 0.9
    w = img_width
    h = img_height
    region = im.crop((x, y, w, h))
    region.save(img_path)
    im = Image.open(img_path)
    im.getcolors()


img_path = save_img(video_path)
# image = Image.open("D:\\video\\demo6\\20.jpg")
# print(image.getcolors())
