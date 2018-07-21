import os

# 文件的操作是用os
rootdir = 'C:\\Users\\user\Desktop\\打篮球'
# 列出文件夹下所有的目录与文件
list = os.listdir(rootdir)
for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            fileName = os.path.basename(path)
            os.rename(path, os.path.join(rootdir, "打篮球_" + str(i) + ".jpg"))
