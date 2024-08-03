# if语句
a = int(input(('请输入此次考试成绩：')))

if a >= 60:
    if 60 <= a <80:
        print('及格')
    elif  80 <= a < 90:
        print('良好')
    elif 90 <= a < 100:
        print('优秀')
    else:
        print('真棒')
else:
    print('考试不及格，需要努力了哦')

print('吃不了学习苦，就要是生活的苦')