""" 考双队列了 不会写

n*m矩阵
价值为 最大数*最小数

取子矩阵 大小为a*b   的价值和

和 % 998244353
"""
































n,m,a,b = map(int,input().split())

"""n行每行m个整数   a = list(map(int,input().split()))  ×
a = [list(map(int,input().split())) for i in range(n)] √
"""

a = []
for i in range(n):
    row = list(map(int,input().split))
    if len(row)!=m:
        continue
    a.append(row)

# 取小矩阵