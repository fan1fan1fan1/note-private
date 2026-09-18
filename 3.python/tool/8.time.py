# 1.间隔多久执行一次
import schedule
import time

def job():
    print("任务执行了")

# 每5秒调用一次job函数
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)



# 2.指定时间
# 指定每天固定时刻执行，每天 22 点 00 分弹出提醒
def daily_notice():
    print("执行")

schedule.every().day.at("22:00").do(daily_notice)
print("启动")

while True:
    schedule.run_pending()
    time.sleep(1)



# 3.取消任务，动态移除定时任务
job = schedule.every(5).seconds.do(job)
cnt = 0
while True:
    schedule.run_pending()
    time.sleep(1)
    cnt += 1
    if cnt > 10:
        schedule.cancel_job(job)
print("任务取消")



# 4.pyinstaller 打包，把 py 脚本变成 exe 程序 电脑
