n = int(input())
a = [0]+list(map(int,input().split()))

f = [0]*(n+1)

ret = 0
for i in range(1,n+1):
    f[i] = 1
    for j in range(1,i):
        if a[j]<a[i]:
            f[i] = max(f[i],f[j]+1)
    ret = max(ret,f[i])
print(ret)