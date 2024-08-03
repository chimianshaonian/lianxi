"""
类属性：
    1、就是类对象所拥有的属性，它被该类所有实例对象所共有
    2、可使用类对象和实例对象访问
    3、只能通过类对象修改，不能通过实例对象修改
"""
class Dog:
    # 设置类属性
    tooth = 10

    # 实例属性
    def __init__(self,name):
        self.name = name

# 调用
if __name__ == '__main__':
    dahuang = Dog('大黄')
    xiaohei = Dog('小黑')
    # 调用类属性：类属性可以被类和实例对象直接调用
    print(xiaohei.tooth)   # 10
    print(Dog.tooth)       # 10
    # 调用实例属性：类属性无法直接调用实例属性，实例对象可以调用自身的实例属性
    # print(Dog.name)     # 报错，因为类没有name属性
    print(xiaohei.name)
    print(dahuang.name)
    # 小黑去打架，咬掉2颗牙齿：实例对象不能直接修改类属性
    # 下发一行代码，只是新增了一个自己对象的实例属性
    xiaohei.tooth = 8     # 只修改了小黑的实例属性
    print(xiaohei.tooth)    # 8
    print(dahuang.tooth)    # 10
    print(Dog.tooth)        # 10
    # 全世界狗狗进化了，变成了12颗牙齿：类属性可以直接修改类属性
    Dog.tooth = 12
    print(Dog.tooth)   # 狗类是12
    print(xiaohei.tooth)   # 小黑会先去找自身的属性，有tooth = 8
    print(dahuang.tooth)


    # 查看各自身上有哪些属性，用__dict__
    print(Dog.__dict__)
    print(dahuang.__dict__)    # 大黄
    print(xiaohei.__dict__)    # 小黑  8
