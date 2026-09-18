import sys
sys.setrecursionlimit(1 << 25)

def main():
    piles = [[] for _ in range(14)]
    char_to_num = {
        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13
    }

    for i in range(1, 14):
        s = input().strip().split()
        for c in s:
            piles[i].append(char_to_num[c])

    face_up = [0] * 14

    def dfs(x):
        if x == 13:
            return
        if not piles[x]:
            return
        v = piles[x].pop()
        face_up[v] += 1
        dfs(v)

    for _ in range(4):
        if not piles[13]:
            break
        v = piles[13].pop()
        if v == 13:
            continue
        face_up[v] += 1
        dfs(v)

    ans = 0
    for i in range(1, 13):
        if face_up[i] == 4:
            ans += 1
    print(ans)

main()