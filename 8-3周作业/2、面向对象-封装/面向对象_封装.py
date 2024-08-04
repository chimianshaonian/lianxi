"""
以下内容包含：
1、创建一个类
2、在类外添加和获取属性
3、魔法方法init()，（）内可以带参数、不带参数两种情况
4、其他魔法方法：str、del

"""

# 导模块
import time
# 语法：class 类名
# 定义一个类
class Washer:   # 符合标识符命名规则，且遵循大驼峰命名习惯
    # 类内部定义实例属性

    # 魔法方法1：init(),可带参数，也可不带参数
    # # init---不带参数
    # def __init__(self):
    #     print('开始')
    #     self.width = 600  # 宽
    #     self.height = 800 # 高
    # init--带参数
    def __init__(self,w,h):
        self.width = w
        self.height = h


    # 实例方法
    def wash(self):
        print('洗干净了')
        print(f'我是self：{id(self)}')
        print(f'我将{id(self)}家衣服洗干净')

    # 在类外或内定义实例属性，在类内部调用实例属性
    def info_print(self):
        print(f'宽是{self.width}')
        print(f'高是{self.height}')

    # 魔法方法2：str
    def __str__(self):
        #  返回的必现是字符串
        return f'我是洗衣机，宽度是{self.width},高度是{self.height}'

    # 魔法方法3：del
    def __del__(self):
        print('释放资源触发的代码，比如关闭了文件或数据库链接')


# 实例化一个对象

# init--不带参数
# haier1 = Washer()  # 需要带（），否则是重新起名
# init--带参数
haier1 = Washer(300,400)

"""
1、类外部定义实例属性

# 在类外面添加实例属性
haier1.height = 500 # 高
haier1.width = 800  # 宽
# 在类外调用实例属性
print(f'类外，宽度是{haier1.width}')
print(f'类外，高度是{haier1.height}')
"""

# 调用实例方法
haier1.wash()
# 类外实例属性，类内部调用实例属性，类外调用该方法
haier1.info_print()

# 如不手动执行del,在最后也会执行del的代码
# 如不操作del,那设置等待时间是一整天，那此期间别人是无法操作的
del haier1
time.sleep(5)   # 需用到time包，sleep()  等待5s
print('完成')
