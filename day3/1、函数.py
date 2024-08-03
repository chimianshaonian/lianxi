'''
计算并打印1+2的和，定义一个函数实现
'''


# def a(x, y):
#     res = x + y
#     return res
#
# print(a(1, 2))

# 函数里调用函数
# 打印n条横线
# def a1():
#     print('----------------------')
# # 定义一个函数a2
# def a2(n):
#     for i in range(n):
#         a1()
#
# a2(5)

# 定义一个函数：计算三个数的和
# def sum_a(x,y,z):
#     '''
#     函数说明文档
#     :param x:
#     :param y:
#     :param z:
#     :return:
#     '''
#     a = x + y + z
#     return a
#
# # 定义一个函数：计算三个数的平均值，要先用第一个函数计算和，再除以3
# def fun(i,j,m):
#     return int(sum_a(i,j,m) / 3)
# print(fun(2,3,4))

# -------------------------------------------
# 局部变量
# m = 1000
# def fun():
#     # 定义一个局部变量（只在当前函数内部生效）
#     m = 100
#     return m
# def fun1():
#     return m + 1
# print(fun())
# print(fun1())

# 全局变量
# def fun2():
#     # 声明m为全局变量
#     global m
#     m = 100
#     return m
# def fun3():
#     return m + 1
#
# print(fun2())
# print(fun3())

# def fun():
#     return 50
# print(fun())

# 多个返回值,
# 当有多个return时，只执行第一个return，因为return可以退出当前函数，导致第一个return下的代码不执行
# def fun4():
#     return 1
#     return 2
# print(fun4())

# 可以把多个返回值写在一个return下
# def fun():
#     return 1,2,'你好'
# print(fun())    # 以元组形式返回

# -------------------------
# 函数的参数
# 位置参数传递（参数的位置和个数必须保持和定义的时候一致）
# def fun(name,age,sex):
#     print(f'姓名{name},年龄{age},性别{sex}')
#
# # fun('A',11,'男')
# # fun(11,'B','男')  # 传的参数值也需要与函数定义的参数名顺序一致
#
# # 关键字参数传递，函数调用时，如有位置参数时，位置参数必现在关键字参数的前面，但关键字参数之间不存在先后顺序
# fun('C',age=12,sex='男')   # 如使用关键字传递，那后面的都需要用关键字传递，前面的可以不用
# # fun(name='D',12,sex='男')    # 报错
# fun(name='d',age=12,sex='男')

# 默认参数传递/缺省参数传递
# 当函数中定义了sex=男，如传参数值，就使用传的；如没有传，就用定义了的
# def fun(name,age,sex='男'):
#     print(f'姓名{name},年龄{age},性别{sex}')
#
# fun('A',11)
# fun('B',12,'女')
# fun('C',12,sex='男')

# 不定长参数传递
# 包裹位置参数传递（元组/序列）
# def fun(*args):
#     return args
# # print(fun(1,2,3))
# # print(fun('F',11,'男'))
# # 如提前准备好一组数据
# a = ['aa','bb','dd']
# b = ('A','B','C')
# # 如不带*，相当于把整个a\b，当做一个整体打印出来
# print(fun(a))
# print(fun(b))
# # 带* 会把a/b里面的数据打散，打印出来
# print(fun(*a))
# print(fun(*b))

# 包裹关键字参数传递（字典/映射）
# 函数内打印，不用带**
# 如果是调用该函数，传参时就需要带**，否则报错
# def fun(**kwargs):
#     print(kwargs)
#
# fun(A="A",B="b",C='C')
# # 有一组字典数据
# a = {'a':'a','b':11,'c':'男'}
# fun(**a)
# # fun(a)  # 报错，必现带**

# 包裹位置参数传递、关键字参数传递
# def fun(*args,**kwargs):    # 如（a,b,*args,**kwargs）,a,b是必传参数
#     print(args,kwargs)    # 函数内打印，都不用带*
#
# fun('a',11,'男',A='A',B= 11,C='男')

# def fun(a,b,*args,**kwargs):
#     print(a,b,args,kwargs)
# fun('aaa','bbb','金吒',11,'男',name='木吒',age=13,sex='男')

# 拆包
# # 元组
# def fun():
#     return 11,22
# print(fun())
# m,n = fun()
# print(m)
# print(n)
# 字典
# a = {'name':'哪吒','age':11,'sex':'男'}
# # 字典拆包，取出来的事字典的key
# x,y,z = a
# print(x)
# print(y)
# print(z)

# 引用
# def fun(a):
#     print(a)
#     print(id(a))
#     a += a
#     print(a)
#     print(id(a))
#
# fun(1)
# fun([1,2,3])

# 可变数据类型：列表，字典，集合
# 不可变数据类型：字符串、元组，整型、浮点型、布尔型，None















