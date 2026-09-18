def dfs(a,b,x,y,k):
    if k<1:
        return
    half = 2**(k-1)
    if x<a+half and y < b+half:
        print(a+half, b+half,1)
        dfs(a,b,x,y,k-1)
        dfs(a,b+half,a+half-1,b+half,k-1)
        dfs(a+half,b,a+half,b+half-1,k-1)
        dfs(a+half,b+half,a+half,b+half,k-1)
    elif x>=a+half and y >= b+half:
        print(a+half, b+half-1,4)
        dfs(a,b,a+half-1,b+half-1,k-1)
        dfs(a,b+half,a+half-1,b+half,k-1)
        dfs(a+half,b,a+half,b+half-1,k-1)
        dfs(a+half,b+half,x,y,k-1)
    elif x>=a+half:
        print(a+half-1, b+half,3)
        dfs(a,b,a+half-1,b+half-1,k-1)
        dfs(a,b+half,a+half-1,b+half,k-1)
        dfs(a+half,b,x,y,k-1)
        dfs(a+half,b+half,a+half,b+half,k-1)
    else:
        print(a+half, b+half-1,2)
        dfs(a,b,a+half-1,b+half-1,k-1)
        dfs(a,b+half,x,y,k-1)
        dfs(a+half,b,a+half,b+half-1,k-1)
        dfs(a+half,b+half,a+half,b+half,k-1)
def main():
    k = int(input())
    x,y = map(int,input().split())
    dfs(1,1,x,y,k)
main()