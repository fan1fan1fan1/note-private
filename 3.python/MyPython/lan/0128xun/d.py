def main():
    a = input().strip()
    b = input().strip()
    a = list(map(int,a[::-1]))
    b = list(map(int,b[::-1]))
    ans = []
    carry = 0
    i = 0
    while i<max(len(a),len(b)) or carry:
        sum_num = carry
        if i < len(a):sum_num += a[i]
        if i < len(b):sum_num += b[i]
        ans.append(sum_num % 10)
        carry = sum_num // 10
        i+=1
    print(''.join(map(str,ans[::-1])))
main()