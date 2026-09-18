# 1.两数之和
from pickletools import bytes4

num1 = 20
num2 = 23
result = num1 + num2
print(result)



# 2.判断并输出100内偶数
list1 = []
for i in range(1, 100):     # *****左位能取到 右位取不到
    if i % 2 == 0:
        # print(i)
        list1.append(i)
print(list1)



# 3.判断并输出100内奇数
list2 = []
for i in range(1, 100, 2):
        list2.append(i)
print(list2)



# 4.判断素数
a = 37
flag = False
for i in range(2, a):
    if a % i == 0:
        flag = True
        break
if flag:
    print('不是素数')
else:
    print('是素数')



# 5.求阶乘
# 方法一
n = 5
sum = 1
for i in range(1, n+1):
    sum *= i
print(sum)

# 方法二
def jie(n):
    if n == 1:
        return 1
    else:
        return n * jie(n-1)
print(jie(n))



# 6.求圆周长 c=2Πr
# 此处可导入数学模块 取Π  import math
pi = 3.14
r = float(input('请输入半径:'))    # input默认输入类型为字符串
c = 2*pi*r
print(f'圆的周长是:{c}')



# 7.求直角三角形斜边长
import math
a = int(input('请输入直角边长:'))
b = int(input('请输入直角边长:'))
m = a*a + b*b
c = math.sqrt(m)
print(f'三角形斜边长为:{c}')



# 8.比较三个数大小
a = int(input('请输入第一个数'))
b = int(input('请输入第二个数'))
c = int(input('请输入第三个数'))
list3 = [a,b,c]
list4 = sorted(list3)    # print(list4)
print(f'从小到大顺序是:{list4[0]},{list4[1]},{list4[2]}')



# 9.找出区间内的所有素数 闭区间
def su(n):
    flag = True
    for i in range(2,n):
        if n % i == 0:
            flag = False
            break
    return flag

a = int(input('请输入左端点:'))
b = int(input('请输入右端点:'))
list5 = []
for i in range(a,b+1):
    if su(i):
        list5.append(i)
print(list5)



# 10.排列组合数字
# 1 2 3 4组成不同的三位数
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):  # 三组随机数
            if(i!=j)and(i!=k)and(j!=k):  # 不能重复
                print(f'{i}{j}{k}')



# 11.乘法口诀表
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end=" ")



# 12.水仙花数   三位数 各个位立方和为本身
"""
n = 567
a = n % 10              # 7
b = (n % 100) // 10     # n%100得到后两位数字 //整除10 6  整除并向下取整
c = n // 100            # 5
"""
for i in range(100,1000):
    a = i % 10
    b = (i % 100) // 10
    c = i // 100
    if a*a*a + b*b*b + c*c*c == i:
        print(f'{i}是水仙花数')



# 13.反向输出四位数
a = int(input('请输入这个数字:'))
a = str(a) # 为了使用字符串切片操作 将整型转为字符型
b = a[::-1]  # 反转 第一个:为输出 第二个:为间隔   间隔为-1代表反向输出
print(int(b))



# 14.判断字母
a = input()
result = a.isalpha() # 判断字母  print(result)
if result:
    print(f'{a}是字母')
else:
    print(f'{a}不是字母')



# 15.判断三角形
a = int(input('请输入一条边长'))
b = int(input('请输入二条边长'))
c = int(input('请输入三条边长'))
if a<=0 or b<=0 or c<=0:
    print('输入数据不合法')
if a+b>c and a+c>b and b+c>a:
    print('这三条边可以是三角形边长')
else:
    print('这三条边不可以是三角形边长')



# 16.完数  一个数恰好等海域除本身以外的所有因子之和
sum = 0
for i in range(1,1000):
    for j in range(1,i):
        if i % j == 0:
            sum += j
        if i == sum:
            print(f'{i}是完数')



# 17.找质数因子
a = int(input('输入这个数'))
y = 2  # 2是最小的质数
list = []
while a != y:
    if a % y == 0: # 说明使质因数
        list.append(y)
        a /= y # 继续判断新的a
    else:
        y += 1  # 寻找下一位的公因数 就是加1再除一次
