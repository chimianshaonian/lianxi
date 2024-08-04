# 重写后，子类调用父类的同名方法和属性
"""
调用父类的方法
1、指名道姓调用
    优点：可以灵活的调用各个父类的方法
    缺点：必现保证继承关系存在，且父类不改名，如父类改名，就需改代码
2、使用super()函数，调用父类方法
    优点：可以不用指定父类名，只要继承关系还存在，就会严格按照继承顺序去找方法
    缺点：严格依赖继承顺序，不灵活，一般用于单继承
"""

class Fulei1:
    def __init__(self):
        self.shouyi = ['五香']

    def zhizuo(self):
        print(f'{self.shouyi}制作')

class Fulei2:
    def __init__(self):
        self.shouyi = ['香辣']

    def zhizuo(self):
        print(f'{self.shouyi}制作')

# 子类
class Erzi(Fulei2,Fulei1):
    def __init__(self):
        self.shouyi = ['独创']

    def zhizuo(self):
        print(f'{self.shouyi}制作')

    # 子类自由方法
    def guozhi(self):
        print('榨果汁')

    # # <1> 子类调用父类方法1、指名道姓
    # # 创建子类调用父类的方法：五香
    # def wuxiang(self):
    #     # 3、重新掉下父类的Fulei1的属性，也需要把self填入（即实例对象）
    #     Fulei1.__init__(self)
    #     # 1、此时调用Wuxiang会报错，因为缺少1个必需的位置参数:'self'
    #     # 2、此时self属性是：独创，如要解决，需重新调下父类Fulei1的属性
    #     Fulei1.zhizuo(self)
    #
    # # 创建子类调用父类的方法：香辣
    # def xiangla(self):
    #     Fulei2.__init__(self)
    #     Fulei2.zhizuo(self)

    # <2> 子类调用父类方法2、super（）函数
    def two_super(self):
        # 方式一：了解
        # 可制作香辣的，但无法制作五香的，因为严格依赖继承顺序
        # super(Erzi, self).__init__()  # 会去调第一个父类的属性
        # super(Erzi, self).zhizuo()    # 使用第一个父类的zhizuo方法
        # 方式二：
        super().__init__()
        super().zhizuo()

# 调用
if __name__ == '__main__':
    xiaoming = Erzi()
    # 此时xiaoming的属性是：独创
    # print(xiaoming.shouyi)
    # xiaoming.zhizuo()

    # <1> 子类调用父类方法1、指名道姓
    # 1、如此时需要制作五香的，没有办法，因为xiaoming现在是的属性是：五香
    # 2、如需要制作五香的，就需要用到子类调用父类的方法：1、指定道姓
    # 3、需要在子类里调用五香的方法
    # 4、调用Wuxiang方法，此时xiaoming的属性为：五香
    # xiaoming.wuxiang()
    # # 5、如再制作香辣的，也是同制作五香的方法一样，子类添加方法、新调父类Fulei2的属性
    # xiaoming.xiangla()   # 此时xiaoming属性为：香辣
    # # 6、后续再想制作那种类型的，就直接调用方法即可

    # <2> 子类调用父类方法2、super（）函数
    xiaoming.two_super()   # 调用two_super方法后，xiaoming属性：香辣