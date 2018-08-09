#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: python_operator.py
# @time: 2018/8/8 20:21
# @desc: python 中的运算符

# "+" 号运算
# int
print(1 + 1)

# str
print("1" + "2")

# 列表
print([1, 2] + [3, 4])

# - 运算
print(2 - 1)

# * 运算
print(3 * 5)

# 幂运算
print(2 ** 3)

# 除法运算
print(5 / 2)

# 除数不能为0!
# print(5 / 0)

# 整除运算 舍一取整,忽略小数
print(5 // 2)
print(7.5 // 2)

# 取余运算
print(5 % 2)

# 赋值运算
x = 5
print(x)
x, y = 5, 6
print(x, y)
x = y = z = 7
print(x, y, z)

# 优先运算 小括号
x = (5 - 2) + 3 * 3
print(x)

# 手误输入居然没有报错
x = (5 - 2) / + 3 * 3
print(x)

# 复合运算符:+=,-=,*=,/=,**=,%=,//=
num = 10
num += 5
print(num)
num -= 3
print(num)
num *= 2
print(num)
num /= 2
print(num)
num **= 2
print(num)
num %= 3
print(num)
num //= 2
print(num)
print("===================")

# 比较运算符
print(10 > 2)
print(2 < 10)
print(2 >= 2)
print(2 <= 2)
print(10 != 2)
print(2 == 2)
print(1 < 2 < 10)
# 内存地址比较 is
i = 10
z = 10
print(i is z)
x = [1]
y = [1]
print(x is y)

print("===================")
# 逻辑运算符
b = True
# not 取非
print(b)
print(not b)
# and 与操作
print(b and False)
print(b and True)
# or 或运算
print(b or False)
print(b or True)

print("===================")
# 非布尔类型值 非0为真 非空为真
print(1 or False)
print(1 or True)
print(1 and False)
print(1 and True)
print(0 and True)
print(0 and False)
print(0 or True)
print(0 or False)
print(1 and 3)
print(1 or 3)
print(0 or 2)
print(bool("0"))


