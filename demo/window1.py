# -*- coding:utf8 -*-

import  tkinter
from tkinter import messagebox

top = tkinter.Tk()

def hello():
    #tkMessageBox.showinfo("Hello ", "你好!")
    messagebox.showinfo("Hello","你好！")


# B = tkinter.BOTTOM(top, text='Hello' , command = hello)
C = tkinter.Canvas(top, bg = "blue", height = 250, width = 300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start = 0, extent = 150, fill =  "green")

C.pack()
# B.pack()
top.mainloop()