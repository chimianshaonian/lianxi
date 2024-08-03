# 1.需求：有三个办公室，8位老师，8位老师随机分配到3个办公室
# import random
# a = [[],[],[]]
# for i in range(1,9):
#     a[random.randint(0,2)].append(i)
# print(a)

# 2、求100以内能被3整除的数，并将作为列表输出
# a = [i for i in range(101) if i % 3 ==0]
# print(a)

# 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表  # 不允许用强制类型转化
# a = [1,2,3,4,3,4,2,5,5,8,9,7]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# 4、求斐波那契数列 1 1 2 3 5 8 13 ……    12个
# a = [1,1]
# for x in range(2,12):
#     y = a[x-1] + a[x-2]
#     a.append(y)
# print(a)

# 5、求100以内的质数（只能被1和它本身整除）
# a = [] # 合数
# b = [] # 质数
# for i in range(2,101):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         b.append(i)
# print(b)

# 6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef #不允许用类型转化
# a = 'aabbbcddef'
# b = ''
# for i in a:
#     if a.count(i) == 1:
#         b += i
# print(b)

# 7、有一堆字符串，“welocme to super&Test”，打印出superTest，#不能查字符的索引
# a = 'welocme to super&Test'
# b = a.split(' ')
# for i in b:
#     if '&' in i:
#         res = i.replace('&','')
#         print(res)

# 8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ... #不允许用reverse,和reversed
# 方式1
a = 'welocme to super&Test'
b = list(a)
# for i in range(len(b) //2):
#     b[i],b[-i-1] = b[-i-1],b[i]
# print(''.join(b))
# 方式2
# c = ''
# for j in range(len(a)):
#     c1 = b.pop()
#     c += c1
# print(c)
# 方式3
# d = ''
# for m in a:
#     d = m + d
# print(d)

# 9、有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用用reverse,和reversed,不允许用步长
# a = 'abcedf'
# b = ''
# for i in a:
#     b = i + b
# print(b)

# 10、有一堆字符串，“aabbbcddef”，输出abcdef # 不允许用set
a = 'aabbbcddef'
b = ''
for i in a:
    if i not in b:
        b += i
print(b)

