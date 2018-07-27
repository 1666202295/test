# shelve 可以在目录中生成一个键值对的存储信息,有点类似redis缓存
import shelve

# 打开shelve文件
shelfFile = shelve.open("../resources/myCat")

cats = ["Garfield", "Tom", "Kitty"]

# 存储shelve信息
shelfFile["cats"] = cats

# 关闭shelve文件
shelfFile.close()

sh = shelve.open("../resources/myCat")

if "cats" in sh.keys():
    print("hah ")

# 读取shelve内容
print(sh["cats"])




