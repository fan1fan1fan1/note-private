import os
import sys
import heapq

"""
两个 长度n
单调不减序列  A B

从A B 中各取出一个数
相加 得到 N^2和 
求最小的n个
"""
data = sys.stdin.read().splitlines()  # splitlines()
n = int(data[0])
A = list(map(int, data[1].split()))
B = list(map(int, data[2].split()))
min_heap = []
# 超内存visited = [[False for _ in range(n)] for _ in range(n)]  # 标记数组由 A B数据构成 都为n个
visited = set() # 集合

# 单调不减 取前最小
# 依旧先放入候选 也就是第一个数 0位置和
heapq.heappush(min_heap, (A[0] + B[0], 0, 0))  # 如果堆后数据多个 括号

# visited[0][0] = True  # 标记
visited.add((0,0))

result = []
# 一共有N方个 取N个
for _ in range(n):
    current_result, i, j = heapq.heappop(min_heap)
    result.append(str(current_result))  # 堆顶加入结果列表要转字符串str()

    # 要判断下一个位置
    if i + 1 < n and (i+1,j)not in visited: #visited[i + 1][j]:
        # 不越界 未访问
        heapq.heappush(min_heap, (A[i + 1] + B[j], i + 1, j))
        visited.add((i+1,j)) #visited[i + 1][j] = True
    if j + 1 < n and (i,j+1)not in visited: #visited[i][j+1]:
        # 不越界 未访问
        heapq.heappush(min_heap, (A[i] + B[j + 1], i, j + 1))
        visited.add((i,j+1))#visited[i][j + 1] = True

print(' '.join(result))
