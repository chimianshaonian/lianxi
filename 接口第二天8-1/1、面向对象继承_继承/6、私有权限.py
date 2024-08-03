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








