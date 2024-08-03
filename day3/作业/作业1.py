# 使用列表推导式生成能被5整除的数（100以内）

a = [i for i in range(0, 101, 5)]
print(a)

b = [i for i in range(101) if i % 5 == 0]
print(b)
