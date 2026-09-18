""" 背包问题
    指定一组物品 在背包容量有限的前提下 选择一些物品放入背包中 使得背包价值最大

    若干商品 每个商品有对应的重量和价值 我们可以取或不取

    优化：中间结果记忆 存储中间结果 减少递归次数

    重量(kg) 1 2 4 2 5
    价值($)  5 3 5 3 2
    五件商品 用yes no标记取或不取

    使用递归方法解决背包问题 首指针指向最后一个元素
    1.初始
    首指针    n=5
    背包容量  c=10  重量和
    总价值初始 v=0

    2.将首指针元素放入背包后   或者   首指针元素没有放进背包中
    n=4                           n=4
    c=10-5=5                      c=10
    v = 2                         v=0
    3.   ...
    4. n=1  递归结束
"""

# 输入数据默认第一个位是0
w = [0,1,2,4,2,5]
v = [0,5,3,5,3,2]
result = 0

def ks1(n,C):
    if n==0 or C==0:
        # 结束
        result = 0
    elif w[n] > C:
        # 商品总重量大于背包容量 放不下
        result = ks1(n-1,C) # 这一件商品忽略掉 不要了
    else:
        tmp1 = ks(n-1,C)  # 不放本次商品
        tmp2 = v[n] + ks(n-1, C-w[n])  # 放了本次的商品 并进入下一次商品判断
        result = max(tmp1,tmp2)
    return result
# 时间复杂度 O(2^n)

n=5
res = ks1(n,10)
print(res)  # 16 最大的价值



print("-----------")



w = [0]; v = [0]
for x in range(n):
    w1, v1 = list(map(int, input().split(',')))
    w.append(w1)
    v.append(v1)


def ks(n,C):
    # 打印数据结果 效果:打印了步骤中的结果
    if memo[n][C] != 0:
        for row in memo:
            print(row)
        print()
        return memo[n][C]   # 取出结果

    # 添加数据结果
    if n==0 or C == 0:
        result = 0
    elif w[n] > C:
        result = ks(n-1,C)
    else:
        tmp1 = ks(n - 1, C)  # 不放本次商品
        tmp2 = v[n] + ks(n - 1, C - w[n])  # 放了本次的商品 并进入下一次商品判断
        result = max(tmp1, tmp2)
    memo[n][C] = result  # 存结果
    return result



# 初始化  n = 5; C = 10
n,C = list(map(int,input().split(',')))

# 创建一个二维列表 n+1行 C+1列
memo = [[0]*(C+1) for x in range(n+1)]  # 数据结果存储在列表中
res = ks(n,C)
print(res)





