# 学生可以用学校提供的教育邮箱账号（一般以edu.cn结尾的）去申请免费 授权（申请网址：https://www.jetbrains.com/community/education/#students）


print("hello world")

# 注释规范要求 注释内容与注释隔一个空格 单行注释   ctrl+/

#多行注释 三个引号开头三个引号结尾 此引号为英文输入法引号
"""多行注释"""

# 数字number 整数int 浮点数float 复数complex 布尔bool
int("666")
float("123")
str("456")
# 字符串string 文本 用""包括 str()类型
# 列表list 有序可变数列
# 元组tuple 有序不可变数列
# 集合set
# 字典dictionary

"666"
print("13.14")
"黑马程序员"

print("666")
print("黑马程序员")

# 打开pycharm后 新建一个python文件
# 运行方式 右键双击屏幕 开始运行run

# 变量 变量格式 变量名称 =变量的值
money = 50
print("钱包还有：",money)

# 买一个冰淇淋，花费十元
money = money - 10
print("买了一个冰淇淋花费十元，还剩余：", money, "元")

# 假设，每隔一小时，输出一下钱包余额
print("现在是下午一点，钱包余额剩余：",money)
print("现在是下午一点，钱包余额剩余：",money)
print("现在是下午一点，钱包余额剩余：",money)
print("现在是下午一点，钱包余额剩余：",money)
# python快捷复制 ctrl+d

# type()类型 验证数据类型 直接输出类型信息
print(type("黑马程序员"))
print(type(666))
print(type(11.345))

name = "黑马程序员"
name_type = type(name)
print(name_type)

# 利用type()存储结果
string_type = type("黑马程序员")
int_type = type(666)
float_type = type(11.345)
print(string_type)
print(int_type)
print(float_type)

# 利用type()查看变量的数据类型
name = "黑马程序员"
name_type = type(name)
print(name_type)

# 数据类型的转换 以结果为语句
# 将数字类型转换为字符串
number_str = str(11)
print(type(number_str),number_str)

# 将浮点转化为字符串
float_str = str(11.345)
print(type(float_str),float_str)

# 将字符串转化为数字
num = int("11")
print(type(num),num)

# 将字符串转化为浮点
float("11.345")
num2 = float("11.345")
print(type(num2),num2)

# 万物都可转字符串
# 不是任何字符都都能转化为数字
print("黑马程序员")

# 将整数转浮点数
float_num = float(11)
print(type(float_num),float_num)

# 将浮点数转化为整数
int_num = int(11.345)
print(type(int_num),int_num)
# 转为整数后 小数点部分丢失

# 标识符命名 英文中文数字下划线_ 数字不可以开头 区分大小写 不能命名关键字
# 关键字中 False True None 首字母大写 若使用小写 则不算作占用关键字
#         其他关键字默认小写 使用大写则不算占用关键字

# 运算符
# 算数运算符 + - * / //取整除 %取余 **取指数
num = 1 + 2 * 3
num1 = 1
num1 += 1 # num1 + num1 = 2
print("num1 += 1;", num1)

# 字符串定义方式
# 单引号定义法：name = '黑马程序员'
# 双引号定义法：name = "黑马程序员"
# 三引号定义法：name = """黑马程序员"""
name = '黑马程序员'
print(type(name))

# 单引号定义法，可以内含双引号
# 双引号定义发，可以内含单引号
# 使用转移字符(\),来将引号解除效用，变成普通字符串
name = '"黑马程序员"'
name1 = "'黑马程序员'"
name2 = "\"黑马程序员"

# 字符串的拼接 +
print("学IT来黑马" + "月薪过万")
""" 字符串格式化 优化字符串拼接   使用%s
    其中 %表示我要占位 s表示将变量变成字符串放入占位的地方
    即先用一个符号进行占位 再把这个位置给字符串
"""

name3 = '"黑马程序员"'
messages = "学IT就来 %s" % name3
print(messages)

