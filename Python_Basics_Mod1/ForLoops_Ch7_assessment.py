# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:46:07 2020

@author: Vasilis
"""
import turtle
#%% Write one for loop to print out each character of the string my_str on a separate line.

my_str = "MICHIGAN"
for i in my_str:
    print(i)




#%%%Write one for loop to print out each element of the list several_things. Then, write
#another for loop to print out the TYPE of each element of the list several_things. 
#To complete this problem you should have written two different for loops, each of which 
#iterates over the list several_things, but each of those 2 for loops should have a different result

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for i in several_things:
    print(str(i))
    
for i in several_things:
    print(str(type(i)))

#%%% Write code that uses iteration to print out the length of each element of the l
#ist stored in str_list

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

for i in str_list:
    print(str(len(i)))

#%%


john = turtle.Turtle()
#wn = turtle.Screen()
john.speed(0)

angle = 5
distance = 10
for i in range (500):
    john.forward(distance)
    distance = distance+5
    john.left(angle)
    angle = angle +5

    

#wn.exitonclick() 


#%%addition_str is a string with a list of numbers separated by the + sign. Write code
#that uses the accumulation pattern to take the sum of all of the numbers and assigns it
#to sum_val (an integer). (You should use the .split("+") function to split by "+" and 
#int() to cast to an integer).
    
addition_str = "2+5+10+20"

pure_str = addition_str.split("+")

sum_val = 0
for i in pure_str:
    sum_val = sum_val + (int(i))
    
#%%5week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign.
#Write code that uses the accumulation pattern to compute the average (sum divided by number 
#of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code
#compute both the sum or the number of items in week_temps_f) (You should use the 
#.split(",") function to split by "," and float() to cast to a float).
#

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

pure_temp = week_temps_f.split(",")

sum_temp = 0.0
cnt1 = 0
for i in pure_temp:
    sum_temp = sum_temp + float(i)
    cnt1 = cnt1 +1
    
avg_temp = sum_temp/cnt1
        
    
#%%Write code to create a list of word lengths for the words in original_str using the 
#accumulation pattern and assign the answer to a variable num_words_list. (You should use 
#the len function).

original_str = "The quick brown rhino jumped over the extremely lazy fox"

words =  original_str.split()
cnt = 0
num_words_list =[]
for i in words:
    num_words_list = num_words_list + [len(i)]
    cnt=cnt+1

#%%

    
    
    