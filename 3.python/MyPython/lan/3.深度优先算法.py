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


























