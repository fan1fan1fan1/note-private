"""
商品 有编号和库存数量
最开始库存数量为0
编号1-n

m种类个操作 每个操作涉及一个商品区间 例如[商品L,商品R]
操作结果区间内商品库存增加1

判断最后有多少商品库存0
"""
n,m = map(int,input().split())  # n商品种类 m操作

a = []   # m操作具体数据
goods = []  # 库存数量
for i in range(n+1): # 初值0
    goods.append(0)

count = 0 # 库存0  需求输出结果

for i in range(m):
    L,R = map(int,input().split())  # 此处写map(int(input())) 错
    a.append((L,R))   # 对每一次 区间内的商品加1
    # 此处可以对商品库存数量进行更改 区间内的商品加1 用for循环加
    for j in range(L,R+1):
        goods[j] += 1

# for i in range(m): # 假设所有操作都执行的最终结果
for i in range(1,n+1):
    if goods[i] == 0:
        count += 1

# 接下来是 每一行的m具体操作不执行的结果
for i in range(m):
    x,y = a[i]
    temp = count
    for j in range(x,y+1):
        goods[j] -= 1
        if(goods[j] == 0):
            temp += 1
        goods[j]+=1  # 避免 别的m操作时 此处被更改过 但没改回来 之前的操作又执行了
    print(temp)

""" 此代码可用差分法简化
n,m = map(int,input().split())
cop = [] m操作

goods =[]
for i in range(n+1):
    goods.append(0)

for i in range(m):
    x,y = map(int,input().split())
    cop.append((x,y))
    for j in range(x,y+1):
        goods[j]+=1

res=0
for i in range(1,n+1): 假设所有操作都执行的最终结果
    if(goods[i]==0):
        res+=1

for i in range(m):
    x,y = cop[i]
    temp = res 赋值
    for j in range(x,y+1): 回退一下 看看
        goods[j]-=1
        if(goods[j]==0):
            temp+=1
        goods[j]+=1 #复原
    print(temp)
"""
