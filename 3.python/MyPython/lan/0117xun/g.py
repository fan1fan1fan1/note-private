import os
import sys
"""
n
长度m
数字 大小写字母

求字符串个数
"""
data = sys.stdin.read().splitlines()
n = int(data[0])
l = []
for i in range(1,n+1):
    part = data[i].split()
    if part not in l:
        l.append(part)

print(len(l))


def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s_set = set()

    for line in data[1:n + 1]:
        s_set.add(line)

    print(len(s_set))


if __name__ == "__main__":
    main()