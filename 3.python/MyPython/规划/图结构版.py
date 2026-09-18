# 图 - 邻接表实现
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # 修正：原代码用self.v，后续函数都调用graph.V，统一为大写V
        self.adj = [[] for i in range(vertices)]  # 邻接表

    # 添加边（无向图）
    def add_edge(self, u, v, weight=1):
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

# 无向图邻接表（字典实现，新手友好）
undir_graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

# 有向图邻接表
dir_graph = {
    0: [1, 2],
    1: [3],
    2: [5],
    3: [4],
    4: [5],
    5: []
}

# 带权图邻接表（存储(邻接点, 权重)）
weighted_graph = {
    0: [(1, 2), (2, 5)],
    1: [(3, 1), (4, 3)],
    2: [(5, 4)],
    3: [(4, 1)],
    4: [(5, 2)],
    5: []
}

# 测试用图初始化
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 5)
g.add_edge(1, 2, 3)
g.add_edge(2, 3, 1)
g.add_edge(3, 4, 4)



from collections import deque
# 1. 深度优先遍历（DFS，递归版）
def graph_dfs(graph, start, visited, res):
    res.append(start)
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            graph_dfs(graph, neighbor, visited, res)

# 2. 广度优先遍历（BFS）
def graph_bfs(graph, start):
    res = []
    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)
    while q:
        cur = q.popleft()
        res.append(cur)
        for neighbor in graph[cur]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return res

# 测试图遍历
dfs_res = []
graph_dfs(undir_graph, 0, set(), dfs_res)
print("图DFS遍历：", dfs_res)  # [0,1,3,4,5,2]（遍历顺序可能因邻接表顺序不同）

bfs_res = graph_bfs(undir_graph, 0)
print("图BFS遍历：", bfs_res)  # [0,1,2,3,4,5]




# 最短路径问题 迪杰斯特拉
import heapq

def dijkstra(graph, start):
    # 初始化距离字典，默认无穷大
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    # 优先队列（存储(距离, 节点)，小顶堆）
    heap = []
    heapq.heappush(heap, (0, start))
    visited = set()

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if cur_node in visited:
            continue
        visited.add(cur_node)
        # 遍历邻接点
        for neighbor, weight in graph[cur_node]:
            if dist[neighbor] > cur_dist + weight:
                dist[neighbor] = cur_dist + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))
    return dist

# 测试Dijkstra
shortest_dist = dijkstra(weighted_graph, 0)
print("单源最短路径（起点0）：", shortest_dist)
# 输出：{0:0, 1:2, 2:5, 3:3, 4:4, 5:6}


# 最短路径 弗洛伊德
def floyd_warshall(graph):
    # 提取所有节点并排序
    nodes = sorted(graph.keys())
    n = len(nodes)
    # 构建节点到索引的映射
    node2idx = {node: i for i, node in enumerate(nodes)}
    # 初始化距离矩阵，无穷大表示不可达
    INF = float('inf')
    dist = [[INF]*n for _ in range(n)]
    # 自身到自身距离为0
    for i in range(n):
        dist[i][i] = 0
    # 填充边的权重
    for u in graph:
        for v, w in graph[u]:
            dist[node2idx[u]][node2idx[v]] = w
    # 动态规划更新距离
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # 转换回节点为键的字典
    res = {}
    for i, u in enumerate(nodes):
        res[u] = {v: dist[i][node2idx[v]] for v in nodes}
    return res

# 测试Floyd-Warshall
floyd_dist = floyd_warshall(weighted_graph)
print("多源最短路径：", floyd_dist)



# 拓扑排序（仅适用于有向无环图DAG）
from collections import deque

def topological_sort(graph):
    # 计算入度
    in_degree = {node: 0 for node in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    # 入度为0的节点入队
    q = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            q.append(node)
    # 拓扑排序结果
    res = []
    while q:
        cur = q.popleft()
        res.append(cur)
        for neighbor in graph[cur]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)
    # 若结果长度不等于节点数，说明有环
    if len(res) != len(graph):
        return "图中有环，无拓扑排序"
    return res

# 测试拓扑排序
topo_res = topological_sort(dir_graph)
print("拓扑排序：", topo_res)  # [0,1,2,3,4,5]（顺序可能不同）


# 最小生成树 克鲁斯卡尔
# 并查集（辅助Kruskal）
class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x


def kruskal(graph):
    # 提取所有边并按权重排序
    edges = []
    for u in graph:
        for v, w in graph[u]:
            edges.append((w, u, v))
    edges.sort()  # 按权重升序
    # 初始化并查集
    nodes = graph.keys()
    uf = UnionFind(nodes)
    mst = []  # 最小生成树的边
    total_weight = 0  # 总权重

    for w, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == len(nodes) - 1:  # 生成树边数=节点数-1
                break
    return mst, total_weight


# 测试Kruskal
mst_edges, total_w = kruskal(weighted_graph)
print("最小生成树边：", mst_edges)
print("最小生成树总权重：", total_w)  # 输出8