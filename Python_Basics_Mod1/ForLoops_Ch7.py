# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:51:57 2020

@author: Vasilis
"""

fruits = ["apple", "orange", "banana", "cherry"]

list2=[]
ww = 0
for afruit in fruits:     # by item
    #list2 =  list2 + [afruit]
    ww=ww+1;
    print (str(ww))


#%% Usinmg range
    
print("This will execute first")

for i in range(3):
    print("This line will execute three times")
    print("This line will also execute three times")

print("Now we are outside of the for loop!")

#%%

aa = list(range(11))
bb = list(range(1,11))

#%%
number=list(range(0,53,1))

#%%
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs = 0
for i in str1:
    numbs=numbs+1
    
print(numbs)

#%%
numbers = list(range(41))

sum1=0
for i in numbers:
    sum1=sum1+i
    
#%% In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are 
#Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop tries to output these 
#names in order.
#Of course, that’s not quite right because Ouack and Quack are misspelled. Can you fix it?
prefixes = ["J", "K", "L", "M", "N", "Ou", "P", "Qu"]
suffix = "ack"

for p in prefixes:
    print(p + suffix)    
    
 #%% Get the user to enter some text and print it out in reverse order
 
input_str ="Vasilis"#input ("Enter some text")

print ( input_str[::-1])

#%% Write a program that uses a for loop to print
months = ["January","February","March","April","May","June","July","August","Seprember","Octiber","November","December"]

for imonth in months:
    print("One of the months of the year is " + imonth)
    
#%%Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
#Write a loop that prints each of the numbers on a new line.
#Write a loop that prints each number and its square on a new line.
    
numbers = [2, 10, 32, 3, 66, 17, 42, 99, 20] 
for inum in numbers:
    print(str(inum))
    
for inum in numbers:
    print(str(inum)," ", str(inum*inum))
    print(str(inum))    