# xpath案例  猪八戒网站
""" 1.确认想要的数据在页面源代码中
    2.拿到页面源代码
    3.提取并解析数据
"""

# 猪八戒网
import requests
from lxml import etree

from 爬虫.爬虫1 import main_page

url = "https://www.zbj.com/"
res = requests.get(url)
# print(res.text)

# 解析
html = etree.HTML(res.text)  # parse html xml都是文件处理格式 但是不能混用

# 对页面多盒子提取处理方法 只提取第一个盒子 其他盒子用循环处理
# 1.拿到每一个服务商的div 及拿到小盒子
divs = html.xpath('//*[@id="home-navigation-3"]/div[2]/div[2]/div[1]')  # 当需要所有div时 只需要删除[1]

# 循环  ！！！
for div in divs:  # 每一个服务商信息 每一个盒子信息
    price = div.xpath("./div/div/div[1]/span[1]/text()")  # 拿到第一个price 不包含最高一级div 第一个div即使子div
    title = div.xpath("./div/div/div[2]/span/text()")  # 拿到第二个price 失败
    print(price)

    price = div.xpath("./div/div/a/div[2]/div[1]/span[1]/text()")  # 去掉输出内容所带的格式 去除列表效果 [0].strip("￥")
    title1 = div.xpath("./div/div/a/div[2]/div[2]/p/text()")
    tiylel = div.xpath("./div/div/a/div[2]/div[2]/p/text()")

    print(price)
    print(title1)
    print(tiylel)



# Requests进阶
# cookie 相当于登陆记录 伪装登陆账号访问网站
""" 登录 -> 返回cookies -> 带着cookies请求数据
    使用session进行操作 会话 回合制对话
    session是上述一连串请求 在这个过程中cookies不会丢失
"""

# 小说网
import requests

session = requests.session()
data = {
    "loginName": "15840282318",
    "password": "fy051121"
}

# 检查 network找点login 复制网址
# 1.登录
url = "http://passport.17k.com/ck/user/login"
resp = session.post(url, data=data)  # header最下面的账户信息
# print(resp.text)
# print(resp.cookies) 查看结果

# 2.拿数据
# 在Network中寻找内容为书架书名的文件  两种操作方法
rep = session.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919")

res = requests.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919", headers={
    "Cookies": "GUID=174a733b-f9a5-491f-ab8d-5018a2acc2c0; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F17%252F37%252F81%252F104008137.jpg-88x88%253Fv%253D1739804731000%26id%3D104008137%26nickname%3D%25E9%2599%25B6%25E6%25A0%25BC1%26e%3D1755357439%26s%3D06eb91d241bb2375; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22104008137%22%2C%22%24device_id%22%3A%22195146f46655b2-0124ea544aa01c-57b4037-1821369-195146f4666271b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22174a733b-f9a5-491f-ab8d-5018a2acc2c0%22%7D; tfstk=gMstalgkBWViJ4KujlanmdXaGy23qiBNs1WSmIAil6Cd3snijnxMlKOpHftGh55ADB1Bs1bGn6HNv_nmj5zNhmKDc7VuquXGpn-bZ5PW-Dcwhdh_mCtXOhJ02SDSWuXNQvGUZYhTqjd5S156GsT6AX9yOAtXlFwpOKprlf1XcJepnK36CnTXdH92UnOfGEwddBJxiFyDOqRjDa_ODR3t-Ye0nMp9WInDTmFbndYO2ORLN7sKfFd5CpnbavXoJIdFVW4dLs_1sp5Y2WK5z6IvPnEtadQCeHOMVz3pX9fN2hs86cvHkCQCfeHjcHtHMe_A653w1NfpzpTIHuJhZB6NfweqOO1k6h9B-uwRdE_hbUSgOcK5zOxGl_NnSC_JhglAqgE4hbXFDVeLpqu2fpSzEMpjK7dlVpduBr0que4WpQ2Lpqu25pJpZJj-uq83P; acw_sc__v2=67b3f1812005e8e5edaf04b8e3ae8215c9d15078; Hm_lvt_9793f42b498361373512340937deb2a0=1739804592,1739846019; HMACCOUNT=FFFD9EADF0DFA9DF; ssxmod_itna=YqUxgDn7i=G=dD540Lx0PDQ92eeqx7KqYmKjN4Yt5ND/SFIDnqD=GFDK40EokeYQa0Q7xIPd8aem547Yl4Twv1z7Apx760AcueDHxY=DUx+TgoD4b5GwD0eG+DD4DWDmm7DnxAQDjxGpBUkN/IqDEDYpBDA3Di4D++k=DmqG0DDt8DqG2D7tS0DDl07WQidPYbnr0mWN=2qe5MAwBD0ttxBLPUPwBjeH12Di5ha9qkO=DzqODtwNZ4WQ=6GtxMM03iApxi7+GKD+oRK4YFGGtWOl3YDhtDOxiDx4qeRxiSDLTS3AtSKDAiYK17s4D===; ssxmod_itna2=YqUxgDn7i=G=dD540Lx0PDQ92eeqx7KqYmKjN4Yt5G97k7DBkOOD7phrkBp7GFiDRINY9Dcg5AKqr7eWRI/SCqe+s1+tAwu77K9EYAve/80Aajq5BaCjtkZ=7OMATNvmoHG9lU9iRkjqxml2eCAR3sY7xCQL=GYMqZiAoKsemk7MEBRlUBjOL5y3ne5cAKS4WkiGG73OY488GxGDaXl8xmeb3kGBN4GLoe00=Yl+uT1q7cASoj33tRtR6niU64KRbL8RLhwxMZAn=/9x+Woc3X9RhLY5x9anZx/hkixM5KOk/6STxfoHo27ojxomrTjDDw=LCPqiAtiWmxemq20wD3Y+wo9xinftAtbDfKWmtjDQ7UyD3i9x77w8BKX7D5UwI7GPZX7SpKiTWgrk7DMAuaoqW/ukeWqijzKu+enxY+k+2GbGxDGcDG77iDD=; Hm_lpvt_9793f42b498361373512340937deb2a0=1739846066"
})  # 在此文件中找 Requests Headers 粘贴cookies内的内容

