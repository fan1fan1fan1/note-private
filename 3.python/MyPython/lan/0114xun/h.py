import os
import sys

"""
去重
"""
data = sys.stdin.read().splitlines()

ptr = 0
t = int(data[ptr])
ptr += 1
for i in range(t):  # 有ptr可以直接写t
    n = int(data[ptr])
    ptr += 1

    nums = data[ptr].split()
    ptr += 1
    seem = set()
    result = []

    for num in nums:
        if num not in seem:
            seem.add(num)
            result.append(num)
    print(' '.join(result))
