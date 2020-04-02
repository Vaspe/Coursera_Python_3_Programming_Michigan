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
b = "banana"

# we can also check the unique id of each object using the id commnad
print(id(a))
print(id(b)) # the immutable strings have the same identifier
print(id(alist))

# this is not valid for lists which are always assigned to UNIQUE IDs
print("-------------------------------")
a = [81,82,83]
b = [81,82,83]

print(a is b)

print(a == b) # they are the same but dont have the same id!

print(id(a))
print(id(b))

print("-------------------------------")

# If we reassign the varible though the lsit tkes the same id
c = b
print(c is b)

print(c == b) # they are the same but dont have the same id!
print(id(c))
print(id(b))

# Now c is alias of b. Practically is the same object with another name. So any mutation
# to the object will reflect in all other named variables 

# Although this behavior can be useful, it is sometimes unexpected or undesirable.
# In general, it is safer to avoid aliasing when you are working with mutable objects.


#%%
# We can clone a list to avoid the alias as explained before. Clone means we assign
# a new name and ID to the same mutable object

a = [81,82,83]
b= a[:]

print("-------------------------------")
print (a is b)
print(a == b) #
print(id(a))
print(id(b))
b[0] = 5

print(a)
print(b)

print("-------------------------------")


#%% Mutability of METHODS
# remeber: https://www.w3schools.com/python/python_ref_list.asp

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12) # inserts stuff in the list permanently
print(mylist)
print(mylist.count(12)) # only counts occurencies
print(mylist.index(3)) # only finds the first index of a nelement
print(mylist.count(5))

mylist.reverse() # reverses the order  of the list permanently
print(mylist)

mylist.sort() # sorts the list from low to high permanently!
print(mylist)

mylist.remove(5) # removes the lement with value 5 (not the fifth!)
print(mylist)

lastitem = mylist.pop() # pop removes an element from a specific position if empty removes the last
print(lastitem)
print(mylist)
print("-------------------------------")

#%%
'''
 methods like append, sort, and reverse all return None !!!!
 Dont use them to create new lists
'''
mylist = mylist.sort()   #probably an error
print(mylist)
print("-------------------------------")

#%% STRING METHODS
#remember: https://www.w3schools.com/python/python_ref_string.asp
ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)

ss = "    Hello, World    "
print (ss)
els = ss.count("l")
print(els)

print("***"+ss.strip()+"***")

news = ss.replace("o", "***")
print(news)

name = "Vasilis"
score = 5
str_form = "Hello {}. Your score is {}".format(name,score)
print (str_form)

origPrice = 100
discount = 17
newPrice = (1 - discount/100)*origPrice
# number format
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)

# overview of fstrinmg formatting types are here:
# https://www.w3schools.com/python/ref_string_format.asp
print("-------------------------------")
a = 5
b = 9
setStr = 'The set is {{ {}, {} }}.'.format(a, b)
print(setStr)


print("-------------------------------")

#%%
#Append vs Concatenate

origlist = [45,32,88]
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list before changes
newlist = origlist + ['cat']
print("newlist:", newlist)
print("the identifier:", id(newlist))              #id of the list after concatentation
origlist.append('cat')
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list after append is used
print("-------------------------------")

origlist = [45,32,88]
print("origlist:", origlist)
aliaslist = origlist
print("aliaslist:", aliaslist)
origlist += ["cat"]
print(origlist)
print (aliaslist)
origlist = origlist + ["cow"]
print("origlist:", origlist)
print("aliaslist:", aliaslist)
print("-------------------------------")