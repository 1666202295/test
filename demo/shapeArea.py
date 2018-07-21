# 计算图形的面积

import math


def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("error")


# 计算长方形的面积
def rectangle_area():
    length = float(input("请输入长:"))
    width = float(input("请输入宽:"))
    area = length * width
    print("长方形的面积为:", area)


# 计算圆形的面积
def circle_area():
    radius = float(input("请输入圆形的半径:"))
    # 引用数学模块的pi常量和pow乘积函数
    area = math.pi * math.pow(radius, 2)
    print("圆形的面积为:{:.2f}".format(area))


shape_type = input("请输入您要计算的图形类型:")
get_area(shape_type)

