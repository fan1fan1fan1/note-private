"""
大于0 的浮点数d
转换参数n 浮点数*2^n 四舍五入到最近的整数
"""
import math
# n,d = input().split() 输入方式不正确 输成字符串了

a = input().split()
n = int(a[0])
d = float(a[1])
num = 2**n
f = float(num)
count = round(d * f)  # 四舍五入
print(count)




n, d = input().split()
n = int(n)
d1, d2 = d.split('.')  # 把小数 根据小数点切割 整数部分 小数部分
d1 = int(d1)

len_float = len(d2)  # 计算小数部分的长度 用于等会还原小数位
d2 = int(d2)

d2 = 2 ** n * d2 # 乘
d2_int = d2 // (10 ** len_float)  # 还原小数部分

x = d2 % 10 ** len_float // 10 ** (len_float - 1)

if x >= 5:
    d2_int = d2_int + 1

print(d1 * 2 ** n + d2_int)