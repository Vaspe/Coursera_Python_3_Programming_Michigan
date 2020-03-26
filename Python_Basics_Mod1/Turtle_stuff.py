# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:26:12 2020

@author: Vasilis
"""

import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.forward(150)         # tell alex to move forward by 150 units
alex.left(90)             # turn by 90 degrees
alex.forward(75)          # complete the second side of a rectangle
alex.left(90)             # turn by 90 degrees
alex.forward(150)          # complete the thirf side of a rectangle
alex.left(90)             # turn by 90 degrees
alex.forward(75)          # complete the foutrh side of a rectangle
print(type(turtle))