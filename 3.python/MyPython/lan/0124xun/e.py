n,m,a,b = map(int,input().split())
f = [[0]*(n+2) for _ in range(m+2)]
f[0][0] = 1

def check(i,j):
    return (i==a and j==b) or (i != a and j != b and abs(i-a)+abs(j-b)==3)

for i in range(1,n+1):
    for j in range(1,m+1):
        if check(i,j):
            continue
        #f[i][j] = f[i-1][j] + f[i][i-1]
        f[i][j] = f[i-1][j] + f[i][j-1]

print(f[n][m])

