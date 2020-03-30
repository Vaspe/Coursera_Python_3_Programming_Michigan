# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:20:09 2020

@author: Vasilis
"""

import turtle

in_sides = "4" #input("define number of sides")
in_length = "100" #input("define length of each side (same for all)")
in_color = "blue"  #input("define color of the lines (same for all)")
in_fill = "red" #input("define color of the fill")

elan = turtle.Turtle()
#wn = turtle.Screen()
elan.pencolor(in_color) 
elan.fillcolor(in_fill)

for i in range(int(in_sides)):
    elan.forward(float(in_length))
    elan.left(360/int(in_sides))

#wn.exitonclick()  