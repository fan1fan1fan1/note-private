

# 基础

1. 变量

2. 运算符计算 

   //整除   /除(小数)    **   %   &   |   ^   >>   <<

   and   or   in   not

3. 流程控制

    If else   while   for   switch

4. 字符串

   切片 内置方法(join   strip   split   count   replace   len)

5. 容器

   列表 字典 集合 

6. 输入 input()

   一次性输入sys.stdin,read().split()

7. 输出 print()

   小数点 end=””

8. 内置库

   ### Math   collections

   ```python
   math.gcd(a,b)
   math.lcm(a,b)
   math.isqrt(n)
   math.pow(x,y)
   pow(x,y,mod)
   math.fabs(x)
   math.floor(x)
   math.pi
   math.e

   from collections import defaultdict
   from collections import deque
   ```

9. 计算机知识

   进制转换bin()

   ASCII转换ord() chr()

# 数据结构

### 数组 

列表list

```python
arr=[] 
arr.append()
arr.pop()
print(arr[0])
```



链表可以用字典模拟



### 栈 

列表模拟list 

```python
stack=[]
stack.append()
stack.pop()
print(stack[-1]
```



### 队列 

collections.deque

```python
from collections import deque

stack_deque = deque()
queue = deque([1,2,3])

stack_deque.append(1)
queue.appendleft()

stack_deque.pop()
queue.popleft()

print(stack_deque[-1])
print(queue[0])

for i in queue:
	print(i,end="")

num = len(queue)

queue.clear()
```



### [二叉树 遍历]()

模拟多个数组构建二叉树    

根(父)  左子 右子

```python
import sys
from collections import deque

lines = sys.stdin.read().splitlines()
n = int(lines[0])  
# 初始化left/right/parent数组，节点编号从1开始，0表示无孩子
left = [0] * (n + 1)
right = [0] * (n + 1)
parent = [0] * (n + 1)

# 遍历输入，填充left/right/parent
for i in range(1, n + 1): # 此处循环条件必须写1，n+1
    l, r = map(int, lines[i].split())
    left[i] = l
    right[i] = r
# 记录父节点
if l != 0:
parent[l] = i
if r != 0:
parent[r] = i

# 遍历结果
print("前序遍历：", pre_order(n, left, right))
print("中序遍历：", in_order(n, left, right))
print("后序遍历：", post_order(n, left, right))
print("二叉树节点总数：", count_nodes(n, left, right))
print("二叉树深度：", get_depth(n, left, right))
print("二叉树宽度：", get_width(n, left, right))

# 前序遍历（根→左→右）
def pre_order(n, left, right):
    res = []
    stack = [1]  # 根节点为1
    while stack:
        node = stack.pop()
        if node == 0: # 叶子
            continue
            
        # 非叶子    
        res.append(str(node))
        stack.append(right[node]) # 栈先进后出 反着写
        stack.append(left[node])
    return " ".join(res)

# 中序遍历（左→根→右）
def in_order():
    res = []
    stack=[]
    cur = 1 # 根节点 开始
    
    while cur!= 0 or stack: # 当前节点非空 栈存在
        while cur != 0: # 不是叶子
            stack.append(cur) # 进栈
            cur = left[cur] # 往左访问
        cur = stack.pop() # 访问到最左了 放到答案里
        res.append(str(cur))
        cur = right[cur] # 此时栈里左和中都输出了 访问右
    return ' '.join(res)

# 后序遍历（左→右→根）
def post_order():
    res = []
    stack = [(1,False)] # 根节点入栈 标记false
    
    while stack:
        node,visited = stack.pop() # 栈顶
        if node == 0: # 叶子
            continue
        if visited: # 左右都访问了 标记true 输出
            res.append(str(node))
        else:
            # 非叶子 未访问
            stack.append((node,True))  # 进栈 标记
            stack.append((right[node],False)) # 右
            stack.append((left[node],False))  # 左
    return ' '.join(res)  # join 前面是. 点

# 2.求叶子节点个数
def count_leaves(left, right, max_node):
     count = 0
     for i in range(1, max_node + 1):
         # 叶子节点：左右子节点均为0
         if left[i] == 0 and right[i] == 0:
             count += 1
     return count

# 3. 节点个数统计 
def count_nodes(n, left, right):
    count = 0
    stack = [1]
    while stack:
        node = stack.pop()
        if node == 0:
            continue
        count += 1
        stack.append(right[node])
        stack.append(left[node])
    return count

# 4. 二叉树深度
def depth():
    if n==0:
        return 0
        
    stack = [(1,1)]
    max_depth = 1 # 初始化
    while stack:
        node,cur_depth = stack.pop() # 更改当前深度
        if cur_depth > max_depth: 
            max_depth = cur_depth
        if right[node]!=0:
            stack.append((right[node],cur_depth+1)) # 入右
        if left[node]!=0:
            stack.append((left[node],cur_depth+1))  # 入左
    return max_depth

#  5. 二叉树宽度
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
            # 这一层的所有节点都进队了 判断下一层 
            # 下一层会放在q的下一个位置里
            
        # q中每个位置存放了 同一层的个数 给level求数量
    return max_width
```

```python
# 用字典 键值对 节点 左右孩子 tree = []
tree = {}
root = None  # 根节点

for i in range(n):
    num = input().strip()  # 字符串读入
    node = num[0]

    if len(num) > 1:
        left = num[1]
    else:
        left = '*'
    if len(num) > 2:
        right = num[2]
    else:
        right = '*'

    tree[node] = (left, right)  # 键值对 {node : (left,right)}
    if i == 0:
        root = node
```

```python
def pre(In,post):
    # 递归终止条件
    if not In or not post:
        return ""
    root = post[-1] #根节点 为 后序 最后一个节点
    index = In.index(root) # 在中序找根节点

    # 拆分左右子树 递归 [起点:终点]
    left_in = In[:index] 
    # 对中序 左中右 左子树 起点->index 右子树 index->终点
    right_in = In[index+1:]
    left_post = post[:index] 
    # 对后序 左右中 左子树 起点->index中间的个数 
    # 右子树 终点->index的个数
    right_post = post[index:-1]

    # 先:  根+左子树+右子树
    return root + pre(left_in,left_post) + pre(right_in,right_post)
```



### [图]()*

##### 存储 邻接表 

列表+字典 

```python
import sys

# 列表型
data = list(map(int, sys.stdin.read().split()))
idx = 0
n = data[idx]  # 节点数（1-based）
idx += 1
m = data[idx]  # 边数
idx += 1
graph_type = data[idx]  # 1=有向图，2=无向图
idx += 1

# 初始化列表型邻接表：adj[u] 存储 (v, w)
adj = [[] for _ in range(n + 1)]

# 建表
for _ in range(m):
    u = data[idx]
    idx += 1
    v = data[idx]
    idx += 1
    w = data[idx]  # 边权
    idx += 1
    adj[u].append((v, w))
    if graph_type == 2:  # 无向图双向添加
        adj[v].append((u, w))

# 打印邻接表验证
print("列表型邻接表：")
for u in range(1, n + 1):
print(f"节点{u}: {adj[u]}")
```

```python
# 字典型
import sys

data = sys.stdin.read().split()
idx = 0
n = int(data[idx])  # 节点数
idx += 1
m = int(data[idx])  # 边数
idx += 1
graph_type = int(data[idx])  # 1=有向图，2=无向图
idx += 1

# 初始化字典型邻接表：adj[u] 存储 (v, w)
adj = {}

# 建表
for _ in range(m):
    u = data[idx]  # 节点可为字符串/非连续整数
    idx += 1
    v = data[idx]
    idx += 1
    w = int(data[idx])  # 边权
    idx += 1
    # 若节点不在字典中，初始化空列表
    if u not in adj:
        adj[u] = []
        adj[u].append((v, w))
        if graph_type == 2:  # 无向图双向添加
            if v not in adj:
                adj[v] = []
                adj[v].append((u, w))

# 打印邻接表验证
print("字典型邻接表：")
for u in adj:
print(f"节点{u}: {adj[u]}")
```



##### 遍历 dfs bfs

```python
visited = [False] * (n + 1)
# DFS 递归函数
def dfs(u):
    print(u, end=' ')
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
dfs(v)

            
visited = [False] * (n + 1) # 重置visited
# BFS 函数
def bfs(s):
    que = deque()
    que.append(s)
    visited[s] = True
    while que:
        u = que.popleft()
        print(u, end=' ')
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                que.append(v)
bfs(v)
```



##### 最短路径  

###### 迪杰斯特拉 堆 

python迪杰斯特拉优先使用堆完成

```python
import sys
import heapq

def dijkstra(n, adj, start):
    """
    堆优化版迪杰斯特拉
    :param n: 节点数
    :param adj: 邻接表
    :param start: 起点
    :return: dist 最短距离数组
    """
    INF = float('inf')
    dist = [INF] * (n + 1) # 初始化
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```



###### 弗洛伊德

```python
def floyd_warshall(n, m, data, idx_start):
    """
    Floyd-Warshall多源最短路径（邻接矩阵实现）
    :param n: 节点数
    :param m: 边数
    :param data: 输入数据列表
    :param idx_start: 边数据起始索引
    :return: dist 邻接矩阵
    """
    INF = float('inf')
    # 初始化邻接矩阵
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0
    
    idx = idx_start
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        w = data[idx + 2]
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w  # 无向图，有向图删除此行
        idx += 3
    
    # Floyd核心三层循环
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
```



##### 最小生成树  

###### 克鲁斯卡尔 并查集 

克鲁斯卡尔使用并查集

```python
class UnionFind:
    """并查集类，处理 Kruskal 算法的连通性判断"""
    def __init__(self, size):
        self.parent = list(range(size + 1))  # 1-based 节点
    
    def find(self, x):
        """查找根节点，带路径压缩"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """合并两个集合"""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            return True
        return False
        
  import sys

def kruskal(n, m, data, idx_start):
    """
    Kruskal 最小生成树算法
    :param n: 节点数
    :param m: 边数
    :param data: 输入数据列表
    :param idx_start: 边数据起始索引
    :return: 最小生成树的总权值，若不连通返回 -1
    """
    edges = []
    idx = idx_start # 起点
    # 提取所有边 (w, u, v)
    for _ in range(m): # m边
        u = data[idx] # 起点
        v = data[idx + 1] # 终点
        w = data[idx + 2] # 权值
        edges.append((w, u, v)) # 一条完整的边
        idx += 3
    
    # 按边权升序排序
    edges.sort() # 取权值最小
    uf = UnionFind(n) # 初始化并查集
    total_weight = 0
    edge_count = 0
    
    for w, u, v in edges:
        if uf.union(u, v): # 结合 
            total_weight += w 
            edge_count += 1
            if edge_count == n - 1:
                break  # 生成树已形成
    
    # 检查是否连通
    return total_weight if edge_count == n - 1 else -1      
```



###### 普里姆 堆

普里姆使用堆

```python
import heapq

def prim(n, adj):
    """
    堆优化版 Prim 最小生成树算法
    :param n: 节点数
    :param adj: 邻接表，格式为 adj[u] = [(v, w)]
    :return: 最小生成树的总权值，若不连通返回 -1
    """
    INF = float('inf')
    visited = [False] * (n + 1)
    heap = []
    # 从节点 1 开始（可任选起点）
    heapq.heappush(heap, (0, 1))
    total_weight = 0
    edge_count = 0
    
    while heap:
        w, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += w
        edge_count += 1
        
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(heap, (weight, v))
    
    return total_weight if edge_count == n else -1
```



##### 拓扑排序

```python
import heapq
import deque

def topological_sort(n, adj):
    """
    拓扑排序（处理有向无环图）
    :param n: 节点数
    :param adj: 邻接表
    :return: res 拓扑序列，若有环返回空列表
    """
    deg = [0] * (n + 1)  # 入度数组
    # 统计入度
    for u in range(1, n + 1):
        for v, _ in adj[u]:
            deg[v] += 1
    
    que = deque()
    # 入度为0的节点入队
    for i in range(1, n + 1):
        if deg[i] == 0:
            que.append(i)
    
    res = []
    while que:
        u = que.popleft()
        res.append(u)
        for v, _ in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                que.append(v)
    
    # 存在环，拓扑排序失败
    if len(res) != n:
        return []
    return res
```





### [堆 ]()

优先队列 heapq

堆是一种完全二叉树的有序集合 

分大头和小头 堆顶一定是个最值

```python
import sys
import heapq

def heap():
    input_str = sys.stdin.read()  # 1.读取 
    if not input_str:  # 空
        return
    data = list(map(int, input_str.split()))
    min_heap = []   # 2.初始化

    # 3.添加元素（heappush）
    for num in data:
        heapq.heappush(min_heap, num)  # 自动调整堆结构

    # 4.删除堆顶元素（heappop）
    while min_heap:
        top_num = heapq.heappop(min_heap)  # 弹出并返回堆顶元素，自动重新调整堆

    # 5.堆排序（基于heappush和heappop）
    sort_heap = [] # 重新初始化堆，用于排序
    for num in data:
        heapq.heappush(sort_heap, num) # 先把所有元素加入堆
    
    sorted_result = []
    while sort_heap: # 逐个弹出堆顶，得到升序结果
        sorted_result.append(heapq.heappop(sort_heap))

    # 6.输出堆顶
    heapq.heapify(min_heap)
    heap_top = min_heap[0]
    print(heap_top)
        
    # python的heapq模拟的是小头堆 大头堆用负数表示
    # 7.模拟大顶堆
    max_heap = []
    for num in data:
        heapq.heappush(max_heap, -num)  # 存负数，最小堆就变成“大顶堆”
    
    big_sorted_result = []
    while max_heap:
        neg_num = heapq.heappop(max_heap)
        original_num = -neg_num  # 还原成原来的数字
        big_sorted_result.append(original_num)
```



### [哈希]()表

##### 普通字典dict={}

```python
# 1.基础字典
# 支持操作：insert 键 值 | search 键 | delete 键 | traverse | count
import sys

def dict_hash():
    # 初始化字典 = 哈希表
    hash_table = {}
    hash_table[1] = "a"

    lines = sys.stdin.read().splitlines()
    for line in lines:
        if not line:
            continue
        parts = line.split()
        op = parts[0] # 操作选项

        # 1. 添加插入元素
        if op == "insert":
            key = parts[1]  # 直接用字符串当key
            value = parts[2]
            hash_table[key] = value # 直接空间赋值

        # 2. 查找元素
        elif op == "search":
            key = parts[1] # 键值对
            if key in hash_table:
                print(f"查找成功：{key} = {hash_table[key]}")
            else:
                print(f"查找失败：{key} 不存在")

        # 3. 删除元素
        elif op == "delete":
            key = parts[1]
            if key in hash_table:
                del hash_table[key] # 删除

        # 4. 遍历哈希表
        elif op == "traverse":
            print("哈希表内容：", hash_table) # 直接print

        # 5. 统计元素个数
        elif op == "count":
            len(hash_table)
            print("哈希表元素总数：", len(hash_table))
```



