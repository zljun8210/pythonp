# -*- coding:utf8 -*-

import tkinter as tk

window = tk.Tk()
window.title('Hello')
window.geometry('400x200')

l_sf = tk.Label(window,text="Source File: ")
l_sf.place(x=30,y=40)
e_sf = tk.Entry(window,width=20)
e_sf.place(x=120,y=40)

def br_file():
    pass

btn_sf = tk.Button(window,text="浏览",command=br_file)
btn_sf.place(x=280,y=40)

l_tar = tk.Label(window,text="Target File: ")
l_tar.place(x=30,y=80)
e_tar = tk.Entry(window,width=20)
e_tar.place(x=120,y=80)
btn_tar = tk.Button(window,text="浏览",command=br_file)
btn_tar.place(x=280,y=80)


window.mainloop()