# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:17:52 2020

@author: Vasilis
"""
#%%Ex1
#numbers = list(range(0,36))
cnt = 0
numbers = []
while cnt<36:
    numbers = numbers + [cnt]
    cnt =cnt+1

#%%
cnt = 0
L = []
while cnt<11:
    L = L + [cnt]
    cnt =cnt+1

  
#%% Ex4
# Modify the walking turtle program so that rather than a 90 degree left or right turn 
# the angle of the turn is determined randomly at each step.
import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.randrange(0, 2)
    deg_val = random.randrange(0, 359)
    if coin == 0:
        t.left(deg_val)
    else:
        t.right(deg_val)

    t.forward(100)

wn.exitonclick()


#%% Ex 5
#Modify the turtle walk program so that you have two turtles each with a random starting 
#location. Keep the turtles moving until one of them leaves the screen.


t = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
t2.shape('classic')
t.pencolor("green")
t2.pencolor("red")
t.penup()
t2.penup()
t.setpos(random.randrange(-200, 200),random.randrange(-200, 200))
t2.setpos(random.randrange(-200, 200),random.randrange(-200, 200))
t.pendown()
t2.pendown()

while isInScreen(wn,t) and isInScreen(wn,t2)  :
    coin = random.randrange(0, 2)
    deg_val = random.randrange(0, 359)
    if coin == 0:
        t.left(deg_val)
    else:
        t.right(deg_val)

    t.forward(100)
    
    coin2 = random.randrange(0, 2)
    deg_val2 = random.randrange(0, 359)
    if coin2 == 0:
        t2.left(deg_val)
    else:
        t2.right(deg_val)

    t2.forward(100)

wn.exitonclick()

#%%Ex6
cnt =0
tens =[]

while cnt<51:
    if cnt%10 ==0:
        tens.append(cnt)
    cnt = cnt +1

#% Ex 7













    