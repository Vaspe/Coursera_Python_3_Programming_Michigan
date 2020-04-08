# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:06:58 2020

@author: Vasilis
"""

#%%Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, 
#append the counter to a list called eve_nums.

cnt = 0
eve_nums = []
while cnt<16:
    if cnt%2 ==0:
        eve_nums = eve_nums + [cnt]
    cnt =cnt +1

print(eve_nums) 


#%%
list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem

accum = 0
iter1 = 0
while iter1 <= len(list1)-1:
    accum =accum +list1[iter1]
    iter1 = iter1 + 1 

#%%
def stop_at_four(alist):
    cnt = 0
    newlist = []
    num1 =alist[cnt]
    while num1 != 4:
        cnt =cnt +1
        newlist =newlist + [num1]
        num1 = alist[cnt]
    return newlist        
aa = stop_at_four([4])
    
#%% the listener loop
theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum = theSum + x

print(theSum)    
print("-----------------------------------------------------------------")

#%% sentinel values to trigger end of a looping procedure
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price < 0:
            print("You entered an invalid negative price. Please try again")
        else:    
            if price != 0:
                count = count + 1
                total = total + price
                print('Subtotal: $','%.2f '% total)
            else:
                moreItems = False
    if count != 0:            
        average = total / count
        print('Total items:','%.2f '% count)
        print('Total $','%.2f '% total)
        print('Average price per item: $','%.2f '% average)
    else:
        print("Can’t compute an average without data")


#checkout()
print("-----------------------------------------------------------------")
#%% using while to check if inputs are valis
def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper() # convert to upper case
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer

response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')
# using the correct input    
if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')
print("-----------------------------------------------------------------")        

#%% use a while to stop the turtle whn it is outside of the window
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
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

wn.exitonclick()

#%% break/continue statement
# break compeltely stops the loop at this point
while True:
    print("this phrase will always print")
    break
    print("Does this phrase print?")

print("We are done with the while loop.")
print("-----------------------------------------------------------------")
# continue mooves to the next iteration ignoring the rest of the stuff in the loop       
x = 0
while x < 10:
    print("we are incrementing x")
    if x % 2 == 0:
        x += 3
        continue    # here it jumps back to the beginnin like goto l.151
    if x % 3 == 0:
        x += 5
    x += 1
print("Done with our loop! X has the value: " + str(x))

