import sys
import heapq

# 小头堆
min_heap = []

data = sys.stdin.read().splitlines()  # 全部数据
n = int(data[0])  # 第一行 n 次数
for d in range(1, n+1):  # n行  这个循环条件固定1,n+1
    part = data[d].split()  # 分割 此处忘记写i
    op = int(part[0])  # 第一个整数op

    if op == 1:
        # 添加
        x = int(part[1])
        heapq.heappush(min_heap, x)
    elif op == 2:
        # 输出堆头
        if min_heap:
            print(min_heap[0])
    elif op == 3:
        # 删除堆头
        if min_heap:
            heapq.heappop(min_heap)

