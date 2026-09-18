def main():
    carpets = []
    n = int(input())
    for i in range(n):
        line = map(int, input().split())
        carpets.append(line)
    x, y = map(int, input().split())

    result = -1
    for carpet in carpets[::-1]:
        if carpet[0] <= x <= carpet[2] and carpet[1] <= y <= carpet[3]:
            result = carpet[4]
            break

    print(result)


main()