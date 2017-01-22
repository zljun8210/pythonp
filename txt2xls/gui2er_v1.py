# -*- coding:utf8 -*-

import tkinter as tk
from tkinter import filedialog
#from FileDialog import LoadFileDialog

window = tk.Tk()
window.title('Hello')
window.geometry('400x200')

def of_file():
    filen = filedialog.askopenfilename(filetypes=[("打开文件", "*.txt")])
    sn.set(filen)

def br_file():
    filename = filedialog.asksaveasfilename(filetypes=[("保存文件", "*.xls")])
    nam.set(filename + '.xls')

sn = tk.StringVar()
nam = tk.StringVar()

def converts():  # 获取txt文档中的数据，并按两列重新写入到xls文件中，其中第2列为内存值，单位为M
    a = 1
    lines = 0
    f = open(sn.get(), "r")
    out = open(nam.get(), "w")
    out.write(" Time \t" + " Memory(M) \n")
    for line in f.readlines():
        #print("    当前数据是: %s" % line.strip())
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

    #print()
    #print()
    #print("\t 一共处理了 %d 组数据" % lines + "\n")
    #print()

l_sf = tk.Label(window,text="Source File: ").place(x=30,y=40)
e_sf = tk.Entry(window,width=30,textvariable =sn )
e_sf.place(x=100,y=40)
btn_sf = tk.Button(window,text="Select ",command=of_file).place(x=300,y=40)

l_tar = tk.Label(window,text="Target File: ").place(x=30,y=80)
e_tar = tk.Entry(window,width=30,textvariable = nam)
e_tar.place(x=100,y=80)
btn_tar = tk.Button(window,text="Save to",command=br_file).place(x=300,y=80)

btn_do = tk.Button(window,text="Convert ",command = converts).place(x=100,y=120)



window.mainloop()
