import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    line = list(map(int,data[1].split()))
    result = []
    for i in range(n, -1, -1):
        a = line[n-i]
        sign = ""
        if a == 0:
            continue
        if a < 0:
            sign = "-"
        elif i != n:
            sign = "+"
        num = abs(a)
        if num != 1 or (num == 1 and i == 0):
            result.append(sign + str(num))
        else:
            result.append(sign)
        if i != 0:
            if i == 1:
                result.append('x')
            else:
                result.append('x^' + str(i))
    print(''.join(result))


main()


