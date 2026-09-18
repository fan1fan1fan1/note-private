def main():
    N =15
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    n = int(input())
    arr = [[0]*N for _ in range(N)]
    x,y = 1,1
    cnt = 1
    pos = 0
    while cnt <=n*n:
        arr[x-1][y-1] = cnt
        a = x+dx[pos]
        b = y+dy[pos]
        if a <1 or a>n or b<1 or b>n or arr[a-1][b-1]:
            pos = (pos+1)%4
            a = x+dx[pos]
            b = y +dy[pos]
        x,a = a,x # x拿到目标值 a被覆盖无用 把下一个a，b给x，y
        y,b = b,y
        cnt+=1
    for i in range(n):
        line = []
        for j in range(n):
            #print('{f:>3}'.format(arr[i][j],end=""))
            line.append(f"{arr[i][j]:>3}")
        print(''.join(line))
main()