"""
1-202504(202505)
各个位 之和 是5倍数

num=0
count = 0
for i in range(1,202505):
    while i / 10 !=0:
        num += i % 10
        i = i / 10
    if num % 5 == 0:
        count+=1
print(count)

"""


count = 0
for i in range(1,202505):
    num = 0  # 此处num放在循环外边会错
    temp = i
    while temp !=0:
        num += temp % 10
        temp = temp // 10  # 此处写/会错
    if num % 5 == 0:
        count+=1
print(count)