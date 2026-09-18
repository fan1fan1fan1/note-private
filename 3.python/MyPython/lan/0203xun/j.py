from collections import deque
import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))  # 0 1

    if n == 0:
        return

    blocks = []  # 存储多个队列

    current = arr[0]  # 第一个数  存的数据是0或1 水果种类
    q = deque([1])  # 第一个队列
    for i in range(1, n):  # 从第二个数开始判断 块
        if arr[i] == current:
            q.append(i + 1)  # 索引+1 = 水果编号
        else:
            blocks.append((current, q))  # 把上一个队列完整加入blocks   (水果种类,队列)
            current = arr[i]  # 变成当前的块
            q = deque([i + 1])  # 建立新队列
    blocks.append((current, q))  # 加入一个队列

    # 准备输出
    while blocks:
        # 输出每个篮子信息
        backet = []

        new_blocks = []  # 拿走后剩下的队列块  传递参数(水果种类,队列)

        for cur, q in blocks:  # 取每个块第一个水果
            if q:
                backet.append(q.popleft())

            if q:
                new_blocks.append((cur, q))

        # 如果拿走了剩余的最后的一种水果 会产生相邻块合并
        hebin = []
        for cur, q in new_blocks:
            if hebin and hebin[-1][0] == cur:
                hebin[-1] = (cur, hebin[-1][1] + q)
            else:
                hebin.append((cur, q))
        blocks = hebin
        backet.sort()
        print(' '.join(map(str, backet)))


main()