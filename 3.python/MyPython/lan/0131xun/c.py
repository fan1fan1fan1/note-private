def main():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    diff = [0] * (n + 2)
    path = list(map(int, input().split()))

    x = path[0]
    for y in path[1:]:  # 遍历该行 除了第一个位置的所有y
        if x > y:
            diff[y] += 1
            diff[x] -= 1
        else:
            diff[x] += 1
            diff[y] -= 1
        x = y  # 更新x为当前y，继续下一段路径


    cnt = [0] * n
    for i in range(1, n):
        cnt[i] = cnt[i-1] + diff[i]

    total = 0
    for i in range(1, n):
        a, b, c = map(int, input().split())
        total += min(a * cnt[i], c + b * cnt[i])
    print(total)

main()