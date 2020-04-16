# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:18:49 2020

@author: Vasilis
"""

#%% Ex1+2


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def reflect_x(self):
        return (self.x,-self.y)

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return str(self.x)+","+str(self.y)


#%%    
print(Point(3, 5).reflect_x())
aa = Point(3,5)
print(aa)
aa.move(10,10)
print(aa)
