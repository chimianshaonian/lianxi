# 1、字符串学习
# 1-1、切片
# 切片语法：序列[开始：结束：步长]  步长默认是1
# 开始或结束是下标，下标如是负数，负几就是倒数第几个元素
# 基本原则：顾头不顾尾，如开始结束是相同值，以不顾尾优先，所以切空
# name = '12345678'

# print(name[2:5:1])   # 345
# print(name[2:5])     # 345
# print(name[:5])      # 12345
# print(name[:])       # 12345678
# print(name[2:])      # 345678
# print(name[-3:])     # 67
# print(name[:-3])     # 12345
# print(name[::-1])    # -1 从右向左 87654321
# print(name[2:5:-1])  # 切空
# print(name[5:2:-1])  # 654
# print(name[-3:5:-1])  # 切空
# print(name[3:3:1])   # 切空

# 1-2、字符串查找
# m = "hello world and supertest and chenghao and Python"
# # 查找某个子串出现的开始下标
# # find() 语法：字符串.find(子串，开始，结束) 找返回第一个匹配项的下标，找不到返回-1
# print(m.find('and',11,100))
# print(m.find('zz'))   # 返-1，如不写开始/结束下标，默认就是全部字符
# #
# # index() 语法：字符串.index(子串，开始，结束) 找到返回第一个匹配项的下标，找不到报错
# print(m.index('and',11,50))
# # print(m.index('ands'))    # 报错
#
# # 统计子串出现的次数
# # count()  语法：字符串.count(子串，开始，结束)
# print(m.count('and',10,99))
#
# # 从右开始查找
# print(m.rfind('and',10,150))
# print(m.rindex('and',11,25))

# 字符串是不可变数据类型
# 1-3、字符串相关修改
# m = "hello world and supertest and chenghao and Python"
#
# # replace() 替换 语法：字符串.replace(旧子串、新子串，次数)
# print(m.replace('and','+',10))  # 如不写次数，默认是全部；如次数超过实际次数，替换就按实际次数替换
#
# # split() 分割字符串：字符串.split(分割符)，注：分割字符会被吃掉
# print(m)
# print(m.split('and'))

# 字符串拼接 语法：字符或子串.join(需要拼接的序列)
# a = 'abcd'
# print('-'.join(a))

# 2、功能性修改
# m = "hello world and supertesT and chenghao and Python"
# 2-1、将整个字符串首字符变为大写，其他变小写
# 语法：字符串.capitalize()
# print(m.capitalize())
# # 2-2、将字符串里面的每个单词非首字母变小写,
# # 语法：字符串.title()
# print(m.title())
# # 2-3、将全部字母变大写
# # 语法：字符串.upper
# print(m.upper())
# 2-4、将全部字符变为小写
# 语法：字符串.lower()
# print(m.lower())
# # 2-5、去除字符串两侧的空白字符
# n = "    hello world and supertest and chenghao and Python     "
# # 语法：字符串.strip()
# # print(n.strip())
# # 2-6、去除左侧空白字符
# # 语法:字符串.lstrip()
# print(n.lstrip())
# # 2-7、去除右侧空白字符
# # 语法：字符串.rstrip()
# print(n.rstrip())
# # 2-8、去除首尾两侧的空白字符，其中首尾字符的位置无所谓
# # 语法：字符串.strip()
# print(n.strip('n h'))

# 3、补全字符，只能用一个字符
# m = 'hello'
# # 居中补全
# # 语法:字符串.center(长度，字符)
# print(m.center(10,'-'))
# # 靠左补齐
# # 语法：字符串.ljust(长度，字符)
# print(m.ljust(10,'-'))
# # 靠右补齐
# # 语法：字符串.rjust(长度，字符)
# print(m.rjust(10,'-'))

