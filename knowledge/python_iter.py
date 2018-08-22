# python 迭代器

# 迭代器的优势在于只要对象是一个可迭代对象,就可以创建该对象的迭代器
# 然后通过for循环获取对象的内容
# 比如下面被注释的数组li和字符串li

import collections

# 如果判断一个对象是否为可迭代对象 isinstance 判定第一个参数是否具备第二个参数代表的特性
li = "1234"
result = isinstance(li, collections.Iterable)

print(result)

# li = [1, 2, 3, 4]


liIter = iter(li)

# 判断一个对象是不是一个迭代器
result = isinstance(liIter, collections.abc.Iterator)
print(result)

# 同时,迭代器也是一个可迭代对象
result = isinstance(liIter, collections.Iterable)
print(result)
for i in liIter:
    print(i)