##### collections.defaultdict

```python
# 2.defaultdict
# 支持操作：insert 键 值 | search 键 | delete 键 | traverse | count
import sys
from collections import defaultdict

def hash_defaultdict():
    hash_table = defaultdict(lambda: None)

	lines = sys.stdin.read().splitlines()
    for line in lines:
        if not line:
            continue
        parts = line.split()
        op = parts[0]

        # 1. 添加插入元素
        if op == "insert":
            key = parts[1]
            value = parts[2]
            hash_table[key] = value  # 直接赋值

        # 2. 查找元素
        elif op == "search":
            key = parts[1]
            value = hash_table[key]
            if value is not None:
                print("查找成功")
            else:
                print("查找失败")

        # 3. 删除元素
        elif op == "delete":
            key = parts[1]
            if key in hash_table:
                del hash_table[key]

        # 4. 遍历哈希表
        elif op == "traverse":
            print(dict(hash_table))  # 转成普通字典更易读

        # 5. 统计元素个数
        elif op == "count":
            len(hash_table)

# 拓展：用defaultdict(int)实现字符频次统计（蓝桥杯高频题）
def char_count():
    s = input("请输入一个字符串：") # 大
    count_dict = defaultdict(int)  # 待查找字符
    for char in s:
        count_dict[char] += 1
    for char, cnt in count_dict.items(): # 转成item  defaultdict是键值对 转成键值元组组合
        print(cnt)
 
# 2. 按键排序（按字符的字典序） x表示每个元组 x[0]第一个元组->键
     sorted_by_key = sorted(char_count.items(), key=lambda x: x[0])
# 3. 按值排序（按频次从高到低，蓝桥杯最常考） x表示每个元组 x[1]第二个元组->值
     sorted_by_value = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
```

```python
from collections import defaultdict # (1)导包

de1 = defaultdict(list) # (2)定义
de1["key1"].append(1)   # (3)添加数据
print(de1["key1"])      # (4)查找输出
del de1["key1"]         # (5)删除
for key in de1:         # (6)遍历
    print(key, end=" ")

de2 = defaultdict(int)
de1["apple"] += 1
de1["banana"] += 1
de1["apple"] += 1 # 2个
print(de1["apple"])
del de2["apple"]
for key in de2:
    print(key, end=" ")

de = defaultdict(lambda:None) 
# defaultdict  要求你告诉它：遇到不存在的  key  时，要返回什么默认值。
# 这里的  lambda: None  就是规则：“如果  key  不存在，就返回  None ”。

de3 = defaultdict(int,{"a":1,"b":2})
de3["c"]=3
print(de3["a"])
del de3["a"]
for key in de2:
    print(key, end=" ")
print("\n")

# (7)排序
hash_sort = defaultdict(int, {"b": 5, "a": 3, "d": 1, "c": 4})

# 1. 按键升序排序
sorted_by_key = sorted(hash_sort.items(), key=lambda x: x[0])
print("按键升序：", sorted_by_key)  # 输出：[('a', 3), ('b', 5), ('c', 4), ('d', 1)]
# 2. 按值降序排序
sorted_by_val = sorted(hash_sort.items(), key=lambda x: x[1], reverse=True)
print("按值降序：", sorted_by_val)  # 输出：[('b', 5), ('c', 4), ('a', 3), ('d', 1)]
```



手机

###### # 16.红花共线问题

```python
""" 16.输入描述：输入n对正整数，每一对正整数之间以一个空格隔开，代表放置红色花
    卉的方格位置。每对正整数中的两个数字以英文逗号隔开
    输出描述:输出最多有多少盆红色花卉在同一条直线上

    样例输入：2,1  3,2  5,2  4,3  3,4  6,5  (红花)
    样例输出：4 (最多四个共线)
    
    1,6 2,6 3,6 4,6 5,6 6,6 ... 100,6
    1,5 2,5 3,5 4,5 5,5 6,5                                         6,5
    1,4 2,4 3,4 4,4 5,4 6,4             ->          3,4
    1,3 2,3 3,3 4,3 5,3 6,3                               4,3
    1,2 2,2 3,2 4,2 5,2 6,2                         3,2         5,2
    1,1 2,1 3,1 4,1 5,1 6,1                    2,1
    
    如果水平看 一共最多有两个同一条直线
    竖直看    2个
    主对角线  3个
    副对角线  4个
    
    对角线判断方法: 主对角线x+y相同 副对角线x-y相同 (x,y)->(1,6)
"""

# 输入
list = input().split()
c = []
for i in list:
    a,b=i.split(",")
    a,b = int(a), int(b) # 将list转换成元组放到c里
    c.append((a,b))

hang = {}    # 行字典
lie = {}     # 列字典
zhuDui = {}  # 主对角线 x+y
fuDui = {}   # 副对角线 x-y

for item in c:
    x,y = item[0],item[1]
    # item是一个二维坐标 无论item取c中的哪个坐标 x代表item[0] y代表item[1]
    # item[0][1]=(x,y)

    if x in hang: # 判断横向直线
        hang[x] += 1
    else:
        hang[x] = 1

    if y in lie: # 判断纵向直线
        lie[y] += 1
    else:
        lie[y] = 1

    if x+y in zhuDui: # 判断主对角线
        zhuDui[x+y] += 1
    else:
        zhuDui[x+y] = 1

    if x-y in fuDui: # 判断副对角线
        fuDui[x-y] += 1
    else:
        fuDui[x-y] = 1

print(hang,lie,zhuDui,fuDui)

a = max(hang.values())
b = max(lie.values())
c = max(zhuDui.values())
d = max(fuDui.values())

res = max(a,b,c,d)
print(res)
```



### [查找  ]()

##### 线性查找 简单查找

```python
import sys

def search():
    # 输入格式：数字列表 + 目标值（最后一个数是目标）
    data = list(map(int, sys.stdin.read().split()))
    nums = data[:-1] # 集合 包含所有数据 
    target = data[-1] # 待查找数据

    if target in nums:
        idx = nums.index(target)
	else:
        print("查找失败")

    # 2. 统计目标出现次数
    cnt = nums.count(target)
    print(cnt)
```



##### bisect二分查找

```python
import sys
import bisect

def binary_searchb():
    # 输入格式：有序数字列表 + 目标值（最后一个数是目标）
    data = list(map(int, sys.stdin.read().split()))
    nums = data[:-1]  # 必须是升序！ 集合
    target = data[-1] # 待查找数据

    # 找插入位置，再判断是否匹配
    pos = bisect.bisect_left(nums, target) # 已知nums升序有序序列 先寻找待查找数据应该插入的位置 判该位置是否是target
    if pos < len(nums) and nums[pos] == target:
        print("查找成功")
    else:
        print("查找失败")

    # 统计重复次数
    pos_right = bisect.bisect_right(nums, target)
    print(pos_right - pos)
```



##### 哈希查找

查字典找法 先按照规律确定范围再找

使用set或dict字典

```python
import sys

# 场景1：集合快速查找
def hash_set_demo():
    data = list(map(int, sys.stdin.read().split()))
    nums = data[:-1]
    target = data[-1]

    num_set = set(nums)
    print(f"去重后的列表：{list(num_set)}")
    print(f"目标{target}是否存在：{target in num_set}")

# 场景2：两数之和（字典）
def two_sum_with_dict():
    data = list(map(int, sys.stdin.read().split()))
    nums = data[:-1]
    target = data[-1]

    num_dict = {}
    for i in range(len(nums)):
        num = nums[i]
        # 搭档 = 目标和 - 当前数字   两数之和: target=num+partner
        partner = target - num
        if partner in num_dict:
            print(f"找到啦！下标是 {num_dict[partner]} 和 {i}")
            return
        
        # 没找到的话，把当前数字和下标存进字典
        num_dict[num] = i
    print(res if res else "无满足条件的两个数") # res存在输出res 不存在输出"无满足条件的两个数"
```



### [排序]()

##### 基础排序

```python
import sys

def basic_sort():
    data = sys.stdin.read().split()
    
    data_sorted_asc = sorted(data) # 升序
    print(data_sorted_asc) 
    
    data_sorted_desc = sorted(data, reverse=True) # 降序
    print(data_sorted_desc)

    nums = list(map(int, data)) # 转数字排序（处理数值型数据）
    nums_sorted = sorted(nums, reverse=True)
    print(nums_sorted)
```



##### 自定义规则key排序

```python
import sys

def custom_sort():
    data = sys.stdin.read().split()

    # 场景1：按字符串长度排序
    sorted_by_len = sorted(data, key=lambda x: len(x))
    print(sorted_by_len)

    # 场景2：按数字绝对值排序
    nums = list(map(int, data))
    sorted_by_abs = sorted(nums, key=lambda x: abs(x))
    print(sorted_by_abs)

    # 场景3：元组按指定位置排序（比如二维列表）
    pairs = [(1, 3), (2, 1), (3, 2)]
    sorted_by_second = sorted(pairs, key=lambda x: x[1])  # 按元组第二个元素排
    print(sorted_by_second)
```



##### 有关频率 defaultdict排序

```python
import sys
from collections import defaultdict

def count_sort():
    # 统计字符/单词频次
    s = sys.stdin.read().strip()
    count = defaultdict(int)
    for c in s:
        count[c] += 1

    # 规则：按频次降序，频次相同按字符升序（直接用sorted的key参数）
    sorted_res = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    print("频次排序结果：")
    for char, cnt in sorted_res:
        print(f"{char}: {cnt}")                                                                                                                                                                                  
```



### [并查集]() 

列表模拟 [Disjoint Set Union,DSU]()

```python
# 初始化
def init_uf(n):
    # 父节点(代表元素)
    parent = list(range(n))
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

# 测试代码
if __name__ == "__main__":
    n = 6  # 元素 0~5
    parent = init_uf(n)
    
    # 合并操作
    union(parent, 0, 1)
    union(parent, 1, 2)
    union(parent, 3, 4)
    
    # 判断同集合
    print(is_same_set(parent, 0, 2))  # True
    print(is_same_set(parent, 0, 3))  # False
    print(is_same_set(parent, 3, 4))  # True
```



##### 岛屿问题

更多用dfs解

```python
# 初始化并查集 父节点数组
def init_uf(size):
    parent = list(range(size))
    return parent

# 查找根节点 + 路径压缩
def find(parent, x):
    if parent[x] != x:
        # 路径压缩：让x直接指向根节点
        parent[x] = find(parent, parent[x])
    return parent[x]

# 合并两个元素所在的集合
def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

# 主函数：计算岛屿数量
def count_islands(grid):
    if not grid or not grid[0]:
        return 0
    
    n = len(grid)
    m = len(grid[0])
    
    # 二维坐标转一维索引：(i,j) → i*m + j
    total = n * m
    parent = init_uf(total)
    
    # 方向数组：上下左右（避免重复判断）
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                # 当前陆地的一维索引
                idx = i * m + j
                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy
                    # 检查相邻坐标是否在网格内，且是陆地
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        neighbor_idx = ni * m + nj
                        union(parent, idx, neighbor_idx)
    
    # 统计不同根节点的数量（即岛屿数）
    island_set = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                idx = i * m + j
                root = find(parent, idx)
                island_set.add(root)
    return len(island_set)

# 测试用例
if __name__ == "__main__":
    # 输入一个3x3的网格
    grid = [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ]
    print("岛屿数量：", count_islands(grid))  # 输出：2
```



##### 判断无向图连通性

看所有节点的代表元素是否相同 find(parent)循环 后是同一个

```python
def init_uf(n):
    parent = list(range(n))
    return parent

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

if __name__ == "__main__":
    n, m = map(int, input().split()) # 节点数 边数
    parent = init_uf(n)
    for _ in range(m):
        u, v = map(int, input().split())
        # 假设节点编号从0开始，若题目从1开始则减1
        union(parent, u, v)
    
    # 统计连通块数量
    cnt = 0
    for i in range(n):
        if find(parent, i) == i:
            cnt += 1
    print(f"连通块数量：{cnt}")
    
    # 判断两个节点是否连通
    a, b = map(int, input().split())
    if find(parent, a) == find(parent, b):
        print(f"节点{a}和{b}连通")
    else:
        print(f"节点{a}和{b}不连通")
```



##### kruskal求最小生成树 

详情见图*



##### 带权并查集

带权并查集的原理和模板(三个)

维护距离关系

维护倍数关系

维护种类关系

维护分类关系

维护异或关系



##### 可持久化并查集

##### 可撤销并查集



### [前缀树 ]()

字典树Trie

###### 类+bool版本

```python
class TrieNode:
    def __init__(self):
        # 字典key是字符，value是下一个TrieNode
        self.children = {}
        # 标记当前节点是否是结尾
        self.is_end = False

class Trie:
    def __init__(self):
        # 根节点是空节点，不存储任何字符
        self.root = TrieNode()
    
    # 插入 添加
    def insert(self, word):
        node = self.root
        for char in word:
            # 判复用 如果字符不在子节点中，创建新节点
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char] # 赋值
        node.is_end = True # 循环结束 标记一个结尾
    
    # 查询
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end # 必须是单词结尾才算存在
    
    # 查询是否存在以prefix为前缀的单词
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True # 只要前缀匹配成功，不管是不是单词结尾
    
    # 删除
    def delete(self, word):
        node = self.root
        
        for c in word: # 第一步：先检查单词是否存在于树中
            if c not in node.children:
                return  # 单词不存在，直接返回
            node = node.children[c]
            
        # 第二步：存在的话，把结尾标记改为False
        if node.is_end:
               node.is_end = False
    
     # 查询单词出现的次数
     def query_word_count(self, word):
         node = self.root
         for c in word:
             if c not in node.children:
                 return 0            # 单词不存在，返回0
             node = node.children[c]
         return node.word_count      # 返回最终节点的计数
    
    # 查询前缀对应的单词个数
     def query_prefix_num(self, prefix):
         node = self.root
         for c in prefix:
             if c not in node.children:
                 return 0            # 前缀不存在，返回0
             node = node.children[c]
         return node.prefix_count    # 返回最终节点的计数 
```

