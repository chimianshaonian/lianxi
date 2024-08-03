# 父类1
class Fulei1:
    def __init__(self):
        self.shouyi = ['五香']

    def zhizuo(self):
        print(f'{self.shouyi}制作')

# 父类2
class Fulei2:
    def __init__(self):
        self.shouyi = ['香辣']

    def zhizuo(self):
        print(f'{self.shouyi}制作')

# 子类
class Erzi(Fulei2,Fulei1): # 继承两个父类：Fulei2、Fulei1，第一个父类：Fulei2
    # 重写
    # 子类重写父类同名方法和属性
    def __init__(self):
        self.shouyi = ['独创']

    def zhizuo(self):
        print(f'{self.shouyi}制作')  # 独创制作

    # 子类也可有自己方法
    def guozhi(self):
        print('榨果汁')

"""
重写的条件
1、依赖于继承
2、重写的必现是父类的同名方法
"""

# 调用
if __name__ == '__main__':
    xiaoming = Erzi()   # 此时xiaomi的属性是：独创
    # 子类和父类相同属性和方法时，默认使用子类的同名属性和方法
    print(xiaoming.shouyi)
    xiaoming.zhizuo()
    xiaoming.guozhi()



