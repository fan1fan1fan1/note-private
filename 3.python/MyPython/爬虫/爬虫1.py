""" 在爬虫的全过程中 最好不要在网页源代码中直接进行抓取数据
    通过f12看到的源码与实际源码有区别 最好将网页源代码中的内容复制到html文件中
    在html文件中进行抓取数据
"""


# 爬虫 用程序模拟浏览器 输入网址并获取内容 百度
from urllib.request import urlopen

# from my_packet.test3 import data1

url = "http://www.baidu.com"
resp = urlopen(url)

# 要打印读取数据内容: print(resp.read()) 此为直接输出,输出内容为字符 ->  print(resp.read().decode("UTF-8"))

with open("mybaidu.html", mode="w") as f:
    f.write(resp.read().decode("UTF-8"))  # 得到网页源代码
print("over")
resp.close()



# 1.服务器渲染: 在服务器中把数据和html整合到一起给浏览器 -> 收集信息加入进代码给浏览器    看得到数据
# 2.客户端渲染: 第一次请求得到框架 第二次请求得到数据 在客户端将数据和框架结合            看不到数据
# 熟悉抓包工具 在页面中 F12



# http协议 超文本协议    html(页面源代码)超文本标记语言
""" 请求: 请求行 请求头 网址 状态码Network
    响应: 响应头 协议 响应体HTML json
    
    常见请求头:
        User-Agent 请求载体的身份标识(用于发送请求)
        Referer 防盗链(页面来源 反爬)
        cookie 本地字符串连接数据信息(用户信息 反爬的token)
        
    常见响应头:
        cookie 
        某些字符串(防止攻击和反爬 加密)
        
    常见请求方式:
        GET 查询信息 
        POST 增删改
"""


# Requests包
import requests

url = "https://www.sogou.com/web?query=周杰伦"   # get方式获取数据 人物百度百科
""" 代码简化方法
    query = input("请输入一个你喜欢的明星")
    url = f"https://www.sogou.com/web?query={query}"
"""

# 反爬处理
""" 若输出失败 则需伪装浏览器 (此步骤为可选) 
    当爬虫结果无数据时 首先使用User-Agent
    通过F12 得到Name为web的请求头 寻找User-Agent 后内容复制 成功伪装浏览器
"""
dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/112 SLBVPV/64-bit"
}

resp1 = requests.get(url,headers=dic)

print(resp1)  # <Response [200]>
print(resp1.text)  # .数据显示的方式/类型   .text得到页面源代码
resp1.close()


""" 若没有防护机制 即不需反爬时 
    import requests
    url = "https://www.sogou.com/web?query=周杰伦"
    
    resp1 = requests.get(url)

    print(resp1)  
    print(resp1.text)  
"""


# post方式获取数据 百度翻译
import requests
url = "https://fanyi.baidu.com/sug"   # Name的请求头中 sug得到网址

# 发送的数据内容必须放在字典中 通过data参数进行传递
s = input( "请输入你要翻译的内容")
dat = {
    # payload中得到具体数据
    "kw": s
}

# 发送post请求
res = requests.post(url, data=dat)
print(res.json())   # json()将结果转化为字典
res.close()



import requests
url = "https://movie.douban.com/j/search_subjects"
# 当网址特别复杂时 重新封装参数 将Payload内容复制下
param = {
    "type": "movie",
    "tag": "热门",
    "page_limit": 50,
    "page_start": 0
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/112 SLBVPV/64-bit X-Requested-With:XMLHttpRequest"
}

resp = requests.get(url=url, params=param, headers=headers)
#print(resp.request.headers)
print(resp.json())
resp.close()



# 数据解析概述  从网页源代码中提取数据
# re解析 bs4解析 xpath解析

# re解析 正则表达式 Regular Expression
# 字符排列组合 组成字符串
# https://tool.oschina.net/regex/

# 元字符 具有固定含义的特殊符号
"""  . 匹配所有字符(除了换行符) \w 匹配字母 数字 下划线   \d 匹配数字  \n 换行符   \S 非空白符
     ^ 字符串的开始            \W 非字母 数字 下划线     \D 非数字   [] 指定范围 a-zA-Z0-9  
     $ 字符串的结尾            [^] 指定范围的补集 反义词  n  次数     * 重复0次或更多次         
     + 重复1次或更多次          ? 重复0次或1次          {} 输出数据指定次数        
     
     .*   贪婪匹配 在关键词内尽可能多内容
     .*?  惰性匹配 在关键词内尽可能少内容
"""
import re
lst = re.findall(r"\d+", "我的电话是:10086")   # findall 匹配字符串中所有符合正则的内容
print(lst)

it = re.finditer(r"\d+", "我的电话是:10086")  # finditer 匹配字符串中所有内容 返回迭代器 .group()
# print(it)  输出迭代器
for i in it: # 返回迭代器内容
    # print(i)  返回码
    print(i.group())  # 返回电话号

s = re.search(r"\d+", "我的电话是:10086")  # re.search() 找到一个结果就返回 输出match对象 .group()
print(s.group())