# 4、判断相关  如是真，返回True，否则返回False
# m = "hello world and supertest and chenghao and Python"
# # 4-1、判断字符串是否以指定子串开始
# # 语法：字符串.startswith(子串，开始，结束)
# print(m.startswith('and',11,50))  # 也可不用输入开始&结束，那就是全部
# # 4-2、判断字符串是否以指定子串结束
# # 语法：字符串.endswith(子串，开始，结束)
# print(m.endswith('Python'))


# a1 = 'he你'
# a2 = 'he123'
# a3 = '123'
# a4 = ' '
# # 4-3、判断字符串中是否全由字母组成
# # 语法：字符串.isalpha()
# print(a1.isalpha())
# # 4-4、判断字符串是否由数字组成
# # 语法：字符串.isdigit()
# print(a3.isdigit())
# # 4-5、判断字符串是否全由字符或数字组成
# # 语法：字符串.isalnum()
# print(a2.isalnum())
# # 4-6、判断字符串是否全由空白字符组成
# # 语法：字符串.isspace()
# print(a4.isspace())

# -----------------------------------------------
# 列表学习
# a = [1,2,3,4,1]
# 列表是可变数据类型
# 1、查找相关语法
# 1-1、根据下标查找元素，超过最大下标则报错
# 语法：列表[下标]
# print(a[0])
# 1-2、用index方法查找某个元素的下标
# 语法：列表.index(元素，开始，结束) 返回第一个匹配项的下标，找不到报错
# print(a.index(1,2,))   # 如不写开始/结束，默认全部
# print(a.index(1))
# # print(a.index(11))    # 报错
# # 1-3、统计元素出现的次数
# # 语法：列表.count(元素，开始，结束)  如开始/结束不写，默认是全部
# print(a.count(1))   # 0次
# # 1-4、统计容器内元素的个数
# # 语法：列表.len()
# print(len(a))
# 1-5、判断元素是否在/不在容器内
# 语法：元素  in(在)/not in(不在) 列表
# print('6' in a)    # False
# print('6' not in a)   # True

# 2、列表新增相关
# m = [1,2,3,4]
# 2-1、新增一个元素，添加到末尾，使用append()
# 语法:列表.append(元素/元组)   添加到末尾
# m.append(5)   # 加元素
# print(m)
# m.append((1,2))   # 加元组，当成一个整体添加到列表末尾
# print(m)
# m.append('你好')
# print(m)
# 2-2、拓展：将序列内的每个元素加到列表内，用extend()
# 语法:列表.extend(序列)
# a = 'abc'
# b = (5,6,7)
# c = [10,20]
# m.extend(a)
# print(m)
# m.extend(b)
# print(m)
# m = m + c
# print(m)
# 2-3、在指定位置添加元素，用insert
# 语法：列表.insert(下标，元素)
# m.insert(2,22)
# print(m)

# 3、删除相关
m = ['a', 'b', 'c']
# 3-1、删除整个列表,用del
# 语法：del 列表
# del m
# print(m)   # 报错，m已经删除
# 3-2、根据下标删除某个元素，用del
# 语法：del 列表[下标]
# del m[1]
# print(m)
# 3-3、根据下标删除某个元素，pop()会将删除掉的元素返回给我们
# 语法：列表.pop(下标)   如不给参数，默认删除最后一个
# n = m.pop(1)
# print(m,n)
# x = m.pop()
# print(m,x)
# 3-4、删除某个元素（根据元素本身删除），使用remove
# 语法：列表.remove(元素)，删除第一个匹配项，如找不到则报错
# m.remove('b')
# print(m)
# # m.remove('s')   # 报错
# # 3-5、清空列表，用clear()
# # 语法：列表.clear()
# m.clear()
# print(m)

# 4、列表修改相关语法
# a = ['a','b','c']
# # 4-1、根据下标直接修改
# a[1 ]= 'B'
# print(a)

