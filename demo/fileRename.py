# 遍历文件夹下的内容,然后将文件重命名
import os

# 文件的操作是用os
root_dir = 'C:\\Users\\user\Desktop\\打篮球'
# 列出文件夹下所有的目录与文件
file_list = os.listdir(root_dir)
for i in range(0, len(file_list)):
    # 获取文件下的文件路径
    path = os.path.join(root_dir, file_list[i])
    if os.path.isfile(path):
        # 如果路径是一个文件 将文件重命名
        os.rename(path, os.path.join(root_dir, "打篮球_" + str(i) + ".jpg"))
