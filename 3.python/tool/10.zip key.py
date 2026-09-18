# 1.压缩
import zipfile

with zipfile.ZipFile("output.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write("zip.txt")
# w新建压缩包 ZIP_DEFLATED开启压缩


# 2.解压到当前文件夹
with zipfile.ZipFile("unzip.zip","r") as zf:
    zf.extractall()
# r读取压缩包 extractall()解压


# 3.加密
from cryptography.fernet import Fernet

key = Fernet.generate_key() # 生成密钥
with open ("secret.key","wb") as f:
    f.write(key)

f = Fernet(key) # 用密钥创建工具对象

with open("key.txt","rb") as file: # 读取原始数据
    original = file.read()

encrypted = f.encrypt(original) # 加密

with open("encrypted.txt","wb") as file_out: # 加密文件
    file_out.write(encrypted)


# 4.解密
with open("secret.key","rb") as f: # 读取密钥
    key = f.read()

f = Fernet(key) # 密钥工具类

with open("test_key.enc","rb") as f_in:  # 读取加密内容
    enc_data = f_in.read()

dec_data = f.decrypt(enc_data) # 解密

with open("test_unkey.txt","wb") as f_out: # 恢复原始文件
    f_out.write(dec_data)