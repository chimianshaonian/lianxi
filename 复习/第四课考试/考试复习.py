# 1.python的数据类型都有哪些(5分)
# 注：开头字母都应该是小写
# 整型、浮点型、布尔型、字符串、列表、元组、字典、集合


# 2.列表，元组、字典、集合如何定义，分别举例（5分）
# list11 = [1,2,3]
# tuple11 = (1,2,3)
# dict11 = {'name':'牛牛'}
# set11 = {1,2,3}
# print(type(set11))
# set12 = set()
# print(type(set12))

# 3.列表[1,2,3,4,5,5,2,3,2,4]	去重，不能使用set函数（10分）
# m = [1,2,3,4,5,5,2,3,2,4]
# n = []
# for i in m:
#     if i not in n:
#       n.append(i)
# print(n)

# 4.比如有这样一个文件data.txt内存在以下内容（15分）
# lucy:21,tom:30,xiaoming:18,xiaohong:15,xiaowang:20,xiaohei:19
# 请通过代码读取文件并输出年龄大于18岁的人名
# with open('data.txt','a+',encoding='utf-8') as f:
#     # f.write('lucy:21,tom:30,xiaoming:18,xiaohong:15,xiaowang:20,xiaohei:19')
#     f.seek(0,0)
#     x = f.read().split(',')
# for i in x:
#     list1 = i.split(':')
#     if int(list1[1]) > 18:
#         print(list1[0])
#
# # 如用字典
# dict1 = {}
# for i in x:
#     list2 = i.split(':')
#     dict1[list2[0]] = int(list2[1])
# print({k:v for k,v in dict1.items() if v > 18})
#
#
# f.close()

# 5.请用列表推导式得出1-100能被3整除的数（5分）
# x = [i for i in range(1,101) if i % 3 ==0]
# print(x)


# 6.continue和break的区别（5分）
"""
continue: 退出当前一次循环，继续下一个循环，一般在while循环内需要再前面加上循环变量发生变化 ,
            可以触发后面的else里的代码
break:  终止整个循环，不会出发循环后面的else里面的代码
"""



# 7.有一堆字符串，“welocme to super&Test”，打印出emcolew ot tseT&repus全部单词原位置反转，不能使用索引[
# ::-1]输出或者reverse/reversed函数实现，自己写字符串首尾交换方法（15分）
# str1 = 'welocme to super&Test'
# def fun(*args):
#     list1 = list(str1.split(" "))
#     print(list1)
#     aa = [fun1(x) for x in list1]
#     return ' '.join(aa)
#
# def fun1(x):
#     list2 = list(x)
#     for i in range(len(list2) // 2):
#         list2[i],list2[-i -1] = list2[-i -1],list2[i]
#     return ''.join(list2)
#
# print(fun(*str1))


# 8.怎么在函数内修改/使用全局变量（5分）
# 使用global
# m = 100
# def fun():
#     global m
#     m += m
#     return m
# print(fun())

# 9.python可变数据类型和不可变数据类型都有哪些（5分）
# 可变数据类型：列表，字典，集合
# 不可变数据类型：整型、浮点型、布尔型，字符串、元组、None

# 10.递归实现斐波那契数列（10分）
# def fun1(num):
#     list1 =[]
#     def fun(n):
#         if n <= 2:
#             return 1
#         else:
#             return fun(n-1) + fun(n - 2)
#     for n in range(1,num):
#         list1.append(fun(n))
#     return list1
# print(fun1(11))

# 11、debug的快捷键：f8/f7/f9分别的作用（5分）
"""
f8：逐行执行代码，遇到函数的话，如函数内没有断点，会快速将代码执行完，
    有断点的话,快速执行到代码位置，再一行行逐步执行
f7: 逐行执行代码，遇到函数也会 进入内部逐行执行
f9：从一个断点快速执行到下一个断点，中间不停
"""

# 12、如何实现["1","2","3"]变成[1,2,3] ?（5分）
# list2 = ["1","2","3"]
# list3 = [int(x) for x in list2]
# print(list3)

# 13、开发一个注册系统，界面可以用print打印，保存姓名和年龄，存在的用户提示已注册，不存在的可以注册成功（提示建议使用函数划分不同的功能，比如查询用户，新增用户）（10分）
list1 = [{'name':'A','age':11},{'name':'B','age':12}]

# 新增
def add():
    name = input("请输入用户姓名:")
    for i in list1:
        if name == i['name']:
            print('用户已存在')
            return
    age = int(input('请输入年龄'))

    list1.append({'name':name,'age':age})
    print('新增成功')


# 查询
def fun():
    name = input("请输入用户姓名:")
    for i in list1:
        if name == i['name']:
            print(i)
            return
    print('用户不存在')

# 查询全部
def fun1():
    for i in list1:
        print(i)

def run():
    while True:
        print('1-新增用户')
        print('2-查询单个用户')
        print('3-查询全部用户')
        print('4-退出系统')
        n = int(input('请选择：'))
        if n ==1:
            add()
        elif n ==2:
            fun()
        elif n ==3:
            fun1()
        elif n ==4:
            break
        else:
            print("输入非法，请重新输入！")
run()