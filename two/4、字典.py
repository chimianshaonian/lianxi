# a = {'one': 1, 'tow': 2, 'three': 3}
# # 1、新增
# a['fove'] = 4
# print(a)
# 2、删除相关
# 2、1删除整个字典
# 语法：del 字典
# del a
# 2、2删除某个指定键值对，根据key进行删除
# 语法：del 字典[key]
# del a['one']
# print(a)
# # 2、3清空字典
# a.clear()
# print(a)

a = {'one': 1, 'tow': 2, 'three': 3}
# 3、查找相关
# # 3、1根据key找value，找不到报错
# print(a['one'])
# # print(a['six'])    # 报错
# # 3、2 get()  直接根据key找value，找不到则不报错
# # 语法：字典.get(key)，找不到默认返回None，可修改返回值
# # 找不到key时，修改返回内容，语法：字典.get(key,返回内容)
# print(a.get('tow'))
# print(a.get('six'))     # 返回None
# print(a.get('six', '找不到'))    # 修改返回值为：找不到

# 3、3获取字典内所有的key，使用keys()
# 语法：字典.keys()
# print(a.keys())         # dict_keys(*******)
# print(list(a.keys()))
# print(tuple(a.keys()))
# # 3、4获取字典内所有的value，使values（）
# # 语法：a.values()
# print(a.values())       # dict_values(********)
# print(list(a.values()))
# print(tuple(a.values()))
# # 3、5获取字典内所有的键值对，使用items()
# # 语法：字典.items()
# print(list(a.items()))
# print(a.items())        # dict_items(********)

# 使用循环打印所有键值对
for i in a.items():
    print(i)
for k, v in a.items():
    print(f'键{k},值{v}')
# 使用循环打印所有键
# 方式一
for i in a.keys():
    print(i)
# 方式二
for i in a:
    print(i)
