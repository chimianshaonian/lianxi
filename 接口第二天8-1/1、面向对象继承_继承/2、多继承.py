# 父类1

class Fulei1:
    def __init__(self):
        self.shouyi = ['五香']

    def zhizuo(self):
        print(f'{self.shouyi}制作')   # 五香制作

# 父类2

class Fulei2:
    def __init__(self):
        self.shouyi = ['香辣']

    def zhizuo(self):
        print(f'{self.shouyi}制作')    # 香辣制作

# 子类
class Eizi(Fulei2,Fulei1):   # 继承两个父类，为：Fulei2、Fulei1
    pass

# 调用
if __name__ == '__main__':
# 实例化
    xiaoming = Eizi()     # xiaoming的第一个父类是：Fulei2
    """
    当子类继承多个父类时，默认使用第一个父类的同名数和方法
    """
    print(xiaoming.shouyi)   # 此时xiaoming的属性为：香辣
    xiaoming.zhizuo()     # 香辣制作


