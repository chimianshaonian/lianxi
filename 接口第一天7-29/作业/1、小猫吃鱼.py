# 小猫吃鱼，小猫喝水  分析要定义的类，属性，方法
"""
需要定义的类：小猫
属性
    名字
方法
    吃鱼
    喝水
"""
class Cat:
    def __init__(self, name):
        self.name = name

    def eat_fish(self):
        print(f'{self.name}吃鱼',end=' ')
        self.drink_water()
    def drink_water(self):
        print(f"{self.name}喝水")

# 创建一个猫的实例
cat = Cat("小猫")

# 调用
cat.eat_fish()    # 输出：小猫吃鱼 小猫喝水



