one = '012345'
# 切片 语法：序列[开始下标：结束下标：步长]  默认是1
# 如下标是负数，负几就是倒数第几个元素
# 原则：顾头不顾尾，左闭右开，如开始&结束一致，以不顾尾优先，所以切空
# print(one[3:3])  # 切空
# print(one[1:3:1])  # 12
# print(one[1:3:-1])  # 空
# print(one[1:])  # 12345，不写结束，默认是到结尾，默认步长是1
# print(one[:4])  # 0123   不写开头，默认是从0开始
# print(one[::-1])  # 543210
# print(one[5:2:-1])  # 543 -1 向左找

# 查找
# a = 'hello world and supertest and chenghao and Python'
# 1、根据子串的出现查找下标
# # 1、1 find（） 语法：字符串.find(子串，开始，结束)，找的返回第一个匹配项的下标，找不到返回-1
# print(a.find('and'))
# print(a.find('and', 13, 155))
# print(a.find('ands'))  # 找不到，返回-1
# # 1、2 index（） 语法：字符串.index(子串，开始，结束)   找到返回第一个匹配项下标，找不到报错
# # print(a.index('ands'))  # 报错
# print(a.index('and'))
# print(a.index('and', 17, 60))
# # 1、3统计子串出现的次数 count（）
# # 语法：字符串.count(子串，开始，结束)
# print(a.count('and'))
# print(a.count('and', 11, 40))
# print(a.count('ands'))         # 0
# # 1、4 从右开始查
# print(a.rfind('and'))
# print(a.rindex('and'))

'''
注意：字符串是不可变数据类型
'''
# 2、字符串修改
# 2、1 替换 replace() 语法：字符串.replace（旧，新，次数），如不写次数，默认全部
# print(a.replace('and', '和'))
# # 2、2 分割 split() 语法：字符串.split(分隔符)，注：分隔符会给吃掉
# print(a.split('and'))
# # 2、3字符串拼接，join  语法： 字符或子串.join(需要拼接的序列)
# a1 = 'abcde'
# print('--'.join(a1))
# print('+'.join(a1))

# 3、功能性修改
# a = 'hello world and supErtest and chenghao and Python'
# # 3、1将整个字符串首字母变为大写，其他变小写
# print(a.capitalize())
# # 3、2将字符串里面每个单词字符变小写
# print(a.title())
# # 3、3将全部字母变大写
# print(a.upper())
# # 3、4将全部字母变小写
# print(a.lower())
#
# c = "    hello world and supertest and chenghao and Python     "
# # 3、5去除字符串两侧的空白字符
# print(c.strip())
# print(c.lstrip())     # 去除左侧空白字符
# print(c.rsplit())     # 去除右侧空白字符
# print(c.strip('n h'))   # 去除首位两侧字母+空白字符，其中n,h的位置无所谓
#
# # 4、补全字符，注意：只能用一个字符
# d = 'hello'
# # 4、1居中补全
# print(d.center(10,'-'))
# # 4、2靠左补齐
# print(d.ljust(10,'-'))
# # 4、3靠右补齐
# print(d.rjust(10,'*'))
#
# # 5、判断，如真，就返回True；否则返False
# a1 = "hello world and supertest and chenghao and Python"
# # 5、1判断字符串是否以指定子串开始
# print(a1.startswith('and', 1, 55))
# # 5、2判断字符串是否以指定子串结尾
# print(a1.endswith('Python'))

a1 = 'he你'
a2 = 'he123'
a3 = '123'
a4 = ' '
# 5、3判断字符串是否全是字符组成
print(a1.isalpha())    # True,中文也视为中文字符
# 5、4判断字符串是否全由数字组成
print(a3.isdigit())
# 5、5判断字符串是否全由字符或数字组成
print(a3.isalnum())
# 5、6判断字符串是否全由空白字符组成
print(a4.isspace())








