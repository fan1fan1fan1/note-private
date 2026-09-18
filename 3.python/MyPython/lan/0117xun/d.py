import os
import sys

"""
n
分数a
q 前m个 最差的分数   升序

qm 第一差       -> 队头
q     2 - m+1  -> 滑动窗口 
q n-m+1 - n    -> 滑动窗口

单调队列
"""
data = sys.stdin.read().splitlines()
first = data[0].split()
n = int(first[0])
m = int(first[1])
nums = list(map(int, data[1].split())) # 前边两个数据

q = []
res = []
for right in range(n):
    while q and nums[right] <= nums[q[-1]]:
        q.pop()
    q.append(right)

    while q[0] < right - m + 1:
        q.pop(0) # 左

    if right >= m - 1:
        res.append(str(nums[q[0]]))

print('\n'.join(res)) # 换行输出方式