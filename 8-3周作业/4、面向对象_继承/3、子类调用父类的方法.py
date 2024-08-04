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
        self.pg = '苹果'

    def zhizuo(self):
        print(f'{self.shouyi}制作')

    def zhazhi(self):
        print(f'{self.pg}榨果汁')


# 子类
class Erzi(Fulei2,Fulei1):  # 继承两个父类，第一个父类为：Fulei2
    # 重写
    # 子类重新父类同名方法和属性
    def __init__(self):
        self.shouyi = ['独创']

    def zhizuo(self):
        print(f'{self.shouyi}制作')

    # 子类也可有自己的方法
    def guozhi(self):
        print('榨果汁')

    # <1>子类调用父类方法1：指名道姓
    # 创建子类调用父类的方法：五香
    def wuxiang(self):
        # 3、重新调下父类Fulei1的属性，也需要把self填入（即实例对象）
        Fulei1.__init__(self)
        # 1、此时调用wuxiang会报错，因为缺少1个必现的位置参数：self
        # 2、此时self属性，还是独创，如若需解决，需要重新掉下父类Fulei的属性，3、的代码
        Fulei1.zhizuo(self)

    # 创建子类调用父类的方法：香辣
    def xiangla(self):
        Fulei2.__init__(self)
        Fulei2.zhizuo(self)

    # <2> 子类调用父类方法2、super（）函数
    def two_super(self):
        # 方式一
        # 可制作香辣的，但无法制作五香的，因为严格依赖继承顺序
        # super(Erzi, self).__init__()   # 会去调用第一个父类的属性
        # super(Erzi, self).zhizuo()     # 使用第一个父类的zhizuo方法
        # 方式二
        super().__init__()
        super().zhizuo()

# 调用
if __name__ == '__main__':
    xiaoming = Erzi()

    # 此时xiaoming的属性是：独创
    print(xiaoming.shouyi)
    xiaoming.zhizuo()

    # <1>指名道姓调用
    # 1、如制作五香的，没有办法，因xiaoming现在属性是：五香
    # 2、如需制作五香的，需要用到子类调用父类的方法1、指名道姓
    # 3、需要在子类里调用五香的方法
    # 4、调用wuxiang的方法，此时xiaonming属性为：五香
    xiaoming.wuxiang()
    # 5、如再制作香辣的，同制作五香的方法一致，子类添加方法，新调父类Fulei2的属性
    xiaoming.xiangla()  # 此时xiaoming属性为香辣
    #6、后续在想制作那种类型的，直接调用其方法即可


    # <2> 子类调用父类方法2：super()函数
    xiaoming.two_super()  # 调用two_super方法后，xiaoming属性：香辣






