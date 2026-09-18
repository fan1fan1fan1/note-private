"""
一个资料  由小写字母组成
另一份资料 长度为8 密码 打乱隐藏在第一份资料

搜索密码在第一个文件中的位置 考虑排列可能性

aaaabbbbaabbcccc 第一个子串aaaabbbb
aaaabbbb
 aaabbbba
  aabbbbaa 三种

aaaabbbbaabbcccc 第二个子串 abcabccc -> aabbcccc
        aabbcccc 一种

"""
s = input()   # 第一份文件 所有的字符
n = int(input())  # 密码个数

# n行密码
str_list = [input() for i in range(n)]
count=0

# 在s中查找n 考虑排列组合
for i in range(len(s)-7):   # 为了让子串不越界
    sub = s[i:i+8]
    for j in str_list:
        if sorted(sub) == sorted(j):
            count+=1


print(count)