# b = [1,3,2,5,4,6]
# 4-2、逆置，使用reverse，修改的就是原始数据，原始数据受影响
# 语法：列表.reverse()
# b.reverse()
# print(b)
# 4-3、不修改原始数据进行逆置，reversed（）
# 语法：reversed(b)，生成一个对象，需要转化类型
# d = list(reversed(b))
# print(d)
# print(b)
# 4-4、对数据进行排序，使用sort()，默认是升序，如降序需添加参数reverse=True，会修改原始数据
# 语法：列表.sort(参数)    # 参数不写默认是升序
# b.sort()   # 升序
# b.sort(reverse=True)    # 降序
# print(b)
# 4-5、不修改原始数据，用sorted()进行排序，默认依然是生效，降序需添加参数reverse=True
# 语法:sorted(列表，参数)    参数不写是默认升序
# c = sorted(b)
# print(c,b)

# 拷贝复制
# b = [1,2,3,4,5,[1,2,3]]
# 分为：浅拷贝、深拷贝
# 浅拷贝：里面存储的可变数据类型内的元素，如发生变化，原始数据和拷贝数据都会跟着改变，造成了数据污染
# 语法：列表.copy()
# b1 = b.copy()
# b1[5][0] = 0
# print(b)
# print(b1)
# 深拷贝：不管可变不可变数据类型的元素，都是独立的id，所以不受影响
# 深拷贝，需要导包，import copy
# 语法：copy.deepcopy(列表)
# import copy
# b2 = copy.deepcopy(b)
# b2[5][0] = 0
# print(b2)
# print(b)

# --------------------------------------------------
# 3、元组
# 特点：一个元组可存储多个数据，元组内的数据，是不可变数据类型
# a = (1, 2, 3, [4, 4, 4], '你好')
# 当元素内只有一个元素时，需要在这个元素后加一个逗号
# b = (1,)  # 如没有逗号，那b的类型是int
# c = (1)
# print(type(b), type(c))
"""
元组：是不可变数据类型，因此修改元组内数据会报错
只支持查询，不支持修改
"""
# a[0] = 0
# print(a)

# a = (1, 2, 3, 3, 3, [4, 4, 4], '你好')
# 3-1、根据下标查询元素
# print(a[1])
# # 3-2、查询某个元素的下标，返回第一个匹配值的下标
# # 语法：元组.index(元素)
# print(a.index(3))
# # 3-3、统计元素个数
# # 语法：len(元组)
# print(len(a))
# 3-4、判断某个元素是否在/不在容器内
# in 在；not in 不在
# print('0' in a)    # False
# print('0' not in a)    # True
# 特殊情况，如元组内有，可变数据类型，这个可变数据类型的元素内部的东西支持修改
# a = (1, 2, 3, [4, 4, 4], '你好')
# print(id(a))
# # 修改前后，元组的id没有改变
# a[3][0] = 0
# print(a,id(a))

# --------------------------------------------------

# 4、字典类型
"""
字典是可变数据类型
字典特点：
1、符号为大括号
2、数据为键值对形式出现
3、各个键值对之间用逗号隔开
"""
# a = {'one':1, 'two':2, 'three':3}
# # 4-1、新增修改
# a['four'] = 4
# a['one'] = 11
# print(a)

# 4-2、删除相关语法
# 4-2-1、删除整个字典 del
# 语法：del 字典
# del a
# print(a)   # 报错，已经被删除
# 4-2-2、删除某个指定键值对，根据key进行删除
# 语法：del 字典[key]
# print(a)
# del a['three']
# print(a)
# # 4-2-3、清空字典
# # 语法：字典.clear()
# a.clear()
# print(a)

