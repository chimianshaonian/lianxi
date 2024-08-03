# 猜拳游戏
# 0剪刀、1石头、2布
# import random
#
# # 用户先出
# user = int(input('用户输入：'))
# # 电脑后出
# cpu = random.randint(0,2)
# print('电脑出的是：',cpu)
#
# # 判断输赢
# if 0 <= user <= 2:
#     if user == cpu:
#         print('平局')
#     elif (user == 0 and cpu ==2) or (user == 1 and cpu == 0) or (user == 2 and cpu == 1):
#         print('用户赢')
#     else:
#         print('电脑赢')
# else:
#     print('请输入0~2的数值')

# -------------------------------------------------------
# # 正方形
# n = 1
# while n <= 5:
#     m = 1
#     while m <= 5:
#         print('*',end=' ')
#         m += 1
#     print()
#     n += 1

# --------------------------------------------------------
# 三角形(左对齐)
# x = 1
# y = 5
# while x <= y:
#     m = 1
#     while m <= x:
#         print('*',end=' ')
#         m += 1
#     print()
#     x += 1

# --------------------------------------------------------
"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
# x = 1
# y = 5
# while x <= 5:
#     m = 1
#     while m <= (y - x):
#         print(' ',end=' ')
#         m += 1
#     n = 1
#     while n <= x:
#         print('*',end=' ')
#         n += 1
#     print()
#     x += 1

# m = 5
# for i in range(1,m+1):
#     for x in range(1,m-i+1):
#         print(' ',end=' ')
#         x += 1
#     for y in range(1,i+1):
#         print('*',end=' ')
#         y += 1
#     print()

# -----------------------------------------------------
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

"""
# x = 1
# y = 5
# while x <= y:
#     m = 1
#     while m <= (y - x):
#         print(' ',end=' ')
#         m += 1
#     n = 1
#     while n <= (x*2 -1):
#         print('*',end=' ')
#         n += 1
#     print()
#     x += 1

m = 5
for i in range(1,m+1):
    for x in range(1,m-i+1):
        print(' ',end=' ')
        x += 1
    for y in range(1,i*2):
        print('*',end=' ')
        y += 1
    print()











