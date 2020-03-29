# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:16:25 2020

@author: Vasilis
"""

import turtle


#%%
#for i in range(100):
#    print("We like Python's turtles!")

#%%

#wn = turtle.Screen()
turtle.clearscreen()
vasi=turtle.Turtle()
for i in range(3):
    vasi.forward(50)
    vasi.left(120)

for i in range(4):
    vasi.forward(50)
    vasi.left(90)
    
for i in range(5):
    vasi.forward(50)
    vasi.left(72) 

for i in range(6):
    vasi.forward(50)
    vasi.left(60) 
   
for i in range(8):
    vasi.forward(50)
    vasi.left(45)    
    

turtle.bye()

#%%% draw a star
turtle.clearscreen()
tasos=turtle.Turtle()
for i in range(5):
    tasos.forward(150)
    tasos.left(216)
#turtle.clearscreen()
#turtle.bye()
    
#%% draw a clock
turtle.clearscreen()
takis = turtle.Turtle()    
takis.shape("turtle")
takis.color("blue")
turtle.bgcolor("lightgreen")
takis.stamp()
for i in range(12): 
    takis.up()
    takis.forward(250)
    takis.down()
    takis.forward(30)
    takis.up()
    takis.forward(10)
    takis.stamp()
    takis.backward(290)
    takis.right(30)

#%% draw something cfeative
turtle.clearscreen()

takis = turtle.Turtle()    
takis.shape("turtle")
takis.color("blue")
turtle.bgcolor("lightgreen")

takis.speed(0)
takis.forward(50)
takis.left(90)
takis.forward(50)
takis.left(45)
takis.forward(50)
takis.left(90)
takis.forward(50)
takis.left(45)
takis.forward(50)
takis.left(90)
takis.forward(60)

#%% draw creative ly 2

vasi = turtle.Turtle()
wn = turtle.Screen()
vasi.speed(0)

for i in range(100):
    vasi.forward(50)
    vasi.left(72+i) 


    
        
