from __future__ import print_function
from PIL import Image
'''
读取两个图片  

使用后者异于前者的部分产生相同格式的新图片  

pillow
'''
#打开图像文件
img1=Image.open("data/lena.png")
img2=Image.open("data/lena_modified.png")
#获得图像尺寸
x,y=img2.size

for i in range(0,x):
    for j in range(0,y):
        #获取像素值
        if img1.getpixel((i,j))==img2.getpixel((i,j)):
            # 将像素值相同的地方涂白
            img2.putpixel((i,j),255)
img2.save("ans_two.png")