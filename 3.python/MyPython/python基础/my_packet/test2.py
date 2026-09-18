# 函数多返回值输出方法
""" 在定义函数后 使用两个print
    print(result1)
    print(result2)
"""
from random import random

# 函数的多种传参方式
""" 函数常见四种参数:
        位置参数：   根据函数定义的参数位置传递参数
        关键字参数： 函数调用时：键=值 形式传递参数
        缺省参数：   默认参数 固定一个参数值 输出时可以改变该默认参数 默认参数必须写在最后
        不定长参数： 可变参数 不确定调用时会传递多少个参数
                   分为位置传递和关键字传递
"""

# 位置参数
def user_info(name, age, gender):
    print(f"您的名字是{name}，年龄是{age}，性别是{gender}")
user_info('Tom', 20, '男')

# 关键字参数
def user_foot(name, age, gender):
    print(f"您的名字是：{name}, 年龄是：{age}，性别是：{gender}")
user_foot(name="小明", age="20", gender="男")  # 可以不按照顺序

# 缺省参数
# def user_nan(name, age, gender="男"):

# 不定长参数 位置传递
def user_xing(*args):
    print(args)  # args为元组类型
user_xing('Tom', 18)

# 不定长参数 关键字传递
def user_xings(**kwargs):
    print(kwargs)
user_xings(name='Tom', age=18)


# 函数作为参数传递 定义两个函数 将一个函数套在另一个函数里
# lambda匿名函数
""" 无名称函数 只能临时使用一次
    lambda 传入参数: 函数体() 
    函数体只能有一行
"""
def test_func(compute):
    result5 = compute(1, 2)
    print(result5)
def compute(x, y):
    return x + y

test_func(compute)  # 输出方式一
test_func(lambda x, y: x + y)  # 输出方式二

# 文件编码 利用二进制
# 文件操作 打开文件 open()
""" python读取文件地址 斜杠需要反向

    open(name, mode, encoding)
    name: 目标文件字符串 
    mode: 设置访问模式 读 写 加
    encoding: 编码格式 UTF-8

    r只读 w写入 a追加  r+读和写

    文件读取方法 文件.read(num)  其中num表示需要读取的字节 若不指出num则读取全部数据
                readlines()    按照行的方式把整个文件内容读取 并返回列表
                readline()     一次只读取一行内容
                for循环读取文件行

    with open 语法: (代替open) 自动完成文件关闭 不用写f.close() 

"""
f = open("D:/22820/Desktop/前端 c python/C/目录.txt", "r+", encoding="UTF-8")  # f是该文件文件对象

print(f"读取10个字节结果：{f.read(10)}")  # 程序中多次调用read 则会接着上一个调用的read卡死hi调用

content = f.readlines()
print(f"content的内容是：{content}")  # \n换行效果

"""
for line in open("D:/22820/Desktop/前端 c python/C/目录.txt", "r+"):
    print(line)   每一个line临时变量 就记录了文件的一行数据
"""

# 文件的写出操作
""" f.write() 文件写入 文件进入缓冲区
    f.flush() 内容更新 文件进入硬盘内存 f.close()内置了flush的功能 
    
    import time
    f.write("hello world")
    f.flush()
    time.sleep(60000)   用于暂停 控制程序运行节奏
    f.close()
"""


# 文件的追加操作 追加到文件的最后
""" # 打开文件 a模式
    f = open(文件，'a')
    f.write("hello world")
    f.flush()
    f.close()
"""


# 异常 bug python报错
""" 获取异常(异常处理): 对可能出现的bug进行提前准备 提前处理   
    bug产生效果: 1.整个程序因为bug停止  2.对bug提醒，并继续执行程序

    try:
        可能出现错误的代码
    except:
        如果出现异常执行的代码    

    try:
        print(name)
    except NameError as e：
        e为一个别名
        print('name变量名称未定义错误') 
    异常输出: ZeroDivisionError NameError

    捕获指定异常: except NameError as e: 
    捕获多个异常: except (NameError, ZeroDivisionError) as e:
    捕获所有异常: except Exception as e:

    异常的传递： 一个函数中有异常 另一个函数引用了这个函数           
"""
try:
    # 正常情况
    f = open("D:/22820/Desktop/前端 c python/python/目录.txt", 'r')
