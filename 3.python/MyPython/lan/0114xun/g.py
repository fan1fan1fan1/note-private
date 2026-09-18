import os
import sys

"""
1
2
3
4
"""
data = sys.stdin.read().splitlines()
q = int(data[0])
student = {}
for i in range(1, q + 1):
    part = data[i].split()
    op = int(part[0])
    #NAME = part[1] 此处不能写 会占掉op==4的输出

    if op == 1:
        # 插入修改
        NAME = part[1]
        SCORE = part[2]
        if NAME in student:
            NAME = part[1]
            student[NAME] = SCORE
            print("OK")
        else:
            student[NAME] = SCORE
            print("OK")


    elif op == 2:
        # 查询
        NAME = part[1]
        if NAME not in student:
            print("Not found")
        else:
            print(student[NAME])

    elif op == 3:
        # 删除
        NAME = part[1]
        if NAME not in student:
            print("Not found")
        else:
            del student[NAME]
            print("Deleted successfully")


    elif op == 4:
        # 输出
        print(len(student))