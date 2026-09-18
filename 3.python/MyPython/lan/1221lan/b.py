"""
一个数组
找两个总和为特定值的索引
有负数
"""
n = int(input())
a = list(map(int,input().split()))
"""a=[]
for i in range(n):
    num = int(input())
    a.append(num)
    """
k = int(input())
for i in range(n):
    for j in range(n):
        if (a[i]+a[j] == k) and i<j:
            print(i,j)

