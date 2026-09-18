""" 已知字母A-Z 分别对应数字1-26 (A=1 B=2 C=3 ...), 给定一个只包含数字的字符串, 计算
    有多少种不同的解码方式。

    输入12 -> AB (1->A 2->B)
           -> L
    因此解码总数为2

    输入226 -> BZ
            -> VF
            -> BBF
    因此解码总数为3
"""
s = "1231"
list = []

def way(s, p):
    if len(s)==0:
        print("--find--", p)
        list.append(p)
        return

    a = s[:1]

    if a == '0':
        return

    way(s[1:], p + ' ' + a) # 切片操作 如果不满足上述if条件就递归调用way方法 遍历s中的从索引1开始每个数据
    # 例如 "045" 0不满足 就递归调用函数执行"45"

    if len(s)>1:
        b = s[:2]
        if int(b)>26:
            return
        way(s[2:], p + ' ' + a)

way(s, '')

d={}

for x in range(1,27):
    d[str(x)] = chr(x+64)

for i,p in enumerate(list):
    print(i+1,":",p,end=":")

    p = p.split()

    for n in p[:-1]:
        print( d[n],end="-")

    print(d[p[-1]])















