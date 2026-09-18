""" 考链表了 不会写
长度为n数组
左移   移动到最左边
右移   移动到最右边
m次操作

双队列
"""
N,M = map(int,input().split())
dict = []   # 添加   "字母 数字"
for i in range(M):
    letter,num = input().split()
    dict.append((letter,num))

