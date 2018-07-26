# 集合
items = {"arrow", "spear", "arrow", "arrow"}

# 集合会自动去重
print(items)

# 集合中是否包含某值
if "rock" in items:
    print("rock exist")
else:
    print("not found")

# 集合的声明
pets = set()
# 参数的添加
pets.add("cat")
pets.add("dog")
pets.add("pig")
print(pets)

# 参数的删除
pets.discard("cat")
pets.discard("tiger")
# 删除不存在的参数时不会报错
print(pets)

# 集合的交集和并集
numbers1 = {1, 2, 3, 4, 5}
numbers2 = {4, 5, 6, 7, 8, 9}
# 并集去重
print(numbers1 | numbers2)
# 交集去重
print(numbers1 & numbers2)
# 去除numbers1 中出现在 numbers2中的元素,保留number1独有的元素
print(numbers1 - numbers2)

# 列表内容添加到number2
numbers2.update([10, 11, 22])
print(numbers2)

# 字典转换成集合会将key值转成一个集合
dict1 = {"cat": 1, "dog": 2, "pig": 5}
keys = set(dict1)
print(keys)

# 字符串与集合 字符串会被拆分成由字符组成的set并且去重
for i in set("apple"):
    print(i, end=", ")
