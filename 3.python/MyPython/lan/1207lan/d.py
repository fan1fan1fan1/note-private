"""
长度为n的字符串s
q次操作
给定整数 l r k    :    将s的第l个字符到第r个字符 循环右移 k次
求结果

a右移1次 b   两次c。。。。。

字符串 其中l-r的字符 全部右移k个位置 执行Q次


N,Q = map(int,input().split())
S = input()
lst = []
test = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(Q):
    l,r,k = map(int,input().split())
    lst.append([l,r,k])

    sub = S[l:r]
    # 26字母表数组 执行右移
"""
from shlex import join

alphasbet = list('abcdefghijklmnopqrstuvwxyz')
N,Q = map(int,input().split())
S = list(input())

diff = [0]*(N+2) # 记录右移次数
for i in range(Q):  # 差分数组
    l, r, k = map(int, input().split())
    diff[l-1] += k  # l-1为第一个右移的字符  从这个字符开始 每个字符的右移次数加k diff数组记录这个次数

    # 但是现在加多了
    diff[r] -= k   # 从第r个字符开始 后边的字符都不加 所以把后边算上的字符都减掉

move = 0
# 现在已经记录好了需要右移的字符 移动的次数
for i in range(N):
    move += diff[i]  # 避免遗漏某一字符的某次右移 每个字符的右移都是move
    movelast = move % 26    # 循环右移 只右移在0-25个位置区间
    origin = alphasbet.index(S[i])
    new = (origin + movelast) % 26
    S[i] = alphasbet[new]
print(''.join(S)) # 取消[''] -> join    取消空格 -> ''.


