#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: python_opencv.py
# @time: 2018/10/17 10:34
# @desc: 打开摄像头

import cv2
import numpy as np  # 添加模块和矩阵模块

cap = cv2.VideoCapture(0)
# 打开摄像头，若打开本地视频，同opencv一样，只需将０换成("×××.avi")
while (1):  # get a frame
    ret, frame = cap.read()  # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# 释放并销毁窗口