# 4-3、查找相关语法
# a = {'one':1, 'two':2, 'three':3}
# 4-3-1、直接根据key找value，找不到则报错
# 语法：字典[key]
# print(a['one'])
# print(a['aa'])   # 找不到报错
# 4-3-2、根据key找value，找不到返货默认值
# 语法：字典.get()，可修改返回值，需要填写返回内容
# print(a.get('one'))
# print(a.get('aa'))
# print(a.get('aa','没找到'))    # 可修改返回值为：找不到
# 4-3-3、获取字典内所有的key
# 语法：字典.keys（）  如要打印，需转化下类型
# a1 = a.keys()
# print(a1)    # dict_keys([所有key])
# print(list(a1))  # 把所有key当成一个列表进行打印
# 4-3-4、获取字典内所有的value
# 语法：字典.values()
# print(a.values())   # dict_values([所有value])，如要打印，需转化类型
# print(list(a.values()))   # 以列表形式打印所有value
# # 4-3-5、获取字典内所有的键值对
# # 语法：字典.items()
# print(a.items())   # 如要打印，也需要转化类型
# print(list(a.items()))

# # 循环打印所有键值对
# for i in a.items():
#     print(list(i))
# for k,v in a.items():
#     print(f'key是{k}，value是{v}')

# # 循环打印所有键
# for j in a:    # 与a.keys()效果一样，都是打印所有的键
#     print(j)
#
# for i in a.keys():
#     print(i)

# --------------------------------------------------
# 5、集合学习
"""
集合是可变数据类型
集合的特点：
1、集合是武学的，所以结合没有下标
2、结合天然去重
3、集合只能存放不可变数据类型
"""
# a = {1,2,3,'a','b',1,1,1}
# 5-1-1、新增
# 5-1-1、新增一个元素，新增的元素如已经存在，则添加不上，也不报错
# 语法：集合.add()
# a.add(2)
# print(a)
# a.add(5)
# print(a)
# b = ('a1','b1')
# a.add(b)    # 把b当成一个整体添加到集合a里面
# print(a)
# 5-1-2、将b里面的元素逐个加到集合a里面
# 语法：集合.update（b）
# a.update(b)
# print(a)
# 5-2、删除相关函数
# 5-2-1、删除某个指定元素，如不存在则报错
# 语法：集合.remove（元素）
# a.remove('a')
# print(a)
# # a.remove('d')    # 删除不存在，报错
# 5-2-2、删除某个指定元素，不如存在不保存
# 语法：集合.discard(元素)
# a.discard('d')
# # 5-2-3、随机删除一个元素，并返回这个元素
# # 语法：集合.pop（）
# b = a.pop()
# print(b)
# print(a)
# 5-2-4、判断某个元素是否在集合内
# in 在；not in 不在
# print('a' in a)   # True
# print('a' not in a)    # False

# 特殊情况：0和False会触发去重，1和True会去重
# c = {True,False,0,1,2,3}
# print(c)

# 5-3、交集、并集、差集
# a1 = {1, 2, 3, 4, 5, 6}
# a2 = {4, 5, 6, 7, 8, 9}
# # 5-3-1、交集，使用&
# print(a1 & a2)
# # 5-3-2、并集，使用|
# print(a1 | a2)
# # 5-3-3、差集，使用-
# print(a1 - a2)

# ------------------------------------

# 6、公共操作
# 6-1、运算符
# 6-1-1、合并  +
# 字符串
# a = 'aa'
# b = 'bb'
# print(a + b)
# # 列表
# a1 = [1,2]
# b1 = [2,3]
# print(a1 + b1)
# # 元组
# a2 = (1,2)
# b2 = ('1','b')
# print(a2 + b2)
# 6-1-2、复制
# 字符串
# print('a' * 3)
# # 列表
# print([4,5] * 2)
# # 元组
# print(('a','b') * 2)
# 6-1-3、判断  in/ not in
# in 为在，True；not in 为不在  False
# 字符串
# a1 = 'aabb'
# print('c' not in a1)     # True
# # 列表
# a2 = [1,2,3,4]
# print(5 in a2)    # False
# # 元组，集合
# a3 = (1,2,3,4)
# a4 = {11,2,3,4}
# print(1 in (a3 and a4))   # 同时在元组和集合内
# print(len(a4))

