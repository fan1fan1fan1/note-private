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


