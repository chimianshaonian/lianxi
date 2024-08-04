# 父类
class Fulei:
    def __init__(self):
        self.shouyi = ['五香']
        # 私有属性
        # 在属性名前添加两个__,变为私有属性，此时子类无法调用
        self.__money = 200  # 私有的

    def zhizuo(self):
        print(f'{self.shouyi}制作')

    # 私有方法，也是在方法名前加上两个__
    def __get_money(self):
        print(self.__money)

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
    xiaoming = Fulei()
    print(xiaoming.shouyi)
    xiaoming.zhizuo()   #五香制作

    # print(xiaoming.__money)    # 报错，无法直接调用父类的私有属性
    # xiaoming.__get_money()       # 报错，无法直接调用父类的私有方法
    xiaoming.print_money()     # 200
    xiaoming.set_money(100)
    xiaoming.print_money()     # 300
    xiaoming.set_money(-100)
    xiaoming.print_money()

# 查看类的属性和方法，用dict
print(Fulei.__dict__)       # 类的属性和方法
print(xiaoming.__dict__)   # 只能看到类的方法
print(xiaoming._Fulei__money)
xiaoming._Fulei__get_money()