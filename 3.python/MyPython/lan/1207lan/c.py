"""
2025 1-2025号
3、8 、38的倍数 红包

count=0
for i in range(1,2026):
    if i % 3 != 0:
        if i % 8 !=0:
            if i % 38 != 0:
                continue
    count+= 1
# python中短路特性 导致遗漏统计同时是 3 8 38中两个以上倍数关系的数
print(count)
"""
count = 0
for i in range(1,2026):
    if i%3==0 or i%8==0 or i%38==0:
        count+=1
print(count)