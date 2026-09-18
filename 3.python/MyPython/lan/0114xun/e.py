import os
import sys

"""
M个单词
高级词汇 N个  单词名称A 长度L 含金量B
"""
data = sys.stdin.read().splitlines()
first_line = data[0].split()
n = int(first_line[0])  # 高级词汇n个
p = int(first_line[1])  # 模数

# 本题对高级词汇信息 使用字典处理
word = {}

for i in range(1, n + 1):
    part = data[i].split()
    a = part[0]  # 该高级词汇 长度L？
    b = int(part[1])  # 含金量

    word[a] = b

# 剩余行是作文正文 有标点符号 , . ! ?

# for i in range(n+1,m+1+n):
essay_line = data[n + 1:]  # 切成一行一行的
essay = ' '.join(essay_line)  # join取消空格分割 就不是一行一行的

separators = {',', '.', '!', '?', ' '}
words = []  # 出现单词
current_word = ''

# 一个字符一个字符遍历剩下内容 如果是字符先添加暂时答案
# 字符遍历到结果 再结算当前单词 加入集合 之后再判断高级词汇和含金量
for char in essay:
    if char not in separators:
        # 不是字符 是单词
        current_word += char
    else:
        if current_word:
            # 避免空 也就是有单词 到当前位置是标点符号 可以结算单词了
            words.append(current_word)
            # 清空
            current_word = ''

if current_word:
    # 如果读取最后剩下一个单词 单独清算
    words.append(current_word)

# 清算含金量
result = 0
for w in words:
    if w in word:
        result += word[w]

# 得到result取模
Result = result % p
print(Result)