###### 类+pass end版本

```python
import sys

class TrieNode:
    def __init__(self):
        self.char_map = {}  # 仅存 字符: 子节点 映射
        self.passed = 0     # 经过该节点的单词数
        self.end = 0        # 以该节点结尾的单词数


    root = TrieNode()

    # 1. 添加插入单词
    def insert(word):
        current = root
        for char in word:
            if char not in current.char_map: # 是否能复用
                current.char_map[char] = TrieNode() # 不能 创建新节点
            current = current.char_map[char] # 创建完 添加
            current.passed += 1
        current.end += 1

    # 2. 查询单词出现次数 → 输出end
    def query_word_count(word):
        current = root
        for char in word:
            if char not in current.char_map: # 没查到
                print(0)
                return
            current = current.char_map[char] # 查到了 输出这个节点的end值
        print(current.end)

    # 3. 查询前缀单词个数 → 输出passed
    def query_prefix_count(prefix):
        current = root
        for char in prefix:
            if char not in current.char_map: # 没查到
                print(0)
                return
            current = current.char_map[char] # 查到了 输出这个节点的pass值
        print(current.passed)

    # 4. 查询单词是否存在 → 存在输出True，否则False
    def query_word_exist(word):
        current = root
        for char in word:
            if char not in current.char_map:
                print(False)
                return
            current = current.char_map[char]
        # 存在的判断依据是 end > 0
        print(current.end > 0)

    # 5. 删除单词 + 回溯更新passed/end + 清理空节点
    def delete_word(word):
        # 第一步：先检查单词是否存在，不存在直接返回
        current = root
        exist = True
        for char in word:
            if char not in current.char_map:
                exist = False
                break
            current = current.char_map[char]
        if not exist or current.end == 0:
            return  # 单词不存在，无需删除

        # 第二步：回溯更新passed和end
        current = root
        # 用列表记录路径上的(父节点, 字符, 当前节点)，方便回溯
        path = []
        for char in word:
            path.append((current, char, current.char_map[char]))
            current = current.char_map[char]
        
        # 1. 单词结尾的end减1
        current.end -= 1
        # 2. 倒序遍历路径，更新passed并清理空节点
        for parent, char, node in reversed(path):
            node.passed -= 1
            # 清理条件：passed=0 且 没有子节点，避免影响其他单词
            if node.passed == 0 and len(node.char_map) == 0:
                del parent.char_map[char]

    # ===== 蓝桥杯一次性输入格式 =====
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    for i in range(1, n + 1):
        parts = data[i].split()
        op = parts[0]
        content = parts[1] if len(parts) > 1 else ""
        
        if op == 'insert':
            insert(content)
        elif op == 'query_count':
            query_word_count(content)
        elif op == 'query_prefix':
            query_prefix_count(content)
        elif op == 'query_exist':
            query_word_exist(content)
        elif op == 'delete':
            delete_word(content)


```

###### 静态数组+pass end版本

```python
import sys

# ========== 静态数组初始化（仅支持小写字母 a-z） ==========
MAX_NODE = 10000  # 节点上限，根据题目数据量调整
son = [[-1] * 26 for _ in range(MAX_NODE)]  # 子节点映射：-1表示无节点
passed = [0] * MAX_NODE  
end = [0] * MAX_NODE    
cnt = 1 

# ========== 1. 插入单词：更新 passed 和 end 标记 ==========
def insert(word):
    global cnt
    p = 0  # 从根节点出发
    for char in word:
        c = ord(char) - ord('a')  # 字符转0-25索引 判断在数组sun的位置 看是否有数字
        if son[p][c] == -1: # 不存在 没有数字
            son[p][c] = cnt # 添加该数字 cnt++
            cnt += 1
        p = son[p][c] # 赋值
        passed[p] += 1 
    end[p] += 1  

# ========== 2. 查询单词出现次数 → 直接输出 end 值 ==========
def query_word_count(word):
    p = 0
    for char in word:
        c = ord(char) - ord('a')
        if son[p][c] == -1:
            print(0)
            return
        p = son[p][c]
    print(end[p])

# ========== 3. 查询前缀单词个数 → 直接输出 passed 值 ==========
def query_prefix_count(prefix):
    p = 0
    for char in prefix:
        c = ord(char) - ord('a')
        if son[p][c] == -1:
            print(0)
            return
        p = son[p][c]
    print(passed[p])

# ========== 4. 删除单词：回溯更新 passed/end + 清理空节点 ==========
def delete_word(word):
    # 第一步：检查单词是否存在
    p = 0
    exist = True
    path = []  # 记录路径：(父节点下标, 字符索引)
    for char in word:
        c = ord(char) - ord('a')
        if son[p][c] == -1:
            exist = False
            break
        path.append((p, c))
        p = son[p][c]
    if not exist or end[p] == 0:
        return

    # 第二步：更新结尾 end 值
    end[p] -= 1
    # 第三步：回溯更新 passed 值并清理空节点
    for parent, c in reversed(path):
        child = son[parent][c]
        passed[child] -= 1
        # 检查子节点是否为空
        has_child = False
        for i in range(26):
            if son[child][i] != -1:
                has_child = True
                break
        # 空节点条件：passed=0 且 无任何子节点，断开连接
        if passed[child] == 0 and not has_child:
            son[parent][c] = -1

# ========== 蓝桥杯一次性输入格式 ==========
def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    for i in range(1, n + 1):
        parts = data[i].split()
        op = parts[0]
        content = parts[1] if len(parts) > 1 else ""
        if op == 'insert':
            insert(content)
        elif op == 'query_end':  # 查单词次数 → 输出 end
            query_word_count(content)
        elif op == 'query_pass':  # 查前缀个数 → 输出 passed
            query_prefix_count(content)
        elif op == 'delete':
            delete_word(content)

if __name__ == "__main__":
    main()
```

###### 静态数组+bool版本

```python
import sys

# ========== 静态数组初始化（仅支持小写字母 a-z） ==========
MAX_NODE = 10000  # 节点上限，根据题目数据量调整
son = [[-1] * 26 for _ in range(MAX_NODE)]  
is_end = [False] * MAX_NODE
cnt = 1  

# ========== 1. 插入单词 ==========
def insert(word):
    global cnt
    p = 0  # 从根节点出发
    for char in word:
        c = ord(char) - ord('a')  # 字符转0-25索引
        if son[p][c] == -1:
            son[p][c] = cnt
            cnt += 1
        p = son[p][c]
    is_end[p] = True  # 标记单词结尾

# ========== 2. 布尔查询：单词是否存在（仅输出 True/False） ==========
def query_word_exist(word):
    p = 0
    for char in word:
        c = ord(char) - ord('a')
        if son[p][c] == -1:
            print(False)
            return
        p = son[p][c]
    print(is_end[p])  # 直接判断是否为单词结尾

# ========== 3. 删除单词：取消结尾标记 ==========
def delete_word(word):
    # 先检查单词是否存在
    p = 0
    exist = True
    for char in word:
        c = ord(char) - ord('a')
        if son[p][c] == -1:
            exist = False
            break
        p = son[p][c]
    if not exist or not is_end[p]:
        return
    is_end[p] = False  # 取消结尾标记

# ========== 蓝桥杯一次性输入格式 ==========
def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    for i in range(1, n + 1):
        parts = data[i].split()
        op = parts[0]
        content = parts[1] if len(parts) > 1 else ""
        if op == 'insert':
            insert(content)
        elif op == 'exist':
            query_word_exist(content)
        elif op == 'delete':
            delete_word(content)

if __name__ == "__main__":
    main()
```



##### 前缀统计

给定n个字符串作为字典，再给定m个查询字符串，统计每个查询字符串是多少个字典中单词的前缀

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0  # 新增：统计经过该节点的单词数

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  # 每经过一个节点，计数+1
        node.is_end = True
    
    # 查询前缀对应的单词数量
    def get_prefix_count(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

# 蓝桥杯标准输入输出
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline  # 提升输入效率
    n, m = map(int, input().split())
    trie = Trie()
    for _ in range(n):
        word = input().strip()
        trie.insert(word)
    for _ in range(m):
        prefix = input().strip()
        print(trie.get_prefix_count(prefix))
```



##### 字典序排序

给定 n 个互不相同的字符串，要求按字典序升序输出所有字符串。

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # key:字符，value:节点
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
    
    # 深度优先遍历，按字典序收集单词
    def dfs(self, node, current_word, result):
        if node.is_end:
            result.append(current_word)
        # 按字符升序遍历子节点，保证字典序
        for c in sorted(node.children.keys()):
            self.dfs(node.children[c], current_word + c, result)
    
    def get_sorted_words(self):
        result = []
        self.dfs(self.root, "", result)
        return result

# 蓝桥杯输入输出格式
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    trie = Trie()
    for _ in range(n):
        word = input().strip()
        trie.insert(word)
    # 输出字典序结果
    sorted_words = trie.get_sorted_words()
    for word in sorted_words:
        print(word)
```



##### 最长公共前缀

给定一个字符串数组，找出所有字符串的最长公共前缀。如果不存在公共前缀，返回空字符串  ""

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word): # 查找 代表元素
        node = self.root
        for c in word:
            if c not in node.children: # 不存在
                node.children[c] = TrieNode() # 创建新节点
            node = node.children[c] # 赋值
        node.is_end = True # 循环结束 结尾
    
    def get_longest_common_prefix(self):
        prefix = [] # 前缀
        node = self.root 
        
        while node: # 判断当前节点是否处于所有单词的公共前缀上   
            
            if len(node.children) == 1 and not node.is_end: 
               	# 当前节点子节点长度1 即当前节点的下一个箭头只有一个 如果有多个箭头 就不是公共前缀
            	# not end 防止单词和前缀混淆 既说是前缀 一定不是结尾 end不能为True
                
                # 是公共前缀 当前节点加入答案
                child_chars = list(node.children.keys())
                c = child_chars[0]  # 因为长度是1，索引0就是唯一字符
                prefix.append(c)
                node = node.children[c] # 判断这个节点的箭头的下一个节点
                """
                c = next(iter(node.children.keys()))
                prefix.append(c)
                node = node.children[c]
                """
            else: # 不是公共前缀 结束了
                break
        return "".join(prefix)

# 蓝桥杯输入输出格式
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    strs = [input().strip() for _ in range(n)] # 字符串数组
    if not strs:
        print("")
        exit()
    trie = Trie() # 初始化前缀树
    for s in strs: # 遍历每一个字符串
        trie.insert(s)
    print(trie.get_longest_common_prefix())
```



```python
# 51.最长公共前缀
"""
    给定一个字符串数组 返回每个元素的最长公共前缀
    ['abcd','abc','abcc','abca'] -> [abc]
"""
# 1.写一个函数
def func(strs):
    # 2.获取strs长度 即字符串个数
    n = len(strs)
    if n == 0:
        return ''

    for i in range(len(strs[0])):
        # 3.先假设第一个字符串的长度最小 第一个字符串的长度 第0行

        # 4.遍历第一个字符串的每一个字母 用于判断的字符串
        temp = strs[0][i]

        # 5.根据第一个字符串的长度及数据 判断其他字符串
        for j in range(1, n):
            if i == len(strs[j]) or temp != strs[j][i]:
                # 如果该其他字符串比第一个字符串更小 或者不匹配 -> 返回结果
                return strs[0][0:i]   # 返回从第一个字符串开头到索引i-1的字串 即最长公共前缀

    return strs[0]    # 如果不出现其他字符串更小 或不匹配 那么第一个字符串就是最长公共前缀
list = ['abcd','abc','abcc','abca']
print(func(list))
```



##### 单词搜索

给定一个 m*n 的二维字符网格  board  和一个单词列表  words ，

找出所有在网格中能找到的单词

（单词由相邻单元格的字符组成，相邻指上下左右，且每个字符只能用一次）

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # 存储完整单词，代替is_end

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word  # 标记单词结尾并存储单词

def find_words(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    m = len(board)
    n = len(board[0])
    result = []
    
    def dfs(i, j, node):
        # 边界判断 + 字符匹配判断
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in node.children:
            return
        c = board[i][j]
        node = node.children[c]
        # 找到完整单词，加入结果
        if node.word:
            result.append(node.word)
            node.word = None  # 去重，避免重复添加
        
        # 标记当前单元格已访问（临时修改字符）
        board[i][j] = '#'
        # 上下左右遍历
        dfs(i-1, j, node)
        dfs(i+1, j, node)
        dfs(i, j-1, node)
        dfs(i, j+1, node)
        # 回溯，恢复字符
        board[i][j] = c
    
    # 遍历网格每个起点
    for i in range(m):
        for j in range(n):
            dfs(i, j, trie.root)
    return result

# 蓝桥杯输入输出格式
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    # 输入网格
    m, n = map(int, input().split())
    board = []
    for _ in range(m):
        row = list(input().strip())
        board.append(row)
    # 输入单词列表
    k = int(input())
    words = [input().strip() for _ in range(k)]
    # 输出结果
    res = find_words(board, words)
    for word in sorted(res):
        print(word)
```







# 算法

### [模拟]()

###### # 19.判断某年某月 距离第一天的天数

```python

# 1.导入时间模块
import datetime

# 2.输入
year,month,day = map(int, input().split(" "))  # map()匹配函数 split切割

# 3.第一天
yuandan = datetime.datetime(year,1,1)

# 4.匹配模块 并输出差值
now = datetime.datetime(year, month, day)
print((now - yuandan).days + 1)  # 输出是第几天
```



###### # 13.输入n个数 整数和小数 求最大数

```python

list = input("输入n个数 用,切割").split(",")

n = len(list)
# 将字符变成数值
for i in range(n):
    list[i] = float(list[i])
print(list)

res = max(list)
print(res)
```



###### # 26.猴子吃桃问题

```python

"""
    猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二
    天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一
    半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
"""
n = 1 # 最后剩下的桃子数量
for i in range(1, 10):
    total = (n+1)*2
    n = total
print(total)
```



###### # 34.求矩阵主对角线元素之和

```python

# 1.矩阵
a = []
sum = 0

# 2.添加矩阵行数据
for i in range(3):

    # 3.添加一排矩阵 表示列
    a.append([])

    # 4.添加矩阵列数据
    for j in range(3):
        k = int(input('请输入数据:'))
        a[i].append(k) # 在第i行添加元素

        # 5.判断主对角线元素 并计算
        if i == j:
            sum += a[i][j]
print(a)
print(sum)
```



###### # 57.IP地址转化

