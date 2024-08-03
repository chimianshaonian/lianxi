# 1、函数一
"""
函数作用：
将一段具有独立功能的代码块整合到一个整体并命名，在需要的位置调用该函数
"""
# 计算并打印1+2的和，定义一个函数实现

# 如需要参数，函数在定义阶段后面的括号里需要添加形成
# def fun(i,j):
#     res = i + j
#     return res
# print(fun(1,2))   # 调用阶段，需要传递实参

# 1-1、题目1：函数内调用函数
# def fun():
#     print('--------------')
#
# # 定义一个函数，打印n条横线
# def fun1(i):
#     for n in range(i):
#         fun()
# fun1(5)

# 1-2、题目2：
# 第一个函数，计算三个数的和
# def fun1(x,y,z):
#     res = x + y + z
#     return res
# #第二个函数，计算三个数的平均值，要先用第一个函数进行计算的和，然后除以3
# def fun2(a,b,c):
#     a = int(fun1(a,b,c) / 3)
#     return a
# print(fun2(2,3,4))    # 3

# ------------------------------------------------
# 2、函数二
# 2-1、变量作用域
"""
变量作用域：指变量生效的范围，分为局部变量、全局变量
"""
# 2-1-1、局部变量
# def fun():
#     # 定义一个局部变量（变量只在当前函数体内生效）
#     m = 100
#     return m
# print(fun())

# 2-1-2、定义全局变量
# m = 1000
# def fun1():
#     # 声明m为全局变量
#     global m
#     m = 100
#     print(m)
# def fun2():
#     print(m + 1)
#
# fun1()   # m 为100，
# # fun2()   # 1001
# # fun1中m,设为全局变量 global m,再次调用fun2
# fun2()

# 2-2、当第一函数内有多个返回值，还返回
# 2-2-1、如有两个return
"""
注：只执行第一个return，因为return可以退出当前函数，
导致第二个return的代码，不再执行
"""
# def fun():
#     return 1
#     return 2
# print(fun())
# 2-2-2、需要把两个人都返回
"""
如把返回值放在一个return中（如下函数），默认返回元组，如指定返回类型
就返回指定的类型
"""
# def fun():
#     return 10,20
# print(list(fun()))   # 元组转化为列表类型

# 2-3、函数的参数
# 2-3-1、定义阶段
# 默认参数传递/缺省参数传递
# def fun(name,age,sex):
#     print(f'名字{name},年龄{age},性别{sex}')
#
# # 2-3-2、调用阶段
# # 2-3-2-1、位置参数传递（参数的位置、个数必现保持和定义的时候一致）
# """
# 位置参数传递（参数的位置、个数必现保持和定义的时候一致）
# """
# fun('悟空',11,'男')
# fun(11,'悟空','男')   # 错误，就出现了年龄在姓名里，姓名在年龄里
# # 2-3-2-2、关键字参数传递
# """
# 关键字参数传递：函数调用时，如有位置参数时，位置参数必现在关键字参数的前面，
# 但关键字参数直接不存在先手顺序
# """
# fun('悟能',age=12,sex='男') # 如有使用关键字传递，那后面的都需要用，前面的可以不用

# 2-3-2-3、默认参数传递/缺省参数传递
# def fun(name,age,sex,Country='中国'):
#     print(f'名字{name},年龄{age},性别{sex}，国籍{Country}')
#
# fun('如来',14,'男','天竺')  #虽然定义了国籍，但如传参数值了，就使用传的；如没有传，就用方法里定义的

# 2-4、不定长参数传递
"""
用于不确定调用时，会传多少个参数,分为两种：包裹位置参数传递、包裹关键字传递
"""
# 2-4-1、包裹位置参数传递(元组/序列)，用*args
"""
如传参时，不带*，相当于把整个参数值当做一个整体打印出来
如带*，会把参数值里面的数据打散，打印出来
"""
# def fun(*args):
#     print(args)
#
# # fun('a',11,'男')
# # fun('bb')
# # 准备好一组数据
# a = ['aa',111,'男']
# fun(a)      # 不带*，把a当成一个整体进行打印
# fun(*a)     # 带*，把a里面的数据打散，进行打印

