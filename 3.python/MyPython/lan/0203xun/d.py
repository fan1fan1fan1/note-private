def main():
    piles = [[] for _ in range(14)]
    cnt = [0]*14
    char_to_num = {
        '0':0,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':1,'J':11,'Q':12,'K':13
    }
    for i in range(1, 14):
        chars = input().strip().replace(' ', '')
        for ch in chars:
            num = char_to_num[ch]
            piles[i].append(num)
        cnt[i] = 4

    # 持续翻牌直到生命牌堆（第13堆）为空
    current_pile = 13
    visited = set()
    while cnt[current_pile] > 0:
        if current_pile in visited:
            break  # 防止闭环
        visited.add(current_pile)
        # 从当前堆的最下面抽牌
        t = piles[current_pile].pop(0)
        cnt[current_pile] -= 1
        # 将牌放到对应编号堆的最上面
        piles[t].append(t)
        cnt[t] += 1
        current_pile = t

    # 统计1~12堆中被清空的数量
    ans = 0
    for i in range(1, 13):
        if cnt[i] == 0:
            ans += 1
    print(ans)

main()