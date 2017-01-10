# -*- coding:utf8 -*-

import os
import tkinter as tk
import fileinput
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext as tkst
from tkinter import *

'''
功能：从一个文件单列文件中读取数据，以两列内容写入新文件，并计算第2列的值（除1024，取1位小数）；
			文件保存为Excel的xls格式；
			Copright by 曾良均, Ver:0.2
更新日志：
  1、 采用图形化界面呈现
  2、 源文件采用选择方式，限制为 txt 文件
'''

t1 = []
root = None

def die(event = None):
    root.destroy()

def about():
    messagebox.showinfo(title = "关于",message = "**作者:曾良均\n**日期：2017/01/04\n**版本：0.2.20170104")

class opreater():
    def __init__(self,rt):
        if rt == None:
            self.t = tk.Tk()
        else:
            self.t = tk.Toplevel(rt)

        self.t.title("数据处理器 ")
        self.t.geometry('420x350')

        self.in_name = tk.StringVar()
        self.lab_input = Label(self.t,text = "    源文件： ")
        self.lab_input.place(x=30,y=40)
        self.ent = Entry(self.t, bd=1)
        self.ent.place(x=100,y=40)
        self.btb = Button(self.t,text = "浏览", command =self.openfilename)
        self.btb.place(x=300,y=40)
        #self.in_name.set(self.openfilename)
        #self.ent.getvar(self.in_name)

        self.lab_output = Label(self.t, text = "    转存为： ")
        self.lab_output.place(x=30,y=80)
        self.ent2 = Entry(self.t,bd = 1)
        self.ent2.place(x=100,y=80)
        #self.ent2.get(self.openfilename)
        self.btb2 = Button(self.t,text = "浏览",command = self.openfilename)
        self.btb2.place(x=300,y=80)

        self.st = tk.Text(self.t)
        self.st.place(x=5,y=120,width=400,height=200)


    def askopenfile(self):

        """Returns an opened file in read mode."""

        return filedialog.askopenfile(mode='r', filetypes=[("打开文件", "*.txt")])

    def openfilename(self):
         filename = filedialog.asksaveasfilename(filetypes=[("打开文件", "*.xls")])

         # open file on your own
         if filename:
            return open(filename, 'w')

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
    root = None
    t1.append(opreater(root))
    root = t1[0].t
    root.mainloop()