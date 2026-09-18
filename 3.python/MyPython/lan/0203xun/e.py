from functools import cmp_to_key
def cmp(x,y):
    if x+y > y+x:
        return -1
    elif x+y < y+x:
        return 1
    else:
        return 0
def main():
    n = int(input())
    nums = list(map(int,input().split()))
    nums = list(map(str,nums)) # 类型转换
    nums.sort(key=cmp_to_key(cmp))
    print( ''.join(nums).lstrip('0'))
main()
