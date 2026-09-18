import os
import sys
n = int(input())
a,b,c = 1,1,2
for i in range(3,n+1):
    t = a+b+c
    a = b
    b = c
    c = t

if n == 1:
    print(b)
else:
    print(c)