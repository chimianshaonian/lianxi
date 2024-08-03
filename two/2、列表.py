# a = [1, 2, 3, 4, 5]
# # 列表是可变数据类型
#
# # 1、查找
# # 1、1根据下标查找元素，超过最大下标则报错
# print(a[1])
# # print(a[33])     # 报错
# # 1、2用index方法查找某个元素的下标，语法：序列.index(元素，开始，结束)  返回第一个匹配项的下标，找不到报错
# print(a.index(2))
# # print(a.index(6))     # 报错
# # 1、3统计出现次数  count()
# print(a.count(2))
# # 1、4统计容器内元素的个数  len()
# print(len(a))
# # 1、5判断元素是否在/不在容器内
# print('2' in a)      # True
# print('2' in a)      # False
#
# b = [1, 2, 3, 4]
# 2、列表新增
# 2、1新增一个元素，append（），语法：列表.append(元素/元组)，加到列表末尾
# b.append('你好')  # 增加元组
# b.append(5)  # 增加元素
# 2、2拓展，列表.extend(序列)，将序列内的每个元素加到列表内
# b1 = [8, 9]
# b.extend(b1)
# print(b)  # [1, 2, 3, 4, '你好', 5, 8, 9]
# b = b + b1      # 合并两个列表
# print(b)

# 3、删除相关
# c = ['a', 'b', 'c']
# 3、1删除整个列表 del
# del c      # 删除整个列表
# del c[2]  # 根据下标删除某个元素
# 3、2 pop()  根据下标删除某个元素，pop()会将删除掉的元素返回给我们，如pop()不给参数默认删除最后一个
# 语法：pop(下标)
# c.pop() 删除最后一位
# print(c.pop(1))
# 3、3 删除某个元素（根据元素本身删除），使用remove
# 语法：列表.remove（元素），删除第一个匹配项，找不到报错
# d = ['a', 'b', 'a', 'd']
# d.remove('a')
# print(d)
# # d.remove('ff')   # 报错
# # 3、4 清空列表 clear()
# # 语法：列表.clear()
# d.clear()
# print(d)

# 4、列表修改相关
# 4、1 根据下标直接修改
# d = ['a', 'b', 'a', 'd']
# d[2] = 'c'
# print(d)
# 4、2逆置：reverse（），修改的是原始数据，原始数据受影响
# 语法：列表.reverse()
# a = [1, 2, 3, 4, 5]
# # a.reverse()
# # print(a)
# # 4、3逆置：reversed（），不修改原始数据，得到一个新的对象，需要转化成列表
# # 语法：reversed(列表)
# a1 = list(reversed(a))
# print(a, a1)
# 4、4排序，修改原始数据，sort()，默认是升序,reverse=False
# 语法：列表.sort(升降序),降序需要添加参数reverse=True，是修改原始数据

# 4、5排序，不修改原始数据，sorted（），默认是生效，reverse=False
# 语法：sorted（列表，升降序），降序添加参数reverse=True
# a = [1, 2, 44, 4, 5]
# sorted(a)   # 升序
# print(sorted(a))
# print(sorted(a,reverse=True))

# 4、6拷贝，复制
# 浅拷贝：里面存储的可变数据类型内的元素，如发生变化，原始数据和拷贝数据都会跟着变，造成了数据污染
# 深拷贝：不管可变不可变数据类型的元素，都是独立的id,所以不受影响
# 深拷贝语法：copy.deepcopy(列表)
a = [1, 2, 3, [4, 5, 6]]
# 浅拷贝
# b = a.copy()
# b[3][0] = 44
# print(a,b)
# 深拷贝

import copy

c = copy.deepcopy(a)
c[3][0] = 55
print(a, c)

# 4、7 列表嵌套，逐层取值
b2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(b2[1][1])
