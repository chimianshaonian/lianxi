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

# ---------------------------------------------------
# 单继承
# # 子类
# class Erzi(Fulei1):  # 单继承父类Fulei1
#     pass
#
# # 调用
# if __name__ == '__main__':
#     # 实例对象
#     xiaoming = Erzi()   # 子类此时身上属性为：五香，继承了父类
#     print(xiaoming.shouyi)
#     xiaoming.zhizuo()

# ----------------------------------------------------
# 多继承
class Erzi(Fulei2,Fulei1):    # 继承的第一个父类为：Fulei2
    pass

# 调用
if __name__ == '__main__':
    xiaoming = Erzi()
    # 当继承多个父类时，默认使用第一个父类的同名属性和方法
    print(xiaoming.shouyi)    # xiaoming此时属性为：香辣
    xiaoming.zhizuo()    # 香辣制作


