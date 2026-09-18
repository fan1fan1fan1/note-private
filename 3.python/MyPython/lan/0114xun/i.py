import os
import sys
"""
N篇作业 生词出现
统计生词出现的位置

输入
n文章个数
n行 第一个是单词个数 后是文章 空格+小写字母
m询问次数
m行 一个生词

输出
生词 每行一个 统计出现的文章 从小到大输出文章序号
"""
data = sys.stdin.read().splitlines()
ptr = 0

n = int(data[0]) # 个数
ptr+=1

result = {}
for i in range(1,n+1):
    part = data[ptr].split() # 每行一篇短文 写过ptr的 此处不写i写ptr
    ptr += 1
    op = int(part[0]) # 单词个数

    words = part[1:]
    for w in words: # 遍历 去重
        if w not in result:
            result[w] = set() # 创建空集合 不重复 为了节约时间
            # 字典的value是单词集合
        result[w].add(i) # 篇章序号添加到字典中 输出

if ptr < len(data):
    # 剩下的数据都是m
    m = int(data[ptr])
    ptr += 1
    for i in range(m):
        if ptr < len(data):
            query = data[ptr].strip() # 要统计的生词
            ptr += 1
            if query in result: # 生词出现了 输出位置 文章序号
                print(' '.join(map(str,sorted(result[query]))))
            else:
                print() # 没有输出空格
