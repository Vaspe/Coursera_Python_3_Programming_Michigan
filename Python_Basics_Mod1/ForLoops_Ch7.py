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

for i in str1:
    numbs=numbs+1
    
print(numbs)

#%%
numbers = list(range(41))

sum1=0
for i in numbers:
    sum1=sum1+i