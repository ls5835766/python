sum = 0
# 轮子轴距的实现
class Whell:

    def __init__(self, delta_left, delta_right,angu,rad):
        self.delta_left = delta_left
        self.delta_right = delta_right
        self.angu =angu
        self.rad=rad;


    def displayCount(self):
        length_one_fram_ang = 12.03*3.1415926/450
        whell_rounds=(self.delta_left + self.delta_right)/2;
        wb=(self.angu*whell_rounds*length_one_fram_ang*2.0)/(self.rad*360*3.1415926/180)
        print("Whell.wbCountb %f" % wb)
        return wb

    def displayWhell(self):
        print("delta_left : ", self.delta_left, ", delta_right: ", self.delta_right, ", angu: ", self.angu)

print("请按顺序输入delta_left，delta_right,angu,rad")

num1=float(input("输入delta_left:"))
num2=float(input("输入delta_right:"))
num3=float(input("输入angu:"))
num4=float(input("输入rad:"))
"创建 Employee 类的第一个对象"
# emp1 = Whell(4413.00, 4414.00,-1,3)
emp1 = Whell(num1,num2,num3,num4)
emp1.displayWhell()
emp1.displayCount()



