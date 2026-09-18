# 1.纯文本邮件
import smtplib
from email.mime.text import MIMEText

# 配置
sender = "你的邮箱@.com"
receiver = "目标邮箱@.com"
password = "授权码"
stmp_server = "smtp.gmail.com"
stmp_port = 465
mail_title = "测试"
mail_content = "内容"

# 邮件内容
msg = MIMEText(mail_content, 'plain', 'utf-8')
msg['Subject'] = mail_title
msg['From'] = sender
msg['To'] = receiver

with smtplib.SMTP_SSL(stmp_server, stmp_port) as server:
    server.login(sender, password)
    server.send_message(msg)
print("成功")



# 2.邮件携带附件
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

# 配置
sender = "你的邮箱@qq.com"
receiver = "接收邮箱@xxx.com"
password = "授权码"
smtp_server = "smtp.qq.com"
smtp_port = 465
attach_file = Path(r"D:\22820\Desktop\code\3.python\tool\1.png")

# 创建复合型邮件（支持正文+附件）
msg = MIMEMultipart()
msg["Subject"] = "带附件邮件"
msg["From"] = sender
msg["To"] = receiver

# 添加正文
body = "你好，附件是图片文件"
msg.attach(MIMEText(body, "plain", "utf-8"))

# 附件
with open(attach_file, "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f'attachment; filename="{attach_file.name}"')
"""
给邮件附件打上标记，告诉接收方邮箱：
这块数据是【附件】，不是邮件正文，允许下载，并且文件名叫什么。
"""
msg.attach(part)

# 发送
with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(sender, password)
    server.send_message(msg)
print("完成")



# 3.简易TCP通信
# (1)服务器代码
import socket

# 监听本机所有地址 端口自定义
HOST = "0.0.0.0"
PORT = 465
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) # 给这个服务端程序绑定指定 IP 和端口
s.listen() # 开启监听模式
print("服务端启动，等待客户端连接...")

conn, addr = s.accept()
"""
accept() 会阻塞程序，停在这里不动，直到有客户端成功连接服务端。
连接成功后返回两组数据。
conn 代表当前这次客户端的通信通道，后续收发数据都依靠 conn。
addr 是元组，保存客户端的 IP 地址和端口号。
"""
print(f"已连接客户端：{addr}")

while True:
    # 接收消息
    data = conn.recv(1024)  # 代表接收对方发来的数据
    if not data:
        break

    msg = data.decode("utf-8")
    print("收到客户端消息：", msg)

    # 回复消息
    reply = "服务端收到：" + msg
    conn.send(reply.encode("utf-8"))
conn.close()



# (2)客户端代码
import socket
HOST = "127.0.0.1"
PORT = 8899
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

send_msg = "测试消息"
client.send(send_msg.encode("utf-8"))

data = client.recv(1024)
print("收到回复:", data.decode("utf-8"))
client.close()