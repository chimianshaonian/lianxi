# author:yang
list1 = [{"name": "Tom", "age": 18, "sex": "男"}, {"name": "Jack", "age": 20, "sex": "男"}]


# 新增用户函数
def user_add(name):
    # 遍历列表判断用户是否已经存在,如果已经存在则提示,并退出循环
    for user in list1:
        if name == user['name']:
            print('学生已存在')
            return
    # 如果不存在则新增信息
    age = int(input("请输入年龄:"))
    sex = input("请输入性别:")
    list1.append({'name': name, 'age': age, 'sex': sex})
    print("学生添加成功！")


# 查询用户信息函数
def print_user(name):
    # 遍历取指定学生信息,取得到则打印并退出循环
    for user in list1:
        if name == user['name']:
            print(user)
            return
    # 找不到则给出友好提示
    print('学生不存在')


# 删除某个学生信息
def del_user(name):
    # 遍历判断学生是否存在,如果存在则删除并退出循环
    for i in list1:
        if name == i['name']:
            # 方法一：根据元素删除列表中学生相关信息
            # list1.remove(i)
            # 方法二：根据该学生的字典，所在列表的下标进行删除
            m = list1.index(i)
            del list1[m]
            return
    # 不存在则给出友好提示
    print('学生不存在')


# 查询所有用户信息
def print_info():
    for stu_all in list1:
        print(stu_all)


# 入口函数
def run():
    # 循环首页让用户进行选择对应的操作:
    while True:
        # 提示信息
        print('===================================')
        print('1-新增用户')
        print('2-查询用户')
        print('3-删除用户')
        print("4-查看所有用户")
        print("5-退出系统")
        print('===================================')
        # 让用户选择
        n = input("请选择:")
        # n如果是1调用新增学生接口
        if n == "1":
            name = input("请输入姓名:")

            user_add(name)
        # n如果是2调用查询学生接口
        elif n == "2":
            name = input("请输入姓名:")
            print_user(name)
        # n如果是3调用删除学生接口
        elif n == "3":
            name = input("请输入姓名:")
            del_user(name)
        # n如果是4调用查询所有学生接口
        elif n == "4":
            print_info()
        # n如果是5退出系统
        elif n == "5":
            print("退出系统")
            break
        else:
            print("输入非法")


run()
print(list1)
