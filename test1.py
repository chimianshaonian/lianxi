class BakedSweetPotato:
    def __init__(self):
        self.cooking_time = 0
        self.status = "raw"
        self.seasonings = []

    def cook(self, time):
        """增加烹饪时间，并更新地瓜的状态。"""
        self.cooking_time += time
        if self.cooking_time < 3:
            self.status = "raw"
        elif 3 <= self.cooking_time < 5:
            self.status = "half-cooked"
        elif 5 <= self.cooking_time < 8:
            self.status = "cooked"
        else:
            self.status = "burned"

    def add_seasoning(self, seasoning):
        """添加调料到地瓜上。"""
        self.seasonings.append(seasoning)

    def get_status(self):
        """返回地瓜的当前状态。"""
        return self.status

    def get_seasonings(self):
        """返回已添加的调料列表。"""
        return self.seasonings

# 使用代码
sweet_potato = BakedSweetPotato()
sweet_potato.cook(4)
print(f"Status after 4 minutes: {sweet_potato.get_status()}")
sweet_potato.add_seasoning("salt")
sweet_potato.add_seasoning("butter")
sweet_potato.cook(3)
print(f"Status after additional 3 minutes: {sweet_potato.get_status()}")
print(f"Seasonings added: {', '.join(sweet_potato.get_seasonings())}")
