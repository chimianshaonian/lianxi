# 使用 lambda 表达式
# 语法：lambda 参数列表：表达式   其中参数列表可有可无
# 无参数
# a = lambda :50
# print(a)      # 返回的是一个对象
# print(a())    # 加()才是调用
# # 一个参数
# a1 = lambda x:x +1
# print(a1(5))
# # 两个参数
# a2 = lambda x,y:x +y
# print(a2(1,2))
# 带默认参数
# a3 = lambda x,y,z=100:x+y+z
# print(a3(1,2))
# 不定长参数，包裹位置参数
# a4 = lambda *args:args
# print(a4('A',11,'男'))
# 不定长参数，包裹关键字参数
# a5 = lambda **kwargs:kwargs
# print(a5(name='A',age=11,sex='男'))
# b = {'name':'B','age':12,'sex':'nan'}
# print(a5(**b))

# 三目表达式
# a = 1
# b = 3
# if a >b:
#     print(a)
# else:
#     print(b)
#
# # 使用 lambda表达式
# x = lambda a,b:a if a > b else b
# print(x(1,2))

# 列表数据按字典key值排序
# student = [
#     {'name':'A','age':20},
#     {'name':'B','age':19},
#     {'name':'C','age':22}
# ]
#
# # def fun(i):
# #     return i['age']
# #
# # for i in student:
# #     print(fun(i))
# # # 排序 sort 默认升序
# # student.sort(key=fun)
# # print(student)
#
# # lambda 表达式 用降序 reverse=True
# student.sort(key=lambda i:i['age'],reverse=True)
# print(student)

# ------------------------------------
# 知识拓展
# 求绝对值 abs()
# print(abs(5))
# print(abs(-5))
# 求四舍五入的结果
# 在参数值大于2以上的 *.5四舍五入后，会去离当前值最近的偶数
# print(round(1.5))   # 2
# print(round(2.5))   # 2
# print(round(3.5))   # 4

# 计算两个数绝对值的和
# def fun(a,b):
#     return abs(a) + abs(b)
# print(fun(1,-2))

# 高阶函数
# def fun(a,b,f):
#     x = f(a)
#     y = f(b)
#     return x + y
# print(fun(2,-2,abs))

# 计算列表内每个数的平法
# list1 = [2,3,4,5]
# def fun(x):
#     return x ** 2
#
# # 高阶函数map -----映射
# res = map(fun,list1)   # 是一个对象
# print(list(res))

# 需求，计算列表内累加和
list2 = [1,2,3,4,5]
def fun1(x,y):
    return x + y

# 高级函数：reduce  ---缩减，reduce接收的函数，必现只能有两个参数
# 导入functools包
import functools
res = functools.reduce(fun1,list2)
print(res)

# 需求：找出列表内所有偶数并保存下来
# list3 = [1,2,3,4,5,6,7,8,9,10]
# def fun(x):
#     '''判断x是否是偶数'''
#     res = x % 2 ==0
#     return res
#
# for i in list3:
#     print(f'当前元素是{i},结果是{fun(i)}')
#
# # 高阶函数：filter
# res = filter(fun,list3)   # 是一个对象
# print(list(res))












