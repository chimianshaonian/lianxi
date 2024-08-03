'''
有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
list1 = ["小明","小红"]
list2 = [18,19]
{"小明":18,"小红":19}
'''

list1 = ["小明", "小红"]
list2 = [18, 19]


# {"小明":18,"小红":19}
# 用函数
# def fun(**kwargs):
#     return kwargs
#
# #
# x = {}
# for i in range(0, len(list1)):
#     x[list1[i]] = list2[i]
# print(fun(**x))
# 方法二
a = {}
for i in range(0, len(list1)):
    a[list1[i]]=list2[i]
print(a)
# 推导式
# b = {list1[i]:list2[i] for i in range(0, len(list1))}
# print(b)
