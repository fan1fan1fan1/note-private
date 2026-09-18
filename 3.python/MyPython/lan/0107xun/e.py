n,m = map(int,input().split()) # 总人数 target
num = n

people = list(range(1, n + 1))  # 人员编号列表
index = 0  # 报数
result = []

while num != 0:
    # 计算要出列的人的索引：(当前索引 + m-1) % 剩余人数
    index = (index + m - 1) % num

    out = people.pop(index) # 删除这个人
    result.append(str(out))
    num -= 1  # 剩余人数减1
print(' '.join(result))