# -*- coding:utf8 -*-

import os

'''
功能：从一个文件单列文件中读取数据，以两列内容写入新文件，并计算第2列的值（除1024，取1位小数）；
			文件保存为Excel的xls格式；
			Copright by 曾良均, Ver:0.1
'''

def welcome():
    print(" *********************************************************")
    print(" *                                                       *")
    print(" *    功能介绍：从记录内存数据的Txt文档中获取数据，并按  *")
    print(" *                 格式保存到xls文件中                   *")
    print(" *                                                       *")
    print(" *    Copyright by 曾良均                                *")
    print(" *    Version: 0.1                                       *")
    print(" *    2017/01/03                                         *")
    print(" *                                                       *")
    print(" *********************************************************")

def inputFile():  # 判断录入的文件是否存在，支持相对路径和绝对路径
    exs = False
    while exs == False:
        welcome()
        print()
        print()
        fn = input("    请输入要转换的文件名（不包含后缀名 .txt）： ")
        fn = fn + ".txt"
        print()
        try:
            f = open(fn)
            data = f.readline()
            f.close()
            exs = True
            return fn
        except:
            print("    文件不存在！ 请重新输入!!")
            print()
            os.system("pause")
            os.system("cls")  # 调用Windonws系统命令

def outFile():
    ofn = input("    请输入转换后的文件名（不包含后缀名 .xls）： ")
    ofn = ofn + ".xls"
    print()
    return ofn

def converts(dst,tar):  # 获取txt文档中的数据，并按两列重新写入到xls文件中，其中第2列为内存值，单位为M
    a = 1
    lines = 0
    f = open(dst, "r")
    out = open(tar, "w")
    out.write(" Time \t" + " Memory(M) \n")
    for line in f.readlines():
        print("    当前数据是: %s" % line.strip())
        if a == 1:
            out.write(line.strip() + "\t")  # 以前数据只有1列，转为两列时，第一列后面按制表符
            a = 0
            lines += 1
        else:
            dat = line.strip()
            m = int(''.join(dat.split(',')))  # 数据中如有 ，的，去除，
            m = float(m / 1024)
            out.write("%.2f" % m + "\n")
            a = 1

    f.close()
    out.close()
    print()
    print()
    print("\t 一共处理了 %d 组数据" % lines + "\n")
    print()

if __name__ == '__main__':
    converts(inputFile(),outFile())
    os.system("pause")
