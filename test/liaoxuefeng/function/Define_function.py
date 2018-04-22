#定义函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-99))

'''
空函数
pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
'''
def nop():
     pass


'''
参数检查
让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
'''
def my_ab(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

print(my_ab(1))

'''
返回多个值
比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
'''
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    nz=0
    return nx, ny, nz


x, y ,z= move(100, 100, 60, math.pi / 6)
print(x,y,z)


# 但其实这只是一种假象，Python函数返回的仍然是单一值,而且是个元组：
r = move(100, 100, 60, math.pi / 6)

'''
(151.96152422706632, 70.0)====>原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便
'''
print(r)