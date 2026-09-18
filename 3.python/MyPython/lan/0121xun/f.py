import itertools

t = int(input())
for i in range(t):
    n = int(input())
    planes = []
    for _ in range(n):
        T,D,L = map(int,input().split())
        planes.append((T,T+D,L))

    success = False
    for order in itertools.permutations(range(n)):
        current_time = 0
        possible =True
        for idx in order:
            T,latest_start,L = planes[idx]
            start = max(current_time,T)
            if start > latest_start:
                possible = False
                break
            current_time = start + L
        if possible:
            success = True
            break
    print("YES" if success else "NO")