# 随笔记录 回车完成输入 写入到本地文件 本地文件不存在会自动创建 输入n退出 记录时间 自动换行
import datetime


# 通过with 打开文件
# mode="a" 表示追加写操作
def with_file_a(write_params):
    # 以urf-8格式打开文件,不然写入中文时会出现乱码情况
    with open(path, mode="a", encoding="utf-8") as heine:
        # write 为写操作
        heine.write("\n" + write_params)


# 数据存储路径
path = "F:\\essaysRecord.txt"

strEnter = ""

while strEnter != "n":
    # 通过 datetime 获得当前时间并格式化
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 获取用户输入
    strEnter = input(nowTime + ":")
    if strEnter == "n":
        print("输入结束")
    else:
        with_file_a(nowTime + strEnter)
        print(nowTime + strEnter)




