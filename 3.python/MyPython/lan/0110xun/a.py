n = int(input())
# 用字典 键值对 节点 左右孩子 tree = []
tree = {}
root = None  # 根节点

for i in range(n):
    num = input().strip()  # 字符串读入
    node = num[0]

    if len(num) > 1:
        left = num[1]
    else:
        left = '*'
    if len(num) > 2:
        right = num[2]
    else:
        right = '*'

    tree[node] = (left, right)  # 键值对 {node : (left,right)}
    if i == 0:
        root = node
result = []


def pre_order(node):
    if node == '*':
        return
    result.append(node)
    pre_order(tree[node][0])
    pre_order(tree[node][1])


pre_order(root)
print("".join(result), end="")