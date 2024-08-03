# 有一堆字符串，“welocme to super&Test”，打印出superTest，#不能查字符的索引

a = 'welocme to super&Test'
for i in a.split():
    if '&' in i:
        b = i.split('&')
        print(b[0]+b[1])