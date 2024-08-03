"""
开发一个注册系统，
[{name:xxx,age:xxx},{name:xxx,age:xxx},{name:xxx,age:xxx}]
----------------
*   1-新增用户
*   2-查询单个用户信息
*   3-查询全部用户信息
*   4-删除用户
    5-退出系统
----------------
功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
功能2：查询学生信息
功能3：删除学生信息
"""

student = [{'name': 'A', 'age': 11}, {'name': 'B', 'age': 12}, {'name': 'C', 'age': 13}]


# 1、新增学生
def stu_add():
    name = input("请输入学生姓名:")
    # 遍历列表判断用户是否已经存在,如果已经存在则提示,并退出循环
    for user in student:
        if name == user['name']:
            print('学生已存在')
            return
    # 如果不存在则新增信息
    age = int(input("请输入年龄:"))
    student.append({'name': name, 'age': age})
    print("学生添加成功！")


# 2、查询单个学生
def stu_find_one():
    name = input("请输入学生姓名:")
    # 遍历取指定学生信息,取得到则打印并退出循环
    for user in student:
        if name == user['name']:
            print(user)
            return
    # 找不到则给出友好提示
    print('学生不存在')


# 3、查询所有学生
def stu_find_all():
    for stu_all in student:
        print(stu_all)


# 4：删除学生
def stu_del():
    name = input("请输入学生姓名:")
    # 遍历判断学生是否存在,如果存在则删除并退出循环
    for i in student:
        if name == i['name']:
            # 方法一：根据元素删除列表中学生相关信息
            # student.remove(i)
            # 方法二：根据该学生的字典，所在列表的下标进行删除
            m = student.index(i)
            del student[m]
            return
    # 不存在则给出友好提示
    print('学生不存在')


# 开始执行
def start():
    # 循环首页让用户进行选择对应的操作:
    while True:
        # 提示信息
        print('===================================')
        print('1-新增学生')
        print('2-查询单个学生')
        print('3-查询所有学生')
        print("4-删除学生")
        print("5-退出系统")
        print('===================================')
        # 用户选择
        n = input("请选择:")
        # 新增学生
        if n == "1":
            stu_add()
        # 查询单个学生
        elif n == "2":
            stu_find_one()
        # 查询所有学生
        elif n == "3":
            stu_find_all()
        # 删除学生
        elif n == "4":
            stu_del()
        # 退出系统
        elif n == "5":
            print("退出系统")
            break
        else:
            print("输入非法，请重新输入！")


start()
print(student)
