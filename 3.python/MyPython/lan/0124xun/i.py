# 超时
# 读取总时间、草药数目
t_total, m_herb = map(int, input().split())
time = []
w = []
# 读取每种草药的时间和价值
for i in range(m_herb):
    ai, bi = map(int, input().split())
    time.append(ai)  # ai是采摘时间ti
    w.append(bi)     # bi是价值wi

# 初始化dp数组：f[j]表示j时间能获得的最大价值
f = [0] * (t_total + 1)

# 完全背包核心逻辑：遍历每个物品（草药）
for i in range(m_herb):
    ti = time[i]
    wi = w[i]  # 修正：wi未定义，改为取w[i]
    # 正序遍历时间（完全背包允许重复选，逆序是01背包）
    for j in range(ti, t_total + 1):
        # 状态转移：选该草药 或 不选，取最大值
        f[j] = max(f[j], f[j - ti] + wi)

# 输出总时间内的最大价值
print(f[t_total])



# 超时
t_total, m_herb = map(int, input().split())

# 过滤无效物品（时间>总时间的草药直接跳过）+ 存储物品
items = []
for _ in range(m_herb):
    ai, bi = map(int, input().split())
    if ai <= t_total and bi > 0:  # 跳过无价值/超时间的物品
        items.append((ai, bi))

f = [0] * (t_total + 1)
for ti, wi in items:
    for j in range(ti, t_total + 1):
        if f[j - ti] + wi > f[j]:
            f[j] = f[j - ti] + wi

print(f[t_total])