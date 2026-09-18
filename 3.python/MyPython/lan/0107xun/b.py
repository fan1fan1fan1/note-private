n, q = map(int, input().split())  # 柜子个数 操作次数
pacts = []

for p in range(q):
    pact = list(map(int, input().split()))  # 一次操作
    # 1    位置i j    物品
    # 2    位置i j
    pacts.append(pact)

# 此数据处理适用于字典
move = {}
for pact in pacts:
    if pact[0] == 1:
        i = pact[1]
        j = pact[2]
        k = pact[3]

        # 此处必须对move初始化
        if i not in move:
            move[i] = {}

        if k == 0:
            # 初始化判断
            if j in move[i]:
                del move[i][j]
        else:
            move[i][j] = k
    else:
        i = pact[1]
        j = pact[2]
        print(move[i][j])