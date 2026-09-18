"""
n个闭区间 两个点 a b
求所有包含a且不包含b的区间

4 3   有4个区间 我要找3个区间
1 3   四个已知区间
2 5
3 7
4 8
1 5  我要在4个区间寻找的3个区间
2 9
5 1

4 3
1 3
2 5
3 7
4 8
1 5
2 9
5 1


区间包含a:  r>=a>=l
区间不包含b:  b>r  b<l

"""
n,q = map(int,input().split())  # 闭区间个数n   询问区间个数q
origin = []
for i in range(n):  # n个闭区间  [l,r]
    l,r = map(int, input().split())
    origin.append((l,r))

for i in range(q): # 询问的区间  [a,b] 我要找[a,b]在[l,r]里边的个数
    a,b = map(int, input().split())

    count = 0
    for l,r in origin:
        if((l<=a<=r) and (b>r or b<l)):
            count+=1
    print(count)



