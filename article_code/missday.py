#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-02 9:20:13
# @Author  : emmmmm

import time

def judgeYear(year):
    if (year%4 == 0) & (year%100 != 0):
        allday = 366
    elif year%400 == 0:
        allday = 366
    else:
        allday = 365
    return allday

def main():
    localt = time.localtime()
    allday = judgeYear(localt.tm_year) # 今年一共有xxx天
    yday = localt.tm_yday # 现在是一年的xxx天
    sad = yday/allday # 一年进度 sad~
    scale = 15 # 进度条长度
    i = int(15*sad)
    passed = '▓' * i # 今年走过的%
    leave = '░' * (scale - i) # 今年剩下的%
    print("\r{0}{1} {2:3.0f}%".format(passed,leave,sad*100),end='')

if __name__ == '__main__':
    main()
