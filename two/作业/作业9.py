# 有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用用reverse,和reversed,不允许用步长

a = 'abcdef'
# 方法一
for i in range(1, len(a) + 1):
    print(a[-i], end='')
# 方法二
b = ''
for j in a:
    b = j + b
print(b)