```python

"""
    IP地址是用'.'隔开的四段数字 
    把IP地址转换成一个整数
    
    eg. 114.55.207.244 -> 0111001000110111 11001111 11110100 -> 1916260340
"""
def func(str):
    # 用'.'将字符串切割
    strs = str.split('.')

    # 准备一个空串
    res = ''

    # 遍历
    for i in strs:
        # 十进制转二进制 高位补0
        # '{:08b}'.format(val)
        res += '{:08b}'.format(int(i))
    return int(res, 2)
print(func('114.55.207.244'))
```



###### # 44.猜数字

```python

# 1.导包
import random

# 2.确定一个随机数
target = random.randint(1, 99)   # 创建一个1-100的随机数

# 3.猜的次数
times = 7 # 最多猜7次

print('猜数字游戏开始，请输入100以内整数')
while times != 0:
    num = int(input('输入：\n'))
    if num > target:
        print('大傻逼，猜大了!')
        times -= 1
        continue
    elif num < target:
        print('大傻逼，猜小了!')
        times -= 1
        continue
    else:
        print('大傻逼，猜对了！')
        break
if times == 7:
    print('很遗憾，您的机会已用完')
```





###### 幸运数字

```python
""" 十进制中 含6 8的数字称幸运数 将所有幸运数排序 第一个幸运数是6
    8 66 68 86 88 ...

    给定n 输出所有从大到小排列的幸运数

    看成二进制 6->0 8->1 用二进制的顺序映射幸运数的序列(不直接转二进制的原因)
    0 1 10 11 100
    6 8 68 96 88

    如何将十进制数字通过上述等式变成6和8
    eg. 输入n=7输出该幸运数字
    二进制每一级是2^n个 可以理解为
    第一排2^1 -> 0 1
    第二排2^2 -> 10(3) 11(4) 100(5) 101(6)
    第三排2^3 -> 110(7) 111 1000 1001 1010 1011 1100 1101

    7 = 2 + 4 + 1 7位于第三排 即2^3=8 而2+4+1=7<8

    如果直接把7转成二进制再转成幸运数字 不符合题目的序列逻辑 只能得到孤立的888结果
    无法满足"生成所有幸运数取前n个的要求"
"""
n = 7
s = 0 # 排数次幂 第一排2 第二排4 第三排8
i = 0 # 指数
while s<n: # 如果s小于n就往下再数一排 直到s>n为正常情况
    s = s + 2**(i+1) # 双乘号表幂级数 2的i+1次幂 i默认为0 因此i+1第一项为1
    i += 1 # 此时i变成了i+1 但排数仍然是2^i 即2**i

# 偏移量 差值 如果n=7 已知2^3=8 2+4+1=7 偏移量offset=1
offset = n - (s-2**i) - 1     # 减1 表示从0开始的偏移量 -6

# 十进制n转换为二进制数 格式
def decimal_biary(n):
    s = "" # 存储转换后的二进制字符串
    while n:
        res = n % 2 # 定义res为n除2的余数 n=7 % 2 = 1
        s = str(res) + s # 把res直接并到s的前面
        n = n // 2 # 再整除再取余
    return s
# print(decimal_biary(n)) # 得到了n的二进制
# 上述函数可以直接用内置函数代替 bin十进制转二进制 bin(n) 然后进行切片
"""
b = bin(n)
b = b[2:] 
"""


# 此处插入对bin的讲解
a = 9
b = bin(a) # b是a的二进制 结果为0b1001
b = b[2:] # 切片操作 [start:end] [2:]从2开始切取到字符串末尾 变成了1001


# 继续该算法
res = decimal_biary(offset)
res = '0'*(i-len(res)) + res # 给字符串长度补0
res = res.replace('0', '6').replace('1', '8')
print(res)
```



###### 时间转移

```python
""" 输入秒的时间 转换成小时分钟
    样例输入 4000
    输出 一个小时6分钟40秒
"""
t = 4000 # t=int(input())

h = 4000//3600 # 1小时

# h是已知的小时 *3600变成秒 用原来的总数减去这些秒 剩下的是分钟和秒
# 再整除60 就是分钟
m = (t-h*3600)//60 # 6分钟

s = t-h*3600-m*60 # 40秒

print("{}:{}:{}".format(h,m,s))
```



### [高精度]()



### 枚举 暴力



### [单调栈 ]()

##### 静态空间面试

```java
public static int MAX = 100000;
public static int[] arr = new int[MAX];
public static int[][] stack = new int[MAX];
public static int[][] ans = new int[MAX][];
```



##### 求下一个更大元素

找出数组中每个元素右侧第一个更大的元素

```python
def next_greater_element(nums):
    n = len(nums) # 数据
    res = [-1] * n # 结果 初始化
    stack = [] # 排序栈 单调
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]: # 单调递增栈
            idx = stack.pop() # 出栈 此时下一个栈顶就是左近小
            res[idx] = nums[i] # 当前这个让栈顶出栈的元素就是右近大 答案
        stack.append(i)
    return res

# 测试
if __name__ == "__main__":
    test_nums = [2, 1, 2, 4, 3]
    print(next_greater_element(test_nums))  # 输出 [4,2,4,-1,-1] 
```



##### 求下一个更小元素                                   

找出数组中每个元素右侧第一个更小的元素

```python
def next_smaller_element(nums):
    n = len(nums) # 数据个数
    res = [-1] * n # 结果初始化
    stack = [] # 单调栈
    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]: # 单调递减栈
            idx = stack.pop() # 出栈
            res[idx] = nums[i] # 让栈顶出栈的就是右近小
        stack.append(i)
    return res

# 测试
if __name__ == "__main__":
    test_nums = [2, 1, 2, 4, 3]
    print(next_smaller_element(test_nums))  # 输出 [1,-1,-1,3,-1]
```



##### 求左右下一个更小元素

找出数组中每个元素左、右侧第一个更小的元素

```python
def get_left_right_bound(nums):
    n = len(nums) # 数据个数
    left = [-1] * n # 左
    right = [n] * n # 右
    stack = [] # 单调递减栈
    # 求左边界
    for i in range(n):
        while stack and nums[i] <= nums[stack[-1]]:
            stack.pop() # 出栈 结算 
        if stack:
            left[i] = stack[-1] # 替代栈顶
        stack.append(i) # 让栈顶出栈的就是左近小
    # 求右边界
    stack = []
    for i in range(n-1, -1, -1): # 倒序
        while stack and nums[i] <= nums[stack[-1]]:
            stack.pop() # 出栈 结算
        if stack:
            right[i] = stack[-1] # 代替栈顶
        stack.append(i) # 让栈顶出栈的就是右近小 
    return left, right # 栈顶存了 左最小和右最小

# 测试
if __name__ == "__main__":
    test_nums = [2, 1, 2, 4, 3]
    left, right = get_left_right_bound(test_nums)
    print("左边界下标:", left)  # 输出 [-1,-1,1,2,2]
    print("右边界下标:", right) # 输出 [1,5,5,4,5]
```



##### 求柱状图最大面积

宽度*高度

```python
# 依赖 get_left_right_bound 函数    求左右下一个更小元素
def largest_rectangle_area(heights):
    left, right = get_left_right_bound(heights) # 得到左右最近最小
    max_area = 0
    n = len(heights) # 高度确定
    for i in range(n): # 遍历每根柱子
        width = right[i] - left[i] - 1 # 左右延伸最大宽度
        area = heights[i] * width # 面积
        if area > max_area:
            max_area = area
        # 换柱子
    return max_area

# 测试
if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    print(largest_rectangle_area(heights))  # 输出 10
```



##### 接雨水

给定  n  个非负整数表示每个柱子的高度，柱子按顺序排列，宽度均为  1 。计算在下雨之后，这些柱子能接多少雨水。

```python
 def trap(height):
    n = len(height)
    if n < 3: # 至少要3根柱子才能形成凹槽接水
        return 0
    
    res = 0
    stack = [] # 单调递增栈
    for i in range(n):
        while stack and height[i] > height[stack[-1]]:  # 有更高
            bottom_idx = stack.pop() # 当前栈顶出栈 成为接水凹槽
            if not stack:
                break
            width = i - stack[-1] - 1 # 宽度 高度低的 就是栈数据 除了栈顶
            h = min(height[i], height[stack[-1]]) - height[bottom_idx] # min(右边界高度，左边界高度) - 柱子高度 = 水高
            res += width * h
        stack.append(i)
    return res

# 测试
if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height))  # 输出 6
```



###### 最大矩形

```python
""" 工人砌了一面奇特的砖墙，该墙由N列砖组成(1 <= N <= 106)，且每列砖的数量
    为Ki(1<=K<=104，相邻两列砖之间无缝隙)，每块砖的长宽高都为1。
    小蓝为了美化这面墙，需要在这面墙中找到一块面积最大的矩形用于涂鸦，
    那么请你帮助小蓝找出最大矩形，并输出其面积。
    例如：N=6，表示这面墙有6列，每列砖的数量依次为3、2、1、5、6、2，

            ■        这面墙如图 透明方块为所求的最大矩形 -> 10
          ▢▢
          ▢▢
    ■     ▢▢
    ■ ■   ▢▢ ■
    ■ ■ ■ ▢▢ ■

    不局限于横竖 只要求最大矩形

    输入描述
    第一行输入一个正整数N(1 <= N <= 106)，表示这面砖墙由几列砖组成
    第二行输入N个正整数Ki(1 <= Ki <= 104)，表示每列砖的数量，正整数之间以一个空格隔开
    输出描述
    输出一个正整数，表示最大矩形的面积
    样例输入
    6
    321562
    样例输出
    10
"""
n = int(input())
a = list(map(int,input().split()))

res = []
for i in range(n):
    # 向左考虑凹陷
    p1 = i - 1

    # 向右考虑凹陷
    p2 = i + 1

    s1 = s2 = 0 # 存储结果

    while p1 >= 0 and a[p1] >= a[i]:
        s1 += 1 # 向左考虑一列 发现可以算作矩形
        p1 -= 1

    while p2 < n and a[p2] >= a[i]:
        s2 += 1
        p2 += 1

    rect = (s1+s2+1) * a[i] # 最终结果=(左侧列个数+右侧列个数) * 第i列的高度
    res.append(rect)
print(res)
print(max(res))
```



###### # 64.字符串的相邻字符去重

将相邻且相同的两个字符删掉构成新的字符串，重复删除
acbbc -> a

```python
def func(s): # 输入一个字符串s
    res = ''
    for i in s: # 遍历每一个字符
        # 与res比较 不同就加进res中 相同就不要
        if res == '': # 空
            res += i # 加
        elif res[-1] == i: # 相邻 重复了
            res = res[:-1]   # 取除了最后一个元素的所有元素 即删除最后一个元素
            # res.pop()
        else:
            res += i
    return res
print(func('acbbc'))
```



### 单调队列

##### 滑动窗口

已知数组 

通过R++的方式添加数据 右边界扩展方式

通过L++的方式减少数据 左边界收缩方式

如果L到R是闭区间  L==R说明只剩下一个数据了

如果L到R是左闭右开 L==R说明窗口没东西了

解决子数组和子串相关问题 连续的

子串一定是连续的 不能有间隔



窗口数据和要达到 target 的 最小数据情况

```java
public class Code01_MinimumSizeSubarraySum {
	public static int minSubArrayLen(int target, int[] nums) {
        int ans = Integer.MAX_VALUE; // 结果 初始化
        for (int l =Ox, r=0, sum =0;r < nums.length; r++){
            // l窗口左边界 r窗口右边界 sum临时数据和
            sum += nums[r]； // 当前窗口数据和
            while (sum - nums[1] >= target)  // 尝试减少左边界
            	sum -= nums[1++]；
            if (sum >= target) {
            	ans = Math.min(ans, r - l +1); // 得到结果
            }
        }     
        return ans == Integer.MAX_VALUE ? 0 : ans;
    }
}
```



##### 使用deque

```python
from collections import deque

def max_sliding_window_deque(nums, k):
    q = deque()  # 双端队列，存下标
    res = []
    for right in range(len(nums)):
        # 维护单调性
        while q and nums[right] >= nums[q[-1]]:
            q.pop() # 队尾被比掉了 右出队 失去成为最大值的可能性
        q.append(right)
        
        # 判断过期下标 滑动窗口被挤掉了
        left = right - k + 1
        while q[0] < left:
            q.popleft()  # 过期下标 原队头 左出队
        
        # 收集结果
        if right >= k - 1:
            res.append(nums[q[0]])
    return res

# 测试
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sliding_window_deque(nums, k))  # 输出 [3, 3, 5, 5, 6, 7]
```



##### 滑动窗口最大值

给定滑动窗口宽度k 依次滑动窗口 求最大值

```python
def max_sliding_window(nums, k):
    q = [] # 单向队列
    res = []
    for right in range(len(nums)):
        # 1. 维护队列单调性：队尾元素 <= 当前元素则弹出
        while q and nums[right] >= nums[q[-1]]: # 单调减队列 
            q.pop() # 如果下一个右数 大于队尾 队尾从右出队(为了保证单调递减)  
        q.append(right) # 右边更大 进队 
        
        # 维护滑动窗口 队头出队
        # 2. 判断队头是否过期（超出窗口左边界）
        left = right - k + 1
        while q[0] < left:
            q.pop(0)
        
        # 3. 窗口形成后收集结果
        if right >= k - 1:
            res.append(nums[q[0]])
    return res

# 测试
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sliding_window(nums, k))  # 输出 [3, 3, 5, 5, 6, 7]
```



##### 滑动窗口最小值

给定滑动窗口宽度k 依次滑动窗口 求最小值

```python
def min_sliding_window(nums, k):
    q = []  
    res = []
    for right in range(len(nums)):
        # 1. 维护队列单调性：队尾元素 >= 当前元素则弹出
        while q and nums[right] <= nums[q[-1]]: # 单调减队列
            q.pop()
        q.append(right)
        
        # 2. 判断队头是否过期
        left = right - k + 1
        while q[0] < left:
            q.pop(0)
        
        # 3. 收集结果
        if right >= k - 1:
            res.append(nums[q[0]])
    return res

# 测试
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(min_sliding_window(nums, k))  # 输出 [-1, -3, -3, -3, 3, 3]
```

##### 前缀和

子数组 子串一定是连续的



### [搜索]()

##### 深度优先搜索

