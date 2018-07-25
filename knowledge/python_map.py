# python 中的字典 相当于java中的map 数据结构为key-values

# 保存加菲猫的信息并进行存取操作

# 数组使用大括号声明 格式为{"key":"value","key":"value"...} 相当于json
myCat = {"name": "Garfield", "color": "orange", "size": "fat"}

# 取值使用 中括号 包裹key的形式
print("My cat's name is :", myCat["name"])

# 通过 中括号 包裹key = value 进行字典的赋值
myCat["city"] = "Xiamen"
print(myCat)

# 修改字典中的值同添加相同
myCat["color"] = "orange tabby"
print(myCat)

# 获取字典中的所有Values 值
print(myCat.values())

# for 循环遍历Values
for v in myCat.values():
    print(v, end=",")
print()

# 获取字典的所有key
print(myCat.keys())

# for 循环遍历key
for k in myCat.keys():
    print(k, end=", ")
print()

# 获取字典的条目
print(myCat.items())

# 循环打印字典的所有条目
for i in myCat.items():
    print(i, end=", ")
print()

# 判断字典是否包含某个key in
print("Is there a city:", "city" in myCat.keys())
print("Is there a city:", "city" in myCat)

# 判断字典是否包含某个value
print("Is there a city:", "Xiamen" in myCat.values())

# 字典取值缺省值 如果字典中包含标识的key值,则返回key对应的Value
# 如果不存在 则返回缺省值
print(myCat.get("sex", "not find"))
print(myCat.get("city", "not find"))

# 删除 字典中 的某个key
del myCat["city"]
print(myCat)

# setdefault 方法 如果数组中没有这个key,则添加,如果有则保留原值
myCat.setdefault("age", "3")
myCat.setdefault("age", "5")
print(myCat)

# 清除字典
myCat.clear()
print(myCat)
