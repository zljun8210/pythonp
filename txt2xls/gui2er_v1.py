 # -*- coding:utf8 -*-

import tkinter as tk
from tkinter import filedialog
#from FileDialog import LoadFileDialog

window = tk.Tk()
window.title('Converter')
window.geometry('400x400')

def of_file():
    filen = filedialog.askopenfilename(filetypes=[("打开文件", "*.txt")])
    sn.set(filen)

def br_file():
    filename = filedialog.asksaveasfilename(filetypes=[("保存文件", "*.xls")])
    nam.set(filename + '.xls')

sn = tk.StringVar()
nam = tk.StringVar()

def converts():  # 获取txt文档中的数据，并按两列重新写入到xls文件中，其中第2列为内存值，单位为M
    a = 0
    lines = 0
    f = open(sn.get(), "r")
    out = open(nam.get(), "w")
    out.write(" Time \t" + " Memory(M) \t" + " CPU (%) \n")
    t_word["state"] = "normal"
    t_word.delete(0.0)
    t_word.insert("end","开始处理：\n")
    l = 1
    for line in f.readlines():
        t = (l+1)%4
        if t != 0:
            t_word.insert("end","  第 " + str(l) + " 行数据是: " + line.strip())
            t_word.see("end")
        if a == 0:
            out.write(line.strip() + "\t")  # 以前数据只有1列，转为两列时，第一列后面按制表符
            a = 1
            lines += 1
            t_word.insert("end","\n")
            t_word.see("end")
        elif a == 1:
            dat = line.strip()
            m = float(''.join(dat.split(',')))  # 数据中如有 ，的，去除，
            m = float(m / 1048576)
            out.write("%.2f" % m + "\t")
            a = 2
            t_word.insert("end","\n")
            t_word.see("end")
        elif a ==2:
            a = 3
            t_word.see("end")
        else:
            out.write(line.strip() + "\n")  # CPU %
            a = 0
            t_word.insert("end","\n")
            t_word.see("end")
        l+=1

    f.close()
    out.close()

    t_word.insert("end","\n")
    t_word.insert("end","\n")
    t_word.insert("end","\t 一共处理了 "+ str(lines) +" 组数据" + "\n")
    t_word.insert("end","\n")
    t_word["state"] = "disabled"
    t_word.see("end")

l_sf = tk.Label(window,text="Source File: ").place(x=30,y=40)
e_sf = tk.Entry(window,width=28,textvariable =sn )
e_sf.place(x=100,y=40)
btn_sf = tk.Button(window,text="Select ",command=of_file).place(x=310,y=40)

l_tar = tk.Label(window,text="Target File: ").place(x=30,y=80)
e_tar = tk.Entry(window,width=28,textvariable = nam)
e_tar.place(x=100,y=80)
btn_tar = tk.Button(window,text="Save to",command=br_file).place(x=310,y=80)

btn_do = tk.Button(window,text="Convert ",command = converts).place(x=100,y=120)

t_word = tk.Text(window, height=15,width=50,bg = "black", fg = "green",state = "disabled")
t_word.place(x=28,y=160)



window.mainloop()
