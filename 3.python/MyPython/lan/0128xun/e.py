def cmp(x,y):
    if len(x) != len(y):
        return len(x) < len(y)
    return x<y

def sub(a,b):
    ans = []
    carry = 0
    i = 0
    while i<len(a) or i < len(b):
        num1 = int(a[i]) if i < len(a) else 0
        num2 = int(b[i]) if i < len(b) else 0
        sum_num = num1-num2-carry
        if sum_num < 0:
            sum_num+=10
            carry = 1
        else:
            carry = 0
        ans.append(sum_num)
        i+=1
    while len(ans) > 1 and ans[-1]==0:
        ans.pop()
    return ans

def main():
    x = input().strip()
    y = input().strip()
    if cmp(x,y):
        print('-',end="")
        x,y = y,x
    a = list(x[::-1])
    b = list(y[::-1])
    result = sub(a,b)
    print(''.join(map(str,result[::-1])))

main()