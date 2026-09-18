In = input().strip()
post = input().strip()

def pre(In,post):
    # 递归终止条件
    if not In or not post:
        return ""
    root = post[-1] #根节点 为 后序 最后一个节点
    index = In.index(root) # 在中序找根节点

    # 拆分左右子树 递归 [起点:终点]
    left_in = In[:index] # 对中序 左中右 左子树 起点->index 右子树 index->终点
    right_in = In[index+1:]
    left_post = post[:index] # 对后序 左右中 左子树 起点->index中间的个数 右子树 终点->index的个数
    right_post = post[index:-1]

    # 先:  根+左子树+右子树
    return root + pre(left_in,left_post) + pre(right_in,right_post)

print(pre(In,post))