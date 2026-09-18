from pathlib import Path
from unicodedata import category

# 本地文件

# 1.遍历打印名称
folder_path = Path(r"D:\22820\Desktop\code\3.python\tool")
for item in folder_path.iterdir():
    if item.is_file():
        print(item.name)
    elif item.is_dir():
        print(item.name)

# 2.重命名
folder = Path(r"D:\22820\Desktop\code\3.python\tool\laji.txt")
num = 1
for item in folder.iterdir():
    if item.is_file():
        new_name = folder / f"{num}.txt"
        # /是pathlib 独有的路径拼接运算符 等价于拼接路径：D:\22820\Desktop\code\3.python\tool\文件名
        item.rename(new_name) # 重命名 / 移动文件
        num += 1
print("完成")

# 3.按后缀分类 图片文档分开
root = Path(r"D:\22820\Desktop\code\3.python\tool\laji.txt")
category1 = {
    "图片": [".jpg",".png",".gif"],
    "文档": [".txt",".docx",".pdf"]
}
for dir_name in category.keys():   # 创建两个文件夹
    target_folder = root / dir_name
    target_folder.mkdir(exist_ok=True)

for file in root.iterdir():
    if not file.is_file():
        continue
    ext = file.suffix.lower() # 获得后缀
    for folder_name, suffix_list in category1.items():
        if ext in suffix_list:
            file.replace(root / folder_name / file.name)
            break
print("完成")

# 4.读写txt
txt_path = Path(r"D:\22820\Desktop\code\3.python\tool\laji.txt")
txt_path.write_text("111\n222",encoding="utf-8")
content = txt_path.read_text(encoding="utf-8")
print(content)

# 5.查找指定内容的txt
folder = Path(r"D:\22820\Desktop\code\3.python\tool")
keyword = "111"
for txt_file in folder.rglob(f"*{keyword}.txt"):   # * 通配符 任意字符
    try:
        text = txt_file.read_text(encoding="utf-8")
        if keyword in text:
            print(txt_file.name)
    except:
        pass

# 6.总结合并txt
folder = Path(r"D:\22820\Desktop\code\3.python\tool\laji")
output_file = folder / "汇总.txt"
all_content = ""
for txt in folder.rglob("*.txt"):
    try:
        content = txt.read_text(encoding="utf-8")
        all_content += f"===文件:{txt.name}===\n"
        all_content += content + "\n\n"
    except Exception as e:
        print(f"失败,原因:{e}")
output_file.write_text(all_content,encoding="utf-8") # 写入
print("完成")

# 7.清理空文件
folder = Path(r"D:\22820\Desktop\code\3.python\tool\laji")
for file in folder.rglob("*"):
    if file.is_file():
        if file.stat().st_size ==0:
            file.unlink()
            print(f"删除了:{file.name}")
print("完成")

# 8.标准库读写csv
"""
CSV 全称：Comma-Separated Values 逗号分隔值
本质：纯文本表格文件，后缀 .csv
你可以用两种软件打开：
记事本 → 看到原始文本
Excel/WPS → 自动变成整齐表格
"""
import csv
csv_path = Path(r"D:\22820\Desktop\code\3.python\tool\数据.csv")
data = [
    ["姓名","年龄"],
    ["小明",20],
    ["小红",19]
]
with open(csv_path, "w", encoding="utf-8", newline="") as f:
     writer = csv.writer(f)
     writer.writerows(data)   # 一次性写入多行
with open(csv_path, "r", encoding="utf-8") as f:
     reader = csv.reader(f)
     for row in reader:
         print(row)

# 9.简单重复文件筛查
folder = Path(r"D:\22820\Desktop\code\3.python\tool")
size_dict = {}
for file in folder.rglob("*"):
    if file.is_file():
        size = file.stat().st_size
        if size==0:
            continue
        if size not in size_dict:
            size_dict[size] = [file]
for size,file_list in size_dict.items():
    if len(file_list) >= 2:
        print(f"大小{size}字节,疑似重复文件:")
        for f in file_list:
            print(f)

