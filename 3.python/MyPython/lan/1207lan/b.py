""" 这题应该去重 需要去重 三个数直接相乘 一定会有重复的 必须写去重
n 三位数乘积   n=a.b.c
相差不超过2     a-b<=2 b-c<=2 c-a<=2

count = 0
for i in range(100):
    for j in range(100):
        for k in range(100):
            for m in range(10):
                if (m*j*k==i and j-k<=2 and k-j<=2 and k-m<=2 and m-k<=2 and m-j<=2 and j-m<=2):
                    count += 1
            if count==23:
                break
print(count)

n = 0
count = 0
for i in range(100):
    for j in range(100):
        for k in range(100):
            n = i*j*k
            if i-j<=2 and j-k<=2 and k-i<=2:
                count+=1
            if count==23:
                break
print(n)

valid = []
for i in range(1,100):
    for j in range(i,i+3):
        for k in range(j,j+3):
            n = i*j*k
            if n not in valid:
                valid.append(n)
valid.sort()
print(valid[22])
"""

valid = []
for i in range(1,101):
    for j in range(i,101):
        if j-i <= 2:
            for k in range(j,101):
                if k-j<=2:
                    n=i*j*k
                    if n not in valid:
                        valid.append(n)
valid.sort()
print(valid[22])



