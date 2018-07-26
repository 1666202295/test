

# 模拟登陆/注册实现 内容写入到本地文件中
def login_in():
    usr, pwd = input("请输入您的用户名和密码,以空格分隔:")
    # 读取本地文件


# 打印欢迎信息 请用户选择是登录/注册
def register():
    print("login_in")
# 登录操作记录日志


input_params = input(" 请选择您要进行的操作(选项后面的字母): 登录(L)/注册(R)")
input_params = input_params.lower()

if input_params == "l":
    # 登录操作
    print("登录操作")
    login_in()
elif input_params == "r":
    # 注册操作
    print("注册操作")
    register()



