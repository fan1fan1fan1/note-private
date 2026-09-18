""" 已知有1 2 5面值的三种硬币 找出兑换7元、21元使用最少的硬币数

    已知目标数额 将每种情况计算出来 输出最少的数量

    7 -> 5 -> 2
      -> 5 -> 1 -> 1
      -> 2 -> 2 -> 2 -> 1
      -> 1
      ...
"""
coins = [1,2,5]
amount = 7
cnt = 0
ans = []

def find(m,sc):
    # m金额   sc交换硬币连接(1 2 1 2)
    global cnt

    if m<0:
        return
    elif m == 0:
        cnt += 1
        ans.append(sc)
        return

    for coin in coins:
        find(m-coin,str(coin) + ' ' + sc) # 递归

find(amount, '')
ans = [x.split() for x in ans]
res = [len(x) for x in ans]
# print(ans)
print(min(res))