import os
import sys
import array
"""
n
f(1...n)
fi表示第i个元素之后 第一个大于它的下标 右近大
若不存在返回0

超内存限制了
把res改成数组 使用 array
"""
n = int(input())
a = list(map(int,input().split()))

res = array.array("i",[0])*n
#res = [0]*n # 不存在返回0
stack = []
for i in range(n):
    while stack and a[i] > a[stack[-1]]: # 单调递增栈
        idx = stack.pop() # 出栈
        res[idx] = i+1 # 题目要求输出下标 让栈顶出栈的就是右近大
    stack.append(i)

# 题目要求输出f(1...n)
print(' '.join(map(str,res))) # 输出错误 str