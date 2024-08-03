# 列表
# 推导式 [i for i in range()]
# 创建一个从0-10的偶数列表
# 方法一
a = []
# for i in range(0, 11, 2):
#     a.append(i)
# print(a)
# # 方法一，推导式
# a = [i for i in range(0, 11, 2)]
# print(a)
# 方法二
# for i in range(11):
#     if i % 2 == 0:
#         a.append(i)
# print(a)
# # 方法二，推导式
# a = [i for i in range(11) if i % 2 == 0]
# print(a)

# 创建如下[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# b = [(i, j) for i in range(1, 3) for j in range(3)]
# print(b)

# 字典
# 推导式  {k,v for .... in ....}
# a1 = ['name', 'age', 'gender']
# a2 = ['Tom', 20, 'man']
#
# # a3 = {i: j for i in a1 for j in a2}
# a3 = {a1[i]: a2[i] for i in range(len(a1))}
# print(a3)

a = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 需求：提前上述电脑数量大于等于200的字典数据

a4 = {k: v for k, v in a.items() if v >= 200}
print(a4)

# 集合
# 推导式 {i for i in ...}
# 创建一个集合，数据为下方列表的2次方
x = [1, 3, 2]
x1 = {y**2 for y in x}
print(x1)
print(type(x1))

