# 导入sys模块，方便一次性读取输入
import sys

data = sys.stdin.read().split()
n = int(data.pop(0))  # 取第一个数
m = int(data.pop(0))  # 取第二个数

# 初始化距离矩阵
INF = float('inf')  # 无穷大
dist = []
for i in range(n):
    row = [INF] * n
    dist.append(row)
for i in range(n):
    dist[i][i] = 0  # 对角线不要

# 读入数据 边
for _ in range(m):
    u = int(data.pop(0))  # 起点
    v = int(data.pop(0))  # 终点
    w = int(data.pop(0))  # 权值
    u_idx = u - 1  # 索引差
    v_idx = v - 1

    # 如果当前边的权值更小，就更新矩阵
    if w < dist[u_idx][v_idx]:
        dist[u_idx][v_idx] = w
    if w < dist[v_idx][u_idx]:
        dist[v_idx][u_idx] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            # 如果i→k和k→j都有路径，且总长度比i→j短，就更新
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(n):
    output_row = []  # 结果
    for j in range(n):
        if dist[i][j] == INF:
            output_row.append('0')
        else:
            output_row.append(str(dist[i][j]))
    print(' '.join(output_row))