import sys
from collections import deque

import os
import sys
from collections import deque

"""
输入多个n m
输入文件有多组信息
while循环套在整个外面
"""
data = sys.stdin.read().splitlines()
ptr = 0

while True:
    if ptr >= len(data):
        break

    first = data[ptr].split()
    ptr += 1
    n = int(first[0])
    m = int(first[1])
    if n == 0 and m == 0:
        break  # 题目给出的结束条件

    grid = []
    for _ in range(n):
        part = data[ptr]  # 字符串用strip
        ptr += 1
        grid.append(part)

    # 读取起点终点
    last = data[ptr].split()
    ptr += 1
    x1, y1, x2, y2 = int(last[0]), int(last[1]), int(last[2]), int(last[3])


    # 初始化距离数组
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((x1, y1))
    dist[x1][y1] = 0  # 起点距离0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        a, b = q.popleft()
        if a == x2 and b == y2:
            break
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and dist[x][y] == -1:
                if grid[a][b] == grid[x][y]:
                    # 同类型格子，费用0，放队首
                    dist[x][y] = dist[a][b]
                    q.appendleft((x, y))
                else:
                    # 不同类型格子，费用1，放队尾
                    dist[x][y] = dist[a][b] + 1
                    q.append((x, y))

    print(dist[x2][y2])