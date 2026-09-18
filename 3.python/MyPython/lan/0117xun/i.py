import os
import sys
"""
n个 s串
询问q次
每次提供一个t串
t是s的前缀 个数
"""
class TrieNode:
    __slots__ = ['children','count'] # 优化内存
    def __init__(self):
        self.children = dict() # 字符串映射节点
        self.count = 0 # 经过该节点的字符串个数 pass

data = sys.stdin.read().splitlines()
ptr=0
T = int(data[0]) # 数据组数
ptr+=1
for i in range(T):
    n,q = map(int,data[ptr].split()) # 模式串个数 询问次数
    ptr+=1

    root = TrieNode() # 创建前缀树

    for j in range(n):
        s= data[ptr] # 具体模式串
        ptr+=1
        node = root
        for c in s:
            if c not in node.children: # 补前缀树
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count += 1

    output = []
    for j in range(q):
        t = data[ptr] # 文本串
        ptr+=1
        node = root
        found = True
        for c in t:
            if c not in node.children: # 没有
                found = False
                break
            node = node.children[c]
        if found: # 有
            output.append(str(node.count))
        else: # 没有
            output.append("0")
    sys.stdout.write('\n'.join(output) + '\n')