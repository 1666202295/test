#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: pythonItChat.py
# @time: 2018/8/3 14:58
# @desc:监控鼠标和键盘的输入 鼠标监听事件和键盘监听事件不能在一个线程中,会阻塞线程,只有一个会生效
from pynput import mouse


# 鼠标按键
Button = mouse.Button
# 鼠标控制
Controller = mouse.Controller

# 读取指针位置
print('The current pointer position is {0}'.format(Controller.position))

# 设置指针位置
Controller.position = (100, 200)

print('Now we have moved it to {0}'.format(Controller.position))

# 指针相对当前位置移动指定变量
Controller.move = (150, 10)

# 左键按下并释放操作
Controller.press = Button.left

# 左键双击
Controller.release = Button.left

#  双击，这与按下并释放不同
# twice on Mac OSX
Controller.click = (Button.left, 2)

# 向下滚动两步
Controller.scroll = (0, 5)


# 鼠标移动事件
def on_move(x, y):
    print('鼠标移动至 {0}'.format((x, y)))


# 鼠标点击事件
def on_click(x, y, button, pressed):
    # x,y 标识当前鼠标的坐标值
    # button 标识当前点击的按键
    # pressed 标识当前的动作(点击/释放)
    pressed_key = ""
    if button == Button.left:
        pressed_key = "左键"
    elif button == Button.right:
        pressed_key = "右键"
    elif button == Button.middle:
        pressed_key = "滑轮"
    print('{0} {1} {2}'.format('按下' if pressed else '释放', pressed_key, (x, y)))


# 鼠标滚动事件
def on_scroll(x, y, dx, dy):
    print(dx)
    print(dy)
    # x,y 标识当前鼠标位置
    # dy 标识向上滚动还是向下滚动(1/-1)
    # dx 暂时不知道是什么作用
    print('鼠标 {0} 滚动 {1}'.format('向下' if dy < 0 else '向上', (x, y)))


# 鼠标监听事件
# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()