# 多个变量进行占位需要()
# 数字也使用%s占位 此时数字被转换成了字符串
class_num = 57
avg_salary = 16781
messages1 = "Python大数据学科, 北京%s期, 毕业平均工资: %s" % (class_num, avg_salary)
print(messages1)

# 常用占位符
""" %s 将内容转换为字符串 放入占位位置
    %d 将内容转换为整数 放入占位位置
    %f 将内容转换为浮点型 放入占位位置
"""

# 若不使用转换字符类型
name4 = "传智播客"
setup_year = 2006
stock_price = 19.99
message2 = "%s.成立于: %d，我今天的股价是: %f" % (name4, setup_year, stock_price)
print(message2)
# 输出 19.9900000

# 格式化精度控制 19.990000->19.99
""" 使用符号 m.n 控制宽度和精度
    m. 控制宽度 要求数字(很少使用)，若设置的宽度小于数字自身，不生效
    n. 控制小数点精度，要求数字，会进行小数的四舍五入
    
    %5d 表示宽度为5位 eg.数字11被设置为宽度5-> [空格][空格]11 用空格来填补宽度
    %5.2f 宽度为5的同时，小数点精度为2
    %.2f 不限制宽度 小数点精度为2
    小数点和小数部分也进入宽度计算 
"""

# 字符串格式化 方式一 %
num1 = 11
num2 = 11.345
print("数字11宽度限制为5，结果是: %5d" % num1)
print("数字11宽度限制为1，结果是: %1d" % num1)
print("数字11.345限制宽度为7，小数精度为2，结果是: %7.2f" % num2)
print("数字11.345小数精度为2，结果是: %.2f" % num2)

# 快速格式化方式 方式二 f"内容(变量)"
# f format
name3 = "传智播客"
set_up_year = 2025
stock_price = 19.99
print(f"我是{name3}, 我成立于:{set_up_year}, 我今天的股票价格是, {stock_price}")
# 快速格式化的方法不限数据类型 同时也不做精度控制

# 表达式字符串格式化
""" 表达式：一条具有明确执行结果的代码语句 
    eg. 1+1 5*2 name = "张三" age = 11+11
    表达式的字符串格式化:
"""
print("1 * 1的结果是：%d % (1 * 1)")
print(f"1 * 1的结果是：(1 * 1)")
print("字符串在Python中的类型是：%s % type('字符串')")

# input语句 输入语句
print("请告诉我你是谁")  # 提示语句
name4 = input()
print("Get! 你是：%s" % name4)

# 不使用提示语句 将提示写在input中
name5 = input("请告诉我你是谁")
print("Get! 你是：%s" % name5)

# input语句不管输入内容是什么类型 返回值都为字符串
# 类型转换 假设要输出一个数字
num1 = input("请告诉我你的银行卡密码")
num2 = int(num1)
print("我的银行卡密码是：", type(num2))

# bool
# 变量名 = 布尔类型字面量

# 比较运算 比较运算符：< > == != >= <=
result = 10 > 5
print(f"10 > 5 的结果是：{result}，类型是{type(result)}")
# 输出结果是 true或false

# if判断语句
age = 30
if age >= 18:
    print("我已经成年了")
# 当条件判断结果为true时 执行if后面的语句 如果结果为false 直接跳过该语句

# if else语句
# 当if的条件满足时 执行if后语句 如果不满足 则执行else后语句
print("欢迎来到黑马游乐场，儿童免费，成人收费。")
age = int(input("请输入你的年龄："))
if age >= 18:
    print("您已成年，游戏需要补票10元。")
else:
    print("您未成年，可以免费游玩。")
print("祝您游玩愉快。")

# if elif else 语句
print("欢迎来到黑马动物园。")
height = int(input("请输入你的身高（cm）："))
vip_level = int(input("请输入您的vip级别（1-5）："))
if height < 120:
    print("您的身高小于120cm，可以免费游玩。")
