import os
import sys

""" 进入教室
    按进教室顺序给出
    第i个学号是多少
"""

n,m=map(int,input().split()) # 人数 询问次数
nums = list(map(int,input().split()))
targets = list(map(int,input().split()))
"""
nums = [] # 总学号
for i in range(n):
    num=int(input())
    nums.append(num)

targets = [] # 被询问的顺序号
for i in range(m):
    target=int(input())
    targets.append(target)
"""
# 输出m个学号
for i in targets:
    print(nums[i-1])

