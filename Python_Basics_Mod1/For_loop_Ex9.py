# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:38:28 2020

@author: Vasilis
"""

import turtle

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

vasi = turtle.Turtle()
#wn = turtle.Screen()

tot_angle = 0
for iangle in angles:
    vasi.left(iangle)
    vasi.forward(100)
    tot_angle = tot_angle + iangle
    
print ("Current heading of the pirate is " + str(tot_angle))



#wn.exitonclick() 