def main():
    piles = [[] for _ in range(14)]
    cnt = [0]*14
    char_to_num = {
        '0':0,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':1,'J':11,'Q':12,'K':13
    }
    for i in range(1, 14):
        # 直接生成不含空格的字符列表
        chars = input().strip().replace(' ', '')
        for ch in chars:
            num = char_to_num[ch]
            piles[i].append(num)
        cnt[i] = 4

    # 迭代版翻牌，避免递归深度问题
    current_pile = 13  # 从生命牌堆（第13堆）开始
    while True:
        if cnt[current_pile] == 0:
            break
        # 从当前堆翻出最下面一张牌
        t = piles[current_pile].pop(0)
        cnt[current_pile] -= 1
        # 检查目标堆是否为空
        if cnt[t] == 0:
            break
        # 目标堆不为空，放牌并继续翻牌
        piles[t].append(t)  # 这里是对的，放的是翻出的牌的数字
        cnt[t] += 1
        current_pile = t  # 下一次从目标堆翻牌
    ans = 0
    for i in range(1, 13):
        if cnt[i] == 0:
            ans += 1
    print(ans)


main()