import requests

# 你的Cookie（保持不变）
cookie = "buvid4=6E80ED98-C51D-E8BD-7BC8-CF277C21C5C679228-024070307-1GkRBwsQd8lTyGB88dwO8w%3D%3D; enable_web_push=DISABLE; DedeUserID=475184934; DedeUserID__ckMd5=ccf114e3f9b9729a; buvid_fp_plain=undefined; LIVE_BUVID=AUTO3017395323346058; PVID=1; enable_feed_channel=ENABLE; fingerprint=b3472589b00900029d65117cdf8777b4; buvid_fp=b3472589b00900029d65117cdf8777b4; buvid3=3B123060-DE90-122A-418D-17123B4DB1BD35960infoc; b_nut=1751532437; _uuid=126A72C6-7486-DCA3-1D77-6BCD8162A11804035infoc; header_theme_version=OPEN; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; CURRENT_QUALITY=80; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjgxMTUxNDMsImlhdCI6MTc2Nzg1NTg4MywicGx0IjotMX0.eFYNQRjZQjXg3XO5MHWGEKsqjWrrPQudLifNpKmfKH4; bili_ticket_expires=1768115083; SESSDATA=1f6cd9d0%2C1783407945%2C60862%2A11CjCSJgBOzxA1mR-9GBFInxULnTwQaiMPjhu_az9jfcfR7wwkzi4ZKHx-A2DfjU6uPpMSVjRwUHBjbmRPcV8xSUNJVWNzZWVsVDlZVlpMZEdPWkVZMVk5dUlaZUlvMm9YR0dPc1F2YlRSQWF1WHYyWHdWZjJHVkFyQVlwRTVMSW85cHdkb0RwR3d3IIEC; bili_jct=ad9761723060022044c35b0ecf20b46e; home_feed_column=5; CURRENT_FNVAL=2000; browser_resolution=1659-915; b_lsid=51B41710C_19B9C6E4A39; bp_t_offset_475184934=1155421931487363072"
# 补充关键请求头
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://space.bilibili.com/",  # 必加，B站验证来源
    "Origin": "https://www.bilibili.com"       # 必加，B站验证跨域
}
fav_id = 1620745734
url = f"https://api.bilibili.com/x/v3/fav/resource/list?media_id={fav_id}&pn=1&ps=50"

# 发送请求并捕获错误
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # 抛出HTTP错误
    data = response.json()
    print("接口响应成功：")
    print(data)

    # 筛选失效视频（title为“已失效视频”）
    if "data" in data and "medias" in data["data"]:
        invalid_videos = [video for video in data["data"]["medias"] if video.get("title") == "已失效视频"]
        if invalid_videos:
            print("\n找到失效视频：")
            for vid in invalid_videos:
                print(f"BV号：{vid.get('bvid', '无')}")
                print(f"UP主：{vid.get('owner', {}).get('name', '无')}")
                print(f"封面链接：{vid.get('pic', '无')}\n")
        else:
            print("\n当前分页无失效视频，请切换pn参数查看其他分页")
except requests.exceptions.RequestException as e:
    print(f"请求失败：{e}")
    print(f"响应状态码：{response.status_code if 'response' in locals() else '无'}")
    print(f"原始响应内容：{response.text if 'response' in locals() else '无'}")