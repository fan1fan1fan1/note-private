"""存钱
利息0.005%   0.005*0.01
当天的总金额  原金额+利息 是下一天的本金
余额0.01单位 用double python不强调

小于0.01的不计入

给定M天 求每天的最后金额
最开始0

M = int(input()) # 天数
balance = 0.0 # 初始钱

A = []
for i in range(M):
    Ai = float(input())  # python处理浮点数 就是float 没有double
    balance += Ai
    interest = balance * 0.000005
    if interest >= 0.01:
        balance += interest
        # 如果题目有关于小数 print输出 print(f"{变量:.位数f}")
print(f"{0:.2f}".format(balance))

"""

M = int(input()) # 天数
balance = 0.0 # 初始钱
pre_balance = 0.0
for i in range(M):
    Ai = float(input())
    balance = pre_balance + Ai

    interest = pre_balance * 0.00005
    # 答案是800.53 我的输出是800.54 此处有一个精度错误
    interest = int(interest*100)/100
    if interest >= 0.01:
        balance += interest

    pre_balance = balance
    # print(f"{0:.2f}".format(balance))
    print(f"{balance:.2f}")






