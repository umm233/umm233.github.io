#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-16 21:07:57
# @Author  : emmmmm


import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


def hour_Hz(file_path):
    datals = []
    date_h = []
    hour_count = {}

    f = open(file_path)   # 对xx文本的分析
    for i in f:
        datals.append(i.split(",")) # 文本格式分割形成列表
    f.close()

    dateall = datals[0] # datals[0]表示所有date的集合
    # print(len(dateall))
    for i in range(len(dateall)):
        date_h.append((dateall[i][11:13])) # 取时间hour部分 ps.date_h是所有小时的集合
    # print(date_h)

    for key in date_h:
        hour_count[key] = hour_count.get(key, 0) + 1
    # print (hour_count)
    return hour_count

def hour_Hz_plot(file_path):
    hour_sort=[]
    h_key_sort = []

    hour_H = hour_Hz(file_path) #得到时间分析数据，各时间的出现频率
    h_key = list(hour_H.keys())
    ind = np.arange(len(h_key)) # 图表的x轴间隔
    # 整理数据
    for i in range(len(h_key)):
        index = str(i) if i>9 else '0' + str(i)
        hour_sort.append(hour_H[index]) # 整理散乱顺序数据为00-23顺序
        h_key_sort.append(i) # 绘图时x轴刻度

    # 绘图
    fig=plt.figure()
    ax = fig.add_subplot(1,1,1)
    rects1 = ax.plot(ind, hour_sort, 'r-', marker='o') # 设置图表参数
    plt.xticks(np.arange(len(h_key)), h_key_sort) # 画x轴标签
    # plt.show()

def weekday_2_box(file_path):
    datals = []
    date_weekday = []
    weekday_count = {}
    f = open(file_path)
    for i in f:
        datals.append(i.split(","))
    f.close()

    dateall = datals[0]
    # print(len(dateall))
    for i in range(len(dateall)):
        weekday = datetime.strptime((dateall[i][0:10]),"%Y-%M-%d").weekday()+1
        date_weekday.append(weekday)
    all_weekday = date_weekday
    # print(all_weekday)
    fig,ax = plt.subplots(figsize=(5,3))
    plt.boxplot(all_weekday)
    plt.title('weekday boxplot')
    plt.setp(ax,xticklabels=['weekday'])
    plt.grid(True)
    # plt.show()

def main(file_path):
    weekday_2_box(file_path)
    hour_Hz_plot(file_path)
    plt.show()


if __name__ == '__main__':
    # commits-test.txt 为测试文本
    main("commits-test.txt") # 在这里修改成要分析的文本就好，格式：xxx.txt



