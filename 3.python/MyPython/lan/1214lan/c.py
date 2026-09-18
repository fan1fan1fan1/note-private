"""
一个整数的各个位 如果奇数位上是奇数 偶数位上是偶数 就是好数
1212121212

给定N 求1-N好数个数

N = int(input())
count = 0
for i in range(1,N+1):
    temp = i
    position = 1 # 标记 这是第几位 或者第几次
    while temp > 0:
        ji = temp % 10
        ou = temp // 10 % 10
        if ji % 2 != 0 and ou % 2 == 0:
            count += 1
        temp = temp // 10 # 此处写 / 错
print(count)
"""

N = int(input())
count = 0
for i in range(1,N+1):
    temp = i
    position = 1 # 标记 这是第几位 或者第几次
    while temp > 0:
        num = temp % 10
        if(position % 2 == 1 and num % 2 ==0) or (position % 2 == 0 and num % 2 !=0):
            break
        temp = temp // 10  # 此处写 / 错
        position += 1
    else:
        count+=1
print(count)


