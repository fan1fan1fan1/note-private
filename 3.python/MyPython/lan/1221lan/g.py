""" 考门电路了 考深搜了 不会写
1 0 1 0 1

最后是1   10个门电路 可为1的组合方式
"""

# 数字
arr = [[0] * i for i in range(5,0,-1)]
arr[0] = [1,0,1,0,1]

ops = [0] * 10
count = 0

# 通过起始数据和门 计算下一组数据
# 门计算
def oper(op,a,b):
    # op为门 a b为门左右上方数据
    if op == 0:
        return a & b # 与门
    elif op == 1:
        return a | b # 或门
    else:
        return a ^ b # 异或门

# 得到下一组数据
def add():
    op = 0
    for i in range(1,5):
        for j in range(5-i):  # 门的个数
            arr[i][j] = oper(ops[op], arr[i-1][j],arr[i-1][j+1])
            op += 1

"""
此处遍历所有的门持续计算 要么写深度优先搜索 要么写枚举笛卡尔积
                           dfs      from itertools.product
                           
此处需要遍历 也就是穷举10个门的所有可能的排列组合 验证是否最后输出i 如果不能再回溯试探别的
而dfs刚好满足这种需要
"""

# 试探每一个门 验证最后输出是否为1 如果不是回溯到上一个 如果是递归下一个
def dfs(k):
    global count  # 函数(def)要修改结果值 需要global
    if k >= 10: # 递归终止条件 即结束深搜条件 所有门都遍历完了
        add() # 计算输出
        if arr[4][0] == 1: # 如果输出结果为1 则可以记录
            count += 1
        return  # 回到上一个门 假设现在是dfs(10)  回到dfs(9)

    for i in range(3): # 当前门不是最后一个 依次试探 与 或 与或门
        ops[k] = i
        dfs(k + 1)  # 递归


dfs(0)
print(count)