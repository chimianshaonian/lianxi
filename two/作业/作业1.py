# 需求：有三个办公室，8位老师，8位老师随机分配到3个办公室
import random
classroom = [[], [], []]
for i in range(1, 9):      # 把8个老师相当于是生成8个数字，用range（1,9）
    classroom[random.randint(0, 2)].append(i)
print(classroom)







