#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-21 15:28:35
# @Author  : emmmmm


import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter
import numpy as np

def pi_formatter(x, pos):
    """
    比较罗嗦地将数值转换为以pi/4为单位的刻度文本
    """
    m = np.round(x / (np.pi/4))
    n = 4
    if m%2==0: m, n = m/2, n/2
    if m%2==0: m, n = m/2, n/2
    if m == 0:
        return "0"
    if m == 1 and n == 1:
        return "$\\pi$"
    if n == 1:
        return r"$%d \pi$" % m
    if m == 1:
        return r"$\frac{\pi}{%d}$" % n
    return r"$\frac{%d \pi}{%d}$" % (m,n)

def main():
    plt.grid() #开启网格
    plt.gca().xaxis.set_major_locator( MultipleLocator(np.pi) )
    plt.gca().xaxis.set_major_formatter( FuncFormatter( pi_formatter ) )
    plt.gca().xaxis.set_minor_locator( MultipleLocator(np.pi/20) )
    plt.subplots_adjust(bottom = 0.1)
    # 判断是与初始相位还是末相位比较
    forwordOrlast = input("与初始相位(0)还是末相位(1)比较: ")
    # mustCode = [0,1,1,0,1,0]
    mustCode = list(eval(input("please input a list:  ")))
    # print(mustCode)
    delta = [] # 储存所有相位变化值
    fc, Rb = eval(input("fc, Rb = "))
    Tb = fc/Rb*2*np.pi # 一个波形周期
    fai0, fai1 = eval(input("fai0,fai1 = \t"))
    fai0 = fai0*np.pi
    fai1 = fai1*np.pi
    deltaAdd = 0 # 相位总变化量
    # 参考波形
    x1 = np.linspace(0, Tb, 100)
    y1 = np.sin(x1 + deltaAdd)
    plt.plot(x1,y1)

    for i in range(len(mustCode)):
        if mustCode[i] == 1:
            delta.append(fai1)
        else:
            delta.append(fai0)
        if forwordOrlast == '1':
            deltaAdd = deltaAdd + delta[i]
        elif forwordOrlast == '0':
            deltaAdd = deltaAdd + delta[i] - Tb
        else:
            print("input data is wrong")
        x1 = np.linspace((i+1)*Tb, i*Tb+2*Tb, 100)
        y1 = np.sin(x1 + deltaAdd)
        plt.plot(x1,y1)
    plt.show()

if __name__ == '__main__':
    main()