# print(rep.json())



# 处理防盗链问题
""" 在抓取图片代码时 显示检查f12中的video的preview最下方srcUrl链接地址无法打开 
    直接复制标签为video的src地址可以打开链接
    此两者链接地址区别为中间一串代码 错误代码为preview中systemTime内容
    将其更改为原页面显示的地址中  cont-数字  即可

    错误代码 preview srcUrl:"https://video.pearvideo.com/mp4/short/20241231/1739849012562-16042954-hd.mp4"
    正确代码      video src= https://video.pearvideo.com/mp4/short/20241231/cont-1797785-16042954-hd.mp4
"""

# 梨视频
import requests

# 1.原页面链接地址 并得到contId
url = "https://www.pearvideo.com/video_1797785"  # 此处得到contId 为1797785
contId = url.split("_")[1]  # 1797785


# 2.拿到videoStatus返回的json. -> srcUrl  f12中video的headers链接地址
# videoStatus = "https://www.pearvideo.com/videoStatus.jsp?contId=1797785&mrd=0.5890178164461952"


# preview中最下方srcUrl链接地址
# 3.把srcUrl里面的内容进行修改 得到有效链接
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.5890178164461952"


# 防盗链
""" 溯源 referer 当前本次请求的上一级
    当前请求的videoStatusUrl的上一级应该为原页面链接地址 
    如果并不是 则需要使用防盗链referer
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/112 SLBVPV/64-bitX-Requested-With:XMLHttpRequest",
    # 防盗链
    # "Referer": "https://www.pearvideo.com/video_1797785" 请求的上一级 即原页面链接
    "Referer": url
}


reb = requests.get(videoStatusUrl, headers=headers)
# print(reb.text)

dic = reb.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']  # preview中逐一寻找数据
systemTime = dic['systemTime']

srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
print(srcUrl)


# 4.下载视频 准备文件 打开文件
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
f.close()



# 代理
""" 通过第三方机器发送请求
    四种代理: 高匿 普匿 透明 间谍代理
"""
# 百度 站大爷
import requests

# 选择一个用于代理的ip:  183.247.152.98:53281	透明	浙江省杭州市 移动
proxies = {
    # 网站使用http或者https
    "http":"http://183.247.152.98:53281"
}

reb = requests.get("https://www.baidu.com", proxies=proxies)
reb.encoding = 'utf-8'
print(reb.text)



# 网易云音乐热评 (难)
import requests

# 1.找到form data中原未加密的参数
# 2.想办法将参数进行加密 必须参考原地址逻辑  params、encSecKey加密
# 3.拿到数据

url = "https://music.163.com/weapi/comment/resource/comments/get?"
resb = requests.post(url)
# print(resb)

# 在f12 source中代码中搜索send 进行标记 然后打开右侧local 找到requests 刷新至下方链接产生get
# 此位置即被加密的位置 call stack从此处向回找 至链接未被加密的地方





# 异步
""" 多线程(执行单位) 多进程(资源单位 每一个进程至少要有一个线程) 协程
    请求 -> 响应 -> 得到数据
    线程相当于人力 进程相当于项目
    启动一个程序 默认会有一个主线程
    
    异步；不等待前一个任务执行完毕就开始下一个任务 从而提高效率
