#链表
#定义节点
class ListNode:
    def __init__(self,val=0,next_node=None):
        self.val = val
        self.next = next
#操作
class LinkedList:
    #初始化
    def __init__(self):
        self.head = None # 头结点

    # 添加插入 头插
    def add_head(self,val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    # 添加 尾插
    def append(self,val):
        new_node = ListNode(val)
        if not self.head: # 当前链不存在
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node # 插在最后

    # 查找
    def find(self,val):
        cur = self.head
        while cur:
            if cur.val == val:
                return cur
            cur = cur.next
        return None

    # 指定位置插入
    def insert(self,pos,val):
        if pos<0:
            return
        cur = self.head
        count = 0
        while cur and count < pos:
            cur = cur.next
            count += 1
        if not cur:
            return
        new_node = ListNode(val)
        new_node.next = cur.next
        cur.next = new_node

    #遍历
    def traverse(self):
        cur = self.head
        while cur:
            print(cur.val,end="")

    #删除
    def delete(self,val):
        dummy = ListNode(next_node=self.head) # 虚拟头节点(头节点的上一个位置) 可以涵盖删除头节点的情况
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next # 覆盖
                break
            cur = cur.next
        self.head = dummy.next

l = LinkedList()
l.append(1)
l.traverse()
l.delete(1)



# 链栈
# 定义节点
class StackNode:
    def __init__(self,val=0,next_node=None):
        self.val = val
        self.next = next_node
# 操作
class LinkedStack:
    # 初始化
    def __init__(self):
        self.top = None
    # 入栈 头插法
    def push(self,val):
        new_node = StackNode(val)
        new_node.next = self.top # 插在top前面 更换新的top
        self.top = new_node
    # 出栈 出top
    def pop(self):
        if self.is_empty():
            return None
        res = self.top.val
        self.top = self.top.val # 往下
        return res
    # 取栈顶
    def peek(self):
        if self.is_empty():
            return None
        return self.top.val
    # 判空
    def is_empty(self):
        return self.top is None

l_stack = LinkedStack()
l_stack.push(1)
print(l_stack.peek())
print(l_stack.pop())



# 链队
class QueueNode:
    def __init__(self,val=0,next_node=None):
        self.val = val
        self.next = next_node

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,val):
        new_node = QueueNode(val)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.is_empty():
            return None
        res = self.front.val
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return res
    def is_empty(self):
        return self.front is None

lq = LinkedQueue()
lq.enqueue(1)
print(lq.dequeue())
















