"""
士兵开枪
    需求：
    1）.士兵瑞恩有一把AK47
    2）.士兵可以开火(士兵开火扣动的是扳机)
	士兵也可以装填子弹
    3）.枪 能够 发射子弹(把子弹发射出去)
    4）.枪 能够 装填子弹 --增加子弹的数量

5.github新建一个仓库，练习克隆，提交，创建分支，切换分支等
"""
"""
类：士兵，枪
士兵类
    属性
        name
        枪名
    方法
        开枪
        装填子弹    增加子弹的数量  int
        
枪类
    属性
        名字
        枪内子弹数
    方法
        发射子弹    减少子弹的数量  int
        装填子弹    增加子弹的数量  int
        
"""
class People:
    def __init__(self,name,gun):
        self.name = name
        self.gun = gun

    def shoot(self):   # shoot  开枪
        print(f"{self.name}开枪！")
        self.gun.shoot()

    def backfill(self, bullets):
        print(f"{self.name}正在装填子弹")
        self.gun.backfill(bullets)

class Gun:     # gun  枪
    def __init__(self,name):
        self.name = name
        self.bullet_count = 0   # bullet  子弹

    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            print(f"{self.name}剩余子弹：{self.bullet_count}颗")
        else:
            print(f"{self.name} 没有子弹了，请装填子弹！")

    def backfill(self,bullets):    # backfill 装填
        self.bullet_count += bullets
        print(f"装填子弹后，{self.name}现在有 {self.bullet_count} 颗子弹")


# 创建枪和士兵的实例
ak47 = Gun("AK47")
ryan = People("瑞恩", ak47)

# 模拟士兵开火和装填子弹的行为
ryan.backfill(30)   # 装填
ryan.shoot()        # 开枪
ryan.shoot()
ryan.backfill(15)
ryan.shoot()

