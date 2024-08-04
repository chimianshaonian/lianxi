# 语法：try: ... except: ...
# try:
#     open('test.txt','r')
# except:
#     print('文件不存在')
#
# # 指定捕获指定异常（一种）
# # 语法：try: ... execpt 异常：...
# try:
#     print(aaa)
# except NameError:
#     print('变量不存在')
#
# # 捕获指定异常（多种，处理方式一致）
# # 语法：try: ... except (异常1，异常2): ...
# try:
#     open('test.txt','r')
#     print(mmm)
# except (NameError,FileExistsError):
#     print('报错了')
#
# # 捕获指定异常（多种，处理方式不一致）
# try:
#     open('test.txt','r')
#     print(aaa)
# except NameError as msg:
#     print('变量未定义')
#     print(msg)
# except FileExistsError as msg:
#     print('文件未找到')
#     print(msg)
#
# # 捕获所有异常，用Exception
# try:
#     open('test.txt','r')
#     print(nnn)
# # 如捕获到异常，要出发代码
# except Exception:
#     print('报错了')
# # 如果没有出现异常，要触发的代码
# else:
#     print('没有异常')
# # 无论有没有出现异常都要触发的代码
# finally:
#     print('有没有异常都要执行的代码')

# 自定义异常：raise 异常类对象
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
            raise Test(len(m),3)  # 主动抛出异常
    except Exception as msg:
        print(msg)
    else:
        print('密码输入完成')
fun()