except:
    # 出现异常时
    print("文件不存在，我将open模式改为w打开")
    f = open("D:/22820/Desktop/前端 c python/python/目录.txt", 'w')
else:
    # 没出现异常时
    print(f"没有异常")  # 此内容也可以写在try里
finally:
    # 无论出不出现异常 都会输出的
    print(f"执行")
f.close()

# 模块module
""" 是一个python文件 以.py结尾
    可以定义函数 类 变量
    用作实现某些功能  eg.time模块可以实现关于时间的相关功能

    模块[from 模块名] import [模块 | 类 | 变量 | 函数 |*] [as 别名]
    import 模块名
    import 模块名2
    模块名.功能名()
    
    eg. import 模块名
        from 模块名 import 类 变量 方法
        from 模块名 import *
        import 模块名 as 别名
        from 模块名 import 功能名 as 别名   1
    其中 中括号[]表示可选 import必写     
"""

# 时间time 可使用其中所有函数
# 时间模块中有sleep函数  执行了一个时间模块：输出开始  暂停1s 输出结束
import time
print("开始")
time.sleep(1)  # 通过.可以使用模块内部的全部功能  暂停1s
print("结束")

# 导入time模块中的sleep方法
# 只使用sleep函数
from time import sleep
print("开始")
sleep(1)
print("结束")

# as别名 相当于给sleep起一个名字
import time as tt  # 使用from也是一样的
tt.sleep(2)
print("hello")


# 自定义模块：新建一个python文件 在里面定义函数
import my_module1
my_module1.test(10, 20)   # 30

""" 如果设置了两个重名文件函数 则第二个直接把第一个函数覆盖掉 执行第二个函数
    
    模块测试方法：   __main__   
    直接写main然后回车
    if __name__ == '__main__':
    
   __all__ 作用在列表上 只在函数内导入all的列表       
"""

# 使用python包 my_module1
__all__ = ['test_A']
from my_module1 import *   # 当有两个以上模块时 使用* 表示全部包括
test_A(1, 2)         # 只能执行testA


# python包
""" 相当于一个文件夹 用于储存管理不同的模块
    __init__.py 文件   python包象征

    all 必须写在__init_.py里
     导入方法1: import 包名.模块名
               包名.模块名.目标 
"""

import python基础.my_packet.my_module1
python基础.my_packet.my_module1.info_print1()
""" 方法2: from my_packet import_my_module1         
           my_module1.info_print1()
    方法3: from my_packet my_module1 import info_print1
           info_print1() 
"""

# 通过all控制import 假设有print2
from python基础.my_packet import *
my_module1.info_print1()


# 第三方包
""" 衍生包(非python官方)  
    numpy科学计数包 pandas数据分析包 pyspark、apache-flink大数据计算包
    matplotlib、pyecharts图形可视化包 tensorflow人工智能包
    
    命令提示符程序 pip install 包名称
                 pip install-i https://pypi.tuna.tsinghua.edu.cn/simple 包名称
"""


# json技术
""" Echarts框架 数据可视化 源产生于js语言 pyecharts包
    json数据交互格式 用于组织和封装数据 负责数据传递和交互: 中文->英文 方言->普通话  python格式->json->c语言格式
    
    展示中文方法：data1 = json.dumps(json1, ensure_ascii=False)
"""
import json  # 导入json模块

json1 = {"name":"admin", "age":18}  # json字典格式
json2 = '[{"name":"admin", "age":18},{"name":"root", "age":18},{"name":"张三", "age":16}]'  # json列表格式(嵌套字典)

data1 = json.dumps(json1, ensure_ascii=False)  # 将python转化为json方法
data2 = json.loads(json2)  # 将json转化为python方法

print(data1)
print(data2)