elif vip_level > 3:
    print("您的vip级别大于3，可以免费游玩。")
else:
    print("不好意思，所有条件均不满足，需要购票10元。")
print("祝您游玩愉快。")
# 从第一个开始判断 至满足条件 输出 执行结束 else不是必选项

# 前置信息可以不写入 在判断条件中使用input语句
# if(int(input("请输入您的VIP级别（1-5）")) > 3):

# 嵌套：判断语句的嵌套 if语句里嵌套if语句

# while循环
""" while循环语句
    条件判断+操作语句
    循环逻辑 判断一个条件 如果条件满足 则执行下方语句 并返回条件判断 并继续执行语句 直至不满足条件 循环结束
    
    while 条件:                      ➡ 此条件为 bool、比较运算
        条件满足时: 执行语句1
        条件满足时: 执行语句2
        条件满足时: 执行语句3  
"""

i = 0     # 初始条件
while i < 3:
    print("小美，我喜欢你")
    i += 1     # 终止条件 如果没有此条件 语句将重复执行不停止
# 从i=0开始执行语句 每一次结束i都增加1 直到i=3 条件判断为false 循环结束

# while嵌套
a = 1
while a <= 3:  # 外层循环
    print(f"今天是第{a}天，准备表白")
    b = 1
    while b <= 4:  # 内层循环
        print(f"送给小美第{b}只玫瑰")
        b += 1
    print(f"小美我喜欢你")
    a += 1
print(f"坚持到第{a - 1}天，表白成功")
# 第一百天时 第一个条件完成 表白成功 但是最后输出时使用a += 1 即输出结果i=4 因此输出时输出到a-1天

print("hello", end='') # print输出不换行的方法
print("hello\tworld") # 制表符\t 多行字符串进行对齐
print() # 换行

# for循环
""" for 临时变量 in 待处理数据集:
    循环满足条件时执行的代码
    
    for ... in ... :
    print(...)
"""
name = "ith"
for x in name:
    print(x)
# 执行结果: i    t    h    输出每个字符

# 这个过程访问了name中的每一个元素 相当于遍历了name


# range语句
""" 简单数字序列
    range(num) 获取一个从0开始到num的数字序列 不包含num本身
    eg. range(5) ➡ [0,1,2,3,4] 通过for循环输出
    
    range(num1, num2) 获取从num1到num2的序列 不包含num2本身
    
    数字之间的步长默认1 由step决定
    range(num1, num2 ,step)
    eg. range(5, 10, 2) ➡ [5,7,9]
"""
for x in range(10):
    print(x)

for x in range(5, 10, 2):
    print(x)
# 通过range可以快速执行for循环完成特定需求

# for循环临时变量作用域
i = 0
for i in range(5):
    print(i)
print(i) # 如果没有前面 i = 0 则不能够正确执行该步 一因为i是for循环内部临时变量 理论上只在for循环内起作用

# for循环嵌套

# 循环控制 循环中断
# continue break
""" for x in range():
        print()
        continue     语句执行到continue时 并不会执行下方语句 直接结束本次循环 进入第二次循环
        print()
        break        语句执行到break时 会结束循环 跳出循环
"""


# 函数
s = "itheima"
length = len(s)
print(length) # 输出s的长度 len()就是python的内置函数 用于计算长度


""" def 函数名(参数):
        函数体
        return 返回值
    调用函数
"""
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")
my_len(s)


# 函数传入参数
""" def 函数名(传入参数):
        函数体
        return 返回值
"""
def add(x, y):  # 形式参数
    result1 = x + y
    print(f"{x} + {y}的结果是: {result1}")
add(1, 2)  # 实际参数


# 函数返回值
def add1(a, b):
    result2 = a + b
    return result  # 返回值(函数调用后的结果) 作用: 将result值返回出去

# 函数的结果 返回给了r
r = add1(1, 2)
print(r)


