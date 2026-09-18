import os
import sys

"""
A-B
正整数序列
正整数C
A-B=C 的数对个数 可不同位置重复
"""
# 你原代码的输入部分（调整为一次性读入，符合竞赛要求）
N,C = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

# 补全：用哈希表统计数字出现次数（高效解法）
num_count = {}
for num in nums:
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1

# 补全：计算满足A-B=C的数对个数
count = 0
for b in num_count:
    a = b + C
    if a in num_count:
        count += num_count[b] * num_count[a]

# 补全：输出结果
print(count)


