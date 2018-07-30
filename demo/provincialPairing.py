#!/usr/bin/env python
# encoding:  utf-8
# @author:  曹会金
# @license:  (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact:  deamoncao100@gmail.com
# @software:  garner
# @file:  provincialPairing.py
# @time:  2018/7/30 19: 54
# @desc:  省和省会考卷的生成 试卷内容如下 运行后将在当前目录下生成考卷和答案卷

"""
姓名: 

学号: 

班级: 

                        省配对省会测试卷X

1. 海南的省会是?
A.海口
B.程度
C.福州
D.呼和浩特

2.黑龙江的省会是?
A.哈尔滨
B.武汉
C.重庆
D.香港

......

"""

import random

captias = {"北京市": "北京", "上海市": "上海", "天津市": "天津", "重庆市": "重庆", "黑龙江省": "哈尔滨", "吉林省": "长春", "辽宁省": "沈阳", "内蒙古自治区": "呼和浩特",
           "河北省": "石家庄", "新疆维吾尔自治区": "乌鲁木齐", "甘肃省": "兰州", "青海省": "西宁", "陕西省": "西安", "宁夏回族自治区": "银川", "河南省": "郑州",
           "山东省": "济南", "山西省": "太原", "安徽省": "合肥", "湖南省": "长沙", "湖北省": "武汉", "江苏省": "南京", "四川省": "成都", "贵州省": "贵阳", "云南省": "昆明",
           "广西壮族自治区": "南宁", "西藏自治区": "拉萨", "浙江省": "杭州", "江西省": "南昌", "广东省": "广州", "福建省": "福州", "台湾省": "台北", "海南省": "海口",
           "香港特别行政区": "香港", "澳门特别行政区": "澳门"}

stuNum = int(input("您要出几份考卷?:"))

for quizNum in range(stuNum):
    # 考题卷
    quizFile = open("problem_{}.txt".format(quizNum + 1), "w", encoding="utf-8")
    # 答案卷
    answerKeyFile = open("answer_{}.txt".format(quizNum + 1), "w", encoding="utf-8")
    # 打印抬头
    quizFile.write("姓名:\n\n学号:\n\n班级:\n\n")
    quizFile.write(" " * 20 + "省配对省会测试卷{}\n".format(quizNum + 1))

    # 生成题目列表
    provinces = list(captias.keys())
    # 打乱顺序
    random.shuffle(provinces)

    # 循环生成问题和答案并写入考卷
    for questionNum in range(len(provinces)):
        # 题目省会
        provincesName = provinces[questionNum]
        # 根据省会获得正确答案
        correctAnswer = captias[provincesName]
        # 错误答案池
        wrongAnswer = list(captias.values())
        # 去除正确答案
        wrongAnswer.remove(correctAnswer)
        # 从错误的答案池中随机选取三个 sample(seq, n) 从序列seq中选择n个随机且独立的元素；
        wrongAnswer = random.sample(wrongAnswer, 3)
        # 合并答案池,将正确答案和错误答案合并成一个列表 answerOptions
        answerOptions = wrongAnswer + [correctAnswer]
        # 打乱答案顺序
        random.shuffle(answerOptions)

        # 写入题目 questionNum + 1 为题号
        quizFile.write("\n{}. {}的省会是? \n".format(questionNum + 1, provincesName))
        for i in range(4):
            quizFile.write("{}. {}\n".format("ABCD"[i], answerOptions[i]))
        # 写入答案
        answerKeyFile.write("{}. {}\n".format(questionNum + 1, "ABCD"[answerOptions.index(correctAnswer)]))
    # 关闭考卷文件
    quizFile.close()
    # 关闭答案文件
    answerKeyFile.close()








