# 函数作为返回值
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


'''
如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量才被新函数引用，
所以，返回的函数并没有立刻执行，而是直到调用了f()才执行。

闭包：在一个外函数中定义一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用
'''


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7)
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
print(f)

# 调用函数f时，才真正计算求和的结果：
print(f())

# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f == f2)  # 说明f1()和f2()的调用相互不影响



def count():
    fs = []
    for i in range(1, 4):

        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

'''
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''
print(f1())
print(f2())
print(f3())


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def One():

    #此处是闭包
    def f(j):
        def g():
            return j * j

        return g


    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


fa, fb, fc = One()

print(fa())
print(fb())
print(fc())


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    def f():
        x = 0
        while True:
            x += 1
            yield x

    it = f()

    def number():
        return next(it)

    return number


createA = createCounter()
print(createA())
print(createA())
print(createA())
print(createA())
print(createA())


