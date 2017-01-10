# -*- coding:utf8 -*-

print("show pictures !")
pst = "*"

for i in range(1, 6, 2):
    for j in range(0, i):
        print(pst, end="")
    print()

for i in range(4, 1, -2):
    for j in range(1, i):
        print("*", end="")
    print()

print()

'''
1、 python 3.5.2中Print函数，默认end为换行，如需连续打印，则要自定义end值；
2、 print必须用括号()包含输出内容；
'''
