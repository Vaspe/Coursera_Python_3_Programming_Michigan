# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:32:44 2020

@author: Vasilis
"""

#%% Theory
# List are mutable we can add, remove or reassign elements
# Strings and tuples are immutable we can only reassign or create a new variable to change them


#%% Basics
# replacing elements
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)

# squeezing in elemnts
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[3:3] = ['x', 'y']
print(alist)

# deleting elements 1st method
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

# deleting elements second method
alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:3]
print(alist)

#%% Check if two variables reference to the same object in python usingis operator

a = "banana"
b = "banana"

print(a is b)
b += b     # reassign it and check again
print(a is b)

#%%


