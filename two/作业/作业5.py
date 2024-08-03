# 求100以内的质数（只能被1和它本身整除）
a = []
for i in range(2, 101):
    x = True
    # 取2到当前数的平方根的下一位数，因range（）是不含end，如25，平方根是5，那用range(),就是range(2,5+1)
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            x = False
            break
    if x:
        a.append(i)
print(a)
