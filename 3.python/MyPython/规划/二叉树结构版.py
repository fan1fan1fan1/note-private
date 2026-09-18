# 二叉树节点
class TreeNode:
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None

#操作
result = []

#递归遍历 深度优先遍历
def pre_order(node):
    if node is not None:
        result.append(node.val) # 先根遍历
        pre_order(node.left)
        pre_order(node.right)

#非递归遍历
def pre_order_iter(node):
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current is not None:
            result.append(current.val)  # 先根遍历
            stack.append(current.right) # 顺序不能换
            stack.append(current.left)

# 按层遍历 广度优先遍历
from collections import deque
def level_order(node):
    res = []
    if node is None:
        print(res)
        return
    q = deque()
    q.append(node)
    while q:
        current = q.popleft()
        res.append(current.val)
        if current.left is not None:
            q.append(current.left)
        if current.right is not None:
            q.append(current.right)
    print(res)

# 求深度 递归
def depth(node):
    """
    if node is None:return 0
    left_depth = dfs(node.left)
    right_depth = dfs(node.right)
    return max(left_depth,right_depth)
    """
    if node is None: depth_num = 0
    else:
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        if left_depth > right_depth:
            depth_num = left_depth + 1
        else:
            depth_num = right_depth + 1
    return depth_num

# 求叶子节点个数 递归
leaf = 0
def count(node):
    global leaf
    if node is None:
        return
    if node.left is None and node.right is None:
        leaf+=1
    count(node.left)
    count(node.right)

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result.clear()

pre_order(root)
print("递归前序结果:", result)
# 测试2：非递归前序遍历
result.clear()
pre_order_iter(root)
print("非递归前序结果:", result)
# 测试3：按层遍历
print("按层遍历结果:", end=" ")
level_order(root)
# 测试4：求树的深度
tree_depth = depth(root)
print("树的深度:", tree_depth)
# 测试5：求叶子节点个数
count(root)
print("叶子节点个数:", leaf)






