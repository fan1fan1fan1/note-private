def main():
    max_size = 5001
    n,R = map(int,input().split())  # n个目标 范围边长R
    grid = [[0] * (max_size + 1) for _ in range(max_size + 1)]
    for _ in range(n):
        i,j,v = map(int,input().split())
        i+=1
        j+=1
        grid[i][j] += v # 写+号
    prefix = [[0] * (max_size + 1) for _ in range(max_size + 1)]
    for i in range(1, max_size + 1):
        for j in range(1, max_size + 1):
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + grid[i][j]
    R = min(R, max_size)
    max_value = 0
    for x2 in range(R, max_size + 1):
        for y2 in range(R, max_size + 1):
            x1 = x2 - R + 1
            y1 = y2 - R + 1
            current = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
            if current > max_value:
                max_value = current
    print(max_value)


main()


def main():
    n, R = map(int, input().split())
    points = []
    max_i = max_j = 0
    # 1. 先存所有点，记录最大坐标（缩小范围核心）
    for _ in range(n):
        i, j, v = map(int, input().split())
        i += 1  # 偏移防越界
        j += 1
        points.append((i, j, v))
        max_i = max(max_i, i)
        max_j = max(max_j, j)

    # 2. 缩小网格大小，只到有效最大坐标+R（避免越界）
    size_x = max_i + R
    size_y = max_j + R
    grid = [[0] * (size_y + 1) for _ in range(size_x + 1)]
    for i, j, v in points:
        grid[i][j] += v

    # 3. 二维前缀和（仅遍历有效范围）
    for i in range(1, size_x + 1):
        row_sum = 0
        for j in range(1, size_y + 1):
            row_sum += grid[i][j]
            grid[i][j] = grid[i - 1][j] + row_sum  # 原地前缀和，省空间

    max_val = 0
    R = min(R, size_x, size_y)
    # 4. 枚举右下角，仅遍历有效范围
    end_x = min(max_i, size_x)
    end_y = min(max_j, size_y)
    for x2 in range(R, end_x + 1):
        for y2 in range(R, end_y + 1):
            x1 = x2 - R + 1
            y1 = y2 - R + 1
            # 前缀和公式（grid已变成前缀和数组）
            cur = grid[x2][y2] - grid[x1 - 1][y2] - grid[x2][y1 - 1] + grid[x1 - 1][y1 - 1]
            if cur > max_val:
                max_val = cur
    print(max_val)


main()
