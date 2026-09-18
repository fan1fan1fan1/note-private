# 1.访问网页打印源码
import requests
url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers = headers) # 发送请求
"""
等号左边 headers：是 get() 函数规定的参数名
等号右边 headers：是你提前定义好的字典变量（存放浏览器信息）
"""
resp.encoding = "utf-8"
print("响应码状态:", resp.status_code)
print(resp.text[:100]) # 打印源码前100字符



# 2.下载网络图片到本地
from pathlib import Path
img_url = "https://img1.baidu.com/it/u=2329722021,3812422113&fm=253&fmt=auto"
save_path = Path(r"D:\22820\Desktop\code\3.python\tool")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
resp = requests.get(img_url,headers = headers)
if resp.status_code == 200:
    save_path.write_bytes(resp.content)
    print("完成")
else:
    print(f"下载失败,状态码:{resp.status_code}")



# 3.网页源码题取全部文字 beautifulsoup
from bs4 import BeautifulSoup  # 拿到杂乱的网页 HTML 源码，提取你想要的数据（标题、链接、文字）
url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers = headers)
resp.encoding = "utf-8"
soup = BeautifulSoup(resp.text,"html.parser")  # 解析源码 格式化
pure_text = soup.get_text(strip=True)  # 删除网页标签 <xxx> 清除字符\n等
Path(r"D:\22820\Desktop\code\3.python\tool\网页文字.txt").write_text(pure_text,encoding="utf-8")
print("完成")



# 4.批量循环下载多张图片
img_list = [
    ".jpg"
]
save_dir = Path(r"D:\22820\Desktop\code\3.python\tool") # 创建保存空间
save_dir.mkdir(exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
for index,url in enumerate(img_list):
    resp = requests.get(url,headers = headers)
    if resp.status_code == 200:
        save_file = save_dir / f"{index}.jpg"
        save_file.write_bytes(resp.content)
        print(f"已下载:图片_{index}.jpg")