```python
# 全局变量：存储结果/标记访问
res = []
visited = []
directions = [(-1,0),(1,0),(0,-1),(0,1)]  # 二维网格用

def dfs(当前状态, 路径):
    # 1. 终止条件
    if 满足结束条件:
        res.append(路径.copy())  # 存入结果
        return
    # 2. 遍历候选
    for 候选 in 候选列表:
        if 候选合法(未越界/未访问/符合条件):
            # 标记+记录路径
            visited[候选位置] = True
            路径.append(候选)
            # 递归
            dfs(新状态, 路径)
            # 回溯：恢复状态
            路径.pop()
            visited[候选位置] = False

# 初始化+启动
visited = [[False]*m for _ in range(n)]  # 二维
# visited = [False]*n  # 一维
dfs(初始状态, [])
```



###### # 案例 迷宫：

```python
# 0表示通路，1表示障碍，求从(0,0)到(n-1,m-1)的最短步数（DFS适合求是否存在，BFS更适合求最短）
n, m = 5, 5
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
visited = [[False for _ in range(m)] for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右
min_step = float('inf')  # 全局变量记录最小步数

def dfs(x, y, step):
    global min_step
    # 递归终止条件：到达终点
    if x == n-1 and y == m-1:
        if step < min_step:
            min_step = step
        return
    # 遍历四个方向
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        # 判断边界、是否障碍、是否未访问
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = True  # 标记已访问
            dfs(nx, ny, step + 1)   # 递归搜索
            visited[nx][ny] = False # 回溯：取消标记

# 启动搜索
visited[0][0] = True
dfs(0, 0, 0)
# 输出结果
print(min_step if min_step != float('inf') else -1)
```



###### 矩阵最长递减路径

```python
""" 深度优先搜索算法 Depth First Search   dfs
    用于搜索树、图
    沿着树的深度遍历节点尽可能多的搜索到树的节点 直到发现所有可达到的结点为止
    经典盲目搜索算法

    使用递归解法
    中间解保存

    eg. 矩阵最长递减路径
    九宫格数字 出发点任意 四个方向 不能越界 下一个数字要比当前数字小
    1 1 3
    2 3 4
    1 0 1
    从最大数字开始 依次选择最大的数字 10
"""
list = [
    [1,2,3],
    [2,3,4],
    [1,0,1]
]

m,n = 3,3  # m n 行 列

def dfs(i,j,value):
    if i < 0 or i==m:
        return 0  # 行越界
    if j < 0 or j==n:
        return 0  # 列越界
    if list[i][j] >= value:
        return 0  # 不是递减

    if (i,j) in dp:    # 判断(i,j)元素是否已经计算过了 如果计算过直接返回
        return dp[(i,j)]

    res = 1
    res = max(res, 1 + dfs(i-1,j,list[i][j]))  # 向上
    res = max(res, 1 + dfs(i+1,j,list[i][j]))  # 向下
    res = max(res, 1 + dfs(i,j-1,list[i][j]))  # 向左
    res = max(res, 1 + dfs(i,j+1,list[i][j]))  # 向右
    dp[(i,j)] = res  # 存储结果
    return res

dp = {}

for x in range(m):
    for y in range(n):
        res = dfs(x,y,100)
        print(res,end=" ")
    print()
# 该输出结果表示 从该位置出发 最多可以经过几个元素

print(dp)
# 匹配格式输出一遍 道理相同

print(max(dp.values()))  # 可以经过的最大元素个数  开始4从 经过5个
```



###### 海域污染问题

```python
""" 例题 如图 
    海域 
    1未被污染 0被污染 
    可以把连续的1区域当作一个大的未被污染的海域 一共有三片未被污染的海域
    
    1 1 0 0 0 
    1 0 1 0 0
    1 0 0 0 0
    1 1 0 1 1
    
    解法: 从左上角开始 上下左右四个方向判断是否为1 
        首先向下判断是否成立 成立就继续向下 直到到底 向右判断
        然后从起点的右边再次开始判断
        这样从左侧和上侧边缘判断完 从第二行开始扫描到成立部位
        
"""
list = [
    [1,1,0,0,0],
    [1,0,1,0,0],
    [1,0,0,0,0],
    [1,1,0,1,1]
]
m = 4;n = 5  # m n 行列

def dfs(x,y):
    # 无需判断的条件
    if x<0 or x==m or y<0 or y==n or list[x][y] == 0:
      # 越界了 超过边界了               已经判断过了
        return 0  # 说明是污染的地方 或者判断过了 或者边界

    # 从左上角起点开始
    list[x][y] = 0  # 标记 把经过的位置标记为0
    # 当第一个位置结束后 下方四个方向会有一次经过0位置 根据上方if判断 该位置将不再考虑

    # 依次从四个方向进行判断
    dfs(x+1,y) # 向上
    dfs(x-1,y) # 向下
    dfs(x,y-1) # 向左
    dfs(x,y+1) # 向右

cnt = 0   # 计数器
for i in range(m):
    for j in range(n):
        if list[i][j] == 1:  # 没污染的地方
            dfs(i,j)
            cnt += 1
print(cnt) # 得到所有的没有被污染的地方

```



###### 岛屿数量

```python
""" 深度优先算法 省赛集训例题 岛屿数量
    给你一个由'1'（陆地）和‘0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
    此外，你可以假设该网格的四条边均被水包围。
    
    示例1：
    输入：grid= [
        [”1”，”1”，”1”，“0”，"0”，“0”，”0”].
        [”1”，”1”，”0“，"1”，”0”，"0”，"0"].
        ["0"，"0"，"0”，"0"，"0"，“1“，"0"] 
        ["O"，"0"，"0”，"0"，“1”，”1”，"1"]
    ]
    输出：3
"""
grid = [
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1]
]

# m=4;n=7
m = len(grid)
n = len(grid[0])


def mark_current_island(x, y):  # 标记
    if x < 0 or x > m - 1 or y < 0 or y > n - 1 or grid[x][y] != 1:
        #   超过边界                        不是岛屿 是水
        return  # 此处return后什么都不写意为return None 和return 0 不是一个意思

    grid[x][y] = 2  # 把正在判断的位置标记为2 当再次遇到这个位置时跳过

    print(x, y)  # 打印每个岛屿坐标

    mark_current_island(x - 1, y)
    mark_current_island(x + 1, y)
    mark_current_island(x, y + 1)
    mark_current_island(x, y - 1)


cnt = 0  # 存储岛屿个数
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:  # 发现新岛屿 二维元素的遍历
            mark_current_island(i, j)
            cnt += 1

mark_current_island(0, 0)  # 起点

print(cnt)

for row in grid:
    print(row)
```



###### 马走日

```python
""" 请编写一段程序，给定n*m大小的棋盘，以及马的初始位置(x，y)，
    要求不能重复经过棋盘上的同一个点，计算马可以有多少途径滴历棋盘上的所有点。

    输入 第一行为整数T(T< 10)，表示测试数据组数。
        每一组测试数据包含一行，为四个整数，分别为棋盘的大小以及初始位置坐标
        n, m, x, y。(0 <= x <= n-1, 0 <= y <= m-1, m<10, n<10)
    输出 每组测试数据包含一行，为一个整数，表示马能遍历棋盘的途径总数，0为无法遍历一次。

    样例输入 1
            5 4 00
    样例输出 32

    递归 + 回溯

    马的走法: 马走日 一共走三步 横向+纵向
             要么x走两步y走一步 要么y走两步x走一步
    ▲: x+2 y+2, x+1 y+1, x-2 y+1, x-1 y+2,
       x-2 y-1, x-1 y-2, x+2 y-1, x+1 y-2
"""
t = int(input("输入一共有多少组"))  # 第一个输入数据 表示一共要测试几组

for _ in range(t):
    m,n = 5, 4 #  行 列
    a,b = map(int, input("输入初始坐标x y").split(" "))  # 初始坐标xy

    dirs = [(2,1),(1,2),(-2,1),(-1,2),(-1,-2),(-2,-1),(2,-1),(1,-2)]

    # 列表生成式 棋盘二维列表
    board = [[0]*n for x in range(m)]  # m行(0, m-1)  n列(0, n-1)

    # 0标记没有走过
    cnt = 0 # 计数器 表示路径数量 不重复

    def move(x,y,step):
        global cnt # 全局变量

        if step == m*n:
            cnt += 1 # 一共走了3步 相当于一种新的走法 计数器+1
            return

        for i in range(8):  # dirs中一共8个走法
            next_x = x + dirs[i][0]  # 行的便移
            next_y = y + dirs[i][1]  # 列的偏移

            if next_x >= 0 and next_x <= m-1 and next_y >= 0 and next_y <= n-1 and board[next_x][next_y] == 0:
                board[next_x][next_y] = 1  # 标记为1 当前位置再经过时不会考虑
                move(next_x, next_y, step+1)  # 下一个位置
                board[next_x][next_y] = 0  # 进入下一次循环后 将本次循环的标记变回0
                """ 此处为深度优先算法的回溯思想
                    标记为1防止重复访问 回溯为0来探索其他路径
                    
                    eg.
                   .
                    /A -> B 
                    -> C -> D   从A到D有两种走法 循环走其中一种时 A标记为1
                                需要回到A判断另一种走法 此时A标记为0
                """

# a,b = 0,0
board[a][b] = 1  # 马走过的地方标记1
move(a,b,1)
print(cnt)
```



###### # 30.农作物区域问题

```python
""" 30.编程实现：有一块农田被划分为N*M块，农作物和杂草分布生长在农田中，其中农作物使用
    大写字母“R"表示，杂草使用大写字母“X”表示，请计算出农田中有几块独立的农作物区域（独
    立的农作物区域指该区域上下左右都被杂草围住，且N"M以外的区域都是杂草）。

    例如：N=4，M=4，4*4的农田中农作物和杂草分布如下图：
    R R R X
    R X R X
    X X X R
    R X X X
    这块4*4的农田中有3块独立的农作物区域（红色的3部分）
    
    输入描述：
    第一行输入两个整数N和M(1SNS100，1SMS100)，N表示农田的行数，M表示农田的列数，且两个正整数之间以一个英文逗号隔开
    接下来的N行每行包括M个字符（字符只能为R或X），R表示农作物，X表示杂草，字符之间以一个英文逗号隔开
    
    输出描述：
    输出一个整数，表示N*M的农田中有几块独立的农作物区域
"""
m,n = input().split()
m,n = int(m), int(n)
a = []
for x in range(m):
    tmp = input().split()
    a.append(tmp)


def dfs(x,y):
    # 超出范围 或 该区域是杂草
    if x < 0 or x >= n or y < 0 or y >= m or a[x][y] == 'X':
        return

    # 该区域是农作物 标记该区域 表示已经判断过了
    a[x][y] = 'X'
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x,y-1)


count = 0
for i in range(m):
    for j in range(n):
        if a[i][j] == "R":
            dfs(i,j)
            count += 1

print(count)
```



##### 广度优先搜索

```python
from collections import deque

def bfs(起点):
    # 初始化队列+访问标记
    q = deque()
    q.append((起点坐标, 初始步数))
    visited = [[False]*m for _ in range(n)]
    visited[起点x][起点y] = True
    # 方向数组
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while q:
        x, y, step = q.popleft()
        # 1. 到达终点，直接返回（BFS首次就是最短）
        if (x, y) == 终点:
            return step
        # 2. 遍历四个方向
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and 合法条件:
                visited[nx][ny] = True
                q.append((nx, ny, step+1))
    # 无法到达终点
    return -1

# 启动
print(bfs((0,0)))
```



###### 案例

```python
from collections import deque  # 竞赛常用，效率高于列表模拟队列

n, m = 5, 5
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
visited = [[False for _ in range(m)] for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    # 队列存储 (x, y, 当前步数)
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = True
    while q:
        x, y, step = q.popleft()  # 队首出队
        # 到达终点，直接返回步数（BFS首次到达就是最短）
        if x == n-1 and y == m-1:
            return step
        # 遍历四个方向
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, step + 1))
    # 无法到达终点
    return -1

print(bfs())
```



###### 传送门

```python
""" 在一个神奇空间里有N个房间，房间从1到N编号，每个房间可能有一个或多个传送门，
    每个传送门都有一个编号，如果相同编号的传送门同时出现在多个房间中，表示这些
    房间可以互通。给定两个房间的编号A和B，请找出从房间A到达房间B最少需要经过几
    个传送门。

    例如：N=3，3个房间中传送门的编号分别为：
    房间1(房间编号)：1(传送门)、4、6；
    房间2：         2、3、    4，8；
    房间3：            3、      6、9

                    3号互通 4号互通 6号互通

    第一行输入一个正整数N(2<=N<=20)，表示房间数量,接下来输入N行，每行包含多个正整
    数(1<=正整数<=100)，第2行到第N+1行依次表示1到N号房间内所有传送门的编号，正
    整数之间以一个英文逗号隔开最后一行输入两个正整数A和B(1<=A<=N，1<=B<=N，且A!=B)，
    表示两个房间的编号，正整数之间以一个英文逗号隔开

    输出描述
    输出一个整数，表示从房间A到达房间B最少需要经过几个传送门，如果
    房间A不能到达房间B，则输出-1

    样例输入
    3         房间数量
    1,4,6     每个房间的传送门编号
    2,3,4,8
    3,6,9
    1,2       需要传送的起始房间和终止房间
    样例输出
    1

    首先判断是否有直通的传送门 如果没有考虑中介传送门

"""
n = int(input("房间数量"))

a = [] # 二维列表
for x in range(n):
    a.append(input("输入各个房间的传送门编号").split(","))

x,y = list(map(int,input().split(",")))

x,y = x-1,y-1 # 房间编号 索引


visited = [] # 记录已经经过的房间 即路线样貌
res = [] # 可以到达目标房间的路线数量 输出最小值即可

def find(room,cnt):
    if room == y:  # 到了
        res.append(cnt)
        return

    visited.append(room) # 路线经过的房间
    for i in range(len(a)):
        if i not in visited and set(a[room]) & set(a[i]):
            # 如果i房间没有被访问过 且与目标房间和起始房间的传送门有交集 就访问该房间
            find(i,cnt+1)
    visited.pop() # 集合.pop() 随机取出一个元素 意为寻找其他路线方法

find(x,0)
if len(res) == 0:
    print(-1)
else:
    print(min(res))

```



### [递归 回溯 剪枝]()  

###### # 29.年龄急转弯

```python

"""
    有5个人坐在一起，问第五个人多少岁?他说比第4个人大2岁。问第4个人岁数，他说
    比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两
    岁。最后问第一个人，他说是10岁。请问第五个人多大?
"""
def func(n):
    if n == 1:   # 第一个人
        return 10
    else:        # 从某人开始 比钱一个人大2岁
        return func(n-1) + 2
print(func(5))
```



