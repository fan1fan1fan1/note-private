def main():
    n = int(input())
    a = list(map(int,input().split()))
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i]+a[i]
    max_sum = -float('inf')
    min_prefix = 0
    for i in range(1,n+1):
        current = prefix[i] - min_prefix
        if current > max_sum:
            max_sum = current
        if prefix[i] < min_prefix:
            min_prefix = prefix[i]
    print(max_sum)
main()