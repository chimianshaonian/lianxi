# 自定义模块
"""
每个py文件都可以作为一个模块
模块的名字需要符合标识符命名规则
1、右数字、字母、下划线组成
2、不能以数字开头
3、区分大小写
4、不能用内置关键字
"""
# 创建，my_one.py  my_two.py
# 1、模块
# 1-1、导入模块的方法
# 方式一：import 模块1，模块2
# import my_one
# # 调用:模块.方法名（）
# my_one.test1(2,3)    # 5
#
# # 方式二：from 模块 import 方法名
# # 如 import 可以是单方法名，也可以是*，*为全部方法名
# from my_one import *
# # 调用：方法名（）
# test1(2,4)    # 6
# test2(3,1)    # 2
#
# # 方法三：给模块起别名，起别名后就只能用别名，不能用原名
# # import 模块 as 别名
# import my_one as one
# # 调用：别名.方法名（）
# one.test1(2,1)    # 3
# one.test2(2,1)    # 1

# 方式四：给方法起别名，起别名后，就只能用别名，不能用原名
# from 模块 import 方法名 as 别名
# from my_one import test1 as ong1
# # 调用：别名（）
# ong1(2,2)   # 4

"""
在对自定义模块进行测试时，如模块文件内，有调用代码，那在对模块文件进行测试时,
也会把调试代码，执行到
"""
# 解决方法，使用 __main__，具体查看模块文件内容，如my_one

# 1-2、在使用from...import..导入两个模块时，分别有同名的方法test1，如my_one是加，my_two是乘
# 此时调用的是后导入的模块内的方法
# from my_one import *
# from my_two import *
#
# test1(1,2)   # 调用的时乘法
#
# # 解决方法，起别名
# from my_one import test1 as one1
# from my_two import test1 as one2
# one1(1,2)   # 3
# one2(1,2)   # 2

# 1-3、查看当前模块的导入顺序列表
# import sys
# print(sys.path)
# 先查看当前目录，如找不到，解释器会去根目录找

# 1-4、__all__
"""
当一个模块文件中有__all__变量时，如用from ... import *时，
只能导入这个列表内的元素，如 __all__ = ['test1'],此时只能用test1
"""
# from my_two import *
# test1(2,3)
# test2(3,2)    # 报错，因为只用用test1

# ------------------------------------------------------------
# 2、包
# 2-1、先创建包
# 再在包里创建方法
"""
当创建包时，会字典创建__init__.py文件，那该文件就称为包
__init__.py文件，控制着包的导入行为
"""

# 2-2、导包
# 方式一：import 包名.模块名
# import bao.my11
# # 调用：包名.模块名.方法名（）
# bao.my11.fun()

# 方法二：from 包名 import 模块名
# from bao import my11
# # 调用：模块名.方法名（）
# my11.fun()

# 方法三：from 包名.模块名 import 方法名
from bao.my22 import fun
# 调用：方法名（）
fun()











