# 列表
randList = ["String", 1.234, 28]
print(randList)

# 通过range生成列表
oneToTen = list(range(11))
print(oneToTen)

# 合并列表
randList = randList + oneToTen
print(randList)

# 通过下标读取列表值 列表下标从0开始
print(randList[0])

# 通过len函数获取列表长度
print(len(randList))

# 切片获取列表中值 包括下限,不包括上限
print(randList[0:3])

# 反向索引获取列表值
print(randList[-1])

# 反向索引切片
print(randList[-9:-2])

# 混合切片
print(randList[2:-1])
print(randList[-10:10])

# 不同步长切片
print(randList[1:10:2])

# 逆向输出数组
print(randList[-1:0:-1])

# 判断参数是否存在数组中
print("String" in randList)

# 判断参数在数组中位置 返回正向索引
print(randList.index(10))

# 遍历列表 并打印每个参数及下标 这里的i对应的列表中的每个参数,而不是下标索引
for i in randList:
    print("{}:{}".format(i, randList.index(i)))

# 添加参数
randList.append("joker")
randList.append(0)
print(randList)

# 计算列表中某个参数的个数
print(randList.count(0))

