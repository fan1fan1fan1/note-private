def main():
    n,m = map(int,input().split())
    left,right = 0,0
    kind = 0
    mp = [0]*(2010)
    begin = 0
    a = list(map(int,input().split()))
    ret = float('inf')
    while right<n:
        if mp[a[right]]==0:
            kind+=1
        mp[a[right]] += 1
        while kind == m:
            if right - left + 1 < ret:
                ret = right - left + 1
                begin = left
            mp[a[left]] -= 1
            if mp[a[left]]==0:
                kind-= 1
            left += 1
        right+=1
    print(begin+1,begin+ret)
main()