T, M = map(int, input().split())  # 时间 数量
herbs = []
for i in range(M):
    ti, mi = map(int, input().split())
    herbs.append([ti, mi])

dp = [0] * (T + 1)
for ti, mi in herbs:
    for j in range(T, ti - 1, -1):
        dp[j] = max(dp[j], dp[j - ti] + mi)

print(dp[T])
