'''
对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
'''
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

'''
如果知道字符的整数编码，还可以用十六进制这么写str：
'''
print('\u4e2d\u6587')


print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d%%' % 7)#多一个百分号在占位符里面将这个百分号添加近进去
print('Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', 17.125))