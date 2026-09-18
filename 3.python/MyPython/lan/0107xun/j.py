import os
import sys

from collections import deque
class SeqQueue:
    # 初始化
    def __init__(self):
        self.queue = deque()
    # 进队
    def enqueue(self,val):
        self.queue.append(val)
    # 出队
    def dequeue(self):
        if self.is_empty():
            print("ERR_CANNOT_POP")
            return # 此处必须return 空队列 终止操作 不然会执行下一行
        self.queue.popleft()
    # 取队头
    def query(self):
        if self.is_empty():
            print("ERR_CANNOT_QUERY")
        else:
            print(self.queue[0])
    # 判空
    def is_empty(self):
        return len(self.queue) == 0
    #求长
    def size(self):
        print(len(self.queue))

n = int(input())
q = SeqQueue()
for i in range(n):
    pact = list(map(int,input().split()))
    if pact[0]==1:
        x=pact[1]
        q.enqueue(x)
    elif pact[0]==2:
        q.dequeue()
    elif pact[0]==3:
        q.query()
    else:
        q.size()