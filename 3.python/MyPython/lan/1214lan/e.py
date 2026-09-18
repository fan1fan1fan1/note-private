"""
N个石头 每个上有数字Ai
取3块 其中数字最小的为力量

查询
数字K 第k小的数
"""
from bisect import *
N,Q = map(int,input().split())  # N石头数量 Q查询次数
A = list(map(int, input().split())) # 石头数字 石头
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

""" 我要查询第k小的结果 
    首先所谓第几小 是相对与三重石的结果
    结果可以得到 假设一共4块石头 排列组合
    如果石头很多 就不能直接排列了 需要整理 升序
"""
A.sort()
"""
分好类之后可以得到三重石
此处导入一个包 执行二分查找
"""
sm = [] # 三重石
Num = 0  # 组合数 避免超时 快速统计 然后使用二分查找

# 循环核心作用是排序后 计算每个位置作为最小值 右边可取的数
for t in range(N-1,0,-1):
    Num += t*(t-1)//2 # 固定公式 “选t个石头 能形成的三元组合数”
    sm.append(Num)

#执行二分查找
for k in K:
    pos = bisect_left(sm,k)
    print(A[pos])







