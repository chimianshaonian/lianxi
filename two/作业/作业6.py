# 有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef #不允许用类型转化

a = 'aabbbcddef'
b = ''
for i in a:
    if a.count(i) == 1:
        #continue
        print(i, end='')
        b += i
print(b)

