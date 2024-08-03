"""
面向对象三大特性：
1、封装
    <1>将属性和方法书写到类的里面的操作即为封装
    <2>封装可以为属性和方法添加私有属性
2、继承
    <1>子类默认继承父类的所有属性和方法
    <2>子类可以重写父类属性和方法
3、多态
    <1>传入不同的对象，产生不同的结果
    操作步骤：
        定义父类，并提供公共方法
        定义子类，继承父类，并重新父类方法
        传递子类对象给调用，可以看到不同子类执行的效果不同，
"""
# 定义一个父类，并定义公共方法
class Dog:
    def work(self):
        print('指哪咬哪')

# 定义子类，继承父类，并重新父类提供的公共方法
class Dog1(Dog):
    def work(self):
        print('最近敌人')

class Dog2(Dog):
    def work(self):
        print('追击毒品')

class Dog3:      # 这是个类似多态，与多态效果一致，但不是多态，提示机器狗，其他是真狗
    def work(self):
        print('下期')
class Human:
    def work_with_dog(self,dog):
        dog.work()

# 调用
if __name__ == '__main__':
    d1 = Dog()    # 指哪咬哪
    d2 = Dog1()   # 追击敌人
    d3 = Dog2()   # 追击毒品
    d4 = Dog3()   # 下棋

    h1 = Human()
    h1.work_with_dog(d3)