m = re.match(r"\d+", "10086")  # re.match()
print(m.group())

# 预加载 效果:可以反复使用
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话是:10086")
for i in ret:
    print(i.group())



# re模块 使用
S = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋铁</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""

obj = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>", re.S)  # re.S 让.能匹配换行符
# 正则表达式 相同地方落 不同地方 字符串.*? 数字\d
resu = obj.finditer(S)
for it in resu:
    print(it.group())  # 输出了五行全部内容

# 只输出正则符号内容      (?P<需要提取的内容>正则)  提取指定内容
obj1 = re.compile(r"<div class='.*?'><span id='\d+'>(?P<W>.*?)</span></div>", re.S)  # re.S 让.能匹配换行符
# 正则表达式 相同地方落 不同地方 字符串.*? 数字\d
resu1 = obj1.finditer(S)
for it1 in resu1:
    print(it1.group("W"))   # 只输出()内的内容 即W包含的内容



# 豆瓣电影排行榜TOP250
""" 1.得到页面源代码    requests
    2.re提取数据       re
    
    ctrl+f 搜索
"""
import requests
import re
import csv
url = "https://www.douban.com/doulist/3936288/"

user = {
    "User-Agent": "https://www.douban.com/doulist/3936288/"
}

res = requests.get(url, headers=user)
# print(res.text)
page_content = res.text

# 解析数据
""" div
    span
    br
    li
    &nbsp
    
    1.找开始位置 中文 不要的地方.*? 要的地方(?P<>.*?) 结束<标签>
"""
# !!!从此处开始有些许错误 有可能正则错误 有可能需要cookies
obj = re.compile(r'<div class="bd doulist-subject">.*?<div class="rating" class="rating_nums>(?P<name>.*?)</span>',re.S)

# 开始匹配
result = obj.finditer(page_content)

# 创建文件 使爬到的数据直接存储在文件里 将输出结果写成字典
f = open("data.csv", mode="w", encoding="UTF-8")
csvwriter = csv.writer(f)

""" 不使用文件直接输出方式
    for it in result:
        print(it.group("name").strip())  # strip()移除首尾或空行
"""
for it in result:
    # print(it.group("name"))
    dic = it.groupdict()
    # 当数据中有年份时 对其特殊处理: dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())  # row意为输出
f.close()
print("over!")



# 天堂电影信息
# 定位网站 提取父页面网址 提取子页面网址拿到需要下载的地址
import requests
import re
domain = "http://dy.dytt8.net/index.htm" # 域名

resp = requests.get(domain)  # 定义resp verify安全验证
resp.encoding='gb2312'       # (二)匹配输出的编码 gb2312国标码
# print(resp.text)           (一)如果此处输出报错: ⬆⬆ 定义resp时改为get(domain, verify=False)

# 开始提取数据
obj2 = re.compile(r"最新电影更新:.*?<ul>(?P<movie>.*?)</ul>", re.S)
result1 = obj2.finditer(resp.text)

obj3 = re.compile(r"<a href='(?P<href>.*?)'", re.S)  # 取<a href>内容格式
child_href_list = []  # 提取子网址

# !!!正则出错
obj4 = re.compile(r'2024年动画喜剧(?P<name>.*?)<br>.*?'
                  r'<a href="(?P<download>.*?)">2024年动画喜剧《十条命》BD国英双语中字</a><br>', re.S)
# 提取子网址 片名

for it in result1:
     movie = it.group('movie')
     # print(movie)

     # 提取子页面网址
     result2 = obj3.finditer(movie)
     for itt in result2:
         """ (三)当输出子网址内容为总网址的一部分时 需要拼接子网址地址  
             域名+子网址=数据地址           
             child_href = domain + itt.group('href').strip("/")     
             
             在for循环外部定义一个列表保存子页面链接 child_href_list.append(child_href)
             
             本次使用网址不需拼接 
         """
         # print(itt.group('href')) 输出子网址
         child_href = itt.group('href')

         # 确保链接完整性 如果该链接不是以http开头 意味着需要添加domain父链接
         if not child_href.startswith('http'):
             child_href = domain + child_href if domain.endswith('/') else domain + '/' + child_href

         child_href_list.append(child_href)

for href in child_href_list:
    # 输出最终子网址数据
    child_resp = requests.get(href) # 如果不能输出 可以使用verify
    child_resp.encoding = "gb2312"
    print(child_resp.text)

    # 输出片名即片网址
    result3 = obj4.search(child_resp.text)
    # print(result3.group("name"))
    # print(result3.group("download"))
    break  # 测试



# bs4         把页面源代码交给BeautifulSoup 生成bs对象
# 北京新发地 菜价
import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.xinfadi.com.cn/priceDetail.html"
res = requests.get(url)
# print(res.text)

page = BeautifulSoup(res.text, "html.parser") # 指定html解析器
# print(page)

# 解析数据: find(标签, 属性=值)只找第一个   find_all(标签, 属性=值)找全部
table = page.find("li", class_="lis") # 得到该标签内容
print(table)
# html标签属性不能直接复制 为python关键字  1.使用下划线_   2.attrs={"style": "width: 100%"}

