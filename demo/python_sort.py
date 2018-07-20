import random

# 通过import引用工具包
# random 为随机数 生成 1到50之间的随机数
randNum = random.randrange(1, 51)

# 随机函数生成要排序的列表
numList = []
for i in range(11):
    numList.append(random.randrange(0, 10))
print(numList)

# sort排序,默认升序,只对列表本身进行排序,不会生成新的列表,所以不能赋值给新的列表
numList.sort()
print(numList)

# 参数 reverse = True 可以降序排列
numList.sort(reverse=True)
print(numList)

# reverse 降序排列
numList.reverse()
print(numList)

# insert 在指定位置添加元素
numList.insert(4, 10)
print(numList)

# remove 删除指定元素
numList.remove(10)
print(numList)

# pop 根据下标删除元素
numList.pop(1)
print(numList)

# python 自带排序函数 但是该方法不改变原有列表排序,只是返回一个排好序的列表,可以定义新的列表接收返回值
print(sorted(numList))
# sorted同样默认升序排列,通过参数reverse=True可以降序排列
print(sorted(numList, reverse=True))
s_list = sorted(numList)
print(s_list)
print(numList)

# 常量使用大写字母定义
PI = 3.14
print(PI)

# 元组相当于不可变列表 元组没有排序方法sort(),但是可以用sorted方法对元组内的元素进行排序,然后赋值给新列表
# 不可以更改值,没有添加元素append和insert方法.没有删除元素remove和pop方法
# 元组用小括号声明,
tup = (1, 2, 7, 5, 7, 3)
s_tup = sorted(tup)
print(s_tup)
print(sorted(tup))

