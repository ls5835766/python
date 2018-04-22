# 获取对象信息

'''
使用type
'''
print(type(123))
print(type('str'))
print(type(None))

# 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))

# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

'''
使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
# 同时可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
'''
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

'''
使用dir()
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：

__len__返回对象长度
'''
print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())


# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))

# 剩下的都是普通属性或方法，比如lower()返回小写的字符串：
print('ABC'.lower())


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

hasattr(obj, 'x')  # 有属性'x'吗？
hasattr(obj, 'y')  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
hasattr(obj, 'y')  # 有属性'y'吗？
getattr(obj, 'y')  # 获取属性'y'
obj.y  # 获取属性'y'

# 如果试图获取不存在的属性，会抛出AttributeError的错误：
getattr(obj, 'z')  # 获取属性'z'

# 可以传入一个default参数，如果属性不存在，就返回默认值：
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
