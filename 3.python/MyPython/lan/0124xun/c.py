MOD = 100003
n,k = map(int,input().split())
f=[0]*(n+1)
f[0]=1
for i in range(1,n+1):
    for j in range(1,k+1):
        if i-j >=0:
            f[i]=(f[i]+f[i-j]) % MOD
print(f[n])