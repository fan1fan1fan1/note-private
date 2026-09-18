class QueueNode:
    def __init__(self, val=0, next_node=None):
        self.val = val  # 每个小朋友
        self.next = next_node  # 小朋友后面的人


n = int(input())  # 总人数
num = list(map(int, input().split()))  # 编号
h = int(input())  # 第一个

head = h
result = []
while head!=0:
    result.append(str(head))
    head = num[head-1]
# print(result) 取消[]格式 此处需要强转 ' '中间空格1隔开
print(' '.join(result))

