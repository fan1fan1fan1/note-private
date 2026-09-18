m, n = map(int, input().split())
groups = {}
for i in range(n):
    ai, bi, ci = map(int, input().split())
    # groups[ci] = [(ai, bi)]
    if ci not in groups:
        groups[ci] = []
    groups[ci].append((ai,bi))

# max_group = 0
max_group = max(groups.keys()) if groups else 0
f = [0] * (m + 1)
for i in range(1, max_group + 1):
    if i not in groups:
        continue
    for j in range(m, -1, -1):
        for (a, b) in groups[i]:
            if j >= a:
                f[j] = max(f[j], f[j - a] + b)

print(f[m])