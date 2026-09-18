""" 考二分查找了 不会写
基德 三重石
二分查找
总数中取三个数 最小的为价值

输出第k小

N个石头 每个上有数字Ai
取3块 其中数字最小的为力量

查询
数字K 第k小的数
"""

N,Q = map(int,input().split())  # N石头数量 Q查询次数
A = list(map(int, input().split())) # 石头
""" 这个写的不对 写分行了
A = [] # 石头数字 石头
for i in range(N):
    num = int(input())
    A.append(num)
"""

K = [] # 查询
for i in range(Q):
    num = int(input())
    K.append(num)




""" 要查询第k小的结果 首先所谓第几小 需要三重石最小值的结果集合 1三次 2一次
    样例中4块石头 每次取3块 得到最小值 
    如果石头很多 就不能直接排列了 需要整理 
    
    升序 任意位置左侧的数都小于等于它，右侧的数都大于等于它
"""
A.sort()
# 分好类后可以得到每个的最小值的组合




sm = [] # 每一个sm[i]表示以这个数为最小值的排列个数 1三次 2一次 sm是Num的总数
Num = 0  # 以某一个元素为最小 能排出的三重石个数

# 从数组中选3个不同的数，令A[i]是这三个数的最小值（i位置右侧至少有2个数 比A[i]大）
# A[i] A[i+1] A[i+2] 一定是A[i]最小 取这个值
for i in range(N - 2):  # i最大为N-3，才能保证右侧有2个元素
    n = N - 1 - i # 以A[i]为最小 右边数的个数
    cnt = n * (n - 1) // 2  # 右边一共有n个数 选2个的组合数个数
    Num += cnt
    sm.append(Num)


# 输出第k小
for k in K:
    pos = 0
    # 遍历sm，找到第一个 >=k 的位置
    while pos < len(sm) and sm[pos] < k:
        pos += 1
    print(A[pos])

