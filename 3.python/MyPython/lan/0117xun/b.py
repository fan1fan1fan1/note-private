import os
import sys

"""
n一排
每个都有不同的h
向左右发射能量v
左右 近 大
"""
data = sys.stdin.read().splitlines()
n = int(data[0])  # 数据个数

# 本题数据适合字典 字典内存大 l = {}
height = []
value = []

for i in range(1, n + 1):
    part = data[i].split()
    h = int(part[0])
    v = int(part[1])
    # l[i] = (h,v)
    height.append(h)
    value.append(v)

left = [-1] * n  # 左 小-1
right = [n] * n  # 右 大n

stack = []  # 单调递增栈 高度高
# 求左边界
for i in range(n):
    while stack and height[i] >= height[stack[-1]]:
        stack.pop()  # 出栈 结算
    if stack:
        left[i] = stack[-1]  # 替代栈顶
    stack.append(i)  # 让栈顶出栈的就是左近大
# 求右边界
stack = []
for i in range(n - 1, -1, -1):  # 倒序
    while stack and height[i] >= height[stack[-1]]:
        stack.pop()  # 出栈 结算
    if stack:
        right[i] = stack[-1]  # 代替栈顶
    stack.append(i)  # 让栈顶出栈的就是右近大

# 得到了数据 计算个数
res = [0] * n
# 通过栈 出栈 在左右列表中的每个i存了 左右 近 大
for i in range(n):
    if left[i] != -1: # 只要左右列表i处有数据 就可以+=1
        res[left[i]] += value[i]
    if right[i] != n:
        res[right[i]] += value[i]
print(max(res))