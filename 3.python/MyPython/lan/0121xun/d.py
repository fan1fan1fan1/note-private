def dfs():
    if len(path)==n:
        print(' '.join(f"{x:5d}" for x in path))
        return
    for i in range(1,n+1):
        if visited[i]:
            continue

        path.append(i)
        visited[i] = True
        dfs()
        path.pop()
        visited[i] = False

n=int(input())
path = []
visited = [False] * (n+1)
dfs()
