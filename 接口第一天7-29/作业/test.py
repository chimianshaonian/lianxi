class People:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def shoot(self):  # shoot  开枪
        self.shoot()


class Gun:  # gun  枪
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def shoot(self):
        # self.backfill()
        while self.number != 0:
            print(f'第{self.number}砰砰砰')
            self.number -= 1
        else:
            print('没子弹了')
            #self.backfill()


    def backfill(self):  # backfill 装填
        self.number += 1
        self.shoot()
        print('又开了一枪')
# 实例枪
gun = Gun('AK47',50)
gun.shoot()
