# 求累加和
# def fun(n):
#     # 设置出口
#     if n ==1:
#         return 1
#     # 计算累加和：n+(n-1的累加和)
#     return n + fun(n-1)
#
# res = fun(100)
# print(res)

# 斐波那契数列：前两个数是1，后面两个数是前两个数的和

def fun(n):
    '''计算第n位的斐波那契值是多少'''
    # 如果n是1，直接放回1
    # 如果n是2，直接返回2
    if n == 1 or n == 2:
        return 1
    # 如果n是其他数，返回前一个数和前两个数的和
    else:
        return fun(n-1) + fun(n-2)
print(fun(40))





