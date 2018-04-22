# 继承和多态

# 我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
class Animal(object):
    def run(self):
        print('Animal is running...')


# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
    # 对子类增加一些方法，此处的run方法将重写父类的run方法
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    pass


# 继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

'''
要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。
我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
'''
a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型

# 判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))

# 看来c不仅仅是Dog，c还是Animal！
isinstance(c, Animal)

# 所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：
# Dog可以看成Animal，但Animal不可以看成Dog。
b = Animal()
print(isinstance(b, Dog))

'''
要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：
'''


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog())
run_twice(Cat())

'''
看上去没啥意思，但是仔细想想，现在，如果我们再定义一个Tortoise类型，也从Animal派生：
'''
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())

'''
你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，
然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，
这就是多态的意思：

对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：
调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

对扩展开放：允许新增Animal子类；

对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
'''