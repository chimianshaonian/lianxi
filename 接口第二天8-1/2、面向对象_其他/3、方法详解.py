"""
1、类方法特点
    需要用装饰圈 @classmothod  赖标识其为类方法
    对于类方法：第一个参数必须是类对象，一般以cls为第一个参数
2、类方法使用场景
    当方法中需要使用类对象（如访问私有类属性等）时，定义类方法
    类方法一般和类属性配合使用

3、静态方法：
    1、需通过装饰圈@staticmethod 来进行装饰，静态方法既不需要传递对象，
    也不需要传递实例对象（没有 self、cls）
    2、也可通过实例对象和类对象方法
    3、静态方法也可传递参数
"""
class Dog:
    # 设置类属性
    tooth = 10

    # 实例属性
    def __init__(self,name):
        self.name = name

    # 实例方法
    def get_name(self):
        print(f'名字是：{self.name}')

    # 定义一个类方法 需用@classmethod 来标识
    @classmethod
    def get_tooth(cls):
        print(f'狗粮有{cls.tooth}颗牙齿')

    # 定义一个静态方法，需用@staticmethod 来标识
    @staticmethod
    def print_info():
        print('这是一个创建狗的类')

    # 静态方法也可以传递参数
    @staticmethod
    def add_fun(x,y):
        print(x + y)

# 调用
if __name__ == '__main__':
    dahuang = Dog('大黄')
    xiaohei = Dog('小黑')
    # 调用实例方法
    # 实例对象可以直接调用实例方法，会自动触发传参，把调用的对象当做第一个参数传给self
    # 类调用实例方法，不会自动传参，需要手动传递一个实例对象给self
    dahuang.get_name()   # 大黄
    Dog.get_name(xiaohei)   # 小黑，需要手动传递一个对象给self
    # 调用类方法：一般搭配类属性使用
    # 类和实例对象都可以直接调用类方法，会自动触发传参，把自己所属的类当成第一个参数传传递进去
    Dog.get_tooth()  # 10  狗类有10颗牙齿
    xiaohei.get_tooth()   # gei_tooth  是类方法、狗类有10颗牙齿
    xiaohei.tooth = 8  # 对小黑新增属性，之前狗类是10，小黑改成了8
    xiaohei.get_tooth()   # 10,因为调用了类方法，也就是狗类有多少个牙齿
    dahuang.get_name()    # 10
    # 调用静态方法，不会再出发字典传参了
    dahuang.print_info()   # 这是一个创建狗的类
    xiaohei.print_info()
    Dog.print_info()       # 这是一个创建狗的类
    # 给静态方法传参
    Dog.add_fun(4,5)      # 9
    dahuang.add_fun(3,3)  # 6