list.append(int(a))  # 输出带上本身
for i in list:   # 打印list格式
    print(i,end=' ')



# 18.用海伦公式求三角形面积 p=(a+b+c)/2   S=math.sqrt(p*(p-a)*(p-b)*(p-c))
import math
a = int(input('请输入第一条边'))
b = int(input('请输入第二条边'))
c = int(input('请输入第三条边'))
p = (a+b+c) / 2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f'三角形的面积是{S}')



# 19.判断某年某月 距离第一天的天数
# 1.导入时间模块
import datetime

# 2.输入
year,month,day = map(int, input().split(" "))  # map()匹配函数 split切割

# 3.第一天
yuandan = datetime.datetime(year,1,1)

# 4.匹配模块 并输出差值
now = datetime.datetime(year, month, day)
print((now - yuandan).days + 1)  # 输出是第几天



# 20.斐波那契
# 方法一
def feibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return feibo(n-1) + feibo(n-2)  # 为n的结果
print(feibo(6))

# 方法二
n = 6
fibs = [1,1]
for i in range(2, n+1):
    fibs.append(fibs[i-1] + fibs[i-2])
print(fibs[n-1])



# 21.复制列表
# 1.导包
import copy

# 2.指定已知列表
list = [1,2,3,4]
# list1 = list   浅复制

# 3.复制
list1 = copy.copy(list)
print(list1)



# 22.暂停后输出
# 1.导包
import time

# 2.睡眠
time.sleep(2)

# 3.程序



# 23.输出成绩排名
score = int(input('输入成绩分数'))
if score >= 90:
    print('A')
elif 60 <= score < 90:
    print('B')
else:
    print('C')



# 24.统计字符
word = input('请输入字符串:')
char = 0     # 字母
number = 0   # 数字
space = 0    # 空格
other = 0    # 其它
for i in word:   # 遍历字符串
    if i.isalpha():  # 判断字符串中字母方法
        char += 1
    elif i.isdigit():
        number += 1
    elif i.isspace():
        space += 1
    else:
        other += 1
print(f'字母有{char}个,数字有{number}个,空格有{space}个,其他字符有{other}个')



# 25.落体反弹问题
""" 一球从100米高度自由落下,每次落地后反跳回原高度一半再落下,
    求它在第10次落地时共经过多少米(一上一下算两次距离), 
    第十次反弹多高
"""
# 1.初始高度 之后每次除二
n = 100

# 2.反弹次数
count = 0

# 3.承载结果 一共经过多少米
list = []

# 4.计算
while count < 10:
    if count == 0:
        # 第一次 只下
        list.append(n)
        n /= 2
        count += 1
    else:
        # 之后的次数 以上以下*2
        list.append(2*n)
        n /= 2
        count += 1
print(list)
print(sum(list))   # 一共经过多少米
print(f'第10次反弹高度为:{n}')   # 第10次高度



# 26.猴子吃桃问题
"""
    猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二
    天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一
    半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
"""
n = 1 # 最后剩下的桃子数量
for i in range(1, 10):
    total = (n+1)*2
    n = total
print(total)



# 27.求指定数列和
"""
    求2/1 3/2 5/3 8/5 13/8 21/13....的前20项和
"""
sum = 0
up = 2
down = 1
for i in range(20):
    sum += up / down  # 和
    a = down          # 分母
    down = up         # 分母变成前一个数的分子
    up = up + a       # 分子变成前一个数的分子加分母(前一个数的两位数字相加)
print(sum)



# 28.求阶乘和
"""
    求1+2!+3!+...+20!
"""
# 1.导包
import math

# 2.承载结果
sum = 0

# 3.计算
for i in range(1,21):
    sum += math.factorial(i)   # 求阶乘方法
print(sum)



