# 打印九九乘法表

# 列数从1开始 行数从1开始
line = 1
while line < 10:
    column = 1
    while column <= line:
        print("{} * {} = {} ".format(column, line, line * column), end="")
        column = column + 1
    print("")
    line = line + 1