###### # 5.密室逃脱问题

可递归 线性dp

```python
""" 5.有一个密室逃脱游戏，有100间密室连在一排。密室编号是从1开始连续
      排列一直排到第100间密室，如下图：
    
      游戏规则：
        1.玩家初始位置在1号密室；
        2.每次玩家可以进入右边的一个密室，也可以跳过一个密室进入下个密室
        （如：当玩家当前在3号密室，他可以进入4号密室也可以进入5号密室）；
        3.有毒气的的密室不能进入
        
      编程实现：
        给定三个正整数X，Y，M(X<Y<Ms100)，表示三个密室编号。X号密
        室和Y号密室有毒气泄漏，不能进入，玩家需要进入到M号密室。按照游
        戏规则进入M号密室有多少种路线方案。例如：X=2，Y=4，M=7，进入
        M号密室有2种路线方案，分别是1->3->5->6->7路线和1->3->5->7路线。
        
      输入描述：输入三个正整数XY，M(X<Y<M)，X和Y表示有毒气密室
            编号，M表示需要进入的密室编号，且三个正整数之间以英文逗号隔开
    
      输出描述：输出进入M号密室有多少种路线方案
      样例输入：2, 4, 7
      样例输出：2
        
        1 -> 2
             3 -> 4
                  5 -> 6 -> 7
                       7
"""
# x,y,m = input().split()
# x,y,m = int(x),int(y),int(m)
x = 2
y = 4
m = 7 # 目标密室
def find(m): # 确认目前是否到达目标密室
    # 必须先判断毒气的房间 否则会在递归过程中把有毒气的路径加进去
    if m == x or m == y: # 如果要到达的密室是毒气密室 那么不能去
        return 0
    if m == 1 or m == 2: # 如果要到达的密室是密室1或者密室2 那只有一种走法不需要后期判断
        return 1

    # 如果不是上述情况
    res = find(m-1) + find(m-2) # 递归
    # 如果判断到该行 说明到达m密室可以达成 我们判断从m-1和m-2是否可行
    # 设有一个不能执行 另一个可行 判断可行的那个密室的上一步
    # 如果两个都可行 判断两个的上一步 就是4个密室再次判断 这样累加下来可以得到最终可以走的密室的个数
    return res

res = find(m)
print(res)
```



###### n皇后

```python
""" N皇后问题原文: 1848年一名国际西洋棋棋手马克斯贝瑟尔提出
    在8*8的国际象棋棋盘上摆放8个皇后 使其不能相互攻击
    即 任意两个皇后不能处于同一行同一列同一对角线 有多少种摆法  92

    有一个NN的矩阵方格 先将N个棋子按照要求放到矩阵方格中
    要求如下: 1.任意两个棋子不能在同一行
             2.任意两个棋子不能在同一列
        即同一个对角线张不允许有两个皇后存在
    □■□□         □□■□
    □□□■         ■□□□
    ■□□□         □□□■
    □□■□         □■□□
    假设一个4*4的矩阵方格 要求放4个棋子 不同行不同列

    判断方法 从已知棋子的所有方向出发 不能碰到棋子 两条直线两条对角线

    深度优先算法dfs+回溯思想 剪枝

    先选定一个位置 然后第二个个棋子有4种摆法 选定后第三个棋子有四种摆法... 此时并没有考虑不能放的位置
    每选定第一个棋子后 都有四种摆法 时间复杂度O(n^n)
"""

""" N皇后问题特点: 正对角线差值相同 反对角线和相同

    假设坐标为i,j 选定一个皇后位置后
    该对角线上的所有i-j相同(作为c旗帜判断) i+j相同(作为d旗帜判断)
"""

""" dfs搜索 万能算法公式

    def dfs():
    if 满足条件:
        输出结果
    遍历循环:
        dfa(下一个)
        
        回溯
"""

n = int(input("输入N"))  # 创建个数 数据
matrix = [[0 for i in range(n)] for j in range(n)]  # 创建n*n的棋盘空间
ans = 0 # 存储走法个数结果

# 判断该位置是否可以放棋子
def check(x,y):

    # 判断水平方向有没有棋子
    for i in range(n):
        if matrix[i][y] == 1:  # 0就是没有 1就是有
            # 判断的思想: 只改变i(x)的数值 不改变数值方向数值
            return False # 标记已为1 证明有棋子

    # 判断正对角线有没有棋子
    for i in range(n):
        for j in range(n):
            if x-y == i-j and matrix[i][j] == 1:
                return False

    # 判断反对角线有没有棋子
    for i in range(n):
        for j in range(n):
            if x+y == i+j and matrix[i][j] == 1:
                return False

    # 上述三个循环走完均没有棋子 代表此处可以放置
    return True


# 进行放置并添加输出结果
def dfs(num):
    global ans

    if num == n:  # 判断到了最后一个棋子 (从第一个位置开始判断)
        ans += 1
        return
    else:
        for i in range(n):
            if check(num,i): # 如果经过了判断函数 已知该位置可放
                matrix[num][i] = 1
                dfs(num+1)
                matrix[num][i] = 0 # 回溯思想

dfs(0)
print(ans)


""" 6.(N皇后)编程实现：有一个N*N的矩阵方格和N个棋子，现在需要将N个棋子按要求
               放置到矩阵方格中。要求如下：
        任意两个棋子不能在同一行、同一列、同一对角线上（下图红色线段都为对角线）
        根据以上要求，问N个棋子放置到N*N矩阵方格中有多少种放置方案
        例如：4*4的矩阵方格，4个棋子，有2种放置方案
        
        N皇后问题主要判断逻辑: 主对角线差等 副对角线和等 水平没有 竖直没有
"""
N = 4 # 需要放置的皇后个数
list = [[0 for i in range(N)] for j in range(N)] # 创建二维棋盘

def check(x,y): # 我现在拿着(x,y)坐标对整个棋盘做检查
    for i in range(N): # 假设我固定y 检查该横向所有的i中有没有皇后 有就与(x,y)的皇后重复
        if list[i][y] == 1: # 检查列
            return False
    for i in range(N):
        for j in range(N): # 遍历整个棋盘检查主对角线
            if x-y == i-j and list[i][j] == 1: # n皇后问题主对角线逻辑 差相等 就说明斜线上有重复
                return False
    for i in range(N):
        for j in range(N): # n皇后问题副对角线逻辑 和相等就说明反斜线上有重复
            if x+y == i+j and list[i][j] == 1:
                return False
    return True

ans = 0 # 统计放置方法
def dfs(num): # 对整个棋盘深度优先搜索算法 num既是皇后个数也是行数 要求第i行及之前已经放好了i个皇后
    global ans

    if num == N: # 所有皇后全部放置了
        ans += 1 # 这代表我执行了一次完整的把所有皇后放下的方案 ans+1 然后重新考虑所有皇后位置
        return
    else:
        for i in range(N): # i变化 遍历棋盘每一列
            if check(num, i): # 如果条件满足了 说明没有皇后
                list[num][i] = 1 # 放置一个皇后
                dfs(num+1)
                list[num][i] = 0 # 回溯 意义是试错后恢复初始状态 为其他所有潜在可能方案准备后悔药

dfs(0)
print(ans)
```



###### # 29.数字排列问题

可用贪心

```python
""" 29.编程实现：有N个正整数，现对N个正整数进行不同方式的排列，每次排列后都会按照以下规则
    进行一次计算，聪明的小蓝发现，排列方式不同，最后计算出的结果也不相同。
    
    计算规则：
    第一次：第一个数乘以第二个数乘以第三个数，结果记录为M(1);
    第二次：第二个数乘以第三个数乘以第四个数，结果记录为M(2)；
    第三次：第三个数乘以第四个数乘以第五个数，结果记录为M(3)；
    第N-2次：第N-2个数乘以第N-1个数乘以第N个数，结果记录为M(N-2)。
    最后计算M(1)+M(2)+M(3).....M(N-2)的数值。
    找出一种排列方式使这个数值最大。
    
    例如：N=4，4个正整数分别为1，2，3，4，那么排列方式就会有24种：
    其中排列方式为1，3，4，2时，按照规则计算2次：1*3*4=12，3*4*2=24；乘积相加：12+24=36
    这种排序方式是所有乘积相加的数值最大，为36。
    
    输入描述：
    输入N个正整数(35N)，正整数之间一个英文逗号隔开
    输出描述：
    找出所有乘积相加的数值愚大的排列方式，并输出数值
"""

# 假设数字有1 2 3 4 数字的全排列表示
a = [1,2,3,4] # a = list(map(int,input().split(',')))
n = len(a)
a.insert(0,0) # 在列表0位置中插入元素0 a = [0,1,2,3,4]

f = [0] * (n+1) # 标记 旗帜   创建一个长度为n+1 (长度为5) 的列表f 所有的元素为0 f = [0,0,0,0,0]
b = [0] * (n+1) # 用于存储结果 创建一个长度为n+1 (长度为5) 的列表b 同样都为0

maxp = 0

def nums(i):
    global maxp

    if i == n+1:
        tmp = 0
        for j in range(n-1):
            tmp += b[j]*b[j+1]*b[j+2]
        if maxp < tmp:
            maxp = tmp
        return # 循环终止条件

    for x in range(1, n+1): # 遍历每一个索引
        if f[x] == 0: # 代表该位置未被使用过
            f[x] = 1 # 标记使用
            b[i] = a[x] # 将这个索引放在b里
            nums(i+1) # 递归
            f[x] = 0

nums(1)
print(maxp)
```



###### # 6.数独

```python
""" 6.给定部分数独 要求把0的位置补充完整
    1234
    4321
    3100
    0000
"""
# 判断函数
def valid(x,y,num):  # x行 y列 num填入的数字
    """ 如果不知道矩阵长宽
        N = len(a)  行列数
        K = int(math.sqrt(N)) 每个小方格的大小
    """
    if num in a[x]: # 该行已经有这个数字了
        return False

    # 该列已经有这个数字了
    """if num in [row[y] for row in a]:"""
    if num in list(zip(*a))[y]:  # 矩阵的转置

        # *a 矩阵的解包 把每一行拆开
        # zip(*a) 对每一行打包 实现行转列
        # (zip(*a))[y] 取转置后的第y列 也就是取每一列
        return False

    """ ax,ay = (x//k)*k, (y//k)*k 
        for i in range(ax,ax+k):
            for j in range(ay,ay+k):
                if a[i][j] == num:
                    return False
        return True
    """

    # 因为设定矩阵为4行4列 每一个部分的小方块是两行两列
    ax,ay = x//2, y//2 # 确定该坐标在2*2的子矩阵中坐标

    # 该设定方块内已经有这个数字了
    for x in range(2):
        for y in range(2):
            nx, ny = ax*2+x, ay*2+y  # 在大矩阵中的实际索引
            if num == a[nx][ny]:  # 该数字在该坐标存在
                return False
    return True # 都没有 证明可以放入这个数字

# 添加函数
def find():
    for i in range(4):
        for j in range(4):
            if a[i][j] == 0:
                for num in (1,2,3,4):
                    if valid(i,j,num):
                        # print(f"({i},{j})-{num} √")
                        a[i][j] = num

                        find()
                        # 递归 处理下一个位置

                        a[i][j] = 0
                        # 在处理下一个位置时 让上一个位置回溯为0
                        # 方便判断下一个位置所有数字是否匹配
                    """else:
                        print(f"({i},{j})-{num} ×")
                    """

                return

    print("...found...")
    for row in a:
        print(row)
    print()

# 主函数
a = [
    list("1234"),
    list("4321"),
    list("3100"),
    list("0000")
]
# 列表生成式 将上述a变成二维列表
a = [ [int(x) for x in row] for row in a]
find() # 开始执行find函数
```



###### 组合合数 难

```python
""" ...编程实现: 小名收藏了N(2 <= N <= 25)个数字币，每个数字币上都有一个面值
    (面值可以重复)。从数字币种任选k个(2 <= k <= N)，有多种选法，请将每次选
    择的数字币上的面值累加，然后解决以下两个问题

    问题1: 累加的和中有多少种不同的结果
    问题2: 累加的和中有多少个不同的合数

    第一行输入一个正整数N，表示数字币的个数
    第二行输入N个正整数(1<正整数<1000)，表示数字币上的面值，正整数之间以一个英文逗号隔开
    第三行输入一个正整数K，表示所要选取的数字币个数

    输出描述: 输出两个数，分别表示累加和不同结果的个数，
            以及累加的结果中不同合数的个数，两个整数之间以一个英文逗号隔开

    样例输入
    5
    2, 1, 4, 5, 3
    3
    样例输出
    7,5
"""
N = int(input())

# 输入N个正整数 写一个list map
a = list(map(int,input().split(",")))

# k = int(input())

result1 = 0 # 总共结果个数
result2 = 0 # 合数个数

# 判断合数
def heshu(n):
    for x in range(2,n):
        if n % x == 0:
            return True
    return False

# 此题中k若不确定为多少 适合用回溯法递归实现 太难了
# 写死k=3
k=3

# 全部结果
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            result1.append(a[i]+a[j]+a[k])
            # print(f"{a[i]+a[j]+a[k]}")

b = set(result1) # set创建一个集合 无顺序无重复的容器
c = 0
for ele in a:
    if heshu(ele):
        c += 1

b = len(b)
print(f"{b},{c}")
```



### [动态规划DP]()

functools.lru_cacle 记忆化搜索 优化神器

##### 线性DP

###### # 27.求指定数列和

```python

"""
    求2/1 3/2 5/3 8/5 13/8 21/13....的前20项和
"""
sum = 0
up = 2
down = 1
for i in range(20):
    sum += up / down  # 和
    a = down          # 分母
    down = up         # 分母变成前一个数的分子
    up = up + a       # 分子变成前一个数的分子加分母(前一个数的两位数字相加)
print(sum)
```



可以用线性dp 滑动窗口 字符串匹配

###### # 66.最长公共字串

```python

"""
    hellopython
    goodlopylike
    
    已知两个字符串 依次将左指针比较 如果相同 就把第一个指针位置往后移 
                                如果不同 就两个指针都往后移
                                
    滑动窗口
"""
def lcs(str1, str2):
    res = ''
    left = 0
    for i in range(len(str1) + 1 ):   # 为保证str1中所有元素都取到 此处 +1
        if str1[left:i+1] in str2:
            # 如果str1中从left(最初默认left为0 即第一个元素)开始
            # 直到i元素都在str2中 就把这些元素添加到res中
            res = str1[left:i+1]
        else:
            # 第一个元素没匹配
            left += 1  # 匹配第二个元素
    return res
print(lcs('hellopython','goodlopylike'))
```



