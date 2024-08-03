# 1、异常 语法  try ... except ...
"""
try:
    可能发生错误的代码
except:
    如出现异常执行的代码
"""
# try:
#     open('11.txt','r')    # 打开不存在的文件，报错
# except:
#     print('文件存在')

# 2、捕获指定异常（一种）
# 如文件存在打开
# open('11.txt','r')   # 文件不存在报错：FileNotFoundError
# try:
#     # open('11.txt','r')
#     print(xxx)     # NameError
# except FileNotFoundError:
#     print('文件存在报错')

# 3、捕获指定异常（多种，处理方式一致）
# 语法：try ... except (异常1，异常2) ...
# try:
#     # open('11.txt','r')
#     print(xxx)     # NameError
# except (FileNotFoundError,NameError):
#     print('文件存在报错')
#     print('变量名不存在')

# 4、捕获指定异常（多种，处理方式不一样）
# try:
#     # open('11.txt','r')
#     print(xxx)     # NameError
# except FileNotFoundError:
#     print('文件存在报错')
# except NameError:
#     print('变量名不存在')

# 5、捕获异常魔术信息
# try:
#     open('11.txt','r')
#     # print(xxx)     # NameError
# except FileNotFoundError as msg:
#     print('文件存在报错')
#     print(msg)
# except NameError as msg:
#     print('变量名不存在')
#     print(msg)

# 6、捕获所有异常，用Exception，相当于是所有异常的父类
# a = 1
# try:
#     # open('11.txt','r')
#     # print(xxx)     # NameError
#     print(a)
# except Exception:
#     print('报错了')
# 7、如没有异常时，要执行的代码，用else
# else:
#     print('没有异常')
# 8、无法是否有异常都会执行的代码，用finally,如关闭文件
# finally:
#     print('无论有无异常，都会执行这行代码')

# 9、自定义异常，raise 异常类对象
class Test(Exception):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    # 抛出异常的描述
    def __str__(self):
        return f'长度{self.a},不少于{self.b}字符'

def fun():
    try:
        m = input('请输入密码：')
        if len(m) < 3:
            raise Test(len(m),3)     # 主动抛出异常
    except Exception as msg:
        print(msg)
    else:
        print('密码输入完成')

fun()