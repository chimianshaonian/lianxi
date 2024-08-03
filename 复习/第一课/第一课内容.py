# 1、变量学习
# # 变量
# # 查看某个变量的id
# print(id(11))
# print(id(12))
#
"""
标识符命名规则：
1、由数字、字母、下划线组成
2、不能用数字开头
3、区分大小写
4、不能用内置关键字
"""
# # 定义变量
# a = 1
# print(a)
# print(id(a))

# 不能使用数字开头
# 2a = 1
# print(2a)
# 区分大小写
# new = 11
# print(New)   # 报错

# -----------------------------------------
# 2、格式化输出
# age = 18
# name = '小明'
# weight = 75.5
# student_id = 1   # int类型除了0本身外，其他数字不能使用0开头
#
# # 我的名字小名
# print('名字%s' % name)
# # 我的学号0001
# print('学号%04d' % student_id)   # 整数用%d，4为字符个数，其中用0进行填充
# # 我的体重75.5
# print('体重%.2f' % weight)    # %f 默认是6位小数，.2是显示2位小数
# # 名字小明，今天18岁了
# print('名字%s,年龄%d' % (name,age))
# # 名字小明，明年19岁
# print('名字%s,明年年龄%d' % (name,age+1))
# # f表达式
# print(f'我的名字{name},年龄{age}')
# # 转义字符
# print('hello wo\nrld')   # \n 换行符
# print('hello wo\trld')   # \t 是tab键
# # 不让转义字符生效
# print('hello wor\\nld')   # \n是换行，\\n转义字符就不生效
# print(r'hello wor\nld')   # 在‘’前加r，就让转义字符失效
# # prtint()里面的结束符，默认是\n
# print(123,end='---')   # 用end='' 把\n替换，在打印完该行后，未换行打印
# print(456)

# -----------------------------------------------
# 输入学习
# 输入
# print('欢迎光临')
# n = input('输入数字：')
# print(type(n))    # 查看n的类型
# print(f'输入的为{n}')
# print('拜拜')
"""
input的特点
1、当代码执行到input，会停下来，等待用户输入，输入成功后继续执行
2、一般存到变量内进行使用
3、input会把接收到的数据全部存储成字符串格式
"""

# -------------------------------------------------
# 数据类型转化
# a = '777'   # 字符串
# a1 = int(a)    # int类型
#
# list1 = [1,2,3]   # 列表
# tup1  = (1,2,3)   # 元组
# tuple(list1)      # 把列表转为元组
# list(tup1)        # 将元组转化为列表
#
# name = True
#
# str1 = '10'
# str2 = '[1,2,3]'
# str3 = '(4,5,6)'
# str4 = 'name'
#
# # eval:将字符串转化为去掉引号后最像的数据类型，前提是能转化成功，而且eval只能接受字符串
# # 一般遇到一个长的像字典的字符串，用eval进行转化，别用dict
# x = eval(str4)
# print(x)
# print(type(x))

# ---------------------------------------------------
# 5、运算符
# 包括：+ - * / // % 等
# 用（）可以提高优先级

# 多变量赋值
# a,b,c = '星','期','五'
# print(a)
# print(b)
# print(c)
# 多变量赋相同值
# a = b = 11
# print(a)
# print(b)
# 其中a = a + 1     与 a += 1  相同

# 比较运算符   真返True，假返False
# a = 1
# b = 2
# c = 3
# print(a == b)    # False
# print(a != b)    # True
# print(a < b)     # True
# print(a > b)     # False
# print(a <= b)    # True
# print(a >= b)    # False
#
# # 逻辑运算符 and 、or、 not
# # 优先级：not>and>or，可以用（）提高优先级
# x = 1
# y = 2
# z = 3
# print((x < y) and (y < z))   # True,当都为True时，才为True，否则为False
# print((x > y) or (y < z))    # True，当有一个为True时，就为True
# print(not(x > y))    # True not(False) 加上not，就是True

# if True or True and False:     # True or False，最后为True
#     print(222)
#
# # 如作为条件，整数0不成立，其他任意数都是成立
# # 0代表False
# if 0:
#     print(111)

# ----------------------------------------------------
# 6、分支学习
# 获取年龄
# age = int(input('请输入年龄：'))

# 判断年龄是否大于18岁
# if age >= 18:
#     print('可以上网')
# else:
#     print('回家写作业去')

# 判断年龄是否在0~18岁之间
# if 0 <= age <= 18:
#     print('未成年')
# elif 18 < age <= 60:
#     print('搬砖')
# elif age > 60:
#     print('颐养天年')
# else:
#     print('非法输入')

# 分支嵌套
# 获取余额
# cash = int(input('请输入余额：'))
# # 判断余额是否大于0
# if cash > 0:
#     # 获取空座位数
#     seat = int(input('请输入空位坐数量：'))
#     if seat > 0:
#         print('请坐')
#     else:
#         print('站着')
# else:
#     print('余额不足')

# ----------------------------------------------
# 7、循环学习
# # 循环次数
# n = 0     # 循环变量
# # 判断播放次数是否小于5       # 循环判断
# while n < 5:
#     print(f'扫码{n+1},必现扫码')     # 循环体
#     n += 1                        # 循环变量发生变化

# 循环四要素
"""
循环变量
循环判断
循环体
循环变量发生变化
"""

# 循环变量
# n = 1
# # 偶数累加和
# sum1 = 0
# # 循环判断
# while n <= 100:
#     # 循环体
#     # 判断n是否是偶数
#     if n % 2 == 0:
#         # print('11',n)
#         sum1 += n
#     # 循环变量发生变化
#     n += 1
# print(sum1)

# break:终止这个循环，不在继续
# 循环变量
# m = 1
# # 循环判断
# while m <= 10:
#     # 循环体
#     if m > 4:
#         print('没有拭子了')
#         break
#     print(f'用第：{m}个拭子做核酸，放到了管理了')
#     # 循环变量发生变化
#     m += 1

"""
continue: 中止这次循环继续下一次循环，在while循环内continue前需要加上循环变量发生变化，否则会陷入死循环
"""
# # 循环变量
# n = 1
# # 循环判断
# while n <= 10:
#     if n == 4:
#         print('拭子损坏')
#         n += 1
#         continue
#     # 循环体
#     print(f'用第：{n}个拭子做核酸，放到了管里')
# # 循环变量发生变化
#     n += 1

# 打印正方形，每次只能打印一个*
'''
*****
*****
*****
*****
*****
'''
# 循环变量
# x = 1
# # 循环判断
# while x <= 5:
#     # 循环体
#     y = 1
#     while y <= 5:
#         print('*',end='')
#         y += 1
#     print()
#     # 循环变量发生变化
#     x += 1

"""
循环后的else:如果循环被break，就不会再执行循环后的else里面的代码
如被continue，还会正常执行else内的代码
"""

# 循环变量
# day = 1
# # 循环判断
# while day <= 3:
#     # 循环体
#     if day == 3:
#         print('第二天没有出结果')
#         day += 1
#         continue
#     print(f'第{day}天核酸结果为阴性')
#     # 循环变量发生变化
#     day += 1
# else:
#     print('可以去上班')

# 循环变量
# day = 1
# # 循环判断
# while day <= 3:
#     # 循环体
#     if day == 2:
#         print('第二天阳了')
#         break
#     print(f'第{day}天核酸结果为阴性')
#     # 循环变量发生变化
#     day += 1
# else:
#     print('可以去上班')