# 数据可视化pyecharts
""" pyecharts模块中配置选项：
        全局配置选项 对标题 图像比例配置 set_global_opts方法
        系列配置选项 对x y轴配置 

    set_global_opts设置全局配置项；
        TitleOpts 标题配置项   LegendOpts 图例配置项   ToolboxOpts 工具箱配置项
        VisualMapOpts 视觉映射配置项   TooltipOpts 提示框配置项   DataZoomOpts 区域缩放配置项         
        
    数据处理 ab173
"""
# 1.折线图
from pyecharts.charts import Line  # 导入line功能构建折线图
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,TooltipOpts  # 用于设置全局配置选项

line = Line()                                         # 得到折线图对象
line.add_xaxis(["中国", "美国", "英国"])                # x轴
line.add_yaxis("GDP", [30, 20, 10])  # y轴

# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True)
)
line.render("折线图.html")                                         # 生成图表


# 2.地图
""" 1.导入模块
    2.导入文件 f.()
    3.导入数据 json
    4.分析数据 创建列表
    5.构建地图 图标 表格 pyecharts
    6.设置全局选项 绘图
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map1 = Map()
data = [
    ("北京省", 99),
    ("上海省",399),
    ("湖南省",1000),
    ("河北省",499),
    ("山东省",5000),
    ("内蒙古省",600),
]
map1.add("地图", data, "china")

map1.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,   # 手动校准
    pieces=[
        {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},  # min max当前这段的最小，大
        {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
        {"min": 100, "max": 499, "label": "99-499人", "color": "#FF9966"},
        {"min": 500, "max": 999, "label": "499-999人", "color": "#FF6666"},
        {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
        {"min": 10000, "label": "10000以上", "color": "#990033"}
    ])
)
map1.render("地图.html")  # " "包命名


# 3.动态柱状图
from pyecharts.charts import Bar   # Bar功能 构建柱状图对象
from pyecharts.options import LabelOpts

bar = Bar()

bar.add_xaxis(["中国", "美国", "英国"])  # x轴
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))  # y轴
# label_opts用于调整表头数据值的位置

bar.reversal_axis()  # 反转x y轴
bar.render("基础柱状图.html")


# 4.时间线 柱状图绘制 (动态)
""" Timeline 相当于一个x轴 轴上的每一个点就是一个图表对象
    即时间1时提供一个柱状图表 时间2提供下一张柱状图表
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType  # 设置主题

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10])

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 30, 20])

# 创建时间线对象
timeline = Timeline(
    {"theme": ThemeType.LIGHT}   # 主题
)
timeline.add(bar1, "2023年GDP")
timeline.add(bar2, "2024年GDP")

# 设置自动播放
timeline.add_schema(
    play_interval=1000,     # 时间间隔
    is_timeline_show=True,  # 是否显示时间线
    is_auto_play=True,      # 是否自动播放
    is_loop_play=True       # 是否循环播放
)
timeline.render("基础柱状图-时间线.html")


# 5.动态GDP柱状图
""" 列表.sort(key=排序依据的函数, reverse=True|False)
    key是函数 排序依据
    reverse是否反转排序结果 true表升序 false表降序

    GDP柱状图: 数据单位大 有时间轴 xy轴反转 标题 主题为LIGHT

    将数据转化成字典 {年份: [[国家，gdp]，[国家，gdp]...],年份: [[国家，gdp]，[国家，gdp]...]}
"""
# (1)有名的函数
my_list = [["a", 33], ["b", 55], ["c", 11]]

def choose_sort_key(element):
    # 定义排序方法
    return element[1]  # 按照列表下标的数字排序 element[a]

my_list.sort(key=choose_sort_key, reverse=True)  # 升序
print(my_list)


# (2)匿名函数lambda
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)



# 使用对象组织数据
# 1.在程序中设计表格 class
""" class 类名称:
        成员变量 类的对象 
        成员方法 类的行为
    
    创建类对象的语法   对象 = 类名称()
    
    类中函数语法
    def 方法名(self, 形参):
        方法体
"""
class Student:
    name = None  # 记录学生 初始设置None   类的对象
    gender = None
    nationality = None
    native_place = None
    age = None

    def say_hi(self):
        print(f"hi大家好，我是{self.name}")  # 类的行为


# 2.在程序中打印生产表格 创建对象
stu_1 = Student()  # 根据类
stu_2 = Student()

