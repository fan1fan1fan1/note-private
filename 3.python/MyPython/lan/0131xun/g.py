"""
import sys
import bisect

每位同学推荐学校
差值最小 可上可下
差值为不满意度
求所有不满意度最小值

def main():
    data = sys.stdin.read().splitlines()
    first = data[0].split()
    ptr = 1
    m = int(first[0]) # 学校数 学生数
    n = int(first[1])
    a = list(map(int,data[ptr:ptr+m])) # ai学校预计分数线
    ptr += 1
    b = list(map(int,data[ptr:ptr+n])) # bi学生预估成绩
    ptr+=1

    global_min = float('inf')  # 全局最小不满意度
    for score in b:
        pos = bisect.bisect_left(a, score)
        curr_min = float('inf')
        # 检查右侧分数线
        if pos < m:
            curr_min = abs(a[pos] - score)
        # 检查左侧分数线
        if pos > 0:
            curr_min = min(curr_min, abs(a[pos-1] - score))
        # 更新全局最小值
        if curr_min < global_min:
            global_min = curr_min
    print(global_min)

    min_count = float('inf')
    for i in range(n):
        for j in range(m):
            count = abs(A[i]-B[j])
            if count < min_count:
                min_count = count
    print(min_count)
"""

"""
main()
"""

import sys
import bisect


def main():
    # 快速读取输入（竞赛中处理大数据的最优方式）
    data = sys.stdin.read().split()
    idx = 0
    m = int(data[idx])  # 学校数量
    idx += 1
    n = int(data[idx])  # 学生数量
    idx += 1

    # 读取学校分数线并排序（二分查找的前提）
    scores_school = list(map(int, data[idx:idx + m]))
    scores_school.sort()
    idx += m

    # 读取学生估分
    scores_student = list(map(int, data[idx:idx + n]))

    total = 0  # 存储所有学生的最小不满意度之和
    for score in scores_student:
        # 二分查找找到score在排序后数组中的插入位置
        pos = bisect.bisect_left(scores_school, score)
        min_diff = float('inf')  # 初始化当前学生的最小差值

        # 检查插入位置的元素（右边的数）
        if pos < m:
            min_diff = abs(scores_school[pos] - score)
        # 检查插入位置前一个元素（左边的数）
        if pos > 0:
            min_diff = min(min_diff, abs(scores_school[pos - 1] - score))

        # 累加当前学生的最小不满意度
        total += min_diff

    # 输出最终的最小不满意度之和
    print(total)


# 竞赛中可直接写main()，也可以用规范写法，两者都能AC
if __name__ == "__main__":
    main()