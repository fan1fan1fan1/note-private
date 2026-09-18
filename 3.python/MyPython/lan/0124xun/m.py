n = int(input())
m = list(map(int,input().split()))

sum_arr = [0]*(n+1)
for i in range(1,n+1):
    sum_arr[i] = sum_arr[i-1]+m[i-1]

INF = float('inf')
dp = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][j] = 0
for length in range(2,n+1):
    for i in range(1,n-length+2):
        j = i + length -1
        total = sum_arr[j]-sum_arr[i-1]
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+total)

print(dp[1][n])