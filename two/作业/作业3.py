# 列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表  # 不允许用强制类型转化

a = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
b = []
# 方法一
for i in a:
    if i not in b:
        b.append(i)
print(b)
# 方法二
for i in a:
    if i in b:    # 判断如i在b列表中时，跳过本轮循环,不在就添加到b列表
        continue
    b.append(i)
print(b)

