from PIL import Image

# 打开 PNG 文件
img = Image.open("/Users/q1/Desktop/website/Blog_v2/static/images/GUIDE.png")

# 保存为 .ico 文件，设置多种分辨率
img.save("GUIDE.ico", format="ICO", sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)])
