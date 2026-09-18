def main():
    import sys
    input = sys.stdin.readline
    q = int(input())

    for i in range(q):
        l, r = map(int, input().split())
        total = 0
        for num in range(l,r+1):
            # 选择数字的范围
            total += (total +num)%9
        print(total)
main()