###### 杨辉三角

```python
""" 杨辉三角就是一个用数排列起来的三角形，杨辉三角规则如下：
    1）每行第一个数和最后一个数都为1，其它每个数等于它左上方和右上方的两数之和；
    2)第n行有n个数。

    注意：“列”指的是如图所标注的斜列。

    小青对杨辉三角的特点和规律研究得很明白，现要考察你对杨辉三角的熟悉程度，首先
    告知你这是一个N行的杨辉三角，然后又告知了两个数值X和Y(X行，Y列)，让你根据杨
    辉三角的特点和观察到的规律解决以下两个问题。
    1）第X行第Y列对应的数是多少；
    2）求出N行的杨辉三角中第Y列中所有数的和。

    输入描述
    第一行输入一个正整数N(2<N<30)，表示杨辉三角的行数
    第二行输入两个正整数X和Y(<=N)，分别表示第X行和第Y列，正整数间以英文逗号隔开
    输出描述
    输出两个整数，分别表示N行的杨辉三角中第X行Y列对应的数，及第Y列上所有数的和，两个
    整数之间以一个英文逗号隔开
"""
N = int(input())
# X Y是列表a里的坐标 因此输入时写list map
X,Y = list(map(int,input().split(",")))

# 列表生成式 [1]*N会创建一个包含N个1的列表
a =[[1]*N for i in range(N)]



# 开始创建杨辉三角 第0行->1 第1行->1 1 第2行-> 1 2 1 从第二行开始更改数字
for x in range(2,N):
    for y in range(1, x): # 1->x 中间的是要更改的数字 即不包含0和最后一个位置x
        a[x][y] = a[x-1][y] + a[x-1][y-1]

# 打印列表 杨辉三角
for row in a:
    print(row)



# 该位置数字 从0开始数
res1 = a[X-1][Y-1]

# 计算竖直和 从最后一个元素 往前加 x-1为当前所在行 再减1为索引表示形式
res2 = 0
for t in range(X-1,Y-1-1,-1):
    res2 += a[t][Y-1]


print("%d,%d"%(res1,res2))


# 42.打印杨辉三角
# 1.列表
a = []

# 2.创建位置`123
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)   # 先全部赋值为0 方便后续计算

# 3.计算首尾
for i in range(10):
    a[i][0] = 1
    a[i][i] = 1

# 4.计算中间数据
for i in range(2, 10):
    for j in range(1, i):
        a[i][j] = a[i-1][j] + a[i-1][j-1]

# 5.打印
for i in range(10):
    for j in range(i+1): # j行有i个元素 因此范围为i+1
        print(a[i][j], end=" ")
    print()

```



##### 路径类DP



##### 区间DP



##### 背包问题

```python
""" 背包问题
    指定一组物品 在背包容量有限的前提下 选择一些物品放入背包中 使得背包价值最大

    若干商品 每个商品有对应的重量和价值 我们可以取或不取

    优化：中间结果记忆 存储中间结果 减少递归次数

    重量(kg) 1 2 4 2 5
    价值($)  5 3 5 3 2
    五件商品 用yes no标记取或不取

    使用递归方法解决背包问题 首指针指向最后一个元素
    1.初始
    首指针    n=5
    背包容量  c=10  重量和
    总价值初始 v=0

    2.将首指针元素放入背包后   或者   首指针元素没有放进背包中
    n=4                           n=4
    c=10-5=5                      c=10
    v = 2                         v=0
    3.   ...
    4. n=1  递归结束
"""

# 输入数据默认第一个位是0
w = [0,1,2,4,2,5]
v = [0,5,3,5,3,2]
result = 0

def ks1(n,C):
    if n==0 or C==0:
        # 结束
        result = 0
    elif w[n] > C:
        # 商品总重量大于背包容量 放不下
        result = ks1(n-1,C) # 这一件商品忽略掉 不要了
    else:
        tmp1 = ks(n-1,C)  # 不放本次商品
        tmp2 = v[n] + ks(n-1, C-w[n])  # 放了本次的商品 并进入下一次商品判断
        result = max(tmp1,tmp2)
    return result
# 时间复杂度 O(2^n)

n=5
res = ks1(n,10)
print(res)  # 16 最大的价值



print("-----------")



w = [0]; v = [0]
for x in range(n):
    w1, v1 = list(map(int, input().split(',')))
    w.append(w1)
    v.append(v1)


def ks(n,C):
    # 打印数据结果 效果:打印了步骤中的结果
    if memo[n][C] != 0:
        for row in memo:
            print(row)
        print()
        return memo[n][C]   # 取出结果

    # 添加数据结果
    if n==0 or C == 0:
        result = 0
    elif w[n] > C:
        result = ks(n-1,C)
    else:
        tmp1 = ks(n - 1, C)  # 不放本次商品
        tmp2 = v[n] + ks(n - 1, C - w[n])  # 放了本次的商品 并进入下一次商品判断
        result = max(tmp1, tmp2)
    memo[n][C] = result  # 存结果
    return result



# 初始化  n = 5; C = 10
n,C = list(map(int,input().split(',')))

# 创建一个二维列表 n+1行 C+1列
memo = [[0]*(C+1) for x in range(n+1)]  # 数据结果存储在列表中
res = ks(n,C)
print(res)
```



###### 硬币兑换

```python
""" 已知有1 2 5面值的三种硬币 找出兑换7元、21元使用最少的硬币数

    已知目标数额 将每种情况计算出来 输出最少的数量

    7 -> 5 -> 2
      -> 5 -> 1 -> 1
      -> 2 -> 2 -> 2 -> 1
      -> 1
      ...
"""
coins = [1,2,5]
amount = 7
cnt = 0
ans = []

def find(m,sc):
    # m金额   sc交换硬币连接(1 2 1 2)
    global cnt

    if m<0:
        return
    elif m == 0:
        cnt += 1
        ans.append(sc)
        return

    for coin in coins:
        find(m-coin,str(coin) + ' ' + sc) # 递归

find(amount, '')
ans = [x.split() for x in ans]
res = [len(x) for x in ans]
# print(ans)
print(min(res))
```





### [数学扩展]()

###### # 17.找质数因子

```python

a = int(input('输入这个数'))
y = 2  # 2是最小的质数
list = []
while a != y:
    if a % y == 0: # 说明使质因数
        list.append(y)
        a /= y # 继续判断新的a
    else:
        y += 1  # 寻找下一位的公因数 就是加1再除一次
list.append(int(a))  # 输出带上本身
for i in list:   # 打印list格式
    print(i,end=' ')
```



###### # 46.最大公因数

```python

"""
    1.如果数相同 最大公因数就是本身
    2.如果两个数成倍数关系 小的数就是最大公因数
    3.如果没有关系 从小的数开始 一次将小的数减1 判断能否整除
"""
def func1(a,b):
    if a == b:
        return a
    num = min(a, b)
    while a % num != 0 or b % num != 0:
        num -= 1
    return num
print(func1(12, 18))
```



###### # 14.给定一个合数n

```python
 将n分解为质因数后 输出其质因数个数
n = int(input())
count = 0
i = 2
while n > 1:
    while n % i == 0:
        count += 1
        n = n // i
        # print(i)
    i += 1
print(count)
```



###### # 73.尾部的0

```python

"""
    给定整数n 计算n!中的尾部的0的个数
"""
def func(n):
    count = 0
    for i in range(5,n+1,5):   # 从5到n+1 步长为5 只需要判断个位5的数的阶乘
        while i % 5 == 0:
            # 为了使尾部有0 判断该n是否为5的倍数
            i //= 5   # 开始整除并计数 计算有多少个0
            count += 1
    return count
print(func(5))
```



###### # 74.统计数字

```python

"""
    给定数字k 计算在0到n中出现的次数
"""
def func(k,n):
    count = 0
    for i in range(0,n+1):
        time = str(i).count(str(k))  # 把i转成字符串 对i调用k字符串
        count += time
    return count
print(func(1,11))
```



###### # 15.质数相加到合数

```python
""" 15.给定一个大于2的偶数，在所有满足“任意一个大于2的偶数可以由两
    个质数相加得到”这个特点的质数对中，找出两个质数差值最小的一对，
    并将差值输出（差值为大数减小数的值，两个质数相等时差值为0）。
    
    例如：偶数16，满足特点的质数对有(5，11)和(3，13)，差值最小的一
    对是(5，11)，11减5，差值为6。

    输入描述：输入一个大于2的偶数N
    输出描述：输出满足“任意一个大于2的偶数可以由两个质数
    相加得到”这个特点的所有质数对中，差值最小的那一对的差值
    
    样例输入：16
    样例输出：6
"""
num = int(input())

