# 有一堆字符串，“aabbbcddef”，输出abcdef # 不允许用set

a = 'aabbbcddef'
b = ''
for i in a:
    if i not in b:
        b = b + i
print(b)

