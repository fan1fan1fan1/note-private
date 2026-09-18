# 1.检测软件是否正在运行并弹窗提示
import psutil
from tkinter import Tk,messagebox
def check_process(process_name:str):
    # 遍历全部进程
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == process_name.lower(): # 获取进程名字 全小写
                return True
        except(psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

# 配置
target = "notepad.exe" # 记事本
if check_process(target):
    root = Tk()
    root.withdraw()
    messagebox.showinfo("检测结果",f"{target}正在运行!")
    root.destroy()
else:
    print(f"{target}未启动")

# 2.磁盘剩余空间监控
disk = psutil.disk_usage("D:\\") # 选择盘符 得到字节大小
total = disk.total / 1024 / 1024 / 1024 # 变成GB大小  换算公式：字节 → GB ÷1024³
free = disk.free / 1024 / 1024 / 1024

print(f"D盘总容量:{total:.2f} GB")
print(f"D盘剩余:{free:.2f} GB")

if free < 10:
    root = Tk()
    root.withdraw()
    messagebox.showwarning("磁盘警告","D盘空间不足10GB,请清理文件!") # 强制输出提醒
    root.destroy()

# 3.获取当前电脑总体CPU 内存占用
import time
while True:
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    free_mem = mem.available / 1024 / 1024 / 1024
    print(f"CPU占用：{cpu}% | 内存占用：{mem_percent}% | 空闲内存：{free_mem:.2f}GB")
    time.sleep(1)

# 4.python调用cmd命令
import subprocess
result = subprocess.run(
    ["ping","www.google.com","-n","2"],
    capture_output=True,
    encoding="utf-8"
)
"""
等价于 CMD 中输入： ping www.google.com -n 2
ping：命令
www.google.com：目标地址
-n 2：发送 2 次数据包
"""
print(result.stdout)

# 5.自动清理n天前的旧文件
def clean_old_files(folder:Path,days:int):
    expire_time = time.time() - days * 24 * 3600
    for file in folder.rglob("*.*"):
        if file.is_file():
            mtime = file.stat().st_mtime
            if mtime < expire_time:
                file.unlink()
                print(f"已删除：{file.name}")
clean_old_files(Path(r"D:\22820\Desktop\code\3.python\tool\laji"),7)