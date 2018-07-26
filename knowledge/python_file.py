# python 中的文件操作

path = "F:\\1.txt"


# 通过普通open方式打开文件,需要手动关闭文件
def open_file():
    # 通过open打开文件
    heine = open(path)
    # 通过 read方法获取文件内容
    poem = heine.read()
    print(poem)
    # type 函数可以获取参数的类型
    print(type(poem))
    # close函数关闭文件
    heine.close()
    # closed变量返回文件关闭状态
    print(heine.closed)
    print("open_file() end ===========")


# 通过with 打开文件
# mode="a" 表示追加写操作
def with_file_a():
    with open(path, mode="a") as heine:
        # tell 函数返回当前的文件指针
        print(heine.tell())
        # write 为写操作
        heine.write("\n this is with write\n")
        print(heine.tell())
        # seek 函数控制指针跳转
        heine.seek(0)

    print("with_file_a() end ===========")


# 通过with 打开文件
# mode="r" 表示读操作
def with_file_r():
    with open(path, mode="r") as heine:
        print(heine.read())

    print("with_file_r() end ===========")


# mode="w" 表示覆盖写操作
def with_file_w():
    with open(path, mode="w") as heine:
        heine.write("is with_file_w")

    print("with_file_w() end ===========")


# mode = "r+" 表示读写操作
def with_file_r_a():
    with open(path, mode="r+") as heine:
        heine.write("is with_file_r_a")
        # 读写操作的指针会随操作变动,即写到哪里指针就在哪里,所以要通过seek将指针回到开头才能读取文件,否则打印为空
        heine.seek(0)
        print(heine.read())

    print("with_file_r_a() end ===========")


# open_file()
# with_file_a()
# open_file()
with_file_r_a()

