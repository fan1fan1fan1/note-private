"""
每一数码和   f(114)=1+1+4
有多少个N位正整数x   满足f(x)=a+b+c
count % 998244353
"""
N,M = map(int,input().split()) # f(N)=M
count = 0
"""
while N>0:
    a = N % 10
    num += a
    N = N / 10

if M==num:
    count += 1
"""
for i in range(10**(N-1),10**N):
    # 比如3位数 N=3   第一个数100->10^(N-1)  最后一个数999->10^N-1 索引范围不包含 10^N
    digit_sum = 0   # 求每一位和
    temp = i # 当前的这个N位数
    while temp>0:
        digit_sum += temp % 10  # 加
        temp = temp // 10 # 去掉最后一位
    if digit_sum == M:
        count += 1

ans = count % 998244353
print(ans)

