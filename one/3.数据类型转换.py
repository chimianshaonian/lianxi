# 字符串 转化为int类型
a = '111'
a1 = int(a)
# 打印并，查看a1类型
print(a1, 'a1的类型：', type(a1))

# 列表
list1 = [1, 2, 3]
# 列表转为元组，并打印类型
print(tuple(list1), 'list1转化后类型：', type(tuple(list1)))

# 元组
tup1 = (4, 5, 6)
# 将元组转为元组，并打印类型
print(list(tup1), 'tup1转化后的类型为：', type(list(tup1)))

# eval使用
'''
将字符串转化为去掉引号后最像的数据类型，前提是能转化成功，而且eval只能接受字符串

注意：一般遇到一个长得像字典的字符串，用eval进行转化，不要用dict
'''
a1 = '10'        # 整数 10
a2 = '[1,2,3]'   # 列表[1,2,3]
a3 = '(4,5,6)'   # 元组（4,5,6）
a4 = 'name'      # 出错

x = eval(a)  # 将a1 分别换成a2\a3\a4执行
print(x)
# 打印x的类型
print(type(x))



