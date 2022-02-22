from PIL import Image, ImageDraw, ImageFont
import os

root_path = os.path.dirname(__file__)     # 获取当前目录
profile = Image.open(root_path + "\profile.jpg")    # 将头像打开
font = ImageFont.truetype('C:/Windows/Fonts/msyh.ttc', size=40)  # 确定字体
draw = ImageDraw.Draw(profile)  # 修改图片
draw.text((560, -5), text='99+', fill=(255, 0, 0), font=font)     # 添加字样
profile.show()  # 打开图片
