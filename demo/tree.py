# 使用while 和 for循环打印任意层数的松树 比如说5层结果如下
"""
    #
   ###
  #####
 #######
#########
    #
"""
# 使用input获取用户输入的松树层数
# input输入的默认为字符串 需要转换成int
height = int(input("请输入您要打印的松树的层数:"))

# 发现每层的空格数为层高 - 1
spaceNum = height - 1

# 发现#号从1开始打印,每层 + 2
specialNum = 1

while height != 0:
    for i in range(spaceNum):
        # print() 函数 end=""表示不换行
        print(" ", end="")
    for i in range(specialNum):
        print("#", end="")
    print("")
    height = height - 1
    spaceNum = height - 1
    specialNum = specialNum + 2

# 循环结束 打印树桩
for i in range(int(specialNum / 2) - 1):
    print(" ", end="")
print("#")
