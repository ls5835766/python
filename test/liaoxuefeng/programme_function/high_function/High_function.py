#map()、reduce()

'''

map用法

我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回
一个list。
'''

def f(x):
    return x*x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(list(r))

#把这个list所有数字转化为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


'''
reduce用法

reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
'''
from functools import reduce
def add(x,y):
    return x+y

print(reduce(add,[1,2,3,4]))    #序列求和








