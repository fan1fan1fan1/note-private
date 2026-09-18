# 超时一个
def dfs(pos,begin):
    global res
    global path

    if pos>k: # 结束了 开始清算
        flag = True
        if path<2: # 不是素数
            flag = False
        else:
            for i in range(2,int(path**0.5)+1):
                if path % i == 0: # 不是素数
                    flag = False
                    break
        if flag: # 是素数
            res += 1
        return

    for i in range(begin,n): # 递归循环 回溯
        path += nums[i]
        dfs(pos+1,i+1)
        path -= nums[i]

n,k = map(int,input().split())
nums = list(map(int,input().split()))

path = 0
res = 0 # 素数个数

dfs(1,0)
print(res)

# 通过
import itertools

def is_prime(x):
    """判断一个数是否为素数"""
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# 输入处理
n, k = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
# 生成所有选k个数的组合
for combo in itertools.combinations(nums, k):
    s = sum(combo)
    if is_prime(s):
        count += 1

print(count)