# 29.年龄急转弯 递归
"""
    有5个人坐在一起，问第五个人多少岁?他说比第4个人大2岁。问第4个人岁数，他说
    比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两
    岁。最后问第一个人，他说是10岁。请问第五个人多大?
"""
def func(n):
    if n == 1:   # 第一个人
        return 10
    else:        # 从某人开始 比钱一个人大2岁
        return func(n-1) + 2
print(func(5))



# 30.判断回文数 对称数字 12321
a = int(input('请输入数字:'))
a = str(a)    # 变成字符串类型
b = a[::-1]   # 反转a
if a == b:
    print(f'是回文数')
else:
    print(f'不是回文数')



# 31.判断星期几
a = input('请输入第一个字母:')
if a == 'M':
    print('星期一')
elif a == 'T':
    b = input('请输入第二个字母:')
    if b == 'u':
        print('星期二')
    elif b == 'h':
        print('星期四')
    else:
        print('错误')
elif a == 'W':
    print('星期三')
elif a == 'F':
    print('星期五')
elif a == 'S':
    c = input('请输入第二个字母')
    if c == 'a':
        print('星期六')
    elif c == 'u':
        print('星期日')
    else:
        print('错误')



# 32.相反顺序输出列表
list = [1,2,3,4]
# 方法一
list.reverse()
print(list)

# 方法二
list1 = list[::-1]
print(list1)



# 33.对10个数排序
"""
    1.输入字符串 根据空格隔开
    input().split(' ')
    
    2.map() 映射 根据输入的空格变成几组数据
    map(int, )  变成整型
    map(int,input().split(' '))
    
    3.list() 转换成列表格式 方便输出
    
    4.sort() 列表内置方法 升序排序
    
    5.输出
"""
a = map(int,input().split(' '))   # 输入一串字符串包括" " 输出时根据" "分割
a = list(a)
a.sort()
print(a)



# 34.求矩阵主对角线元素之和
# 1.矩阵
a = []
sum = 0

# 2.添加矩阵行数据
for i in range(3):

    # 3.添加一排矩阵 表示列
    a.append([])

    # 4.添加矩阵列数据
    for j in range(3):
        k = int(input('请输入数据:'))
        a[i].append(k) # 在第i行添加元素

        # 5.判断主对角线元素 并计算
        if i == j:
            sum += a[i][j]
print(a)
print(sum)



# 35.有序列表添加元素
list = [1, 2, 3, 5]
n = int(input('请输入添加的数据'))
list.append(n)
list.sort()
print(list)



# 36.变量值交换
a = 5
b = 10
# 方法一
a, b = b, a
print(a)
print(b)

# 方法二
temp = a
a = b
b = temp
print(a)
print(b)



# 37.产生随机数
import random
a = random.random()    # 浮点数
b = random.randint(1, 10)
c = random.randrange(1, 10, 3)   # 10取不到
print(a,b,c)



# 38.lambda表达式    匿名表达式
a = lambda x,y:x*y
print(a(3,4))



# 39.温度转换 摄氏度华氏度  华氏度 = 摄氏度 * 1.8 + 32
a = (int(input('摄氏度请按1，华氏度请按2')))

if a == 1:
    b = float(input('请输入摄氏度；'))
    result = b*1.8+32
    print(f'你输入的是摄氏度{b},转换为华氏度{result}')
elif a == 2:
    c = float((input('请输入华氏度；')))
    result1 = (c-32)/1.8
    print(f'你输入的是华氏度{c},转换为摄氏度{result1}')
else:
    print('输入错误')



# 40.按位与或非
"""
    1.按位与: 有0则0 全1则1 转换为二进制判断
            0&0=0 0&1=0 1&1=1
    
        3->0011
        5->0101
        比 0001 ->1
        
    2.按位或: 有1则1 全0则0
    3.按位异或: 比较 相同0 不同1
    4.按位取反: 0变1 1变0   ~x = -(x+1)
"""
print(3 & 5)  # 1
print(4 & 12) # 4
print(3 | 5)  # 7
print(4 | 12) # 12
print(3 ^ 3)  # 0
print(4 ^ 12) # 8
print(~3)     # -4
print(~9)     # -10



