# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:32:57 2020

@author: Vasilis
"""

#%% defining optional arguments in finctions

initial = 7
def f(x, y =3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

print(f(2))
print(f(2, 5))
print(f(2, 5, 8))
print("-----------------------------------------------------------")
#%%
def str_mult(str_in,num_in=3):
    return str_in*num_in

#print(str_mult()) gives an error since the first not optional argument
print(str_mult("all work and no play...\n"))
print(str_mult("all work and no play...\n",5))
print("-----------------------------------------------------------")

#%% keyword arguments, kwargs 
# read :https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
'''
Keyword arguments must follow positional arguments. All the keyword arguments passed
must match one of the arguments accepted by the function and their order is not important!
'''

def parrot(voltage, state='a stiff', action='voom', typ='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", typ)
    print("-- It's", state, "!")
    
parrot(1000)                                          # 1 positional argument
print("-----------------------------------------------------------")
parrot(voltage=1000)                                  # 1 keyword argument
print("-----------------------------------------------------------")
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
print("-----------------------------------------------------------")
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
print("-----------------------------------------------------------")
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
print("-----------------------------------------------------------")
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
print("-----------------------------------------------------------")

#%% Using format command for jeyword arguments
names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))

print("-----------------------------------------------------------")

# this works
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))

# moreover this also also works!
names = ["Jack","Jill","Mary"]
print("'{0}!' she yelled. '{1}! {2}, {3}!'".format(names[0],names[1],names[2],"say hello"))

"""
ALWAYS IN CALLS OR DEFINITIONS:
    FIRST THE POSITIONAL ARGUMENTS AND THE KEYWORD ARGUMENTSD FOLLOW!!!!
"""
print("-----------------------------------------------------------")

#%% LAMBDA EXPRESSIONS anonymous functions
def f(x):
    return x - 2

print(f)
print(type(f))
print(f(3))

print(lambda x: x-2)
print(type(lambda x: x-2))
print((lambda x: x-2)(3))  
print("-----------------------------------------------------------")

#%% defininf functions with both ways and getting the same object:
def last_char(s):
    return s[-1]

print(last_char("I am just a string"))
print(type(last_char))
print(last_char)
last_char2 = (lambda s: s[-1])
print((lambda s: s[-1])('I am just a string'))
print(type(last_char2))
print(last_char2)
print(last_char2("I am just a string"))
print("-----------------------------------------------------------")

#%%
"""
Programming stryle:
use 4 spaces for indentation

- imports should go at the top of the file
- separate function definitions with two blank lines
- keep function definitions together
- keep top level statements, including function calls, together at the bottom of 
  the program


"""


