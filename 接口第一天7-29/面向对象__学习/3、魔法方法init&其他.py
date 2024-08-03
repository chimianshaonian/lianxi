"""
在Python中，__XX__()的函数叫魔法方法
指的是具有特殊功能的函数
"""
# 1、init
# 1-1、不带参数

# 如洗衣机的宽高是天生属性，可在生产中赋予这些属性
# class Washer:
#     def __init__(self):
#         self.width = 100
#         self.height = 200
#
#     def wash(self):
#         print(f'我的id是：{id(self)}')
#         print(f'我将{id(self)}的衣服洗干净了')
#
#     # 在类内部调用实例属性
#     def fun(self):
#         print(f'宽度是{self.width}')
#         print(f'高度是{self.height}')
#
# # 实例化对象
# haier1 = Washer()
# haier1.fun()

# 1-2、带参数
class Washer:
    def __init__(self,a,b):
        self.width = a
        self.height = b

    def fun(self):
        print(f'我的id是{id(self)}')
        print(f'我将{id(self)}的衣服洗干净了')

    def fun1(self):
        print(f'宽是{self.width}')
        print(f'高湿{self.height}')
        self.fun()

    # 2、魔法方法 str
    # 如定义了str方法，那就打印从这个方法中return的数据
    def __str__(self):
        # 返回的必现是字符串
        return f'我是洗衣机，宽度是{self.width},高度是{self.height}'

    # 3、魔法方法del
    # 当删除对象时，解释器会默认调用__del__（）方法
    def __del__(self):
        print('资源释放，比如关闭文件')

# 实例化函数，并传参
haier1 = Washer(10,20)
haier1.fun1()

# 如不手动执行，那在最后也会执行del的代码





