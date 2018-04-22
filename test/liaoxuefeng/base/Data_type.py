"""
 String
"""
print('I\'m,ok')
print('\\\n\\')
print(r'\\\t\\')
print(3>2)
print(3>5)

print('''line1
... line2
... line3''')


'''
and运算是与运算，只有所有都为True，and运算结果才是True：
'''
b = 5 > 3 and 3 > 1
print(b)


'''
or运算是或运算，只要其中有一个为True，or运算结果就是True：
'''
a=5 > 3 or 1 > 3
print(a)

c=not True
print(c)


'''
所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
'''

PI = 3.14159265359
print(10/3)
print(10//3)#地板除