#! /usr/bin/python
# -*- coding:utf8 -*-

from random import randint

a = randint(1, 100)  # 赋值一个1到100之间的随机数
qu = False

print("猜猜数字吧 !")

while qu == False:  # 进入猜数过程
    print("")  # 输出空行
    i = input("猜： ")

    if str(a) > i:
        print("说小了！")
        print("")
        print("再猜一次")

    if str(a) < i:
        print("说大了!")
        print("")
        print("再猜一次")

    if str(a) == i:
        print("猜对了！！")
        qu = True

''''
1、 print 输出必须用英文符号（）括起来
2、 要支持中文，必须指明如文件第2行的 Coding
3、 布尔值的False/True，首字母必须大写
4、 条件或判断语句后接 ：后面的内容须换行并缩进
5、 语句以缩进排版为一体
''''
