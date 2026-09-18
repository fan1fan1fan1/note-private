def div(a,b):
    result = []
    remainder = 0
    for i in range(len(a)):
        remainder = remainder*10 + int(a[i])
        quatient = remainder // b
        result.append(quatient)
        remainder %= b
    while len(result)>1 and result[0]==0:
        result.pop(0)

    return result

def main():
    a = input().strip()
    b = input().strip()
    a_s = list(a[::-1])
    b_s = list(b[::-1])
    if a_s == "0" or b_s == "0":
        print(0)
        return
    result = div(a_s,b_s)
    print(result)


main()