import os
import sys
"""
dna 26小写字母
判相同

把字符串转换成整数(哈希值) 再进行比较

基数base
十进制以10为基数 进位 乘以进位数等于位

c0*base^(n-1)  .... cn*base^1

如果每一个字符的哈希值都这样计算 计算量非常大 我们可以使用前缀哈希数组
这样处于后面的字符就可以直接使用前面字符的哈希结果 + ci的值

但数字本身仍然非常大
我们取一个mod 取模 每个结果除以模数 再进行最终比较 
"""
# 一次性读取所有数据，按空格拆分，避免行分割开销
data = sys.stdin.read().split()
s = data[0]
n=len(s)
m = int(data[1])

# 字符串哈希前置准备
base = 911382629 # 哈希的基数(进制数) 选择大质数减少哈希冲突
mod = 10 ** 18 + 3 # 模数 极大的数 接近2^60 减少冲突
prefix_hash = [0] * (n + 1) # 前缀哈希数组 其中每个i表示前i个字符的哈希值 下标从1开始
power = [1] * (n + 1) # 基数的幂次数组 base^i % mod
for i in range(n):
    prefix_hash[i + 1] = (prefix_hash[i] * base + ord(s[i])) % mod
    # 递推公式 前i个字符的哈希值*基数 + 当前字符的ascii 取模

    power[i + 1] = (power[i] * base) % mod
    # 计算base的i+1次幂取模 为后序准备

output = []
for i in range(2, m + 2): # 前边两行
    part = data[i].split()
    l1 = int(part[0])
    r1 = int(part[1])
    l2 = int(part[2])
    r2 = int(part[3])

    if (r1 - l1) != (r2 - l2):  # 长度不同
        output.append("No")
        continue

    # 计算子串哈希
    # 利用前缀哈希计算任意子串的哈希值
    # 子串s[l->r]哈希值 = (前缀哈希[r]-前缀哈希[l-1]*base^(r-l+1)) % mod
    hash1 = (prefix_hash[r1] - prefix_hash[l1 - 1] * power[r1 - l1 + 1]) % mod
    hash2 = (prefix_hash[r2] - prefix_hash[l2 - 1] * power[r2 - l2 + 1]) % mod

    if hash1 == hash2:
        output.append("Yes")
    else:
        output.append("No")

#print('\n'.join(output))
# 一次性输出所有结果，最小化IO次数
sys.stdout.write('\n'.join(output) + '\n')