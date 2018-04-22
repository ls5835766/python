'''
以Student类为例，在Python中，定义类是通过class关键字：

class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
'''


class Student(object):
    pass


bart = Student()
print(bart)

print(Student)

bart.name = "zhangy"
print(bart.name)

'''
由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
'''


class Students(object):
    # 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 数据封装
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
barts = Students('zhangy', 59)
lisa = Students("xiaom", 99)
print(barts.print_score())
print(barts.name, barts.get_grade())
print(lisa.name, lisa.get_grade())

# 上面的代码是可以被自由修改一个实例的name，score属性
b = Students('xx', 66)
b.name = 'aa'
print(b.print_score())

'''
针对上面的问题，如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

'''


class Studentss(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法,允许外部代码修改score怎么办？可以再给Student类增加set_score方法：

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def set_name(self,name):
        self.__name = name


bartzz = Studentss('Bart Simpson', 59)
print(bartzz.get_name())
bartzz.set_name("zhangy")
print(bartzz.get_name(),bartzz.get_score())