# None类型返回值 函数默认返回值
# 变量无内容时 也可以使用None    name = None
def say_hello():
    print("hello...")
result2 = say_hello()     # 使用变量接收函数返回值
print(result2)            # 打印返回值 结果为None
print(type(result2))      # 输出返回值数据类型 结果为<class NoneType>

# 也可以在返回值处 return None


# 使用None进行if判断 此时None相当于False
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None
result3 = check_age(16)
if not result3:
    # 执行该if 意味着result3的结果输出了else 也就是None 即年龄不满18岁
    print("未成年，不可以进入")


# 函数说明文档
def func(x, y):
    """
    函数说明
    :param x: 形参x说明
    :param y:  形参y说明
    :return:  返回值说明

    函数体print()

    返回值return

    调用函数时 鼠标悬停到实际参数位置 可以查看函数文档
    """

# 函数的嵌套调用
def func_b():
    print("-1-")

def func_a():
    print("-2-")
    func_b() # 嵌套
    print("-3-")
func_a()



# 数据容器
""" 批量存储并使用数据
    分为5类: list列表   tuple元组   str字符串   set集合   dict字典 
    
    列表 元组 字符串：支持下标索引    集合 字典：不支持下标索引
    列表 元组 字符串：序列类型       集合 字典：非序列类型 
    列表 元组 字符串：可以有重复元素  集合 字典：无重复元素
    列表 集合 字典：可以修改         元组 字符串：不可以修改 
    列表 元组 字符串：支持使用for循环遍历
"""

# 列表list []
""" # 字面量
    [元素1，元素2，元素3，元素4...]

    # 定义变量
    变量名称 = [元素1，元素2，元素3，元素4...]

    # 定义空列表
    变量名称 = list()
"""
name_list = ['itheima', 'itcast', 'python']   # list = [[1, 2, 3], [a, b, c]]
print(name_list)
print(type(name_list))


# 列表下标索引
""" [第0个元素， 第1个元素， 第2个元素， 第3个元素...]
    [...第-5个元素， 第-4个元素， 第-3个元素， 第-2个元素，第-1个元素]

    嵌套下标索引
    [ [第0个元素， 第1个元素]第0个元素,  [第0个元素， 第1个元素]第1个元素...]
                                        ⬆ 列表[1][0]
"""

# 列表的方法
""" 函数:
    def add(x, y):
        return x + y
    num = add(1, 2)
    print(num)

    方法:    (列表函数)
    class Student:
        def add(self, x, y):
            return x + y
    Student = Student()
    num = student.add(1, 2)        
    
    1.列表查询元素下标:
    列表.index()
    如果找不到 报出ValueError    
"""
index = name_list.index("itheima")
print(f"itheima在列表中的下标索引值是: {index}")

# 2.列表修改元素: 列表[下标] = 值
# 正向下标
my_list = [1, 2, 3]
my_list[0] = 5     # 将第一个元素替换为5
print(my_list)
# 反向下标
my_list[-3] = 5    # 将第一个元素替换为5
print(my_list)

# 3.列表插入元素: 列表.insert(下标，元素)
my_list.insert(1, "itheima")
print(my_list)

# 4.列表追加单个元素:  (1) 列表.append(元素)
my_list.append(4)
print(my_list)     # 结果 [1, 2, 3, 4]

# 5.列表追加批量元素:  (2) 列表.extend(元素)
my_list.extend([4, 5])

# 6.列表删除指定下标元素:  (1) del 列表[下标]     (2) 列表.pop(下标)
del my_list[0]
my_list.pop(1)

# 7.列表指定一个元素的内容删除: 列表.remove(元素)
my_list.remove("itheima")

# 8.清空列表内容: 列表.clear()
my_list.clear()

# 9.统计某元素在列表内的数量: 列表.count(元素)
count = my_list.count(5)
print(f"列表中1的数量为: {count}")

# 10.统计列表内有多少个元素: len(列表)
print(len(my_list))


