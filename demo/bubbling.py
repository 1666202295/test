import random

# 通过import引用工具包
# random 为随机数 生成 1到50之间的随机数
randNum = random.randrange(1, 51)

# 随机函数生成要排序的列表
numList = []
for i in range(11):
    numList.append(random.randrange(0, 10))
# 冒泡排序原则,每两个相邻的元素进行比较,如果左边的元素比右边的元素小,则不动,否则左边的元素和右边的元素交换
length = len(numList) - 1
print("inti:", numList)
while length != 0:
    j = 0
    while j < length:
        if numList[j] > numList[j+1]:
            numList[j], numList[j+1] = numList[j+1], numList[j]
        j = j + 1
    print(numList)
    length = length - 1
