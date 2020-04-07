# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:23:54 2020

@author: Vasilis
"""

#%% My first dunction
def hello():
    """This function says hello and greets you"""
    print("Hello")
    print("Glad to meet you")

hello()

# The comments blow def are used as documentation with <function_name>.__doc__
print(hello.__doc__)

#%%
alist = [1,2,3,4]

def dummy_fun(alist):
    """ I dont do anything like my creator"""
    result = 42 # its the meaning of life, come on!
    blist =alist
    blist.append(5)
    return result

# be carefull the a list is mutated inside the function and this is returned to the 
# global space! 

result = dummy_fun(alist)
result2 = dummy_fun(alist) 
print(str(alist))

#%%
list1 = ["Sam","Tera","Sal","Amita"]
list2 = ["Rey","Ayo","Lauren","Natalie"]

def longer_than_five(lst,n):
    """ I am a function that gets a list and says which word has more than 5 letters"""
    output = []
    for i in lst:
        output=output + [len(i)>n]
    return output

longer_than_five(list1,5)        
print(longer_than_five(list1,5))
print(longer_than_five(list2,5))

#%%
def intro(in_str):
    out_str = "Hello, my name is {} and I love SI 106.".format(in_str)
    return out_str

print(intro("Vasilis")            )

#%% name space
#print(len.__file__)
aa = 55
innum=55
def foo1(x):
    y=x+aa
    return y
# the local space sees the global space!!!!!! 
# This is a grweat difference from matlab
# the local sees always the global which always sees the built-in
# the other way around does not work!!! Flobal does not see local!    
res1 = foo1(innum)
    
    
def addit(innum):
    y = innum +5
    return y
def mult(innum):
    y = innum*addit(innum)
    return y

print(mult(5))

#%% Protecting mutable objects
"""
Make a copy of an object and pass the copy in to the function. Then return the modified 
copy and reassign it to the original variable if you want to save the changes. The
 built-in list function, which takes a sequence as a parameter and returns a new list,
 works to copy an existing list. For dictionaries, you can similarly call the dict 
 function
"""
def changeit(lst):
   lst[0] = "Michigan"  # i am changinf only the local we dont reassign it as 
   lst[1] = "Wolverines"
   return lst
	
mylst = ['106', 'students', 'are', 'awesome']
newlst = changeit(list(mylst))
print(mylst)
print(newlst)

"""
In general, any lasting effect that occurs in a function, not through its return value, 
is called a side effect. There are three ways to have side effects:

1.Printing out a value. This doesn’t change any objects or variable bindings, but it 
does have a potential lasting effect outside the function execution, because a person 
might see the output and be influenced by it.

2. Changing the value of a mutable object.

3. Changing the binding of a global variable.
"""






