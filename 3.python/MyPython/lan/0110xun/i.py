import heapq
import os
import sys


def dijkstra(n, start, graph):
    INF = float('inf')
    dist = [INF] * (n + 1)  # 节点1~n，所以列表长度n+1，索引0不用
    dist[start] = 0  # 起点距离为0

    heap = []  # 堆
    heapq.heappush(heap, (0, start))  # 起点入堆

    visited = set()  # 标记 集合
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)  # 入堆
        if cur_node in visited:
            continue
        visited.add(cur_node)
        if cur_node not in graph:  # 没有邻接边
            continue
        for neighbor, weight in graph[cur_node]:
            if dist[neighbor] > cur_dist + weight:  # 替换
                dist[neighbor] = cur_dist + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))  # 新距离入堆
    return dist[1:n + 1]


data = sys.stdin.read().split()
n = int(data.pop(0))
m = int(data.pop(0))
s = int(data.pop(0))

graph = {}
for _ in range(m):
    u = int(data.pop(0))
    v = int(data.pop(0))
    w = int(data.pop(0))
    if u not in graph:
        graph[u] = []
    # 添加有向边u→v，权值w
    graph[u].append((v, w))

print(' '.join(map(str, dijkstra(n, s, graph))))
