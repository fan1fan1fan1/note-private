# 扒一部小说 西游记

""" 寻找包含全部章节目录的文件 getCatalog?data (同步)
    getCatalog?data -> preview -> data -> novel -> item
    得到第一个url
    https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}
    进行改动 https://dushu.baidu.com/api/pc/getDetail?data={"book_id":"4306063500"}
    得到的内容包括章节名称 cid

    点击章节寻找包含小说内容文字的文件 getChapterContent?data (异步)
    getChapterContent?data -> data -> novel -> content
    得到第二个url
    https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|1569782244%22,%22need_bookinfo%22:1}
    进行改动 https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}
"""
import requests
import asyncio
import aiohttp
import json
import aiofiles

from 爬虫.爬虫1 import headers


# 得到第二个url内容
async def aiodownload(cid, b_id, title):
    data = {
        "book_id":b_id,         # "book_id":"4306063500",
        "cid":f"{b_id}|{cid}",  # "cid":"4306063500|1569782244",
        "need_bookinfo":1
    }
    data = json.dumps(data)  # 请求数据
    url = "https://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    # 请求得到数据内容
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = resp.json()

            # 将数据写入文件
            async with aiofiles.open(title, mode="w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])  # 小说内容

# 得到第一个url的内容
async def getCatalog(url):
    resp = requests.get(url)
    # print(resp.text)
    dic = resp.json()

    tasks = []
    for items in dic['data']['novel']['items']:   # 得到每个章节内容的路径
        title = items['title']
        cid = items['cid']
        # print(cid, title)

        # 准备异步任务 第二个url
        tasks.append(aiodownload(cid, b_id, title))
    await asyncio.gather(*tasks)


# 运行第一个url
if __name__ == '__main__':
    b_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+ b_id +'"}'
    # asyncio.run(getCatalog(url))



# 上述实际爬不到结果 下方为正确代码 区别为请求第一个url时应使用异步 整个过程没有requests
async def aiodownload(cid, b_id, title):
    data = {
        "book_id": b_id,
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = "https://dushu.baidu.com/api/pc/getChapterContent?data=" + data
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open(title, mode="w", encoding='utf - 8') as f:
                await f.write(dic['data']['novel']['content'])


async def getCatalog(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            tasks = []
            for items in dic['data']['novel']['items']:
                title = items['title']
                cid = items['cid']
                tasks.append(aiodownload(cid, b_id, title))
            await asyncio.gather(*tasks)


if __name__ == "__main__":
    b_id = "4306063500"
    url = "https://dushu.baidu.com/api/pc/getCatalog?data=" + json.dumps({"book_id": b_id})
    # asyncio.run(getCatalog(url))

# 在极短的时间内 扒完了整部小说 url越多代码的执行效率越高



# 抓取视频
""" 视频网站做法
    用户上传视频 -> 转码(把视频做处理: 压缩 将视频做成多分 分清晰度 4k->2k 改变视频大小) -> 切片处理(把单个的文件或视频进行拆分)
    -> 便于用户进行点播或者拉动进度条 减少用户等待时间 减少服务器压力 -> 此时需要文件 记录视频切片后的播放顺序和视频存储路径   
    
    此文件为 M3U -> M3U8文件(utf-8编码)
    # 表特殊含义  没有#的是链接地址  ts视频切片 
    KEY key.key 加密 密钥
    
    抓取视频的步骤:  
    1.通过各种手段找到M3U8 
    2.通过M3U8下载到ts文件
    3.通过各种手段(不只是编程手段 pr 剪辑工具) 把ts文件合并为一个mp4文件 
"""



# 电影网站 https://www.106s.com/products/14-0-12.html
""" 在页面源代码中寻找video 如果没有 证明视频通过脚本生成
    检查台中寻找m3u8   1.url链接末尾.m3u8   2.文件名index.m3u8 
    找到后在preview可以看到m3u8格式即寻找正确
    
    视频网站的一种反爬程序 note  访问m3u8文件时 不能直接读取到结果 需要note
    note=kkry47&m3u8
    note为m3u8文件 链接地址的一部分 需要通过note 访问kkry47 获取m3u8文件   
    
    1.拿到video的页面源代码
    2.提取m3u8的url
    3.下载m3u8
    4.读取m3u8文件
    5.下载视频
    6.合并视频(切片)
"""
import requests
import re

headers  = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/112 SLBVPV/64-bit"
}

obj = re.compile(r"url: '(?P<url>.*?)',", re.S)  # 用来提取m3u8的地址

url1 = "https://www.106s.com/products/14-0-12.html"  # 拿到页面源代码
resp = requests.get(url1, headers=headers)
resp.encoding = 'utf-8'
# print(resp.text)

m3u8_url = obj.search(resp.text).group("url1")  # 拿到url地址    报错!!!
# print(m3u8_url)
resp.close()

# 下载
resp2 = requests.get(m3u8_url, headers=headers)

with open("video", mode="wb") as f:
    f.write(resp2.content)  # 二进制

resp2.close()
print("下载完毕")



# 解析m3u8文件




















