# # 导包模块方式
# # 方式一：import 模块名
# import mokuai1
# # 调用：模块名.方法名（）
# mokuai1.test1(1,2)   # 3
# # 涉及模块mokuai2调式代码
# import mokuai2
# mokuai2   # 在调用包内，如有测试代码，在其他调用该模块时，也会执行模块内的测试代码
#
# # 方法二：from 模块名 import 方法名
# from mokuai1 import test1
# # 调用：方法名（）
# test1(2,3)    # 5
#
# # 方式三：给模块起别名，起名后只能用别名，不能用原来的名字
# import mokuai1 as one
# # 调用：别名.方法名()
# one.test1(3,4)    # 7
#
# # 方式四：给方法起别名，起名后只能用别名，不能用原来的名字
# from mokuai1 import test1 as testone
# # 调用
# testone(1,5)    # 6

# 如导入的两个模块分别有同名的方法，A模块时加，B模块是乘，此时调用，使用后导入的模块的方法
# 解决方法：可以给方法起别名，解决该问题
# from mokuai1 import test1 as mk1_test1
# from mokuai2 import test1 as mk2_test1
# mk1_test1(2,3)    # 5
# mk2_test1(2,3)    # 6
#
# # 查看当前模块的导入顺序列表
# import sys
# print(sys.path)
#
# # 如出现，执行文件时，提示包不存在，可对包列表进行添加
# sys.path.append()

# 模块内的__all__
# 如 在__all__后变量那个方法，在调用时，就只能调用该方法，其他的无法再调用
from mokuai1 import *


# ---------------------------------------

# 导包
# 方式一：import 包名.模块名
import bao.bao_mk1
# 调用：包名.模块名.方法名（）
bao.bao_mk1.fun()

# 方式二：from 包名 import 模块名
from bao import bao_mk1
# 调用：模块名.方法名（）
bao_mk1.fun()

# 方式三：from 包名.模块名 import 方法（）
from bao.bao_mk1 import fun
# 调用 方法名（）
fun()






