import os
import sys
"""
并查集
合并
删除
"""
# 初始化
def init_uf(n):
    # 父节点(代表元素)
    parent = list(range(n+1)) # 题目数据从1开始
    return parent

# 查询 代表元素
def find(parent, x):
    if parent[x] != x: # 这是直接查找箭头指向的上一个位置 如果不是x 持续递归查找
        # 路径压缩：直接让x的父节点指向根节点
        parent[x] = find(parent, parent[x])
    return parent[x]

# 结合 代表元素
def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y: # 确定不是同一个集合
        parent[root_y] = root_x # 把y的根节点挂到x的根节点下


# 判同集合
def is_same_set(parent, x, y):
    return find(parent, x) == find(parent, y)

data = sys.stdin.read().splitlines()
first = data[0].split()
n = int(first[0])
m = int(first[1])

parent = init_uf(n)
output = []

for i in range(1,m+1):
    part = data[i].split()
    z = int(part[0])
    x = int(part[1])
    y = int(part[2])

    if z == 1:
        union(parent,x,y)

    elif z == 2:
        if is_same_set(parent,x,y):
            print("Y")
        else:
            print("N")