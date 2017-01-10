# -*- coding:utf8 -*-

import os

'''
功能：从一个文件单列文件中读取数据，以两列内容写入新文件，并计算第2列的值（除1024，取1位小数）；
			文件保存为Excel的xlsx格式；
'''

print("*********************************************************")
print()
fn = input("    请输入要转换的文件名（不包含后缀名）： ")
fn = fn + ".txt"
print()
try:
    f = open(fn)
    data = f.readline()
    f.close()
except:
    print("    文件不存在！！")
    os.system("pause")
    os.system("cls")  # 调用Windonws系统命令

ofn = input("    请输入转换后的文件名（不包含后缀名）： ")
ofn = ofn + ".xls"
print()
print("**********************************************************")

a = 1
f = open(fn, "r")
out = open(ofn, "w")
out.write(" 时间 \t" + " 内存(M) \n")
for line in f.readlines():
    print("    当前数据是: %s" % line.strip())
    if a == 1:
        out.write(line.strip() + "\t")
        a = 0
    else:
        dat = line.strip()
        m = int(''.join(dat.split(',')))  # 数据中如有 ，的，去除，
        m = float(m / 1024)
        out.write("%.2f" % m + "\n")
        a = 1

        # out.write(data)
f.close
out.close()