# 2-4-2、包裹关键字参数传递（字典/映射），用**kwargs
"""
传参时，必须带**，否则报错
"""
# def fun(**kwargs):
#     print(kwargs)   # 在函数内，打印不用带**
#
# fun(name='金吒',age=11,sex='男')
# a = {'name':'哪吒','age':12,'sex':'男'}
# fun(**a)
# fun(a)   # 报错，必现要带**

# 包含默认参数，不定长参数
# def fun(a,b,*args,**kwargs): # a,b是必传参数，其他为非必传参数
#     print(args,kwargs)
#     # 如打印某个值
#     print(args[0])
#     print(kwargs['name'])
#
# fun('木吒',12,'男','你好',name='八戒',age=122)

# 2-5、拆包
# 2-5-1、元组
# def fun():
#     return 10,20
# print(fun())
# m , n = fun()
# print(n)
# # 类似于如下
# list1 = [1,2]
# a,b = list1
# print(a)

# 2-5-2、字典
# 对字典拆包，取出来的时字典的key
# dict1 = {'name':'a','age':11}
# a,b = dict1
# print(a)

# 2-6、引用
# 可以用id(),来判断两个变量是否为同一个值的引用
"""
可变数据类型：列表、字典、集合------id不变
不可变数据类型：字符串、元组、整型、浮点型、布尔型型、None------id会变
"""
# def fun(a):
#     print(a)
#     print(id(a))
#     a += a
#     print(a)
#     print(id(a))
#
# fun(1)
# fun([1,2,3])

# --------------------------------------------------
# 3、文件操作
# 3-1、打开文件
# 语法：open(文件名/路径，以那种模式打开，编码类型)
# with open('33.txt','a+',encoding='utf-8') as f:   # 后续代码需要缩进

"""
r：只读方式打开文件，且指针移到最开始，如文件不存在，则报错
r+:对文件进行读写，指针移到最开始，编辑的内容会从开始覆盖已有内容，如文件不存在
w: 用于写入，文件如不存在，则会创建一个；如已存在，则会把原文件内容删除，从头编辑
w+:用于读写，文件如不存在，则会创建一个；如已存在，则会把原文件内容删除，从头编辑
a: 用于追加，文件如不存在，则会创建一个；如已存在，指针移动端末尾，编辑内容后，追加到已有内容之后
a+:用于读写，文件如不存在，则会创建一个；如已存在，指针移动端末尾，编辑内容后，追加到已有内容之后
    """
# 3-2、操作文件
# 3-2-1、写入
#     f.write('hell0')
# # 读取指针位置
# # 语法：文件.tell()
#     print(f.tell())
# # 移动指针位置
# # 语法：文件.seek()
#     f.seek(0,0)   # 移动端开头位置，且只有移动位置为开头时，才能使用非0整数，向后读取几位
#     # f.seek(0,1)   # 当前位置
#     # f.seek(0,2)   # 末尾位置
# # 读取内容
#     # 读取指针支行所有的内容
#     # 语法：文件.read()   默认是全部，如传参，就是读取指针后的*个字符
#     print(f.read())
#     # 读取指针后的一张数据
#     # 语法：文件.readline()
#     # 读取指针后所有行数据
#     # 语法：文件.readlines()
# # 关闭文件
#     f.close()

# ---------------------------------------------
# 4、os包学习
# 导包 os
import os,shutil
# 1、文件
# 1-1、文件重命名
# 语法：os.rename(现在，新的)，找不到则报错
# os.rename('33.txt','333.txt')
# 1-2、删除文件
# 语法：os.remove(文件名)
# os.remove('test.txt')

# 2、文件夹
# 2-1、创建文件夹
# 语法：os.mkdir(文件名)   # 创建单层文件夹
# os.mkdir('test')
# 语法：os.makedirs(文件夹1/文件夹2)    # 创建多层级文件夹
# os.makedirs('test1/test2')
# 2-2、删除文件夹
# 删除空文件夹 语法：os.rmdir(名称)
# os.rmdir('test')
# 删除非空文件件，需要导包shutil
# 语法：shutil.rmtree(名称)
# 2-3、查看当前所在的工作目录
# 语法：os.getcwd()
# print(os.getcwd())
# # 2-4、查看整个目录的列表
# # 语法：os.listdir(路径)
# print(os.listdir('D:/student/lianxi/复习/第三课'))
# # 2-5、改变工作目录
# # 语法：os.chdir(路径)
# os.chdir('D:/student/lianxi/复习/第三课/test')
# print(os.getcwd())
# # 2-6、获取某个文件/目录的父级路劲
# # 语法：os.path.dirname(文件/路径)  # 即可以是文件，也可以是指定路径查看
# print(os.path.dirname('第三课内容.py'))
# # print(os.path.dirname('D:/student/lianxi/复习/第三课'))
# # 2-7、获取当前文件的所在路径
# # 语法：os.path.dirname(__file__)
# print(os.path.dirname(__file__))

