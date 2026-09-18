import os
import sys
import heapq

"""
n个函数 每个函数都是 Ax^2+Bx+C
给定A B C
求m个最小结果 重复都输出
"""
data = sys.stdin.read().splitlines()
# 取第一行
first_line = data[0].split()
n = int(first_line[0]) # n个函数 次数
m = int(first_line[1]) # m个结果

func = [] # 具体函数
min_heap = [] # 全部结果

for i in range(1,n+1):
    part = data[i].split()
    A = int(part[0])
    B = int(part[1])
    C = int(part[2])

    func.append((A,B,C)) # 此处传A,B,C 要用括号括起来 一个append只能传一个数据
    # x是正整数 求最小值 先得到1 之后再依次比较 减少循环空间浪费
    result = A*1*1+B*1+C
    heapq.heappush(min_heap,(result,i-1,1)) # i-1为该结果位置 1为x取值

Result = [] # 结果 取前m个 就是m个最小
for i in range(m):
    result,fun,x = heapq.heappop(min_heap) # 取堆中最小
    Result.append(str(result)) # 加入Result
    next_x = x+1 # x取1未必是最小值 继续计算
    A,B,C = func[fun] # 再计算得到的要放在该函数的最小值位置
    new_result = A*next_x*next_x+B*next_x+C
    heapq.heappush(min_heap,(new_result,fun,next_x))

print(' '.join(Result))