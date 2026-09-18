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