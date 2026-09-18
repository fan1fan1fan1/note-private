# 5.动态GDP柱状图

# 处理gdp数据
from pyecharts.charts import Bar, Timeline  # 柱状图 时间线
from pyecharts.options import LabelOpts  # 横向

f = open("D:/22820/Desktop/前端 c python/python/gdp.txt", "r", encoding="UTF-8")  # 读取文件时不使用UTF-8 使用GB2312
data_lines = f.readlines()
f.close()


data_dict = {}  # 定义一个字典 便于后续存储数据

for line in data_lines:
    # 读取动态多国家时间线 使用for循环

    year = int(line.split(",")[0])  # 使用 , 对元素今昔分割 第0个元素: 年份1960
    country = line.split(",")[1]  # 第1个元素: 国家
    gdp = float(line.split(",")[2])  # 第2个元素: gdp   科学计数法可以转换成float

    # 若不存在该key 捕获异常
    try:
        data_dict[year].append((country, gdp))
    except KeyError:
        data_dict[year] = []
        data_dict[year].append((country, gdp))


timeline = Timeline()  # 时间线


""" 当数据年份过多时 使用排序
    sorted_year = sorted(data_dict.keys())
    for year in sorted_year:
        data_dict[year].sorted(key=lambda element: element[1], reverse=True)
        year_data = data_dict[year][0:8]    取出本年份gdp前八的国家 
        x_data = []
        y_data = []
        for country_gdp in year_data:
            x_data.append(country_gdp[0])     x轴
            y_data.append(country_gdp[1])     y轴 
"""
sorted_year = sorted(data_dict.keys())
for year in sorted_year:
    data_dict[year].sorted(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8]  # 取出本年份gdp前八的国家
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # x轴
        y_data.append(country_gdp[1] / 100000000)  # y轴


bar3 = Bar()  # 柱状图
x_data.reverse()
y_data.reverse()
bar3.add_xaxis(x_data)
bar3.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))  # 数值位置
bar3.reversal_axis()  # 反转


timeline.add(bar3, str(year))  # 时间线
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
timeline.render("1960全球GDP前8国家.html")
print(data_dict)





# 案例 九九乘法表
# while循环
""" 需要有 控制行的循环(外循环 i<=9) 和 控制列的循环(内循环 j<=i) 
    内层循环输出内容 j*i 每一行i不动 j依次递增每个都输出 此时输出时需要print不换行 end=''
    每一列需要对齐 \t
"""
print()
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t", end='')
        j += 1
    i += 1
    print() # print() 输出空内容 即换行

print()
# 案例 九九乘法表
# for循环
x = 1
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f"{y} * {x} = {y * x}\t", end='')
    print()


# 案例 一个句子 数里面有多少个"a"
name = "it is a brand of itcast"
count = 0  # 定义一个变量用来计数
for x in name:
    if x == "a":
        count += 1  # 进行计数
print(f"被统计的字符串中有{count}个a")


# 案例 猜数字
import random
number = random.randint(1, 100)  # 规定1-100的随机数字
flag = True  # 循环条件标记 通过一个bool类型的变量 做循环是否继续的标记 当flag为true时执行循环 当flag为false时停止循环
count = 0  # 定义一个变量 来记录一共猜测的次数
while flag:
    guess_number = int(input("请输入你猜测的数字"))
    count += 1  # 记录猜测的次数 即循环进行的次数
    if guess_number == number:
        print("猜中了")
        flag = False  # 终止循环
    else:
        if guess_number > number:
            print("你猜大了")
        else:
            print("你猜小了")
print(f"你总共猜测了{count}次")