# 判断质数
def isPrime(n):
    for i in range(2,n//2+1):
        # 范围 从2开始 到n的一半
        if n % i == 0:
            return False
    return True

mid = num // 2
for a in range(mid,1,-1): # 从mid开始遍历 到第一个数据
    b = num - a
    if isPrime(a) and isPrime(b):
        print(b-a)
        break
```



###### # 65.2的幂

```python

"""
    给定非负整数n 请问是否存在一个x满足 2^x=n  有就返回true 没有就返回false
    
    2的幂在二进制中只有一位是1    
    4 -> 0100      8 -> 1000
    3 -> 0011      7 -> 0111
    
    根据按位与计算
    规律: 3和4 7和8的按位与运算都是0000
    
    n和n-1做按位与运算 如果结果为0000 我们就可以判断n是2的幂
"""
def func(n):
    return n > 0 and n & (n-1) == 0
print(func(32))
print(func(31))
```



###### # 25.落体反弹问题

```python

""" 一球从100米高度自由落下,每次落地后反跳回原高度一半再落下,
    求它在第10次落地时共经过多少米(一上一下算两次距离), 
    第十次反弹多高
"""
# 1.初始高度 之后每次除二
n = 100

# 2.反弹次数
count = 0

# 3.承载结果 一共经过多少米
list = []

# 4.计算
while count < 10:
    if count == 0:
        # 第一次 只下
        list.append(n)
        n /= 2
        count += 1
    else:
        # 之后的次数 以上以下*2
        list.append(2*n)
        n /= 2
        count += 1
print(list)
print(sum(list))   # 一共经过多少米
print(f'第10次反弹高度为:{n}')   # 第10次高度
```



###### # 49.快乐数

```python

"""
    给定一个正整数，请你判断这个数是不是快乐数。快乐数：对于一个正整数，每次把他替换为他每
    个位置上的数字的平方和，如果这个数能变为1则是快乐数，如果不可能变成1则不是快乐数。
    
    例如：正整数19
        转换过程为1*1+9*9=82，8*8+2*2=68，6*6+8*8=100，1*1+0*0+0*0=1，所以他是快乐数。
"""
def change(x):
    sum = 0
    while x > 0:
        j = x % 10
        sum += j*j
        x //= 10
    return sum   # 1.得到两位数各个平方和
# print(change(12))

def happy(n):
    while n > 9:  # 2.得到的平方和是两位数
        n = change(n)  # 3。就继续执行change函数 直到只剩下一位数
    if n == 1:   # 4.判断得到的一位数是否为1
        return True
    else:
        return False
print(happy(12))
```



###### # 3.连续整数寻找丢失的数

```python
""" 3.有一组连续正整数，随机乱序后生成一组数据后，小蓝不小心删掉了其中一个数，
    已知所删掉的这个数 不是这组数据中最小的也不是最大的，现在请你编写程序帮助
    小蓝找到删除的那个数。
    
    输入描述：按照“编程实现”中的描述模仿输入一组这样的正整数数（正整数之间以英
    文逗号隔开），在输入的时候少一个数（这个数不是这组数据中最小的也不是最大的），
    这个数作为小蓝删除掉的那个数，且加上小蓝删除 的那个数这组数据是连续的

    输出描述：输出删除掉的是哪个数
    样例输入：3, 2, 4, 6, 7
    样例输出：5
"""
list = input("连续整数丢了一个数").split(",")
for i in range(len(list)):
    list[i] = int(list[i])

list.sort() # sort从小到大

a = list[0]
b = list[-1] # 最后一个元素

for num in range(a,b+1):
    if num not in list:
        print(num)
        break
```



###### # 约瑟夫环 

```python
与28题逻辑相似 循环报数
""" 28.编程实现：N个小朋友围成一圈(N<=60)，并按照顺序进行编号(编号1到N)，然后从编号为1
    的小朋友开始持续报数，当报到的数字中含3或者数字是3的倍数的小朋友，不能报数字而是报“过”（
    例如，6，13，31这些数字都报“过”）。
    
    一次游戏中，小朋友们玩的不亦乐乎，突然有小朋友发现前边报过的数字中已经有报错的，而后边小
    朋友还在继续报数。请你帮助小朋友找出第一次报错的小朋友是编号几。
    
    例如：有3个小朋友，编号为1，2，3。编号1的小朋友报1、编号2的小朋友报2、编号3的小朋友报“过”、
    编号1的小朋友报4、编号2的小朋友报5、编号3的小朋友报6、编号1的小朋友报7；此时第一次报错的小
    朋友为编号3。（因为编号3的小朋友应该报“过”时，报成了“6”，而“6"是3的倍数）
    
    输入描述：
    第一行输入一个正整数N，表示小朋友的人数
    第二行输入一组有错的报数序列(“0"表示含3或者是3的倍数的数字)，序列元素之间以一个英文逗号隔开
    
    输出描述：
    输出第一次报错的小朋友是编号几
"""
n = int(input("输入n个小朋友"))
a = eval(input("输入报的数(字符串)"))
a = list(a)

c = 0
value = 0

for i in a:
    c += 1
    value += 1 # 报序号 1 2 3 4 5 6 不考虑"过"

    if c > n:
        c = 1 # 进行第二轮循环

    if (value % 3 == 0 or '3' in str(value)) and i != 0:
        # 如果value是3的倍数了 那么i应该是0 如果i != 0 那么就是报数错误了
        print(c) # 是应该"过"的数字
        break

    if i != value:
        print(c)
        break
```



### [前缀和]()



### [差分]()



### [双指针]()

###### # 75.合并排序数组

```python

"""
    合并数组A和B 要求合并后仍有序
    
    使用两个指针
    先取两个小的 按大小放入新数组
"""
def func(A,B):
    i,j = 0,0  # 准备两个指针
    c = []  # 存放结果数组

    # 进行第一次数值比较
    while i < len(A) and j < len(B):
        # 存放更小的数组  直到有一个数组比较完
        if A[i] < B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    # 将剩余的数组数值存放进结果
    while i < len(A):
        c.append(A[i])
        i += 1
    while j < len(B):
        c.append(B[j])
        j += 1
    return c
print(func([1,4,9],[2,3,11]))
```



###### # 63.数组重复数字

```python

"""
    [2,3,1,0,2,5,3] -> 2或3   如果没有输出-1
"""
def func(nums):
    for i in nums:
        if nums.count(i) >= 2:
            # 重复
            return i
    return -1
print(func([1,2,4,5,5]))
```



###### # 60.移动0

```python

"""
    给定一个数组，将所有0移动到数组末尾并且不改变其他数字的相对顺序
"""
def func(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)   # 先删除
            nums.append(0)   # 再添加
    return nums
print(func([0,1,3,0,4,5,0]))
```



###### # 71.目标移动

```python

"""
    给定一个数组nums和目标值target 将target元素移动到数组前面 其他元素相对顺序不变
    使用双指针 但都是从右向左的
"""
def func(nums,target):
    count = 0  # 计数器
    left = len(nums) - 1 # 最后一个索引
    right = len(nums) - 1  # 同上

    while left >= 0:
        if nums[left] != target:
            # left不是应删除并前移的元素 那么把left和right同时向前移一个位置 判断上一个元素
            nums[right] = nums[left]
            right -= 1
        else:
            # left == target 此时left为应删除元素 并添加到最前面
            count += 1
        left -= 1  # 前移
    for i in range(count):
        # 将所有的target判断元素都添加到前面
        nums[i] = target
list = [1,1,2,1,3,4]
target = 1
func(list,target)
print(list)
```



###### # 62.判断子序列

```python

"""
    给定两个字符串S、T 判断S是否为T的子序列  
    即是否可以从T中删除一些字符变成S
"""
def func(s,t):
    c = ''  # 空串用于存储结果
    n = 0   # 用于计数 表示下标

    if len(s) > len(t):
        return False

    for i in t:
        if n<len(s) and i == s[n]:  # s中的字母在t中存在 就加入c 表结果
            c += i
            n += 1   # 计数 直到n == s长度 停止循环
    if s == c:
        return True
    return False
print(func('hlo', 'hello'))
```



###### # 47.数组里没有出现过的数字

```python
"""
    给定一个长度为N的正整数数组nums，其中nums[i]的值都在区间[1，n]中，请你找出
    nums数组在[1，n]范围里面没有出现过的数字，并将它们放在数组里面返回（在数组里
    面的顺序可以不唯一）
"""
# 输入[2,1,4,5,1,2]
# 输出[3,6]

def func(nums):
    # 1.输入一个列表
    l = [i for i in range(1, len(nums) + 1)]   # nums+1  范围上取到1-nums
        # 列表生成式  i for i in range(,)

    # 2.准备一个结果列表 判断列表没有的数字 放到该列表中 最后输出该列表
    l2 = []

    # 3.删除重复的数字
    nums = set(nums)

    # 4.开始判断
    for o in l:
        if o in nums:  # 存在
            continue
        else:          # 不存在
            l2.append(o)

    return l2

list = [2,1,4,5,1,2]
print(func(list))
```



### [二分]()



### [贪心]()

###### # 54.三个数的最大乘积

```python

"""
    已知一个列表 中有很多数 要求得到这一堆数中 三个数的最大乘积
"""
def func(list):
    list.sort()  # 排序
    """ list.sort() 
        [min, ... ,max-1 , max]    
        list[0] < list[1] < list[2] ...
        
        list[0]最小 list[1]第二小 list[-1]最大  即两个负数 * 最大值
        list[-1]最大 list[-2]第二大 list[-3]第三大  即三个最大的正数相乘
    """
    return max(list[0]*list[1]*list[-1], list[-1]*list[-2]*list[-3]) # 找最大
print(func([1,2,3,4,5]))
```



###### # 76.插入5

```python

# 给定一个数字 在数字的任意位置插入5 使该数字最大
def func(a):
    string = ''  # 转换a为字符串
    ans = 0      #
    n = 0        # 字符串长度
    flag = False  # 旗帜 替换为5

    # a是正数
    if a >= 0:
        string = str(a)
        n = len(string)

        for i in range(n):
            # i为字符串索引
            if (ord(string[i]) - ord('0')) < 5 and flag == False:
                # ord ASCII码
                # 当前数字小于5且还没替换过5
                ans = ans * 10 + 5  # 结果乘10加5   ans=0+5=5  ans=5*10+5=55 ...
                flag = True
            ans = ans * 10 + ord(string[i]) - ord('0')
        if flag == False:
            ans = ans * 10 + 5

    # a是负数
    else:
        a = -a
        string = str(a)
        n = len(string)

        for i in range(n):
            if ord(string[i]) - ord('0') > 5 and flag == False:
                ans = ans * 10 + 5
                flag = True
            ans = ans * 10 + ord(string[i]) - ord('0')
        if flag == False:
            ans = ans * 10 + 5
        ans = -ans
    return ans
print(func(234))
```



###### 交换的最大值

```python
""" 给定一个正整数N(100<=N<=999) 交换三位数中的任意两位得到一个新的数字
    使得这个数字最大 并输出 如果都不大 输出原来的N

    样例输入 145
    输出 541

    一共三位数 全排列 输出最大的即可
"""
n = int(input())
a = n//100 # 百位数
b = n//10%10 # 十位数
c = n%10 # 个位数

n1 = b*100+a*10+c
n2 = b*100+c*10+a
n3 = a*100+c*10+b
n4 = c*100+b*10+a
n5 = c*100+a*10+b

res = max(n,n1,n2,n3,n4,n5)
print(res)
```



###### 剪绳子

```python
""" 有N(1<=N<=100)根绳子 已知每根绳子初始长度(1<=长度<=1000) 每根绳子都可以
    再任意位置剪断 请计算小明最多可以剪成多少根长度为K(1<=K<=200)的绳子 如果
    不能剪成长度为K的绳子 输出0

    例如 N=4 4根绳子初始长度为2 3 4 10 K=3 最多可以剪成5根长度为3的绳子
    第一根不能剪 0
    第二根不用剪 3 +1
    第三根剪一次 3 +1
    第四根剪三次 +3 一共5根

    第一行输入一个正整数N表示原有绳子个数
    第二行输入N个正整数表示各个绳子长度
    第三行输入一个正数K 表示需要剪到的长度

    输出一个整数 表示指定长度的绳子最后有多少根 如果都没有输出0

    样例输入 2 3 4 10
    输出 5
"""
N = int(input())
a = list(map(int,input().split()))
K = int(input())

res = 0
for s in a: # 遍历所有绳子
    res += s//K # 如果s能被K整除 就说明可剪成要求长度
print(res)


```



###### # 27.搭积木

```python
""" 27.编程实现：小蓝和小青在玩积木搭建游戏，具体玩法如下：
    小蓝报一个数字N，代表高楼的高度，小青则需要使用最少的积木搭建出高度大于N的高楼，
    给出小蓝所报出的数字N，及已有积木块每一块的高度，请你帮助小青找出最少需要多少块
    积木可以搭建出高度大于N的高楼，
    
    例如：N=12，已有4个积木块的高度分别为4.7.84
    则最少需要2块积木，可以使搭建的高楼高度大于12，2块积木为7和8。
    
    输入描述：
    第一行输入一个正整数N，表示小蓝报出的数字
    第二行输入多个正整数，表示已有积木块每一块的高度，正整数之间以一个英文逗号隔开。（要求所有正整数之和大于N）
    
    输出描述：
    输出最少需要使用多少块积木，可以搭建出高度大于N的高楼
"""
n = int(input("输入一个高度"))
blocks = list(map(int,input().split(','))) # 输入积木 列表 通过map映射操作把积木变成int类型
blocks.sort(reverse = True) # 降序排序

i = 0
res = 0
while n >= 0:
    n = n - blocks[i]
    i += 1
    res += 1
print(res) # 输出积木个数 计数器
```



###### # 72.柠檬水找零

```python

""" 在柠檬水摊上，每一杯柠檬水的售价为5美元。顾客排队购买你的产品，（按账单bills支付的顺序）一次购买一杯。
    每位顾客只买一杯柠檬水，然后向你付5美元、10美元或20美元。你必须给每个顾客正确找零，也就是说净交易是每
    位顾客向你支付5美元。注意，一开始你手头没有任何零钱。如果你能给每位顾客正确找零，返回true，否则返回 false。
    
    贪心算法
    1.第一位顾客支付五元
    2.第一位顾客支付十元 需要找零五元 
    3.第一位顾客支付二十元 需要找零十五元 -> 一张五元+一张十元(更优) 三张五元
    
    [5,5,5,10,20] 返回true
    [5,5,10,10,20] 返回false
"""
def func(bills):
    five = 0
    ten = 0

    for bill in bills:
        # 支付了五元
        if bill == 5:
            five += 1

        # 支付了十元
        elif bill == 10:
            # 无法找零
            if five == 0:
                return False
            # 可以找零
            five -= 1
            ten += 1

        # 支付了二十元
        else:
            # 可以找零
            if five > 0 and ten > 0:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            # 无法找零
            else:
                return False
    return True

print(func([5,5,5,10,20]))
print(func([5,5,10,10,20]))
```



###### 移动石子 难

```python
""" 将N(1<N<50)堆石子围成一个圆圈 已知每堆石子的数量 且石子总数可以被N整除
    请按照如下要求移动石子 使得N堆石子的数量变为相同

    要求 可以从每堆石子中拿去石子移动到它左右相邻的两队石子堆中

    计算要移动多少颗石子可以使每堆石子相同

    例如N=3 3堆石子顺时针方向的数量一次为2 6 7
    最少需要移动上颗石子 使每堆数量相同 每堆5颗

    把所有数字加在一起求平均值 确认相同堆数的数
"""
N = int(input())
stones = list(map(int,input().split()))

total = sum(stones)
average = total // N

d = [num - average for num in stones]
s = [0] * N
s[0] = d[0]
for i in range(1,N):
    s[i] = s[i-1] + d[i]

total_move = 0
for i in range(N):
    p = s[i-1] if i>0 else s[-1]
    total_move += abs(p)
print({total_move})
```



### [倍增]()



### [离散化]()



### [字符串匹配]()

###### # 77.字符串置换 

可以通过改变顺序使两个字符串相同

```python

def func(A,B):
    A = sorted(A)
    B = sorted(B)
    return A == B
print(func('abc','cba'))
```



###### # 56.判断字符是否唯一 

每个字符都不同

```python

def func(str):
    for i in range(1, len(str)):
        if str[i] in str[i+1:]:   # 从i+1取到最后
            return False    # 如果第i个元素 在i之后的所有元素中出现过 就不唯一
    return True
print(func('Hello'))
```





###### # 61.旋转字符串

```python

"""
    给定字符串A B，如果能将A从中间某个位置切割为左右两部分，
    且将左边字符串移动到右边字符串后面
    组成新字符串刚好等于B 返回True
"""
def func(a,b):
    # 首先判断a b长度是否相同 不相同就不用继续判断了
    if len(a) != len(b):
        return False

    else:
        # 直接写两个A拼在一起 如果满足条件 那么两个A拼在一起中一定有B
        bigA = a + a
        result = b in bigA
        return result
print(func('hello','llohe'))
```



###### # 48.替换空格

```python

# 将Hello World 变成 Hello%World
def func(s):
    # 已知一个字符串 准备一个新的空字符串 将每个字母依次判断

    res = ''  # 空
    for i in s:
        if i != ' ':   # 这个字母不是空格 直接输出字母
            res += i
        else:          # 这个字母是空格 变成%
            res += '%'
    return res
print(func('Hello World'))
```



###### # 70.字符删除

```python

"""
    给定两个字符串str、sub， 从str中完全删除在sub中存在的字符
    
    已知str删除指定字符
"""
def func(str,sub):
    s = set(sub)   # 将字符串转换为集合
    ans = ''
    for c in str:
        if c not in s:
            ans += c
    return ans

print(func('Thank you', 'you'))
```



###### # 45.第一个只出现一次的字符

```python

str = 'Hello World'   # 寻找该字符串中 只出现一次的字母

a = -1  # 旗帜

mp = dict()  # 存储结果

for i in str:
    if i in mp:
        mp[i] += 1  # 出现次数加1
    else:
        mp[i] = 1   # 只出现一次

for i in range(len(str)):
    if mp[str[i]] == 1:  # 只出现一次
        a = i
        break
print(a)
```



手机

###### # 17.字符串最长字串

```python
""" 17. 给定一个含有字母和数字的字符串，输出字符串中最长的数字子串的长度。
    如：字符串‘a2a22d’，最长的数字子串为22，长度为2，故输出2
    字符串‘lql2h567j765'，最长数字子串为567和765（长度都为3）故输出3
    
    输入描述：输入一个含有字母和数字的字符串(5<字符串长度<101)
    输出描述：输出此字符串中最长的数字子串的长度
    样例输入：a2a22d
    样例输出：2
"""
s = input()
b = ''  # 存储字符串结果
n = len(s)
for i in range(n):
    if '0' <= s[i] <= '9':
        b += s[i] # 拼接字符串
    else:
        b += ' '

b = b.split()
c = [] # 存储数字长度结果
for i in b:
    c.append(len(i))
print(max(c))
```



###### # 52.字符串变形

```python

"""
    1.有空格的单词换位置
    2.大写变小写 小写变大写
    
    Hello World 
         ⬇ 
    wORLD hELLO
"""
def func(s):
    # 1.输入了字符串 根据' '变成列表
    list = s.split(' ')

    # 2.反转
    list = list[::-1]

    # 3.s置为空
    s = ''

    # 4.向s中输出结果
    for i in list:
        i = i.swapcase()   # 5.大小写转换
        s += i
        s += ' '
    return s[0:len(s)-1]
print(func('Hello World'))
```



###### # 53.压缩字符串

```python

"""
    aabcccccaaa -> a2bc5a3
"""
def func(s):
    # 存储结果
    list = []

    for i in s:
        if not list or list[-2] != i:
            # 倒数第二个字母不是i(一个新的字母) 或者列表不存在
            list.append(i)  # 存字母
            list.append(1)  # 存字母出现次数
        else:
            # 和上一个字母是一样的 直接加1
            list[-1] += 1
    return ''.join(map(str, [x for x in list if x != 1]))
print(func('aabcccccaaa'))
```



### [分治]()

### 



​ 