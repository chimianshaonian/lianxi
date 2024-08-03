# 求斐波那契数列 1 1 2 3 5 8 13 ……    12个
# 初始两个斐波那契数列
a = [1, 1]
for i in range(2, 12):
    x = a[-1] + a[-2]
    a.append(x)
print(a)
