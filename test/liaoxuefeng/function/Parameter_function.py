# 函数参数

# 我们先写一个计算x²的函数
def power(x):
    return x * x


# 对于power(x)函数，参数x就是一个位置参数。
print(power(5))


# 把power(x)修改为power(x, n)，用来计算xn，说干就干：
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2, 3))

'''
将上诉函数修改为默认参数,默认参数降低了函数调用的难度，
而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。
'''


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


'''
这样，当我们调用power(5)时，相当于调用power(5, 2)：
而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)。
'''


# 可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
nums = (1, 2, 3, 6)
nums1=[1,2,3,4]
print(calc(*nums1))



# 关键字参数
'''
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')

'''
关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，
我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
'''
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

person('Jack', 24, **extra)  # 简便写法


#命名关键字参数

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        print("我是小松鼠")
        pass
    if 'job' in kw:
        # 有job参数
        print("我是小白兔")
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


'''
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
'''
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')