# 41.计算字符串长度
a = input()
# 方法一
print(len(a))

# 方法二
length = 0
for i in a:
    length += 1
print(length)



# 42.打印杨辉三角
# 1.列表
a = []

# 2.创建位置`123
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)   # 先全部赋值为0 方便后续计算

# 3.计算首尾
for i in range(10):
    a[i][0] = 1
    a[i][i] = 1

# 4.计算中间数据
for i in range(2, 10):
    for j in range(1, i):
        a[i][j] = a[i-1][j] + a[i-1][j-1]

# 5.打印
for i in range(10):
    for j in range(i+1): # j行有i个元素 因此范围为i+1
        print(a[i][j], end=" ")
    print()



# 43.查找字符串
a = 'Hello World!'
b = 'World'
print(a.find(b))  # -1未找到



# 44.猜数字
# 1.导包
import random

# 2.确定一个随机数
target = random.randint(1, 99)   # 创建一个1-100的随机数

# 3.猜的次数
times = 7 # 最多猜7次

print('猜数字游戏开始，请输入100以内整数')
while times != 0:
    num = int(input('输入：\n'))
    if num > target:
        print('大傻逼，猜大了!')
        times -= 1
        continue
    elif num < target:
        print('大傻逼，猜小了!')
        times -= 1
        continue
    else:
        print('大傻逼，猜对了！')
        break
if times == 7:
    print('很遗憾，您的机会已用完')



# 45.第一个只出现一次的字符
str = 'Hello World'   # 寻找该字符串中 只出现一次的字母

a = -1  # 旗帜

mp = dict()  # 存储结果

for i in str:
    if i in mp:
        mp[i] += 1  # 出现次数加1
    else:
        mp[i] = 1   # 只出现一次

for i in range(len(str)):
    if mp[str[i]] == 1:  # 只出现一次
        a = i
        break
print(a)



# 46.最大公因数
"""
    1.如果数相同 最大公因数就是本身
    2.如果两个数成倍数关系 小的数就是最大公因数
    3.如果没有关系 从小的数开始 一次将小的数减1 判断能否整除
"""
def func1(a,b):
    if a == b:
        return a
    num = min(a, b)
    while a % num != 0 or b % num != 0:
        num -= 1
    return num
print(func1(12, 18))



# 47.数组里没有出现过的数字
"""
    给定一个长度为N的正整数数组nums，其中nums[i]的值都在区间[1，n]中，请你找出
    nums数组在[1，n]范围里面没有出现过的数字，并将它们放在数组里面返回（在数组里
    面的顺序可以不唯一）
"""
# 输入[2,1,4,5,1,2]
# 输出[3,6]

def func(nums):
    # 1.输入一个列表
    l = [i for i in range(1, len(nums) + 1)]   # nums+1  范围上取到1-nums
        # 列表生成式  i for i in range(,)

    # 2.准备一个结果列表 判断列表没有的数字 放到该列表中 最后输出该列表
    l2 = []

    # 3.删除重复的数字
    nums = set(nums)

    # 4.开始判断
    for o in l:
        if o in nums:  # 存在
            continue
        else:          # 不存在
            l2.append(o)

    return l2

list = [2,1,4,5,1,2]
print(func(list))



# 48.替换空格
# 将Hello World 变成 Hello%World
def func(s):
    # 已知一个字符串 准备一个新的空字符串 将每个字母依次判断

    res = ''  # 空
    for i in s:
        if i != ' ':   # 这个字母不是空格 直接输出字母
            res += i
        else:          # 这个字母是空格 变成%
            res += '%'
    return res
print(func('Hello World'))



# 49.快乐数
"""
    给定一个正整数，请你判断这个数是不是快乐数。快乐数：对于一个正整数，每次把他替换为他每
    个位置上的数字的平方和，如果这个数能变为1则是快乐数，如果不可能变成1则不是快乐数。
    
    例如：正整数19
        转换过程为1*1+9*9=82，8*8+2*2=68，6*6+8*8=100，1*1+0*0+0*0=1，所以他是快乐数。
"""
def change(x):
    sum = 0
    while x > 0:
        j = x % 10
        sum += j*j
        x //= 10
    return sum   # 1.得到两位数各个平方和
