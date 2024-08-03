# 求100以内能被3整除的数，并将作为列表输出
# 推导式
a = [i for i in range(0, 101) if i % 3 == 0]
print(a)
