# 遍历文件夹下的内容,然后将文件重命名
import os
import withFile

# 文件的操作是用os
root_dir = 'F:\\test\\demo\\pic'
# 列出文件夹下所有的目录与文件
file_list = os.listdir(root_dir)
for i in range(0, len(file_list)):
    # 获取文件下的文件夹
    path = os.path.join(root_dir, file_list[i])
    if os.path.isdir(path):
        # 如果是一个文件,则打开目录
        dir_file_list = os.listdir(path)
        for x in range(0, len(dir_file_list)):
            file_path = os.path.join(os.path.join(root_dir, file_list[i]), dir_file_list[x])
            if os.path.isfile(file_path):
                # 获取后缀名
                suffix_name = file_path.split(".")[-1]
                withFile.copy_file(file_path, root_dir + "\\" + str(i) + "_" + str(x) + "." + suffix_name)