# print(change(12))

def happy(n):
    while n > 9:  # 2.得到的平方和是两位数
        n = change(n)  # 3。就继续执行change函数 直到只剩下一位数
    if n == 1:   # 4.判断得到的一位数是否为1
        return True
    else:
        return False
print(happy(12))



# 50.立方根 开立方根并向下取整
import math
def func(n):
    result = math.pow(n, 1/3)   # 1/3次幂
    return int(result)          # 向下取整
print(func(8))



# 51.最长公共前缀
"""
    给定一个字符串数组 返回每个元素的最长公共前缀
    ['abcd','abc','abcc','abca'] -> [abc]
"""
# 1.写一个函数
def func(strs):
    # 2.获取strs长度 即字符串个数
    n = len(strs)
    if n == 0:
        return ''

    for i in range(len(strs[0])):
        # 3.先假设第一个字符串的长度最小 第一个字符串的长度 第0行

        # 4.遍历第一个字符串的每一个字母 用于判断的字符串
        temp = strs[0][i]

        # 5.根据第一个字符串的长度及数据 判断其他字符串
        for j in range(1, n):
            if i == len(strs[j]) or temp != strs[j][i]:
                # 如果该其他字符串比第一个字符串更小 或者不匹配 -> 返回结果
                return strs[0][0:i]   # 返回从第一个字符串开头到索引i-1的字串 即最长公共前缀

    return strs[0]    # 如果不出现其他字符串更小 或不匹配 那么第一个字符串就是最长公共前缀
list = ['abcd','abc','abcc','abca']
print(func(list))



# 52.字符串变形
"""
    1.有空格的单词换位置
    2.大写变小写 小写变大写
    
    Hello World 
         ⬇ 
    wORLD hELLO
"""
def func(s):
    # 1.输入了字符串 根据' '变成列表
    list = s.split(' ')

    # 2.反转
    list = list[::-1]

    # 3.s置为空
    s = ''

    # 4.向s中输出结果
    for i in list:
        i = i.swapcase()   # 5.大小写转换
        s += i
        s += ' '
    return s[0:len(s)-1]
print(func('Hello World'))



# 53.压缩字符串
"""
    aabcccccaaa -> a2bc5a3
"""
def func(s):
    # 存储结果
    list = []

    for i in s:
        if not list or list[-2] != i:
            # 倒数第二个字母不是i(一个新的字母) 或者列表不存在
            list.append(i)  # 存字母
            list.append(1)  # 存字母出现次数
        else:
            # 和上一个字母是一样的 直接加1
            list[-1] += 1
    return ''.join(map(str, [x for x in list if x != 1]))
print(func('aabcccccaaa'))

"""
    return + 具体返回内容
    1. ''.join() 
        字符串拼接操作 拼接成新字符串
        
    2. map(str, ) 
        把列表里每个元素转成字符串  join要求为字符串
        
    3. [x for x in list if x != 1] 
        列表推导式 过滤掉列表中1的数据 得到新列表
"""



# 54.三个数的最大乘积
"""
    已知一个列表 中有很多数 要求得到这一堆数中 三个数的最大乘积
"""
def func(list):
    list.sort()  # 排序
    """ list.sort() 
        [min, ... ,max-1 , max]    
        list[0] < list[1] < list[2] ...
        
        list[0]最小 list[1]第二小 list[-1]最大  即两个负数 * 最大值
        list[-1]最大 list[-2]第二大 list[-3]第三大  即三个最大的正数相乘
    """
    return max(list[0]*list[1]*list[-1], list[-1]*list[-2]*list[-3]) # 找最大
print(func([1,2,3,4,5]))



# 55.十进制转二进制
a = 10
b= bin(a)
print(b)



# 56.判断字符是否唯一 每个字符都不同
def func(str):
    for i in range(1, len(str)):
        if str[i] in str[i+1:]:   # 从i+1取到最后
            return False    # 如果第i个元素 在i之后的所有元素中出现过 就不唯一
    return True
