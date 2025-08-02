#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-25 16:57:55
# @Author  : emmmmm

S = []  # 用于存放尾随后缀(dangling）
arr = []  # 用于存放本次产生的尾随后缀
arrclone = []  # 用于存放数据，克隆arr数组
array = []  # 用于存放原始数据


# 用于第一次寻找
def seek(a):
    a_len = len(a)
    for i in range(a_len):
        for j in range(a_len):
            if len(a[i]) < len(a[j]):

                if a[i] == a[j][0:len(a[i])]:
                    str1 = a[j][len(a[i]):]
                    flag1 = True

                    for k in range(len(S)):
                        if S[k] == str1:
                            flag1 = False
                            break

                    if flag1 and str1 != "":
                        S.append(str1)
                        arr.append(str1)


# 指的是第一次以后的寻找
def seek2(a, ar):
    arr.clear()
    length = len(a)
    length1 = len(ar)

    for i in range(length):
        for j in range(length1):
            if len(a[i]) < len(ar[j]):
                if a[i] == ar[j][0:len(a[i])]:
                    str1 = ar[j][len(a[i]):]
                    flag1 = True

                    for k in range(len(S)):
                        if S[k] == str1:
                            flag1 = False
                            break

                    if flag1 and str1 != "":
                        S.append(str1)
                        arr.append(str1)

                    else:
                        if ar[j] == a[i][0:len(ar[j])]:
                            str1 = a[i][len(ar[j]):]
                            flag1 = True

                            for k in range(len(S)):
                                if S[k] == str1:
                                    flag1 = False
                                    break

                            if flag1 and str1 != "":
                                S.append(str1)
                                arr.append(str1)


def main():
    # N = int(input("请输入C（X）序列中字符串的个数："))
    # array[] 依次用于存放信源码
    # 输入数字以空格隔开
    flag = False
    flag2 = False
    print("请依次输入C（X）序列中的各个字符串：")
    array = input("data: ").split(" ")
    # print(line)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                flag2 = True
                break

    if flag2:
        print("该有限序列C（X）是奇异的")
    else:
        seek(array)
        while len(arr) != 0:
            arrclone = arr.copy()
            seek2(array, arrclone)

        if len(S) == 0:
            print("尾随后缀（dangling suffix）为空，所以C（X）是即时码")
        else:
            print("输出尾随后缀（dangling suffix）的集合：")
            it = iter(S)

            for x in it:
                print(x, end=" ")

            for i in range(len(S)):
                for j in range(len(array)):
                    if S[i] == array[j]:
                        flag = True
                        break
            if flag:
                print("该有限序列C（X）不是唯一可译码")
            else:
                print("该有限序列C（X）是唯一可译码")


if __name__ == '__main__':
    main()
