"""
私有权限的特点：
1、父类无法继承给子类直接使用
2、添加私有权限的属性和方法，不能在类外面使用

设置私有权限的方法：
在属性和方法名，前加上两个下划线：__
"""

# 父类
class Fulei:
    def __init__(self):
        self.shouyi = ['五香']
        # 私有属性
        # 在属性名前添加两个__，变为私有的属性，此时子类是无法调用的
        self.__money = 200  # 私有的

    def zhizuo(self):
        print(f'{self.shouyi}制作')

    # 私有方法,也是在方法名前加上两个__
    def __get_money(self):
        print(self.__money)

    """
    一般定义获取和修改私有属性值的命名习惯
    获取：get_XX  用来获取私有属性
    修改：set_XX  用来修改私有属性值
    """

    # 私有的属性和方法，只能在内部进行调用
    def set_money(self,n):
        if n > 0:
            self.__money += n
        else:
            print('攒钱呢')

    def print_money(self):
        self.__get_money()

# 子类
class Erzi(Fulei):
    pass

# 调用
if __name__ == '__main__':
    xiaoming = Erzi()
    print(xiaoming.shouyi)
    xiaoming.zhizuo()  # 五香制作
    # print(xiaoming.__money)     # 报错，无法直接调用父类的私有属性
    # xiaoming.__get_money()      # 报错，无法直接调用父类的私有方法
    xiaoming.print_money()     # 200
    xiaoming.set_money(100)
    xiaoming.print_money()     # 300，此时父类的私有属性money = 300
    xiaoming.set_money(-100)   # 攒钱呢
    xiaoming.print_money()

# 查看类的属性和方法
print(Fulei.__dict__)   # 类的属性和方法
print(xiaoming.__dict__)  # 只能看到类的方法
print(xiaoming._Fulei__money)
xiaoming._Fulei__get_money()