# 3.在程序中填写表格 对象属性赋值
stu_1.name = "周杰伦"  # 学生1的名称属性值
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "山东省"
stu_1.age = 31
stu_2.name = "林俊杰"  # 学生2的名称属性值

stu_1.say_hi()  # 输出hi大家好，我是{self.name}周杰伦

print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)


# 面向对象
class Clock:
    id = None         # 序列号
    price = None      # 零售价

    # 行为
    def ring(self):   # 响铃
        import winsound  # 内置模块 响铃 发出声音
        winsound.Beep(2000, 3000)

clock1 = Clock()  # 基于类创建对象
Clock.id = "003032"
clock1.price = 19.99
print(f"闹钟id：{clock1.id}, 价格：{clock1.price}")  # 使用对象的属性和行为
clock1.ring()


# 构造方法  __init__()
# 自动执行(不调用也会执行)
class Student:
    # 在init中 以下三个定义可不写
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个对象")
stu = Student("周杰伦", 31, "185500006666")


# 内置方法(魔术方法)
""" 常见5种:
        __init__ 构造方法
        __str__  字符串方法
        __lt__   < >
        __le__   <= >= 
        __eq__   ==
"""

# __str__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"student类对象, name={self.name}, age={self.age}"
student = Student("周杰伦", 11)
print(student)
print(str(student))
""" 不使用__str__: 
     <__main__.Student object at 0x0000028E3A251B50> 
     <__main__.Student object at 0x0000028E3A251B50>
    使用__str__:
     student类对象, name=周杰伦, age=11
     student类对象, name=周杰伦, age=11
"""

# __lt__  __le__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 两个对象通过定义lt可以进行比较 不定义不能比较  other指相对于一个对象的另一个对象
    def __lt__(self, other):   # def __le__(self, other)
        return self.age < other.age
stu1 = Student("小周", 11)
stu2 = Student("小林", 13)
print(stu1 < stu2)  # 结果true
print(stu1 > stu2)  # 结果false

# __eq__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age
stu3 = Student("小周", 11)
stu4 = Student("小林", 11)
print(stu3 == stu4)   # 结果true


# 面向对象: 封装 继承 多态
""" 封装: 将现实世界的 属性和行为 -> 成员变量和成员方法
    私有成员: 对现实世界中不公开的内容 在程序中的映射 
        私有成员变量 私有成员方法 -> 私有成员变量 私有成员方法: 变量名以__开头  
"""

# 1.封装
class Phone:
   # IMEI = None
   # producer = None

    __current__voltage = 1.2  # 当前电压(私有成员变量)

    def __keep_single_core(self):  # 私有成员方法
        print("让CPU以单核模式运行以节省电量")

    # 私有成员不能被类对象使用，但可以被其他成员使用 即公开私有成员
    def call_by_5g(self):
        if self.__current__voltage >= 1:
            print("5g通话开始")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核运行进行省电")

""" phone = Phone()     
    phone.__keep_single_core() 私有对象无法直接被类对象使用
    
    phone.__current_voltage = 33 私有对象无法赋值
    print(phone.__current_voltage) 也无法获取值
"""
phone = Phone()
phone.call_by_5g()  # 输出 5g通话已开启
# print(phone.__current_voltage)


# 2.继承
""" class 类名(父类名):
        类内容体
"""

# 单继承
class Phone2024:
    IMEI = None      # 序列号
    producer = "HM"  # 厂商

    def call_by_4g(self):
        print("4g通话")

class Phone2025(Phone2024):
    face_id = True   # 面部识别

    def call_by_5g(self):
        print("2025最新5g手机")
phone = Phone2024()
print(phone.producer)
phone.call_by_4g()

phone1 = Phone2025()
phone1.call_by_5g()

# 多继承
""" class 1
    class 2
    class 3
    
    class 总(1, 2, 3):
        pass 
"""


# 复写
""" 子类继承父类后 对父类成员的属性不满意 则可以重新定义属性或方法
    直接指出该属性并进行描述
"""
class Phone1:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("父类的5g通话")
class Phone2:
    producer = "ITHEIMA"  # 复写

    def call_by_5g(self):
        print("子类的5g通话")
phone2 = Phone1()
phone2.call_by_5g()
print(phone2.producer)




