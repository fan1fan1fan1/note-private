# 1.批量修改图片尺寸
from PIL import Image
from pathlib import Path

# 配置
img_folder = Path(r"D:\22820\Desktop\code\3.python\tool\laji")
output_folder = Path(r"D:\22820\Desktop\code\3.python\tool\laji\pic")
output_folder.mkdir(parents=True, exist_ok=True)

# 遍历图片
for img_file in img_folder.rglob("*.jpg"):
    try:
        img = Image.open(img_file)
        # 修改为宽度800 高度自由等比例缩放
        w,h = img.size
        new_w = 800
        new_h = int(h * new_w / w)  # 等比例缩放高度，防止图片拉伸变形
        img_resized = img.resize((new_w,new_h))

        save_path = output_folder / img_file.name
        img_resized.save(save_path)
        print(f"处理完成: {img_file.name}")
    except Exception as e:
        print(f"失败 {img_file.name} : {e}")



# 2.图片格式转换 png->jpg
from PIL import Image
from pathlib import Path
img_path = Path(r"D:\22820\Desktop\code\3.python\tool\1.png")
img = Image.open(img_path)
# png 转 jpg
if img.mode in ("RGBA","P"):
    """
    
    mode = "RGB" → 三色通道，彩色，无透明
    mode = "RGBA" → 四通道，彩色 + 透明
    mode = "L" → 单通道，黑白灰度，无透明
    mode = "LA" → 双通道，灰度 + 透明
    mode = "P" → 调色板模式，可能存在透明
    """
    # 使用白色底色画布 jpg不支持透明通道，png 透明图转 jpg 必须填充底色
    background = Image.new("RGB", img.size, (255,255,255))
    background.paste(img, mask=img.split()[-1])
    img = background
img.save(r"D:\22820\Desktop\code\3.python\tool\laji\2.jpg")
print("成功")



# 3.批量给图片添加文字水印
from PIL import Image, ImageDraw, ImageFont
img = Image.open(r"D:\22820\Desktop\code\3.python\tool\1.png")
draw = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype("simhei.ttf", 30)
except:
    font = ImageFont.load_default()

text = "水印"
draw.text((20, 20), text, font=font,fill=(255,50,50))
img.save(r"D:\22820\Desktop\code\3.python\tool\laji\2.png")



# 4.类似工资照片水印
from PIL import Image, ImageDraw, ImageFont

# ========== 配置区，按需修改 ==========
img_path = r"D:\22820\Desktop\code\3.python\tool\1.png"
save_path = r"D:\22820\Desktop\code\3.python\tool\laji\2.png"
water_text = "水印"
font_size = 35
angle = -30  # 负数，反向倾斜
gap_x = 180  # 横向水印间距
gap_y = 120  # 纵向水印间距
# 最后数值调高，水印加深 0透明~255不透明
water_color = (120, 120, 120, 200)
# ====================================

# 打开原图
img = Image.open(img_path).convert("RGBA")
w, h = img.size

# 创建透明图层专门画水印
water_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(water_layer)

# 加载字体
try:
    font = ImageFont.truetype("simhei.ttf", font_size)
except:
    font = ImageFont.load_default()

# 获取文字占用大小
bbox = draw.textbbox((0, 0), water_text, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

# 循环平铺绘制倾斜文字
for y in range(-text_h, h + text_h, gap_y):
    for x in range(-text_w, w + text_w, gap_x):
        temp = Image.new("RGBA", (text_w + 50, text_h + 50), (255, 255, 255, 0))
        temp_draw = ImageDraw.Draw(temp)
        temp_draw.text((25, 25), water_text, font=font, fill=water_color)
        temp = temp.rotate(angle, expand=1)
        water_layer.paste(temp, (x, y), mask=temp)

# 合并水印
img.paste(water_layer, mask=water_layer)
img.convert("RGB").save(save_path)
print("水印生成完成")



# 5.批量图片压缩 降低体积不改变分辨率
from PIL import Image
from pathlib import Path

img = Image.open(r"D:\22820\Desktop\code\3.python\tool\1.png")
img.save(r"D:\22820\Desktop\code\3.python\tool\laji\2.png",quality=90)



# 6.彩色图片批量转为灰度图
img_folder = Path(r"D:\22820\Desktop\code\3.python\tool\1.png")
output_folder = Path(r"D:\22820\Desktop\code\3.python\tool\laji\2.png")
output_folder.mkdir(exist_ok=True)
for img_file in img_folder.rglob("*.jpg"):
    try:
        img = Image.open(img_file)
        gray_img = img.convert("L")
        save_path = output_folder / img_file.name
        gray_img.save(save_path)
        print(f"已处理：{img_file.name}")
    except Exception as e:
        print(f"失败 {img_file.name}，错误：{e}")



# 7.生成二维码
import qrcode
content = "https://www.bilibili.com"

# 创建二维码对象容器
qr = qrcode.QRCode(
    version=1,     # 二维码大小
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 容错等级
    box_size=10,   # 每个方块像素大小
    border=2       # 二维码白边宽度
)
"""
error_correction 容错等级
ERROR_CORRECT_L：7% 内容损坏仍可识别
ERROR_CORRECT_M：15%（默认）
ERROR_CORRECT_Q：25%
ERROR_CORRECT_H：30%
等级越高，二维码图案越复杂，适合中间放 logo 的场景。
"""
qr.add_data(content)
qr.make(fit=True) # 根据填入数据生成二维码矩阵
# fit=True：自动选择合适尺寸，不用手动纠结 version

# 生成图片
img = qr.make_image(fill_color="black", back_color="white")
img.save(r"D:\22820\Desktop\code\3.python\tool\二维码.png")
print("完成")



# 8.识别本地图片里的二维码
from pyzbar.pyzbar import decode
from PIL import Image

img_path = r"D:\22820\Desktop\code\3.python\tool\二维码.png"
img = Image.open(img_path)

# 解析二维码
result_list = decode(img)
if not result_list:
    print("未识别到二维码")
else:
    for item in result_list:
        # 解析后的数据从bytes->字符串
        text = item.data.decode("utf-8")
        print("内容为:",text)
        print("类型：", item.type)