"""

# 单线程
def func():
    for i in range(1000):
        print("func", i)

if __name__ == '__main__':
    func()
    for i in range(1000):
        print("main", i)



from threading import Thread  # 线程类
def func():   # 子线程
    for i in range(1000):
        print("func", i)

# 多线程(一)
if __name__ == '__main__':
    t = Thread(target=func)  # 创建多线程并给线程安排任务
    t.start()  # 多线程状态为: 可以开始执行该线程 执行时间由CPU决定

    # t2=....   t3=....   t4=....

    func()
    for i in range(1000):  # 主线程
        print("main", i)

# 多线程(二)
class MyThread(Thread):
    # 构造函数 传参 def __init__(self):

    def run(self):  # 继承  当线程开始执行时 执行的即为run
        for i in range(1000):
            print("子线程", i)

if __name__ == '__main__':
    t = MyThread()
    t.start()  # t.run() 单线程

    for i in range(1000):
        print("主线程", i)



# 多线程传参 区分线程
from threading import Thread
def func(name):
    for i in range(1000):
        print(name, i)
if __name__ == '__main__':
    t1 = Thread(target = func, args=("子线程1", ))  # 参数必须是元组
    t1.start()

    t2 = Thread(target = func, args=("子线程2", ))
    t2.start()



# 多进程
from multiprocessing import Process

def func():
    for i in range(1000):
        print("子进程", i)

if __name__ == '__main__':
    p = Process(target=func)
    p.start()

    for i in range(1000):
        print("主进程", i)



# 线程池: 一次性开辟一些线程 我们用户直接给线程池提交任务 线程任务交给线程池完成
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor       # 线程池, 进程池

def fn(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    # 创建50个线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f"线程{i}")

    # 创建进程池 with ProcessPoolExecutor() as t:

    # 等待线程池中的任务全部执行完毕后执行(守护线程)
    print("123")



# 北京新发地菜价表格数据   (使用多线程爬取网页表格数据内容)
# 提取单个页面数据 上线程池提取多个页面数据
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("date.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

def download_one_page(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'

    # print(resp.text)

    html = etree.HTML(resp.text)
    table = html.xpath('//*[@id="index_ajax_list"]')[0]  # 此处不打[0]为列表 加上为表格
    # print(table)

    # 提取 table(在页面源代码中为ul) 中的li的个数

    lis = table.xpath("./li")[1:]  # 此处不加[1:]输出20 其中一个是表头 加上则数字为数据个数
    # 或者也可写为("./li[position()>1])
    # print(len(lis))   # 20 = 表头1 + 数据19个

    # 拿到数据中的每个li
    for li in lis:
        txt = li.xpath("./div/div/a/text()")

        # 数据处理
        txt = (item.replace("\\", "").replace("/", "") for item in txt)

    # !!! 只输出了一个结果
    csvwriter.writerow(txt)
    # print(list(txt))
    print(url, "提取完毕")

if __name__ == '__main__':
    # 得到所有数据

    """
    for i in range(1, 14870):  # 效率低
        # range后为页面数据量 链接上
        download_one_page(f"https://www.umtuku.com/fengjing/{i}")
    """
    # 创建线程池 提交下载任务
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):   # 1意为从第一个开始 每50个任务完成使用一次线程池
            t.submit(download_one_page, f"https://www.umtuku.com/fengjing/{i}")  # 此处数据非表格 因此链接{i}未发挥作用
    print("全部下载完毕")
    f.close()



# 协程
import time

def func():
    print("我爱黎明")
    time.sleep(3)  # 让当前线程处于阻塞状态 cpu不为我工作 降低运行效率 同理input requests.get()
    print("我真的爱黎明")

if __name__ == '__main__':
    func()


""" input程序进入输入状态 操作人需要输入内容 线程处于阻塞状态
    requests.get()发送一个请求到某网址 线程处于阻塞状态
    当程序处于IO操作 线程会处于阻塞状态 相当于运行停止 
    IO状态 输入输出状态
    
    (单线程中)
    协程 当多个任务需要进行 其中一个程序进行IO操作时 选择性切换到其他任务上 当再次遇见IO 再次切换其他任务
    此时cpu利用率最高 提高程序运行效率 视觉上多个任务在同时进行 -> 多任务异步操作
    
    协程运行需要asyncio模块支持
