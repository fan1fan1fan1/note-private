MOD = 10**6 + 7

n,m = map(int,input().split())
a=list(map(int,input().split()))

f = [0]*(m+1)
f[0]=1

for i in range(1,n+1):
    for j in range(m,-1,-1):
        max_k = min(a[i-1],j) # i-1 索引越界异常
        for k in range(1,max_k+1):
            f[j] = (f[j]+f[j-k]) % MOD

print(f[m] % MOD)
