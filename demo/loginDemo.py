import shelve
# 模拟登陆/注册实现 内容写入到本地文件中


def login_in(sh_path):
    shelf_file = shelve.open(sh_path)
    usr, pwd = input("请输入您的用户名和密码,以空格分隔:").split()
    # 读取本地文件
    if usr in shelf_file.keys():
        password = shelf_file[usr]
        if pwd == password:
            print("登录成功")
        else:
            print("密码错误")
    else:
        print("用户名不存在")


# 打印欢迎信息 请用户选择是登录/注册
def register(sh_path):
    shelf_file = shelve.open(sh_path)
    usr, pwd = input("请输入您的用户名和密码,以空格分隔:").split()
    while usr in shelf_file.keys():
        print("您的用户名已经存在,请输入新的用户名:")
        usr = input()
    shelf_file[usr] = pwd
    print("注册成功,您的用户名为:{},密码为{}:".format(usr, pwd))
    shelf_file.close()


path = "../resources/login"
input_params = input(" 请选择您要进行的操作(选项后面的字母): 登录(L)/注册(R)")
input_params = input_params.lower()

if input_params == "l":
    # 登录操作
    print("登录操作")
    login_in(path)
elif input_params == "r":
    # 注册操作
    print("注册操作")
    register(path)