"""
import asyncio
import time

async def func():
    print("你好啊, 我叫赛利亚")

if __name__ == '__main__':
    g = func()  # 使用async后 该函数是一个异步协程函数 此时函数执行得到一个携程对象
    asyncio.run(g)

""" await挂起操作
    暂停当前执行的异步 等待对象 将执行权交给其他事件 允许其他协程在这段时间内执行
"""


# 当前python新版本不支持该写法
async def func1():
    print("你好啊, 我叫潘金莲")
    time.sleep(2)
    await asyncio.sleep(2)  # 异步
    print("你好啊, 我叫潘金莲")

async def func2():
    print("你好啊, 我叫王建国")
    time.sleep(1)
    await asyncio.sleep(1)
    print("你好啊, 我叫王建国")

async def func3():
    print("你好啊, 我叫李雪琴")
    time.sleep(3)
    await asyncio.sleep(3)
    print("你好啊, 我叫李雪琴")

if __name__ == '__main__':
    f1 = func1()  # 定义函数执行
    f2 = func2()
    f3 = func3()
    tasks = [
        f1, f2, f3
    ]

    t1 = time.time()  # 记录执行时间1
    # 一次性启动所有任务
    asyncio.run(asyncio.wait(tasks))
    t2 = time.time()
    print(t2 - t1)  # 记录时间差

""" 在上述程序中 如果使用同步 一共需要6秒 如果使用异步3秒 执行效率提高
    当出现同步操作时 异步就会中断
    上述内容目前可使用的写法:
"""


async def func1():
    print("你好啊, 我叫潘金莲")
    time.sleep(2)
    await asyncio.sleep(2)  # 异步 此处需要进行挂起
    print("你好啊, 我叫潘金莲")

async def func2():
    print("你好啊, 我叫王建国")
    time.sleep(1)
    await asyncio.sleep(1)
    print("你好啊, 我叫王建国")

async def func3():
    print("你好啊, 我叫李雪琴")
    time.sleep(3)
    await asyncio.sleep(3)
    print("你好啊, 我叫李雪琴")

async def main():
    """ 第一种写法
    f1 = func1()
    await f1    调用协程  await要求在函数里使用  await挂起操作放在协程对象前面
    """

    # 第二种写法 推荐
    tasks = [
        func1(),
        func2(),
        func3()
    ]
    await asyncio.gather(*tasks)  # 此处需要进行挂起

    """ 第三种写法
    tasks = [
        asyncio.create_task(func1()),  将函数包装成task任务
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks) 
    """

if __name__ == '__main__':
    t1 = time.time()  # 记录执行时间1
    # 一次性启动所有任务
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)  # 记录时间差



# 可执行的爬虫模板
async def download(url):
    print("准备开始下载")

    await asyncio.sleep(2)   # 网络请求过程  IO操作  requests.get()
    # 加入await后 当进入IO操作后 await挂起 执行其他程序 当IO程序结束后 回到该程序

    print("下载完成")

async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.bilibili.com",
        "http://www.163.com"
    ]

    tasks = []
    for url in urls:
        d = download(url)
        tasks.append(d)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())



# aiohttp包 安装
# requests.get()  转换为异步操作
import asyncio
import aiohttp

urls = [
    "https://img36.tp3001.com/wp-content/uploads/ti/fengjing/5.jpg",   # 如果要爬取图片 后缀名一定是jpg
    "https://img36.tp3001.com/wp-content/uploads/ti/fengjing/188.jpg",
    "https://img36.tp3001.com/wp-content/uploads/ti/fengjing/1097.jpg"
]
async def aiodownload(url):
    # 发送请求 请求过程 下载图片
    name = url.rsplit("/", 1)[1]   # 分割 从右边开始切 切[1] 得到5.jpg   188.jpg   1097.jpg

    # aiohttp.ClientSession()   等价于requests模块
    async with aiohttp.ClientSession() as session:  # 发送请求requests
        async with session.get(url) as resp:        # 得到请求结果 resp = requests.get()

            with open(name, mode="wb") as f:        # 将爬取的数据存入文件 with会自动关闭打开的文件
                # 文件写入操作 属于IO操作 可以使用异步协程 提高效率 aiofiles包
                f.write(await resp.content.read())  # resp.content.read() 等价于resp.text() 但使用异步 需要await挂起

    print(name, "请求完成")

async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())







