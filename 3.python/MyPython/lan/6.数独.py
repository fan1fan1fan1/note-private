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