# 列表的遍历(迭代)
# 使用while循环进行遍历
""" index = 0                 # 下标
    while index < len(列表):
        元素 = 列表[index]
        对元素处理
        index += 1
"""
def list_while_func():
    # 循环控制变量通过下标索引控制 默认为0 每一次循环将索引加1 条件为下标索引变量小于列表元素数量
    my_list = [1, 2, 3]
    index = 0  # 初始值为0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的元素：{element}")
        index += 1
list_while_func()

# 使用for循环进行遍历
def list_for_func():
    my_list = [1, 2, 3]
    for element in my_list:
        print(f"列表的元素有：{element}")
list_for_func()


# 元组tuple   ()
""" 元组一旦定义完成 就不可以修改

    # 定义元组字面量
    (元素，元素，元素...)
    
    # 定义元组变量
    变量名称 = (元素，元素，元素...)
    
    # 定义空元组
    变量名称 = ()
    变量名称 = tuple()
    
    只有一个元素的元组 需要逗号 t1 = ("hello", )
    
    元组可以嵌套
    
    元组可以查找下标索引
    
    元组内容不能进行修改 否则会直接报错 
    若元组内嵌套了一个list 则可以修改
"""
t1 = (1, "hello", True)
t2 = tuple()  # t2 = ()   两种写法都是空元组
print(f"t1的类型是：{type(t1)}, 内容是：{t1}")

index1 = t1.index(1)
print(f"在t1中1的下标是：{index1}")

num = t1.count(1)
print(f"在t1中1的个数是：{num}")

num1 = len(t1)
print(f"t1中的元素有：{num1}个")

# 元组的遍历 while
index2 = 0
while index2 < len(t1):
    print(f"元组的元素有：{t1[index2]}")
    index2 += 1
# 元组的遍历 for
for element in t1:
    print(f"元组的元素有：{element}")


# 字符串str
# 字符串不能进行修改 若修改则会得到一个新的字符串
my_str = "itheima and itcast"

# 1.查找字符串索引值  字符串.index(字符串)
value = my_str[2]  # h
value1 = my_str[-16]  # h
print(f"在字符串{my_str}中下标为2的元素为{value}， 下标为-16的元素为{value1}")

# 2.字符串的替换
# 字符串.replace(字符串1，字符串2) 将1的内容完全变成2 得到了一个新的字符串
new_my_str = my_str.replace("it", "程序")
print(f"替换后得到：{new_my_str}")

# 3.字符串的分割
# 字符串.split(分隔符字符串) 按照指令分割 将字符串划为多个字符串 存入列表对象中 得到新的列表对象
my_str_list = my_str.split(" ")
print(f"切分后得到：{my_str_list},类型是：{type(my_str_list)}")

# 4.字符串的规整操作 (去前后空格)   字符串.strip() 为默认值
print(my_str.strip())

# 5.字符串的规整操作(去前后指定字符串)   字符串.strip(字符串)
print(my_str.strip("t"))

# 6.统计某字符个数
count = my_str.count("i")
print(f"字符串{my_str}中i出现次数为：{count}")

# 7.统计字符串的长度 len()
num3 = len(my_str)
print(f"字符串{my_str}的长度是：{num3}")


# 序列
""" 序列指内容连续、有序、可使用下标索引的一类数据容器
    列表 元组 字符串都可以视为序列
    
    序列的切片 从一个序列中取出一个子序列
    序列[起始下标：结束下标：步长]
    步长：隔一个一取 隔两个一取 每个都取
    省略冒号内的内容意味着默认1
    
    此操作会得到一个新的序列
"""
my_tuple = (0, 1, 2, 3)
resulted = my_tuple[:]  # 从头到尾输出 步长为1
print(f"结果为：{resulted}")

my_str1 = "0123456"
result4 = my_str1[::2]  # 从头到尾输出 步长为2
print(f"结果为：{result4}")