# 6-2公共方法
# 6-2-1、len()  计算个数
# 字符串、列表、元组、集合，字典都卡使用
# 语法：len(**) 其中字典是返回多少个键值对

# 6-2-2、del 类型  删除 全部
# 列表、字典都卡使用,其中字符串\元组，是不可变数据类型
# 集合有单独删除方法，remove(元素)、discard(元素)
# del 字典、字典
# 列表、集合，字典都卡使用,其中字符串\元组，是不可变数据类型
# 字符串，可以用replace（替换），元组只能查不可修改
# 删除指定
# del 列表(元素)
# del 元组(元素)
# del 字典(key)

# 6-2-3、返回最大值、最小值
# 最大值 max(类型)
# 最小值 min(类型)

# 6-2-4、遍历数，range（）
# 语法：range（开始、结束、步长）   # 生成的数，不包含结束
# for i in range(1,5,1):
#     print(i)   # 1,2,3,4

# 6-2-5、enumerate()
# 语法：enumerate（可遍历对象，start=0），
"""
其中start参数用来设置遍历的下标，起始值默认为0
# 作用：用于将一个可遍历的数据对象（如列表、元组、字符串），
组合成一个索引序列，同时列出数据和数据下标一般用在for循环中
"""
# a = {'a','b','c','d'}
# for i in enumerate(a,start=1):
#     print(i)
# """
# 结果：(1, 'a')
# (2, 'b')
# (3, 'c')
# (4, 'd')
# """
# for k,v in enumerate(a,start=1):
#     print(f'key是{k},value是{v}')
"""
结果是：key是1,value是a
key是2,value是c
key是3,value是d
key是4,value是b
"""

# 6-3、类型转化
# 6-3-1、转元组
# tuple(list)
# tuple(set)
# # 6-3-2、将某个序列换列表
# a = ('a','b','c')
# b = {1,2,3}
# list(a)
# list(b)
# 6-3-3、转集合  set()
# 集合可以快速列表去重
# 集合不支持下标

# ---------------------------------------------
# 7、推导式
# 7-1、列表
# a = [i for i in range(***)]
# 创建0-10的列表
# a = []
# for i in range(0,11):
#     a.append(i)
# print(a)
# # 推导式
# b = [i for i in range(0,11)]
# print(b)

# 带if的推导式
# 创建0-10的偶数列表
# a = [i for i in range(11) if i % 2 == 0]
# print(a)
# b = [i for i in range(0,11,2)]
# print(b)
# c = []
# for i in range(11):
#     if i % 2 == 0:
#         c.append(i)
# print(c)

# 带多个for循环的列表推导式
# 创建[(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
# a = []
# for i in range(1,3):
#     for j in range(0,2):
#         a.append((i,j))
# print(a)
# # 推导式
# b = [(x,y) for x in range(1,3) for y in range(0,2)]
# print(b)

# 7-2、字典
# 推导式
# a = {x1:x2 for ** in ***}
# list1 = ['name', 'age', 'gender']
# list2 = ['Tom', 20, 'man']
# # 用for循环实现
# n = {}
# for i in range(len(list1)):
#      n[list1[i]] = list2[i]
# print(n)
# # 推导式
# a1 = {list1[i]:list2[i] for i in range(len(list1))}
# print(a1)

# counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# # # 需求：提前上述电脑数量大于等于200的字典数据
# a2 = {}
# for k,v in counts.items():
#     if v >= 200:
#         a2[k] = v
# print(a2)
# # 推导式
# a3 = {k:v for k,v in counts.items() if v >= 200}
# print(a3)


# 7-3、集合
# 推导式 a = {x for x in ***}
# 需求：创建一个集合，数据为下发列表的2次方
# x4 = [1,1,2]
# a4 = set()
# for i in x4:
#     if i**2 not in a4:
#         a4.add(i**2)
# print(a4)
# # 推导式
# a5 = {x**2 for x in x4}
# print(a5)





























