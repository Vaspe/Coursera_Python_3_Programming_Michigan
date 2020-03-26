# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:26:12 2020

@author: Vasilis
"""


import turtle             # allows us to use the turtles library
#%%
#wn = turtle.Screen()      # creates a graphics window
#alex = turtle.Turtle()    # create a turtle named alex
#alex.forward(150)         # tell alex to move forward by 150 units
#alex.left(90)             # turn by 90 degrees
#alex.forward(75)          # complete the second side of a rectangle
#alex.left(90)             # turn by 90 degrees
#alex.forward(150)          # complete the thirf side of a rectangle
#alex.left(90)             # turn by 90 degrees
#alex.forward(75)          # complete the foutrh side of a rectangle
#wn.exitonclick()                # wait for a user click on the canvas
##print(type(turtle))

#%%
# colur names: https://www.w3schools.com/colors/colors_names.aspAlice blue
bgcolor_str =  input('Choose background color')
color_str = input('Choose turtle color')
pensize_str = input('Choose turtle pen size')

wn = turtle.Screen()
wn.bgcolor(bgcolor_str)        # set the window background color

tess = turtle.Turtle()
tess.color(color_str)              # make tess blue
tess.pensize(int(pensize_str))                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
