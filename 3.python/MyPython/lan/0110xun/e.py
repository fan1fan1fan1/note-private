import os
import sys
from collections import deque

"""
距离: u到v 最短路径上 到根节点(向上指) 的两倍 + 到叶子的(向下指)
从8到6 向上指 3*2=6 向下指 2  6+2=8

求任意x y的距离
"""
data = sys.stdin.read().split()
n = int(data[0])
edge = data[1:1 + 2 * (n - 1)]  # uv间有边 从1(第二个)开始 每次取两个 直到n-1行
x, y = map(int, data[1 + 2 * (n - 1):])

left = [0] * (n + 1)
right = [0] * (n + 1)
parent = [0] * (n + 1)

# u是v的父节点
for i in range(0, len(edge), 2):  # n-1条边 每次取2个
    u = int(edge[i])  # 取两个邻边 i取步长2 i+1 保证所有边都取到
    v = int(edge[i + 1])

    parent[v] = u  # u是v的父节点
    if left[u] == 0:
        left[u] = v
    else:
        right[u] = v


# 求深度
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


# 求宽度  bfs 模拟队列
def width():
    q = deque([1])
    max_width = 0  # 初始化
    while q:
        level_size = len(q)  # 从第一层开始 第一层 根->1
        max_width = max(max_width, level_size)
        for _ in range(level_size):
            node = q.popleft()  # 出队 相当于这一层判断完了 找左右孩子
            if left[node] != 0:  # 有左孩子 进队
                q.append(left[node])
            if right[node] != 0:  # 有右孩子 进队
                q.append(right[node])
            # 这一层的所有节点都进队了 判断下一层 下一层会放在q的下一个位置里
        # q中每个位置存放了 同一层的个数 给level求数量

    return max_width


# 求距离
def get_distance(x, y):
    def get_path(node, lca):
        path = []
        while node != lca:
            path.append(node)
            node = parent[node]
        return path

    def find_lca(a, b):
        ancestors = set()
        while a != 0:
            ancestors.add(a)
            a = parent[a]
        while b not in ancestors:
            b = parent[b]
        return b

    lca = find_lca(x, y)

    root1 = len(get_path(x, lca))
    leaf1 = len(get_path(y, lca))

    return root1 * 2 + leaf1


print(depth())
print(width())
print(get_distance(x, y))