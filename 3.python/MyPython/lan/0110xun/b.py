import sys
lines = sys.stdin.read().splitlines() # 全部读入
n = int(lines[0])

# 两个列表 分别存储读入的l、r
left = [0]*(n+1)
right = [0]*(n+1)
for i in range(1,n+1): # 此处循环条件必须写1，n+1
    l,r = map(int,lines[i].split())
    left[i] = l
    right[i] = r


# 前序遍历
def pre_order():
    res = []
    stack=[1] # 使用栈存储遍历结果 1为根节点
    while stack:
        node = stack.pop()
        if node == 0: # 叶子
            continue
        # 非叶子
        res.append((str(node)))
        stack.append(right[node]) # 栈先进后出 反着写
        stack.append(left[node])
    return ' '.join(res)

# 中序遍历
def in_order():
    res = []
    stack=[]
    cur = 1 # 根节点 开始
    while cur!= 0 or stack: # 当前节点非空 栈存在
        while cur != 0: # 不是叶子
            stack.append(cur) # 进栈
            cur = left[cur] # 往左访问
        cur = stack.pop() # 访问到最左了 放到答案里
        res.append(str(cur))
        cur = right[cur] # 此时栈里左和中都输出了 访问右
    return ' '.join(res)

# 后序遍历
def post_order():
    res = []
    stack = [(1,False)] # 根节点入栈 标记false
    while stack:
        node,visited = stack.pop() # 栈顶
        if node == 0: # 叶子
            continue
        if visited: # 左右都访问了 标记true 输出
            res.append(str(node))
        else:
            # 非叶子 未访问
            stack.append((node,True))  # 进栈 标记
            stack.append((right[node],False)) # 右
            stack.append((left[node],False)) #左
    return ' '.join(res)  # join 前面是. 点

print(pre_order())
print(in_order())
print(post_order())