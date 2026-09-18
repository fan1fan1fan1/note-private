n, k = map(int, input().split())
ret = 0
path = 0

def dfs(pos, begin):
    global ret, path
    if pos == k:
        if path == n:
            ret += 1
        return
    # 可行性剪枝：如果当前路径 + 后续所有位置都填最小可能值仍超过 n，直接返回
    for i in range(begin, n + 1):
        if path + i * (k - pos) > n:
            break
        path += i
        dfs(pos + 1, i)
        path -= i

dfs(0, 1)
print(ret)