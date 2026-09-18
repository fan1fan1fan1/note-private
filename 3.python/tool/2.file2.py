# office文件

# 1.新建excel
from openpyxl import Workbook
wb = Workbook()        # 创建工作簿
ws = wb.active
ws.title = "数据表格"    # 获取
ws["A1"] = "姓名"
ws["B1"] = "年龄"
ws["A2"] = "张三"
ws["B2"] = "22"        # 写入
wb.save(r"D:\22820\Desktop\code\3.python\tool\execl.xlsx") # 保存

# 2.读取excel内容
from openpyxl import load_workbook
wb = load_workbook(r"D:\22820\Desktop\code\3.python\tool\execl.xlsx")
ws = wb.active
print(ws["A1"].value)
for row in ws.iter_rows(values_only=True):
    print(row)

# 3.excel条件筛选数据
wb = load_workbook(r"D:\22820\Desktop\code\3.python\tool\execl.xlsx")
ws = wb.active
for row in ws.iter_rows(min_row=2,values_only=True):
    name = row[0]
    age = row[1]
    if age and age>10:
        print(name)

# 4.excel求和
wb = load_workbook(r"D:\22820\Desktop\code\3.python\tool\execl.xlsx")
ws = wb.active
total_age = 0
cout = 0
for row in ws.iter_rows(min_row=2,values_only=True):
    age = row[1]
    if isinstance(age,int): # 判断数据类型
        total_age += age
        cout += 1
print(total_age)
print(cout)
if cout > 0:
    print(f"平均年龄:{total_age / cout}")

ws.append(["统计结果"])
ws.append(["总人数",cout])
ws.append(["年龄总和",total_age])
if cout > 0:
    ws.append(["平均年龄",round(total_age / cout)])
wb.save(r"D:\22820\Desktop\code\3.python\tool\execl.xlsx")

# 5.循环批量生成多条数据
wb = Workbook()
ws = wb.active
ws.title = "学生信息"
ws["A1"] = "姓名"
ws["B1"] = "编号"
lst = [
    ["小王",1001],
    ["小李",1002],
    ["小张",1003]
]
for i in lst:
    ws.append(i)
wb.save(r"D:\22820\Desktop\code\3.python\tool\execl.xlsx")

# 6.新建word写入
from docx import Document
doc = Document()
doc.add_paragraph("文字1")
doc.add_paragraph("文字2")
doc.save(r"D:\22820\Desktop\code\3.python\tool\文档.docx")

# 7.读取word
doc = Document(r"D:\22820\Desktop\code\3.python\tool\文档.docx")
for paragraph in doc.paragraphs:
    print(paragraph.text)

# 8.文字加粗 换行 段落格式
doc = Document()
p1 = doc.add_paragraph("文字1")
run = p1.add_run("加粗了") # 定义
run.bold = True # 加粗格式
doc.add_paragraph("文字2")
doc.save(r"D:\22820\Desktop\code\3.python\tool\文档.docx")

# 9.word内自动生成表格
doc = Document()
doc.add_paragraph("人员清单表格")
table = doc.add_table(rows=3, cols=2)
table.cell(0,0).text = "姓名"
table.cell(0,1).text = "年龄"
table.cell(1,0).text = "小明"
table.cell(1,1).text = "20"
table.cell(2,0).text = "小红"
table.cell(2,1).text = "19"
doc.save(r"D:\22820\Desktop\code\3.python\tool\文档.docx")

# 10.新建ppt
# prs.slides 所有幻灯片集合
from pptx import Presentation
prs = Presentation() # 新建空白ppt
slide_layout = prs.slide_layouts[5]
""" 默认空白 PPT 各个下标对应的版式（python-pptx 内置）
[0] → 标题幻灯片（封面版式）
    自带两个占位框：大标题 + 副标题
[1] → 标题和内容
    顶部标题框，下方一大块内容占位框
[2] → 节标题
[3] → 两栏内容
    标题 + 左右两个内容框
[4] → 比较
[5] → 空白版式 ⭐你代码里用的
    页面上！没有任何预设文本框、占位框，干干净净

做 PPT 优先选 [5] 空白版式
"""
slide = prs.slides.add_slide(slide_layout) # 添加幻灯片

text_box = slide.shapes.add_textbox(1,1,4,2) # 添加文本
"""
slide.shapes：当前页面上所有形状（文本框、图片、矩形等）

.add_textbox(left, top, width, height)
四个参数单位：英寸 (inch)
add_textbox(左距离, 上距离, 宽度, 高度)
add_textbox(1, 1, 4, 2)
"""

text_frame = text_box.text_frame # text_frame 文本容器
text_frame.text = "ppt文字"
prs.save(r"D:\22820\Desktop\code\3.python\tool\ppt.pptx")

# 11.幻灯片插入图片
prs = Presentation()
blank_layout = prs.slide_layouts[5]
slide = prs.slides.add_slide(blank_layout)
slide.shapes.add_picture(
    r"D:\22820\Desktop\code\3.python\tool\1.png",
    left = 1,
    top = 1,
    width = 1
)
prs.save(r"D:\22820\Desktop\code\3.python\tool\ppt.pptx")

# 12.多页面批量生成
prs = Presentation()
layout = prs.slide_layouts[5]
page_text = ["第一页内容","第二页内容","第三页内容"]
for text in page_text:
    slide = prs.slides.add_slide(layout)
    text_box = slide.shapes.add_textbox(1,1,4,2)
    text_box.text_frame.text = text
prs.save(r"D:\22820\Desktop\code\3.python\tool\ppt.pptx")