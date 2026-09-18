import os
import sys
# 导入bisect模块实现二分查找（新手友好，蓝桥杯允许使用）
import bisect

"""
统计营业情况
每天营业额
节假日 大减价 特殊情况
很高 很低 状况出现问题
最小波动值越大 情况越不稳定
每一天的最小波动值 加起来
最小波动值 前某一天的营业额-该天营业额
第一天的直接就是第一天
"""
n = int(input()) # 天数
a = [] # 每天的营业额
for i in range(n):
    ai = int(input())
    a.append(ai)

num = []  # 存储已遍历的营业额（保持有序）
total = 0  # 总最小波动值
# 补全：遍历每一天的营业额计算最小波动值
for i in range(n):
    current = a[i]
    if i == 0:
        # 第一天的最小波动值为自身绝对值
        total += abs(current)
        num.append(current)
    else:
        # 用bisect找当前数在有序列表中的插入位置
        pos = bisect.bisect_left(num, current)
        min_diff = float('inf')  # 初始化最小差值为无穷大
        # 检查左边相邻的数
        if pos > 0:
            min_diff = min(min_diff, abs(current - num[pos-1]))
        # 检查右边相邻的数
        if pos < len(num):
            min_diff = min(min_diff, abs(current - num[pos]))
        # 累加最小波动值
        total += min_diff
        # 将当前数插入有序列表，保持有序
        bisect.insort(num, current)

# 输出最终结果
print(total)