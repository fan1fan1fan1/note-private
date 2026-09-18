"""
日期转换 YYYYMMDD 8位数
汉字 总笔画
count>50篮球
反之 书法

20000101-20240413

零13画
"""
import datetime
start = datetime.date(2000,1,1)
end = datetime.date(2024,4,13)

count = 0 # 篮球

#变汉字
dict = {
    "0":13,
    "1":1,
    "2":2,
    "3":3,
    "4":5,
    "5":4,
    "6":4,
    "7":2,
    "8":2,
    "9":2
}

"""
strftime()   str+time 时间变字符串 变成了8个字符的字符串
timedelta()  时间差    时间间隔
"""
current = start
while current<=end:
    num = 0 # 判50
    data_str = current.strftime("%Y%m%d")  # 20240413 -> 2 0 2 4 0 4 1 3
    for i in data_str:
        dight = i
        num += dict[dight]
    if num>50:
        count+=1
    current += datetime.timedelta(days=1)   # 日期1天1天加   i++
print(count)

FR

