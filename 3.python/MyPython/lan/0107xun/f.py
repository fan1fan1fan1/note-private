class SeqStack:
    # 初始化
    def __init__ (self):
        self.stack = []
        # 判空
    def is_empty(self):
        return len(self.stack) == 0
    # 入栈
    def push(self,val):
        self.stack.append(val)
    # 出栈
    def pop(self):
        if self.is_empty():
            print("Empty")
        else:
            self.stack.pop()
    # 取栈顶
    def query(self):
        if self.is_empty():
            print("Anguei!")
        else:
            print(self.stack[-1]) # 取倒序最后一个
    #求长
    def size(self):
        print(len(self.stack))

n = int(input()) # 执行次数
for i in range(n):
    num = int(input()) # 每组操作次数
    stack = SeqStack()
    for j in range(num):
        op = input().split() # 具体操作
        one = op[0]
        if op[0] == "push":
            x = int(op[1])
            stack.push(x)
        elif op[0] == "pop":
            stack.pop()
        elif op[0]=="query":
            stack.query()
        else:
            stack.size()