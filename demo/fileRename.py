import os

# 文件的操作是用os
root_dir = 'C:\\Users\\user\Desktop\\打篮球'
# 列出文件夹下所有的目录与文件
file_list = os.listdir(root_dir)
for i in range(0, len(file_list)):
        path = os.path.join(root_dir, file_list[i])
        if os.path.isfile(path):
            fileName = os.path.basename(path)
            os.rename(path, os.path.join(root_dir, "打篮球_" + str(i) + ".jpg"))
