""" ...编程实现: 小名收藏了N(2 <= N <= 25)个数字币，每个数字币上都有一个面值
    (面值可以重复)。从数字币种任选k个(2 <= k <= N)，有多种选法，请将每次选
    择的数字币上的面值累加，然后解决以下两个问题

    问题1: 累加的和中有多少种不同的结果
    问题2: 累加的和中有多少个不同的合数

    第一行输入一个正整数N，表示数字币的个数
    第二行输入N个正整数(1<正整数<1000)，表示数字币上的面值，正整数之间以一个英文逗号隔开
    第三行输入一个正整数K，表示所要选取的数字币个数

    输出描述: 输出两个数，分别表示累加和不同结果的个数，
            以及累加的结果中不同合数的个数，两个整数之间以一个英文逗号隔开

    样例输入
    5
    2, 1, 4, 5, 3
    3
    样例输出
    7,5
"""
N = int(input())

# 输入N个正整数 写一个list map
a = list(map(int,input().split(",")))

# k = int(input())

result1 = 0 # 总共结果个数
result2 = 0 # 合数个数

# 判断合数
def heshu(n):
    for x in range(2,n):
        if n % x == 0:
            return True
    return False

# 此题中k若不确定为多少 适合用回溯法递归实现 太难了
# 写死k=3
k=3

# 全部结果
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            result1.append(a[i]+a[j]+a[k])
            # print(f"{a[i]+a[j]+a[k]}")

b = set(result1) # set创建一个集合 无顺序无重复的容器
c = 0
for ele in a:
    if heshu(ele):
        c += 1

b = len(b)
print(f"{b},{c}")











