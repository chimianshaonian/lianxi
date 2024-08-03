# 父类

class Fulei:
    def __init__(self):
        self.shouyi = ['五香']

    def  zhizuo(self):
        print(f'{self.shouyi}制作')

# 子类
class Erzi(Fulei):   # 单继承父类
    pass

# 调式
if __name__ == '__main__':
    # 实例对象
    xiaoming = Erzi()     # xiaoming 此时身上的属性为：五香，继承了父类
    print(xiaoming.shouyi)
    xiaoming.zhizuo()


