count=0
sum=0
# 轮子半径
class Whell:

    def __init__(self, delta_left, delta_right,x):
        self.delta_left = delta_left
        self.delta_right = delta_right
        self.x = x


    def displayCount(self):
        a = 450.0*2.0*self.x/3.14
        #print("Whell.whellCounta %f" % a)
        c=self.delta_left + self.delta_right;
        #print("Whell.whellCountb %f" % c)
        b = a / c
        print("Whell.whellCountb %f" % b)
        global count
        global sum
        count+=1
        sum+=b
        return b

    def displayWhell(self):
        print("delta_left : ", self.delta_left, ", delta_right: ", self.delta_right, ", x: ", self.x)

    def disPlayavg(self):
        return sum/count

print("请按顺序输入delta_left，delta_right,x")

num1=float(input("输入delta_left:"))
num2=float(input("输入delta_right:"))
num3=float(input("输入x:"))

"创建 Employee 类的第一个对象"
emp1 = Whell(num1, num2, num3)
emp1.displayWhell()

#将文件写入d.txt文件里面去
#encoding=utf-8
fileName="d.txt"
content=u"平均数"
content=content.encode("utf-8")#写入的文件编码格式为utf-8
with open(fileName,'a') as f: #如果fileName不存在会自动创建，'w'表示写入数据写之前会清空文件中的原有数据！,'a'表示将数据写到原数据之后
    f.write(str(emp1.displayCount())+"\n")

emp1.disPlayavg()





