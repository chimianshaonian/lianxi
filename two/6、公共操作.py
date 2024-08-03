a = [1, 2, 3, 1]
b = [4, 5, 6]
# 1、运算符
# 1、1 合并（加）到一起
# print(a + b)
# # 1、2 复制
# print(a * 2)
# # 1、3 在不在容器内 in/not in
# print(1 in a)
# print(1 not in a)
# 2、公共方法
# 2、1 容器长度，len()
# print(len(a))
# # 2、2删除，del
# del a
# 2、3最大值max()，最小值min()
# print(max(a))
# print(min(b))
# # 2、4range(),语法：for i in range(start,end,步长)
# # 生成以start开始到end结束的数字，但不包含end
# for i in range(1,10,2):
#     print(i)      # 1,3,5,7,9
# # 只写一个数字如10，那就是生成0~9的数字，默认步长是1
# for i in range(10):
#     print(i)
# 2、5enumerate（）
# 语法：enumerate(可遍历对象，start=0),其中start参数用来设置遍历数据的下标起始值，默认是0
# 函数用于将一个可遍历的数据对象（如列表、元组或字典）组合成一个索引序列，同时列出数据和数据下标，一般用在for循环当中
a1 = ['a', 'b', 'c', 'd', '你好']
for i in enumerate(a1, start=1):
    print(i)
for i,j in enumerate(a1,start=1):
    print(f'下标是{i},值是{j}')

# 3、数据类型转化
# 3、1某个序列转元组
# 语法 tuple(序列)
# 3、2将序列转列表
# 语法：list(序列)
# 3、3将序列转集合   ---- 快速去重，且不支持下标
# 语法：set(序列)