# ----------------------------
# 5、匿名函数
# 语法：lambda 参数列表：表达式   其中参数列表可有可无
# 5-1、无参数
# fn2 = lambda: 100
# print(fn2)
# print(fn2())   # 需要加（），才是调用
# 5-2、一个参数
# a = lambda a1:a1+1
# print(a(5))
# 5-3、两个参数
# a2 = lambda m,n:m + n
# print(a2(3,4))
# 5-4、带默认参数
# a = lambda x,y,z=100:x+y+z
# print(a(1,2))
# 5-5、不定长参数：包裹位置传递
# a = lambda *args:args
# print(a('后羿',1500,'男','野区'))
# b = ('后羿',1500,'男','野区')
# print(a(*b))   # 如不带*，是把b当做一个整体给a;带*，把b内的元素打散给a
# 5-6、不定长参数：包裹关键字
# a = lambda **kwargs:kwargs
# print(a(name='牛牛',age=110,sex='男'))
#
# b = {'name':'猪猪','age':120,'sex':'男'}
# print(a(**b))   # 如不带**，报错

# 5-7、三目表达式
# a = 1
# b = 2
# n = a if a < b else b  # 如果a < b,那n=a，否则n = b
# m = lambda a,b:a if a < b else b
# print(m(2,3))

# student = [
#     {'name':'A','age':20},
#     {'name':'B','age':19},
#     {'name':'C','age':22}
# ]
#
# # 将列表安装年龄进行排序
# def fun(x):
#     return x['age']
#
# for i in student:
#     print(fun(i))
#
# student.sort(key=fun)
# print(student)
#
# # 使用lambda,对上面代码简化
# student.sort(key=lambda x:x['age'],reverse=True)

# ------------------------------------------------
# 6、知识点拓展
# 6-1、绝对值 abs()
# print(abs(5))
# print(abs(-5))
# # 6-2、求一个四舍五入的结果，当数大于2时，2.5、3.5、4.5，取离最近的偶数
# # round()
# print(round(1.4))  # 1
# print(round(1.5))  # 2
# print(round(2.5))  # 2
# print(round(2.6))  # 3
# print(round(3.5))  # 4
# print(round(4.5))  # 4

# 计算两个数绝对值的和
# def fun(a,b):
#     return abs(a)+abs(b)
# print(fun(-4,6))

# 6-3、高阶函数
# def fun(a,b,f):
#     return f(a)+f(b)
# print(fun(-3,5,abs))    # abs不要用（），加（）就是调用
#
# # 计算两个数四舍五入的和
# print(fun(1.4,2.5,round))

# 需求：计算列表内的每个数的平方
# list1 = [1,2,3,4]
# def fun(x):
#     return x ** 2

# 6-3-1、高阶函数 map -----映射
# 语法：map(方法，列表)
# 将传入的函数变量，作用到lst变量的每个元素中，并将结果组成新的类别返回
# res = map(fun,list1)
# print(list(res))
# 6-3-2、reduce()
# reduce(方法，lst)
# 其中方法必现有两个参数，每次方法计算的结果继续喝序列的下一个元素做累积计算
# import functools
# a = [1,2,3,4]
# def fun(a,b):
#     return a + b
# x = functools.reduce(fun,a)
# print(x)

# ------------------------------------------------
# 7、递归学习
"""
特点：
1、函数内部自己调用自己
2、必现有出口
"""
# 计算3以内的累加和
a = []
def fun(x):
    # 如是1，直接返回1---出口
    if x == 1:
        return 1
    return x + fun(x-1)
print(fun(5))



