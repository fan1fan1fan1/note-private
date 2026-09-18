import os
import sys

"""
a数据长度 n
窗口大小k
求最大值 最小值
"""
data = sys.stdin.read().splitlines()
first = data[0].split()
n = int(first[0])
k = int(first[1])
nums = data[1].split()


def min_num(nums, k):
    queue = []
    res = []
    for right in range(len(nums)):
        while queue and nums[right] <= nums[queue[-1]]:
            queue.pop()
        queue.append(right)

        left = right - k + 1
        while queue[0] < left:
            queue.pop(0)  # 左

        if right >= k - 1:
            res.append(nums[queue[0]])
    return res


def max_num(nums, k):
    queue = []
    res = []
    for right in range(len(nums)):
        while queue and nums[right] >= nums[queue[-1]]:
            queue.pop()

        queue.append(right)

        left = right - k + 1
        while queue[0] < left:
            queue.pop(0)  # 左

        if right >= k - 1:
            res.append(nums[queue[0]])
    return res


print(' '.join(min_num(nums, k)))
print(' '.join(max_num(nums, k)))