class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class LinkedList:
    #初始化
    def __init__(self):
        # self.head = None  头结点 当前题目设置为1
        self.head = ListNode(1)
        # 字典映射 通过在链中位置得到数据 类似指针
        self.map = {1:self.head}
    # 添加插入
    def append(self,x,y): # 形参
        x = self.map[x] # 得到x的位置
        y = ListNode(y)
        self.map[y.val] = y # y.val
        y.next = x.next # 插
        x.next = y
    #查找
    def query(self,x):
        x= self.map[x]
        if x.next is not None:
            return x.next.val
        else:
            return 0
    #删除
    def delete(self,x):
        x = self.map[x]
        if x.next:
            del_node = x.next
            del self.map[del_node.val]
            x.next = del_node.next


q = int(input())
List = LinkedList()
pacts = []
for i in range(q):
    num = list(map(int,input().split()))
    pacts.append(num)

move = {}
for pact in pacts:
    if pact[0] == 1:
        x = pact[1]
        y = pact[2]
        List.append(x,y)
    elif pact[0]==2:
        x = pact[1]
        print(List.query(x))
    else:
        x = pact[1]
        List.delete(x)