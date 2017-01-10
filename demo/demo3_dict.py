# -*- coding:utf8 -*-

x = {'a': 'aaa', 'b': 'bbb', 'c': 12, 5: 'dd'}
print(x['a'])
print(x['b'])
print(x['c'])
print(x[5])

for key in x:
    print("Key is %s and value is %s" % (key, x[key]))

'''
1、 字典x
2、 多组用 ， 隔开
3、 组内ID和值用 ：隔开
4、 此 for 循环里的输出随机:
    Key is c and value is 12
    Key is a and value is aaa
    Key is b and value is bbb
    Key is 5 and value is dd
    
'''