# 集合
""" # 定义集合字面量
    {元素，元素，元素...}
    
    # 定义集合变量
    变量名称 = {元素，元素，元素...}
    
    # 定义空集合
    变量名称 = set()
    
    不支持元素重复 且内容无序
    因此集合没有下标索引
    
    允许修改
"""
my_set_empty = set()

my_set = {"itheima", 1, "itheima"}
print(f"my_set的内容是：{my_set}, 类型是：{type(my_set)}")

# 1.添加新元素  集合.add(元素)
my_set.add("heima")
print(my_set)

# 2.删除元素  集合.remove(元素)
my_set.remove(1)
print(my_set)

# 3.随机取出一个元素  集合.pop()
element = my_set.pop()
print(element)

# 4.清空集合  集合.clear()
my_set_empty.clear()

# 5.取两个集合的差值  集合1.difference(集合2)
set = {"itheima", 2}
set1 = set.difference(my_set)
print(set1)

# 6.消除两个集合的差值  集合1.difference_update(集合2)

# 7.两个集合合并为1个  集合1.union(集合2)

# 8.统计集合元素数量 len(集合)

# 集合的遍历 因集合没有下标索引 所以不使用while循环
for element in my_set:
    print(f"集合的元素有：{element}")


# 字典 dict
""" 通过key找到对应的value
    key；value
    
    # 定义字典字面量
    {key: value, key: value, ...}  键值对
    
    # 定义字典变量
    my_dict = {key: value, key: value, ...}
    
    # 定义空字典
    my_dict = {}  或者   my_dict = dict()
    
    不允许重复
    没有下标索引 只能通过key寻找value
    
    字典可以嵌套 在key里嵌套一个字典 ➡ 表格: 有横向和纵向 横向为key 纵向为value 
"""
my_dict_empty = {}

my_dict = {"小王":99, "小明":88, "小林":77}

# 1.获取value 寻找元素
print(my_dict["小王"])

# 2.嵌套字典 表格
score_dict = {
    "小王": {"语文":99, "数学":99, "英语": 99},
    "小周": {"语文":88, "数学":88, "英语": 88},
    "小林": {"语文":77, "数学":77, "英语": 77}
}
print(f"学生的考试成绩信息是：{score_dict}")

# 3.查询字典信息
score = score_dict["小王"]["语文"]
print(f"小周的语文成绩是：{score}")

# 4.修改字典元素  字典[key] = value
# 如果字典内本身并不存在这个被修改的元素 相当于新增一个元素
my_dict["小林"] = 66

# 5.删除字典元素  字典.pop(key)
my_dict.pop("小明")

# 6.清空字典元素  字典.clear()

# 7.获取全部的key  字典.keys()
keys = score_dict.keys()
print(f"字典的全部key为: {keys}")

# 8.遍历字典
# 方式一 通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是: {key}")
    print(f"字典的value是: {score_dict[key]}")

# 方式二 直接对字典进行for循环 每一次循环都是直接得到key
for key in my_dict:
    print(f"2字典的key是: {key}")
    print(f"2字典的value是: {score_dict[key]}")

# 9.统计字典内的元素数量 len()
number = len(my_dict)
print(f"元素个数为：{my_dict}")


# 数据容器通用操作
""" 容器的通用统计功能：
    len(容器) 统计容器的元素个数
    max(容器) 统计容器中的最大值
    min(容器) 统计容器中的最小值
    
    字符串的比较：比较其ASCII
    
    容器的通用转化功能： (类型转换)
    list(容器)  将给定容器(列表)转化为列表
    str(容器)   将给定容器(字符串)转化为字符串
    tuple(容器) 将给定容器(元组)转化为元组
    set(容器)   将给定容器(集合)转化为集合   内容会变无序
    
    字典无法转换
    
    容器通用排序功能：   sorted(容器, [reverse = True])  将给定容器进行排序
    print(f"列表对象的排序结果：{sorted(my_list)}") 
"""

