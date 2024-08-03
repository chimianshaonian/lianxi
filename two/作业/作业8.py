# 有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ... #不允许用reverse,和reversed

a = 'welocme to super&Test'
# 方法一
i = 1
while i <= len(a):
    print(a[-i], end='')
    i += 1
# 方法二
for j in range(1, len(a)+1):
    print(a[-j], end='')
# 方法三
print(a[::-1])

