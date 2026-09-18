#二叉排序树
#节点
class BSTNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

#排序树
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.search_result = None # 结果

    def insert(self,val): # 插入
        if self.root is None:
            self.root = BSTNode(val)
            return

        current = self.root # 中间循环代替变量
        while True:
            if val<current.val:
                if current.left is None:
                    current.left = BSTNode(val)
                    break
                current = current.left # 替代
            else:
                if current.right is None:
                    current.right = BSTNode(val)
                    break
                current = current.right # 替代

    def search(self,val): # 查找
        self.search_result = None
        current = self.root
        while current:
            if current.val == val:
                self.search_result = current
                break
            elif val < current.val:
                current = current.left
            else:
                current = current.right

    def delete(self,val): # 删除
        parent = None
        current = self.root
        while current and current.val != val:
            parent = current
            if val < current.val:
                current = current .left
            else:
                current = current.right

        if current is None:
            return
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        elif not current.right:
            if not parent:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right =current.left

        elif not current.left:
            if not parent:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right

#测试BST
bst = BinarySearchTree()
for num in [5,3,7,2,4,6,8]:
 bst.insert(num)
print("查找7：", bst.search(7).val if bst.search(7) else "未找到")  # 7
bst.delete(3)
print("删除3后查找：", bst.search(3))  # None


# 排序查找
# 1.基础排序
arr = [1,3,2]
arr.sort()
arr.sort(reverse= True)

new_arr = sorted(arr)


# 冒泡排序
def maopao(list):
    for i in range(len(list)):   # 此处范围可以写len  也可以写len - 1
        for j in range(len(list) - i - 1):  # 冒泡排序比较次数 n-1
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

list = [1,5,4,2,3]
print(maopao(list))


# 选择排序
def xuanze(list):
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[min_index],list[i] = list[i],list[min_index]
    return list
list = [5,2,3,89,1]
print(xuanze(list))


# 插入排序
"""
    两列列表 一列是已排元素 一列是待排元素
    默认第一个是已排元素 将第二个与其对比 大的在后面 
    然后让下一个待排元素与这个新排出来的比较 大的在后面
"""
def charu(list):
    for i in range(1, len(list)):
        j = i - 1  # 已排最后一个元素

        key = list[i]  # 待排

        while j >= 0:
            # j >= 0 还不是最后一个元素

            if list[j] > key:
                list[j+1] = list[j]   # 将j向后移一个位置 原j的位置赋值给key
                list[j] = key
            j -= 1  # j指向新的待排元素 越来越少
    return list

list = [5,78,2,3,12]
print(charu(list))


# 快速排序
def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick(left)+[pivot]+quick(right)


# 归并排序
def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge(arr[:mid])
    right = merge(arr[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res += left[i:]
    res += left[j:]
    return res
