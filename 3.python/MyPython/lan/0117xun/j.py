import os
import sys

"""
重复点名
"""
def main():
    data = sys.stdin.read().splitlines()
    ptr = 0

    n = int(data[ptr]) # 人数
    ptr += 1

    # name = [] 此处不用列表 用字典
    name_set = set()
    for _ in range(n):
        name = data[ptr].strip() # 姓名
        name_set.add(name)
        ptr += 1


    m = int(data[ptr]) # 读取点名次数
    ptr += 1

    # 用字典记录已点过的名字
    seen = dict()

    # 处理每次点名
    for _ in range(m):
        target = data[ptr].strip()
        ptr += 1

        if target not in name_set:
            print("WRONG")
        else:
            if target not in seen:
                seen[target] = True
                print("OK")
            else:
                print("REPEAT")

if __name__ == "__main__":
    main()



"""      
visited = [False] * n
for i in range(m):
    if target[i] in name and not visited:
        print("OK")
    elif target[i] not in name:
        print("WRONG")
    elif visited[i]:
        print("REPEAT")
"""