s = input()
stack = []

num = ""   # 数据

for i in s:
    number=0
    if i.isdigit():
        num+=i # 拼接
    elif i == ".":
        stack.append(int(num)) # 是一个完整的数据 进栈
        num = "" # 重置
    elif i in "+-*/":
        right = stack.pop()
        left = stack.pop()
        if i == "+":
            number = right+left
        elif i == "-":
            number = left-right
        elif i == "*":
            number = right*left
        elif i == "/":
            # 向0取整
            if left*right>0: # 同号
                number = left // right
            else:
                number = int(left/right)
        stack.append(number)
    elif i == "@":
        break
print(stack.pop())