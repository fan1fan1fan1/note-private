# bisect.insort
# remove
# abs

import os
import sys
import bisect

"""
仓库
不等长木材 不能有相同长度的
可进可出 
进货 长度Length 如果有相同的输出Already Exist
出货 取出长度Length 没有 取出最接近的 如果多 就取短的 如果空Empty

二分查找
"""
data = sys.stdin.read().splitlines()
m = int(data[0])  # 次数
cang = []
for i in range(1, m + 1):
    part = data[i].split()
    op = int(part[0])
    Length = int(part[1]) # sys取的数只要是数字要转整数

    if op == 1:
        if Length in cang:
            print("Already Exist")
        else:
            # 二分查找 保证有序  测试中输出3 按照顺序放入的
            bisect.insort(cang, Length)
    elif op == 2:
        result=0
        if not cang:
            print("Empty")
            continue

        # 找接近 二分查找
        # idx是当前长度应该在的最左位置 在数组中索引为idx-1
        # 如果这个数据存在 idx就是要找的
        # 如果不存在 idx就是比我待找数据大一点的数据
        idx = bisect.bisect_left(cang,Length) # 容器 数据
        candition = []
        if idx > 0:
            # 待插入位置不是第一个数据 防止索引越界
            candition.append(cang[idx - 1])  # 小于待插数据的最大数据 左
        if idx < len(cang):
            # 待插入位置不是最后一个数据 防止索引越界
            candition.append(cang[idx])  # 大于待插数据的最小数据 右

        if not candition:
            # 只要不是第一和最后 就有数据
            print("Empty")
        else:
            # 先比较最接近的 如果同时左右一样接近选左
            if len(candition) == 1:
                result = candition[0]
            else:
                left = candition[0]
                right = candition[1]

                # dist_left = abs(left-Length) 绝对值
                # dist_right = abs(right-Length)
                dist_left = Length - left
                dist_right = right - Length

                if dist_left > dist_right:
                    result = right
                else:
                    result = left
        print(result)
        cang.remove(result)
