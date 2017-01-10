# -*- coding:utf8 -*-

import  win32ui
import  os

dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
dlg.SetOFNInitialDir('D:\\')        # 设置打开的初始位置
dlg.DoModal()

filename = dlg.GetPathName()       # 获取选择的文件名称
print("  选择的文件是： " + filename)
os.system("pause")
