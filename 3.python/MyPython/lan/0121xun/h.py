n, w = map(int, input().split())
c = [int(input()) for _ in range(n)]
c.sort(reverse=True)  # 剪枝1：先放重的小猫，减少分支

res = n  # 初始最坏情况：每只猫一个缆车
cnt = 0  # 当前已用缆车数量
s = [0] * n  # 每个缆车的当前总重量


def dfs(pos):
    global res, cnt
    if cnt >= res:
        return  # 剪枝2：当前用的缆车数已经超过已知最优解，直接返回
    if pos == n:
        res = cnt  # 所有猫都放好了，更新最优解
        return

    # 先尝试放到已有的缆车里
    for i in range(cnt):
        if s[i] + c[pos] <= w:
            s[i] += c[pos]
            dfs(pos + 1)
            s[i] -= c[pos]  # 回溯

    # 如果没找到合适的，新开一个缆车
    s[cnt] = c[pos]
    cnt += 1
    dfs(pos + 1)
    cnt -= 1  # 回溯
    s[cnt] = 0


dfs(0)
print(res)