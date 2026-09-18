def mul(a, b):
    ans = [0] * (len(a) + len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            ans[i+j] += int(a[i]) * int(b[j])
    for i in range(len(ans) - 1):
        ans[i + 1] += ans[i] // 10
        ans[i] %= 10
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return ''.join(str(x) for x in ans[::-1])


def main():
    a = input().strip()
    b = input().strip()
    a_s = list(a[::-1])
    b_s = list(b[::-1])
    if a_s == "0" or b_s == "0":
        print(0)
        return
    result = mul(a_s,b_s)
    print(result)


main()