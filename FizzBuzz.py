# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:11:30 2020

@author: Vasilis
Write a program that prints the numbers from 1 to 100. But for multiples of three 
print "Fizz" instead of the number and for the multiples of five print "Buzz". For
 numbers which are multiples of both three and five print "FizzBuzz".
"""

#%% NAive Vasilis
for i in range(1,101):
    if i %3 ==0 and i%5==0:
        print ('FizzBuzz')
    elif i%3 == 0:
        print ('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)

#%% Dont Repeat Yourself (DRY) less repetiotion more robust
for i in range(1,101):
    fizz = i%3==0
    buzz = i%5==0
    if fizz and buzz:
        print ('FizzBuzz')
    elif fizz:
        print ('Fizz')
    elif buzz:
        print ('Buzz')        
    else:
        print (i)    
        
#%% This would be good enough if we can do it fast!
def fizzbuzz(min_range=1, max_range = 100 ,triggers = {'Fizz':3,'Buzz':5}):         
    out = []
    for i in range(min_range,max_range+1):       
        text = ""
        for iKey in triggers:
            if i%triggers[iKey] == 0:
                text = text + iKey   
        if text =="":
            print(i)
        else:
            print(text)
    return out        
    
#%% Full on parametrization! Too much, wrong approach!!! DOn;t overdo it!

def fizzbuzz_Comp(min_range=1, max_range = 100 ,triggers = {'Fizz':3,'Buzz':5}):
    '''
    Function to create the FuzzBizz game structure:
        inputs:
            min_range : minimum value for out range, has to be an integer def 3
            max_range : maximum value for out range, has to be an integer def 5
            triggers : a dictionary with keys the words we want to ptint and 
                      value of its key the integer we want to checl in order to 
                      assign this word. def {'Fizz':3,'Buzz':5}
        output: a list object with mixed integers and strings
        example usage:
            a = fizzbuzz(1,10,{'Fizz':3,'Buzz':5})       
            for i in a:
                print (i) 
            --> a = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']    
    '''         
    out = []
    for i in range(min_range,max_range+1):       
        text = ""
        for iKey in triggers:
            if i%triggers[iKey]==0:
                text = text + iKey   
        if text =="":
            out = out + [i]
        else:
            out = out + [text]
    return out
       
#%%
a = fizzbuzz_Comp(1,100,{'Fizz':3,'Buzz':5})       
for i in a:
    print (i)

fizzbuzz(1,100,{'Fizz':3,'Buzz':5})   