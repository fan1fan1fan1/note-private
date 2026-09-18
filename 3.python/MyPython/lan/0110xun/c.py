import sys

lines = sys.stdin.read().splitlines()  # 全部读入
n = int(lines[0])

# 两个列表 分别存储读入的l、r
left = [0] * (n + 1)
right = [0] * (n + 1)
for i in range(1, n + 1):  # 此处循环条件必须写1，n+1
    l, r = map(int, lines[i].split())
    node = i + 1  # 节点编号从1开始 不用写if node==0的判断了
    left[i] = l
    right[i] = r


# dfs求深度
def depth():
    if n == 0:
        return 0

    stack = [(1, 1)]
    max_depth = 1  # 初始化

    while stack:
        node, cur_depth = stack.pop()
        if cur_depth > max_depth:
            max_depth = cur_depth
        if right[node] != 0:
            stack.append((right[node], cur_depth + 1))
        if left[node] != 0:
            stack.append((left[node], cur_depth + 1))
    return max_depth


print(depth())