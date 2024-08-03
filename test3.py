# 7. 有一堆字符串，“welocme to super&Test”，打印出emcolew ot tseT&repus全部单词原位置反转，不能使用索引[
# ::-1]输出或者reverse/reversed函数实现，自己写字符串首尾交换方法（15分） 前后互换元素
str1 = "welocome to super&Test"
list1 = list(str1.split(" "))
str2 = str(list1)

def fun1(str1):
    for i in list(str1.split(" ")):
        return list(i)

#
# def fun(str1):
#     for m in list1:
#         print(list(m))
#         # for i in list(m):
#         #     print(i)
#         for j in range(len(list(m))//2):
#             #     # 根据下标首尾互换元素
#             list(m)[j], list(m)[-j - 1] = list(m)[-j - 1], list(m)[j]
#             print(list(m))
#             return
print(fun1(str1))
# print("".join(list1))  # 拼接



