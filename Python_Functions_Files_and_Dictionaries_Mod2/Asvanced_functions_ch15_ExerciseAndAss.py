# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:32:14 2020

@author: Vasilis
"""

#%% Ex1
def g(x,y=4,z=0):
    return 2*x + y + z
print(g(3))       # should output 10
print(g(3, 2))    # should output 8
print(g(3, 2, 1)) #should output 9
print("--------------------------------------------------------------")

#%% Ex2
def nums(numin,mult_int=5,switch =False):
    val_out = numin*mult_int
    if switch:
        val_out = -val_out
    return val_out  

print(nums(4, mult_int = 3, switch = True))

print("--------------------------------------------------------------")

#%% Ex 3 
def together(num_in,str_in,con_str= " "):
    return str(num_in)+con_str+str_in
print(together(17.3, 'birthday cakes')) 
print(together(493.3, 'beans', 'lima')) 

