# 格式化输出
age = 11
name = '小李'
weight = 49.8
student_id = 12

# 我的名字小李
print('名字%s' % name)
# 我的序号0011
print('学号%4d' % student_id)  # 4个字符长度，如不够，用0填充
# 体重49.8
print('体重%.2f' % weight)  # 小数用%f  默认是6位小数，其中.2是显示2位
# 名字小李，今年11岁，明年12岁
print('名字%s,今年%d岁,明年%d' % (name, age, age+1))
# f表达式
print(f'名字{name},年龄{age}')

# 转义字符
print('hello wo\nrld')    # \n 是换行符
print('hello wo\trld')    # \t 是tab

# 不让转义字符生效
print('hello wor\\nld')
print(r'hello wor\\nld')

# print里默认有\n
print(123,end='----')
print(456)

# ---------------------------------------------------------
# 输入，input练习
'''
ipput的特点
1、当执行到input（），等用户输入后，再继续执行
2、一般存储到变量内使用
3、input 会把接收到的数据全部存储成字符串处理

'''

print('开始')
a = input('请输入今天是周几：')
# 打印a的类型
print(type(a))
# 使用f表达式
print(f'今天是周{a}')
print('结束')