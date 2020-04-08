# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:43:54 2020

@author: Vasilis
14.8 assessment
"""

#%% 1
def sublist(alist):
    
    if len(alist) != 0: 
        cnt = 0
        el = alist[0]
        out_list = []
        while el != 5:
            if type(el) == int or type(el) == float:
                out_list =out_list + [el]
            cnt = cnt + 1
            if cnt > len(alist)-1:
                break
            el = alist[cnt]
            
    else:
        out_list = []
        
    return out_list      

print(sublist([1, 2, 3, 4, 5, 6, 7, 8]) )

#%% 2
def check_nums(alist):
    
    if len(alist) != 0: 
        cnt = 0
        el = alist[0]
        out_list = []
        while el != 7:
            if type(el) == int or type(el) == float:
                out_list =out_list + [el]
            cnt = cnt + 1
            if cnt > len(alist)-1:
                break
            el = alist[cnt]
            
    else:
        out_list = []
        
    return out_list   

out1 = check_nums([2,'a'])

print(check_nums([0,2,4,9,2,3,6,8,12,14,7,9,10,8,3]))
#%% ex3 
def sublist(alist):
    
    if len(alist) != 0: 
        cnt = 0
        el = alist[0]
        out_list = []
        while el != 'STOP':
            if type(el) == str:
                out_list =out_list + [el]
            cnt = cnt + 1
            if cnt > len(alist)-1:
                break
            el = alist[cnt]
            
    else:
        out_list = []
        
    return out_list  
print(sublist(['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']) ) 
#%% ex4
def stop_at_z(alist):
    el = alist[0]
    outlist = []
    cnt = 0
    while el != 'z':
        outlist = outlist + [el]
        cnt =cnt+1
        if cnt > len(alist)-1:
            break
        el = alist[cnt]        
    return outlist    
    
print(stop_at_z( ['c', 'b', 'd', 'zebra', 'h', 'r', 'z', 'm', 'a', 'k']))        

#%%ex 5 change a for to a while
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
cnt = 0
sum2 = 0
while  cnt<len(lst):
    sum2 = sum2 + lst[cnt]
    cnt = cnt +1

print("sum1 is "+ str(sum1) +" sum2 is "+ str(sum2) )

#%% ex6
def beginning(alist):
    cnt = 0
    el = alist[0]
    outlist = []
    while el!= 'bye' and len(outlist)<=9:
        outlist = outlist + [el]
        cnt = cnt +1
        if cnt > len(alist)-1:
            break
        el = alist[cnt]
    return outlist    

print(beginning(['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook', 'social media']))
input1 = ['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']
print(beginning(input1))   