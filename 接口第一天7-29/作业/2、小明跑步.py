"""
小明爱跑步，爱吃东西。
    1）小明体重75.0公斤
    2）每次跑步会减肥0.5公斤
    3）每次吃东西体重会增加1公斤
    4）小美的体重是45.0公斤
"""
"""
定义类：人
    属性
        名字
        体重
    方法
        跑步  减重 
        吃东西 增加体重 
"""

class People():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight


    def run(self):
        self.weight -= 0.5  # 跑步后体重减少0.5公斤
        print(f"{self.name} 跑步后体重：{self.weight} 公斤")

    def eat(self):
        self.weight += 1  # 吃东西后体重增加1公斤
        print(f"{self.name} 吃东西后体重：{self.weight} 公斤")

    def __str__(self):
        if self.name == '小美':
            return f'{self.name}的体重为{self.weight}'


# 实例化
xiaoming = People("小明", 75.0)
xiaomei = People("小美", 45.0)

xiaoming.run()  # 小明跑步
xiaoming.eat()  # 小明吃东西



