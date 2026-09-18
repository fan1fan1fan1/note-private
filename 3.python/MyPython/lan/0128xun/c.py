def isdigit(ch):
    return '0' <= ch <='9'
def islower(ch):
    return 'a' <= ch <= 'z'
def add(left,right,p1,p2,p3):
    t = []
    for ascii_code in range(ord(left)+1,ord(right)):
        tmp = chr(ascii_code)
        if p1 == 2 and islower(tmp):
            tmp=tmp.upper()
        elif p1 == 3:
            tmp = '*'
        t.append(tmp*p2)
    t = ''.join(t)
    if p3==2:
        t = t[::-1]
    return t
def main():
    p1,p2,p3 = map(int,input().split())
    s = input().strip()
    n = len(s)
    result = []
    for i in range(n):
        ch = s[i]
        if ch != '-' or i in (0,n-1):
            result.append(ch)
        else:
            left,right = s[i-1],s[i+1]
            if((isdigit(left) and isdigit(right)) or (islower(left) and islower(right))) and right>left:
                result.append(add(left,right,p1,p2,p3))
            else:
                result.append(ch)
    print(''.join(result))

main()