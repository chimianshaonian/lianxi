"""
摆放家具
    需求：
    1）.房子有户型，总面积和家具名称列表
       新房子没有任何的家具
    2）.家具有名字和占地面积，其中
       床：占4平米
       衣柜：占2平面
       餐桌：占1.5平米
    3）.将以上三件家具添加到房子中
    4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

"""
"""
# 需要定义的类: 房子类,家具类
家具类:
    属性:
        名字      外界给予     str
        占地面积   外界给予     int
    方法:
        str
房子类:
    属性:
        户型      外界给予       字符串
        总面积     外界给予       int
        剩余面积    默认就是总面积   int
        家具列表    默认:[]      list  
    方法:
        摆放家具(参数): 参数: 家具类实例化出来对象
            房子剩余面积是否大于家具面积:
                是: 摆放家具
                    家具列表.append(家具的名字)
                    剩余面积-=家具面积
                否:
                    提示退货
        str
"""


# # 需要定义的类: 房子类,家具类
# 家具类:
class Jiaju:
    # 属性:
    def __init__(self, name, area):
        self.name = name
        self.area = area  # area 面积

    # 方法:
    def __str__(self):
        return f"名称:{self.name},面积:{self.area}"


class House:
    def __init__(self, model, total_area):
        self.model = model  # model 型
        self.total_area = total_area  # total_area  总面积
        self.remaining_area = total_area  # remaining_area 剩余面积
        self.furniture_list = []  # furniture_list  家具列表

    def put_furniture(self, jiaju):
        if self.remaining_area >= jiaju.area:
            self.furniture_list.append(jiaju.name)
            self.remaining_area -= jiaju.area
        else:
            print(f"没有足够的空间放置 {jiaju.name}")

    def __str__(self):
        return f"户型：{self.model}\n总面积：{self.total_area} 平米\n" \
               f"剩余面积：{self.remaining_area} 平米\n" \
               f"家具：{', '.join(self.furniture_list)}"


# 创建家具实例
bed = Jiaju("床", 4)
wardrobe = Jiaju("衣柜", 2)
dining_table = Jiaju("餐桌", 1.5)

# 创建房子实例并添加家具
home = House("三室一厅", 100)
home.put_furniture(bed)
home.put_furniture(wardrobe)
home.put_furniture(dining_table)

print(home)
