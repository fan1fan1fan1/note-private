# 1.定时提醒
import time
from tkinter import Tk,messagebox
def timer_remind(wait_second,title,msg):
    print(f"倒计时开始,等待{wait_second}秒后提醒")
    time.sleep(wait_second)

    # 生成弹窗
    root = Tk()
    root.withdraw() # 隐藏空白主窗口
    messagebox.showinfo(title,msg)
    root.destroy()
timer_remind(10,"休息提醒","起身活动一下!")

# 2.定时提醒 40分钟循环
import time
from tkinter import Tk,messagebox
def timer_remind(wait_second,title,msg):
    print(f"倒计时开始,等待{wait_second}秒后提醒")
    time.sleep(wait_second)
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title,msg)
    root.destroy()
    timer_remind(wait_second,title,msg)

timer_remind(40*60,"休息提醒","起身活动一下!")


# 3.自动复制粘贴 模拟输入 （pyautogui + pyperclip）
import pyautogui
import pyperclip
import time
time.sleep(3)
text = "测试文字"
pyperclip.copy(text) # 复制文字到剪切板
pyautogui.hotkey("ctrl","v") # 模拟粘贴 模板
pyautogui.press("enter") # 按下回车换行

# 4.自动循环输入模板
time.sleep(3)
content = "自动化测试模板"
pyperclip.copy(content)
for i in range(3):
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(1)

# 5.自动连发消息
print("3秒内把光标放到聊天输入框")
time.sleep(3)

text = "干活别久坐记得起来动动"
pyperclip.copy(text)
for _ in range(3):
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(1)

# 6.获取鼠标实时坐标
print("持续输出鼠标坐标，按控制台Ctrl+C停止")
try:
    while True:
        x, y = pyautogui.position()
        print(f"X:{x},Y:{y}")
        time.sleep(1)
except KeyboardInterrupt:
    print("结束")

# 7.自动连续点击 连点器
print("5秒后开始点击，鼠标移左上角停止")
time.sleep(5)
# 连点10次 每次间隔0.8秒
for _ in range(10):
    pyautogui.click()
    time.sleep(0.8)
print("完成")

# 8.防锁屏
print("防锁屏启动，Ctrl+C停止程序")
try:
    while True:
        # 微小移动鼠标 再复原 系统判定有人操作
        pyautogui.moveRel(1,0)
        pyautogui.moveRel(-1,0)
        time.sleep(120) # 间隔两分钟
except KeyboardInterrupt:
    print("结束")

# 9.批量输入文字模板
time.sleep(3)
text = "文字内容"
pyautogui.typewrite(text, interval=0.08) # 间隔0.08
pyautogui.press("enter") # 模拟回车

# 10.窗口自动向下滚动
print("开始自动滚动,移动鼠标到左上角停止")
time.sleep(3)
while True:
    pyautogui.scroll(-120)
    time.sleep(1)

# 11.持续监听剪切板 复制内容保存到txt文档
last_text = ""
sava_pave = "剪切板.txt"
while True:
    content = pyperclip.paste() # 获取剪切板内荣
    if content != last_text:
        last_text = content
        with open(sava_pave,"a",encoding="utf-8") as f:
            """
            r：只读
            w：覆盖写入！会清空原有文件
            a：追加，在文件末尾新增内容，不删除旧内容（当前代码用这个）
            """
            f.write(content+"\n"+"-"*30+"\n")
        print("已保存新剪切内容")
    time.sleep(1)

# 12.批量点击确认弹窗（大量弹窗一直点 “确定”）
time.sleep(3)
# 根据你屏幕，修改坐标！先用下面代码获取坐标
# print(pyautogui.position())
x, y = 920, 530

while True:
    pyautogui.click(x,y)
    time.sleep(1.3)

# 13.模拟按下 Ctrl+S、Ctrl+C 组合键
time.sleep(2)
pyautogui.hotkey("ctrl","s")
time.sleep(1)
pyautogui.hotkey("ctrl","a")




