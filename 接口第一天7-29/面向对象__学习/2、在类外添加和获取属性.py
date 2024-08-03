"""
对象属性，即可在类外面添加和获取，也能在里面添加和获取
"""

class Washer:
    def wash(self):
        print(f'我的id是{id(self)}')
        print(f'我将{id(self)}家的衣服洗干净了')

    # 2、在类内部调用实例属性
    def fun(self):
        print(f"宽度是：{self.width}")
        print(f'高度是：{self.height}')
        self.wash()

# 先实例化对象
haier1 = Washer()

# 1、类外面添加对象属性
# 语法：对象名.属性名 = 值
haier1.width = 100
haier1.height = 200

# # 1-1、类外面获取对象属性
# print(f'宽是{haier1.width}')
# print(f"高湿{haier1.heigh}")

# 3 调用
haier1.fun()





