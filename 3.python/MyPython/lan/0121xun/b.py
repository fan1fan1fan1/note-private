# 超时两个点
def dfs(begin):
    if len(path)==m:
        print(' '.join(map(str,path))) # 报错 字符串类型

    for i in range(begin,n+1):
        path.append(i)
        dfs(i+1)
        path.pop()

n,m = map(int,input().split())
path = []
dfs(1)

# 超时一个点
def dfs(begin):
    if len(path)==m:
        #print(' '.join(map(str,path))) # 报错 字符串类型
        res.append(' '.join(map(str,path)))
        return

    for i in range(begin,n+1):
        path.append(i)
        dfs(i+1)
        path.pop()

n,m = map(int,input().split())
path = []
res = [] # 超时了 加个res
dfs(1)
print('\n'.join(res))

# 通过
import itertools # 快速生成序列

n, m = map(int, input().split())
for combo in itertools.combinations(range(1, n+1), m): # 总数中选出k个
    print(' '.join(map(str, combo)))