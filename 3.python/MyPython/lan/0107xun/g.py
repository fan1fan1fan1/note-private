def stack(pushed, popped):
    stack = [] # 空的进栈
    popped_copy = popped.copy() # 出栈
    for num in pushed:
         stack.append(num) # 依次进栈
         while stack and stack[-1] == popped_copy[0]: # 判是否可以出栈 如果不可以就继续进栈
             stack.pop()
             popped_copy.pop(0)
    return len(popped_copy) == 0 # 最后能够全部出栈就可以匹配

q = int(input()) # 询问次数
for i in range(q):
    n = int(input()) # 序列长度
    pushed = list(map(int,input().split()))
    popped = list(map(int,input().split()))
    if stack(pushed, popped):
        print("Yes")
    else:
        print("No")