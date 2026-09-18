def dfs():
    if len(path) == k:
        print(' '.join(map(str, path)))
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        path.append(i)
        visited[i] = True

        dfs()

        path.pop()
        visited[i] = False


n, k = map(int, input().split())
path = []
visited = [False] * (n+1)
dfs()
