# 函数的实现
# 函数声明上部和结尾后应该有两个空行,不然IDE会置灰提醒
# 函数可以有多个参数,也可以无参
# 通过return返回处理结果,可以有多个,也可以无返回值


def allot_email(name):
    return "您的用户名是:" + name


def multiple_return(num1, num2):
    return (num1*num2), (num1/num2)


# name = input("请输入您的用户名:")
# print(allot_email(name))

params1 = int(input("请输入第一个参数"))
params2 = int(input("请输入第二个参数"))

# 多个返回值使用多个参数依次接收
return1, return2 = multiple_return(params1, params2)

print(return1)
print(return2)
