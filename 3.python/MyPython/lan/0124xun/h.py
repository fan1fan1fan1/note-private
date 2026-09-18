n,m = map(int,input().split())
a = list(map(int,input().split()))

def count_order():
    dp = [0]*(m+1)
    dp[0]=1
    for price in a:
        for j in range(m,price-1,-1):
            dp[j] += dp[j-price]
    print(dp[m])

count_order()