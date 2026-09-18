def dfs(pos, n, path):
    # pos当前这个人 n总人数 path已经选的人数

    if pos > n:
        print(''.join(path))

    # 要出现所有种类情况 从N开始 枚举修改 然后出Y
    path.append('N')  # 赋值为N
    if pos <= n:
        dfs(pos + 1, n, path)  # 递归
    path.pop()

    path.append('Y')  # 赋值为Y
    if pos <= n:
        dfs(pos + 1, n,path)
    path.pop()


n = int(input())
dfs(1, n, [])

