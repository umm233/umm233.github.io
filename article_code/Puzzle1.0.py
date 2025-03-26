#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-22 11:20:03
# @Author  : emmmmm


import os
from PIL import Image

def getImgPath(i):
    pasteImgP = './tuku1/'
    modelImgP = './model/'
    paste_path = pasteImgP + os.listdir('./tuku1/')[i] #列出文件夹下所有的目录与文件
    model_path = modelImgP + os.listdir('./model/')[0]
    # print(model_path)
    # print(paste_path)
    # print(type(model_path)) # str
    return paste_path,model_path


# 打开模板图像，及读取图像尺寸
def openModel(model_path):
    modelImg = Image.open(model_path)
    im1 = modelImg.resize((500,500)) # 重设modelImg的尺寸
    print("修改图像尺寸为: ",im1.size)
    width,height = im1.size # 图片尺寸

    # 修改图像模式为:
    im = im1.convert("L")
    print("修改图像模式为: ",im.mode)
    # 读取像素值
    array = [] # 存放像素值的列表
    # for y in range(0, height, 10):
        # for x in range(0, width, 10):
    for x in range(0, width, 10):
        for y in range(0, height, 10):
            pixel = im.getpixel((x,y))
            array.append(pixel)
    # print(array)
    # print(len(array))
    return array

# 创建新图像 im.resize im.save(path, format, options…)
# eg.im_30.save("D:\\Code\\Python\\test\\img\\test_rotate_30.jpg")


def main():
    model_path = getImgPath(0)[1]
    print(model_path)
    # 新建画布
    imnew = Image.new("RGB", (2500,2500),"#FFFFFF")
    piclen = 1654 # 文件夹下拼接图片数量
    array = openModel(model_path) # 模板像素点数组

    for i in range(len(array)):
        if(i < piclen):
            picI = i
        else:
            picI = i-1000
        pasteImg = getImgPath(picI)[0] # 第picI张图片
        imgpaste = Image.open(pasteImg).resize((50,50))
        # imgpaste = Image.open(modelImg).resize((50,50))
        # 行 Row 列 Column
        row, column = i/50,i%50
        if(10 < array[i] < 245):
            imnew.paste(imgpaste,(int(row*50), int(column*50)))
            print("正在拼接第 %d 张图，还剩下 %d 张" %(i,len(array)-i))
            # print((int(row*50), int(column*50)))
    imnew.show()

if __name__ == '__main__':
    main()
