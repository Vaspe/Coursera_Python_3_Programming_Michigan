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
print("--------------------------------------------------------------")
#%% Ass1
def mult(numin,par2 =6):
    return numin*par2
print(mult(2))
print(mult(4,'hello'))
print("--------------------------------------------------------------")

#%% Ass2
def greeting(name,greeting="Hello ",  excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))
print("--------------------------------------------------------------")
#%%  Ass 3
def sumy(intx,intz=5 ):
    return intz + intx
print("--------------------------------------------------------------")

#%% Ass4
def test(par1,par2=True,dict1={2:3,4:5,6:8}):
    if not par2:
        out = False
    else:
        if par1 in dict1.keys():
            out = dict1[par1]
        else:
            out = []
    return out

print(test(2)    )
print(test(4,False))
print( test(5, dict1 = {5:4, 2:1}))
print("--------------------------------------------------------------")

#%% Ass 5

def checkingIfIn(str1,direction = True, d ={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7} ) :
    if direction:
        if str1 in d.keys():
            outy = True
        else:
            outy = False        
    else: 
        if str1 not in d.keys():
            outy = True
        else:
            outy = False  
    return outy    

print(checkingIfIn('grapes', d = {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}))
print(checkingIfIn('carrots', False))
print("--------------------------------------------------------------")

#%% Ass6

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn(2,True)
print(c_false)
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('apples',False)
print(c_true)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn('fruit',True)
print(fruit_ans)
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('strawberry',d={'strawberry':8})
print(param_check)

