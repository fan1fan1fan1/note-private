import sys
import math


def gong(x, y):
    if x==0 and y==0:
        return 0
    if x==0:
        return y
    if y==0:
        return x
    return (x * y) // math.gcd(x, y)


def main():
    t = int(input())
    for _ in range(t):
        maxx = 0
        current = 0
        n = int(input())
        for i in range(1,n+1):
            for j in range(1,n+1):
                current = gong(i, j)
                if current > maxx:
                    maxx = current
        print(maxx)


main()