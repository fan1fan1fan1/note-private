import sys
def main():
    sys.setrecursionlimit(1 << 25)
    piles = [[] for _ in range(14)]
    cnt = [0]*14
    char_to_num = {
        '0':10,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':1,'J':11,'Q':12,'K':13
    }
    for i in range(1,14):
        chars = input().strip().replace(' ', '')
        for ch in chars:
            num = char_to_num[ch]
            piles[i].append(num)
        cnt[i]=4
    def dfs(x):
        if x==13:
            return
        t = piles[x].pop()
        cnt[x]-=1
        piles[t].append(t)
        cnt[t]+=1
        dfs(t)
    for card in piles[13]:
        dfs(card)
    ans = 0
    for i in range(1,13):
        if cnt[i]==0:
            ans+=1
    print(ans)
main()