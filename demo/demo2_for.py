# -*- coding:utf8 -*-

sum1 = 0
print("计算:1 + ... + 100 = ")

for i in range(1, 101):
    sum1 += i
    print("现在加到： " + str(i))
    print("计算结果是： " + str(sum1))
    print("")

'''
1、 for循环的range里有三个参数，格式为：
        range(start,end,step)
2、 其中步长可以省略,默认为 1


'''
