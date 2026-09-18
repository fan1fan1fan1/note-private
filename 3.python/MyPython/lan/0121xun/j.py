from collections import deque
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
n,m,x,y = map(int,input().split())
dist = [[-1 for _ in range(m)] for _ in range(n)]

def bfs():
    global dist,n,m
    q=deque()
    q.append((x-1,y-1))
    dist[x-1][y-1] = 0
    while q:
        i,j = q.popleft()
        for k in range(8):
            new_x,new_y = i+dx[k],j+dy[k]
            if 0<=new_x<n and 0<= new_y < m and dist[new_x][new_y] == -1:
                dist[new_x][new_y] = dist[i][j]+1
                q.append((new_x,new_y))


bfs()
#print(dist)
for row in dist:
    print(' '.join(map(str,row)))