# 创建文件 承接获取的数据
f = open("菜价.csv", mode="w")
csvwriter = csv.writer(f)

# 提取表格元素 !!!此处有错误
table1 = page.finditer("table", border_="0", cellspacing_="0", cellpadding_="0")
trs = table1.find_all("tr")[1:]    # 得到该打标签中 th标签内容  [1:]从第一个开始做切片
for tr in trs:
    ths = tr.find_all("th")
    level1 = ths[0].text  # .text 拿到标签包含的内容
    level2 = ths[2].text
    name = ths[3].text
    low = ths[4].text
    ave = ths[5].text
    long = ths[6].text
    place = ths[7].text
    # print(level1, level2, name, low, ave, long, place)
    csvwriter.writerow([level1, level2, name, low, ave, long, place]) # 将获取到的数据放在文件中
f.close()
print("over")  # 输出最终结果



# 抓取优美库图片
# 拿到主页面代码 提取网址 通过href得到子页面 从子页面得到图片下载地址 img -> src 下载图片
import requests
from bs4 import BeautifulSoup
import time
url = "https://www.umtuku.com/"

resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)

# 把源代码交给bs
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="update_area").find_all("a")
# 第一步缩小范围 至该div
# print(alist)
for a in alist:
    href = a.get('href')  # 得到图片数据
    # print(a.get('href'))

    # 得到子页面(图片)源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text

    # 从子页面中得到图片下载链接 请求过程
    child_page = BeautifulSoup(child_page_text, "html.parser")
    p = child_page.find("div", class_="content_left")
    img = p.find("img")
    # print(img.get("src"))
    src = img.get("src")   # 在img标签中 通过.get() 得到具体属性值

    # 下载图片 下载过程
    img_resp = requests.get(src)     # 得到图片
    img_resp.content    # 这里拿到图片的字节
    img_name = src.split("/")[-1]    # 拿到url中的最后一个/以后的内容
    with open(img_name, mode="wb") as f:
        f.write(img_resp.content)    # 图片内容写入文件
    print("over", img_name)
    time.sleep(1)  # 下载过程
print("all over")  # 此时打开文件 图片会加载在文件内



# xpath
# 在XML文档中搜索内容的一门语言 html是XML中的一个子集
""" xml实现的一部分 其中每一个都称为节点
<book> 父节点
      <id> </id> 子节点 彼此称为同胞节点
      <name> </name> 
      <price> </price>
      <auther>
            <nick> </nick>
            <nick> </nick> 
      </auther>            
<book>

寻找name:   /book/name
"""


from lxml import etree
# etree.XML().xpath()
xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <auther>
        <nick id="10086">小周</nick>
        <nick id="10010">小若</nick>
        <nick class="joy">小杰</nick>
        <div>
            <nick>惹了</nick>
        </div>
        <span>
            <nick>没惹</nick>
        </span>
    </auther>
</book>
"""
tree = etree.XML(xml)  # etree.HTML etree.parse
# result = tree.xpath("/book")  直接抓取所有内容

# 想输出name中内容
result = tree.xpath("/book/name/text()")
# print(result)

# 想输出auther中内容
result1 = tree.xpath("/book/auther/nick/text()") # 只有nick前三个内容
                    # /book/auther/div/nick/text() 只有div中的nick
                    # /book/auther//nick/text()    同时拿到所有的nick
# print(result1)

# 想输出auther 中div及span内容 1.可以单独输出 /book/auther/div/text()   /book/auther/span/text()
# 2.一起输出
result2 = tree.xpath("/book/auther/*/nick/text()")   # * 任意节点 通配符
# print(result2)



# 提取html文件中数据
# xml.html
from lxml import etree
tree = etree.parse("xml.html")
# 1.取全部内容
result0 = tree.xpath('/html')
print(result0)

# 2.取全部a href中内容
result01 = tree.xpath("/html/body/ul/li/a/text()")
print(result01)

# 3.取第一个a href中内容  [1]索引 从1开始取
result02 = tree.xpath("/html/body/ul/li[1]/a/text()")
# print(result02)

# 4.取href后是dapao的值  [@属性='属性值']
result3= tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")
# print(result3)

# 想要遍历每一个li
ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    # 5.print(li) 直接遍历

    # 6.需要从每一个li中提取文字信息 <li><a href> </li>
    result4 = li.xpath("./a/text()")  # 在li中继续查找 相对查找需要./
    print(result4)

    # 7.提取文字信息的同时拿到href的值
    result5 = li.xpath("./a/@href")
    print(result5) # 同时使用result4

# 8.想拿到所有的href
print(tree.xpath("/html/body/ul/li/a/@href"))

# 想要快速拿到指定标签的位置并输出 打开html并f12 复制所属元素的标签 粘贴
print(tree.xpath('/html/body/div[1]'))  # 得到编码 想要得到汉字 div[1]/text()
print(tree.xpath('/html/body/ol/li[2]/a/text()'))


