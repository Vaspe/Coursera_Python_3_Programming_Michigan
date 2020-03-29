# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:20:46 2020

@author: Vasilis
"""

#%% Definitions

"""
string: A single variable which is a concatenation of single strings (nubers,letters,
        symbols, etc,,,). Empty string is also a single character. They are marked with quotes
        Example: 'I am a string'. "I'm also a string", '''She said, "I 'm also a string" and left''' 
        Strings are immutable, cannot be changed after creation
list:  A list of any data type (string,int,float,list, etc...). All can be mixed 
       in there although is not recommended as best practice they are marked with
       [] and the (possibly mixed) variables are comma separated
       Example: ["hello", 2.0, 5, [10, 20]] 
       Lists are mutable, CAN be changed after creation
tuples: It is the same idea with the list and can contain any type of comma separated
        elements. They are marked with (). Tuples can contain lists   
        Example ("hello", 2.0, 5, [10, 20]) 
        Tuples are immutable, CANNOT be changed after creation. Although internal elements 
        like list mainteain their mutable nature
"""

#%% String definition examples

aa = 'I am a string'
print(aa)
bb = "I'm also a string"
print(bb)
cc = '''She said, "I 'm also a string" and left''' 
print(cc)
dd = ''' 
I am a multiple 
line string
defined with 3'
'''
print(dd)
ee = """
I am a second multiple
line string
defined with triple "
"""
print(ee)
ff =" "
print (ff)
gg=""
print(gg)


#%% List definition examples
hh = ["Hello", " ", "I", 'am', 'a random list', "of strings only"]
print (hh)
ii = ["hello", 2.0, 5, [10, 20], "I am a random list which includes another random list"] 
print(ii)
ii1 = [5]
print(ii1)
#%% Tuples definition examples
jj = ("hello", 2.0, 5, [10, 20], "I am a random tuple which includes a random list")
print(jj)
kk=(5,)
print(kk)

#%% INDEXING OPERATOR IN PYTHON IS []     (same to () in matlab...)
# Indexing starts at 0!!!! 
# Last value is not inclusive when defining a range!!!!
sString = 'Pyhton'
lList = ['one',2,'three']
tTuple = ("hello", 2.0, 5, [10, 20], "I am a random tuple which includes a random list")

for i in range (len(sString)):
    print('The character i = '+str(i) +' in the string is ' +(sString[i]))
    
for i in range (len(tTuple)):
    print ('The item i = '+str(i) +' in the tuple is ' + str(tTuple[i]) )
    
for i in range (len(lList)):
    print ('The item i = '+str(i) +' in the list is ' + str(lList[i]))
   
    
    
        