print(func('Hello'))



# 57.IP地址转化
"""
    IP地址是用'.'隔开的四段数字 
    把IP地址转换成一个整数
    
    eg. 114.55.207.244 -> 0111001000110111 11001111 11110100 -> 1916260340
"""
def func(str):
    # 用'.'将字符串切割
    strs = str.split('.')

    # 准备一个空串
    res = ''

    # 遍历
    for i in strs:
        # 十进制转二进制 高位补0
        # '{:08b}'.format(val)
        res += '{:08b}'.format(int(i))
    return int(res, 2)
print(func('114.55.207.244'))



# 58.二分查找
"""
    给定有序升序数组 搜索给定数据在数组中的位置 并返回
"""
def func(nums, target):
    left = 0               # 数组左指针 第一个数据元素
    right = len(nums) - 1  # 数组右指针 最后一个数据元素

    # 从数组的首尾开始 直到两个指针相遇
    while left <= right:
        # 左指针在右指针左边
        middle = int((left + right)/2)
        if nums[middle] == target:   # 此处nums为列表 元素[]   nums[middle]
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            # nums(middle < target):
            left = middle + 1
    return -1
list = [1,3,5,7,9]
target = 7
print(func(list, target))



# 59.二分查找 重复 只输出第一次遇见的下标值
def func(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2    # // 整除 只返回整数部分

        if nums[middle] == target:
            # 判断是否有重复

            # middle是计算得到的确定数字 不能改变 因此设定新的变量等于middle
            temp = middle

            while nums[temp] == target and temp >= 0:
                # 如果temp满足条件

                temp -= 1
                # 依次从这个中间位置左移判断 如果满足条件就向左移一个数据
                # 如果没有重复元素就可以输出该数据

            return temp + 1
            # 该循环执行到最后终止条件为temp为左指针也就是temp >= 0
            # 此时执行temp -= 1 变成负数 因此输出结果 temp += 1

        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
list = [1,3,3,4,5]
target = 3
print(func(list, target))



# 60.移动0
"""
    给定一个数组，将所有0移动到数组末尾并且不改变其他数字的相对顺序
"""
def func(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)   # 先删除
            nums.append(0)   # 再添加
    return nums
print(func([0,1,3,0,4,5,0]))



# 61.旋转字符串
"""
    给定字符串A B，如果能将A从中间某个位置切割为左右两部分，
    且将左边字符串移动到右边字符串后面
    组成新字符串刚好等于B 返回True
"""
def func(a,b):
    # 首先判断a b长度是否相同 不相同就不用继续判断了
    if len(a) != len(b):
        return False

    else:
        # 直接写两个A拼在一起 如果满足条件 那么两个A拼在一起中一定有B
        bigA = a + a
        result = b in bigA
        return result
print(func('hello','llohe'))



# 62.判断子序列
"""
    给定两个字符串S、T 判断S是否为T的子序列  
    即是否可以从T中删除一些字符变成S
"""
def func(s,t):
    c = ''  # 空串用于存储结果
    n = 0   # 用于计数 表示下标

    if len(s) > len(t):
        return False

    for i in t:
        if n<len(s) and i == s[n]:  # s中的字母在t中存在 就加入c 表结果
            c += i
            n += 1   # 计数 直到n == s长度 停止循环
    if s == c:
        return True
    return False
print(func('hlo', 'hello'))



# 63.数组重复数字
"""
    [2,3,1,0,2,5,3] -> 2或3   如果没有输出-1
"""
def func(nums):
    for i in nums:
        if nums.count(i) >= 2:
            # 重复
            return i
    return -1
print(func([1,2,4,5,5]))



# 64.字符串的相邻字符去重
"""
    将相邻且相同的两个字符删掉构成新的字符串，重复删除
    acbbc -> a
"""
def func(s):
    res = ''
    for i in s:
        # s为一个字符串 依次拿出字符串中的字母 与res比较 不同就加进res中 相同就不要
        if res == '':
            res += i
        elif res[-1] == i:
            res = res[:-1]   # 从前面的任一个位置 取到倒数第一个元素之前
        else:
            res += i
    return res
print(func('acbbc'))



# 65.2的幂
"""
    给定非负整数n 请问是否存在一个x满足 2^x=n  有就返回true 没有就返回false
    
    2的幂在二进制中只有一位是1    
    4 -> 0100      8 -> 1000
    3 -> 0011      7 -> 0111
    
    根据按位与计算
    规律: 3和4 7和8的按位与运算都是0000
    
    n和n-1做按位与运算 如果结果为0000 我们就可以判断n是2的幂
"""
def func(n):
    return n > 0 and n & (n-1) == 0
print(func(32))
print(func(31))



# 66.最长公共字串
"""
    hellopython
    goodlopylike
    
    已知两个字符串 依次将左指针比较 如果相同 就把第一个指针位置往后移 
                                如果不同 就两个指针都往后移
                                
    滑动窗口
"""
def lcs(str1, str2):
    res = ''
    left = 0
    for i in range(len(str1) + 1 ):   # 为保证str1中所有元素都取到 此处 +1
        if str1[left:i+1] in str2:
            # 如果str1中从left(最初默认left为0 即第一个元素)开始
            # 直到i元素都在str2中 就把这些元素添加到res中
            res = str1[left:i+1]
        else:
            # 第一个元素没匹配
            left += 1  # 匹配第二个元素
    return res
print(lcs('hellopython','goodlopylike'))



# 67.冒泡排序
def maopao(list):
    for i in range(len(list)):   # 此处范围可以写len  也可以写len - 1
        for j in range(len(list) - i - 1):  # 冒泡排序比较次数 n-1
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

list = [1,5,4,2,3]
print(maopao(list))



# 68.选择排序
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



# 69.插入排序
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



# 70.字符删除
"""
    给定两个字符串str、sub， 从str中完全删除在sub中存在的字符
    
    已知str删除指定字符
"""
def func(str,sub):
    s = set(sub)   # 将字符串转换为集合
    ans = ''
    for c in str:
        if c not in s:
            ans += c
    return ans

print(func('Thank you', 'you'))



# 71.目标移动
"""
    给定一个数组nums和目标值target 将target元素移动到数组前面 其他元素相对顺序不变
    使用双指针 但都是从右向左的
"""
def func(nums,target):
    count = 0  # 计数器
    left = len(nums) - 1 # 最后一个索引
    right = len(nums) - 1  # 同上

    while left >= 0:
        if nums[left] != target:
            # left不是应删除并前移的元素 那么把left和right同时向前移一个位置 判断上一个元素
            nums[right] = nums[left]
            right -= 1
        else:
            # left == target 此时left为应删除元素 并添加到最前面
            count += 1
        left -= 1  # 前移
    for i in range(count):
        # 将所有的target判断元素都添加到前面
        nums[i] = target
list = [1,1,2,1,3,4]
target = 1
func(list,target)
print(list)



# 72.柠檬水找零
""" 在柠檬水摊上，每一杯柠檬水的售价为5美元。顾客排队购买你的产品，（按账单bills支付的顺序）一次购买一杯。
    每位顾客只买一杯柠檬水，然后向你付5美元、10美元或20美元。你必须给每个顾客正确找零，也就是说净交易是每
    位顾客向你支付5美元。注意，一开始你手头没有任何零钱。如果你能给每位顾客正确找零，返回true，否则返回 false。
    
    贪心算法
    1.第一位顾客支付五元
    2.第一位顾客支付十元 需要找零五元 
    3.第一位顾客支付二十元 需要找零十五元 -> 一张五元+一张十元(更优) 三张五元
    
    [5,5,5,10,20] 返回true
    [5,5,10,10,20] 返回false
"""
def func(bills):
    five = 0
    ten = 0

    for bill in bills:
        # 支付了五元
        if bill == 5:
            five += 1

        # 支付了十元
        elif bill == 10:
            # 无法找零
            if five == 0:
                return False
            # 可以找零
            five -= 1
            ten += 1

        # 支付了二十元
        else:
            # 可以找零
            if five > 0 and ten > 0:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            # 无法找零
            else:
                return False
    return True

print(func([5,5,5,10,20]))
print(func([5,5,10,10,20]))



# 73.尾部的0
"""
    给定整数n 计算n!中的尾部的0的个数
"""
def func(n):
    count = 0
    for i in range(5,n+1,5):   # 从5到n+1 步长为5 只需要判断个位5的数的阶乘
        while i % 5 == 0:
            # 为了使尾部有0 判断该n是否为5的倍数
            i //= 5   # 开始整除并计数 计算有多少个0
            count += 1
    return count
print(func(5))



# 74.统计数字
"""
    给定数字k 计算在0到n中出现的次数
"""
def func(k,n):
    count = 0
    for i in range(0,n+1):
        time = str(i).count(str(k))  # 把i转成字符串 对i调用k字符串
        count += time
    return count
print(func(1,11))



# 75.合并排序数组*****
"""
    合并数组A和B 要求合并后仍有序
    
    使用两个指针
    先取两个小的 按大小放入新数组
"""
def func(A,B):
    i,j = 0,0  # 准备两个指针
    c = []  # 存放结果数组

    # 进行第一次数值比较
    while i < len(A) and j < len(B):
        # 存放更小的数组  直到有一个数组比较完
        if A[i] < B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    # 将剩余的数组数值存放进结果
    while i < len(A):
        c.append(A[i])
        i += 1
    while j < len(B):
        c.append(B[j])
        j += 1
    return c
print(func([1,4,9],[2,3,11]))



# 76.插入5
# 给定一个数字 在数字的任意位置插入5 使该数字最大
def func(a):
    string = ''  # 转换a为字符串
    ans = 0      #
    n = 0        # 字符串长度
    flag = False  # 旗帜 替换为5

    # a是正数
    if a >= 0:
        string = str(a)
        n = len(string)

        for i in range(n):
            # i为字符串索引
            if (ord(string[i]) - ord('0')) < 5 and flag == False:
                # ord ASCII码
                # 当前数字小于5且还没替换过5
                ans = ans * 10 + 5  # 结果乘10加5   ans=0+5=5  ans=5*10+5=55 ...
                flag = True
            ans = ans * 10 + ord(string[i]) - ord('0')
        if flag == False:
            ans = ans * 10 + 5

    # a是负数
    else:
        a = -a
        string = str(a)
        n = len(string)

        for i in range(n):
            if ord(string[i]) - ord('0') > 5 and flag == False:
                ans = ans * 10 + 5
                flag = True
            ans = ans * 10 + ord(string[i]) - ord('0')
        if flag == False:
            ans = ans * 10 + 5
        ans = -ans
    return ans
print(func(234))



# 77.字符串置换 可以通过改变顺序使两个字符串相同
def func(A,B):
    A = sorted(A)
    B = sorted(B)
    return A == B
print(func('abc','cba'))



# python语法进阶
"""
    1.列表推导器 expression for item in iterable if condition
                i for i in range(1,100)
                [0 for _ in range(3)] -> [0,0,0]
    
    2.双端队列 栈 队列

            q = deque()      初始化
            q.append(x)      从右侧入队
            q.appendleft(x)  从左侧入队
            x = q.popleft()  从左侧出队   时间复杂度O(1)
            len(q)           获取队列长度
            
        栈  stk = [] 列表模拟
            stk.append(x)    入栈
            x = stk.pop()    出栈  默认弹出最后一个元素 时间复杂度O(1)
            stk[-1]          获取栈顶元素不移除
            
        使用技巧:
            快速判断空队列、栈     if not q:       判空
            栈的反转              stack[::-1]     同期图片获取逆序
            队列转列表            list(q)         将deque转换为普通列表
            一次性初始化           duque([1,2,3])  用迭代器初始化队列
                    队列 from collections import deque
    3.埃氏筛
    4.逆波兰表达式
"""





