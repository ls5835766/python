# -*- coding:utf-8 -*-
from tkinter import *
from random import  randint

#地图类

class Grid(object):
    def __init__(self,master=None,window_width=500,window_height=400,grid_width=20,offset=10):
        pass  #表示占位语句，什么都不表示
        self.height=window_height
        self.width=window_width
        self.grid_width=grid_width
        self.offset=offset
        self.grid_x=self.width/self.grid_width
        self.grid_y=self.height/self.grid_width
        self.bg='white'
        self.canvas=Canvas(master , width=self.width+2*self.offset,heigh=self.height+self.offset*2,bg=self.bg)
        self.canvas.pack()

if __name__ == '__main__':
    root = Tk()
    root.title('我的贪吃蛇')
    grid=Grid(root)
    root.mainloop()

