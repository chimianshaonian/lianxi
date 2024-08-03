# author:yang
list1 = [{"name": "Tom", "age": 18, "sex": "男"}, {"name": "Jack", "age": 20, "sex": "男"}]


# 新增用户函数
def user_add(name):
    # 遍历现有的所有同学的数据库,判断该用户是否已经存在,如果已经存在则给出提示,并退出循环
    for i in list1:
        if i["name"] == name:
            print("该用户已经存在")
            break
    # 如果不存在,则新增信息
    else:
        age = int(input("请输入您的年龄:"))
        sex = input("请输入您的性别:")
        msg = {"name": name, "age": age, "sex": sex}
        list1.append(msg)
        print(f"新增用户成功:{msg}")


# 查询用户信息
def print_user(name):
    # 遍历数据库,判断用户是否已经存在:如果已经存在则打印他的消息,并退出循环
    for i in list1:
        if i["name"] == name:
            print(f"您要查找的用户信息:{i}")
            break
    # 如果不存在,则给出提示
    else:
        print("您要查找的用户不存在")


# 查找全部用户
def print_info():
    for i in list1:
        print(i)


# 删除某个学生信息
def del_user(name):
    # 遍历数据库,判断用户是否存在,如果已经存在则删除该用户,并退出循环
    for i in list1:
        if i["name"] == name:
            list1.remove(i)
            print(f"用户已删除:{i}")
            break
    # 否则提示用户不存在
    else:
        print("您要删除的用户不存在")


# 入口函数
def main():
    while True:
        # 提示信息
        print('===================================')
        print('1-新增用户')
        print('2-查询用户')
        print('3-删除用户')
        print("4-查看所有用户")
        print("5-退出系统")
        print('===================================')

        n = input("请选择:")
        if n == "1":
            name = input("请输入您要添加的用户姓名:")
            user_add(name)
        elif n == "2":
            name = input("请输入您要查询的用户姓名:")
            print_user(name)
        elif n == "3":
            name = input("请输入您要删除的用户姓名:")
            del_user(name)
        elif n == "4":
            print_info()
            pass
        elif n == "5":
            print("退出系统")
            break
        else:
            print("输入非法")


main()
