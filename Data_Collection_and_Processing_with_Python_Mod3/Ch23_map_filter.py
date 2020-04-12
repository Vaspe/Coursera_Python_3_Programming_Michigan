# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:09:31 2020

@author: Vasilis
map documentation:
    https://www.w3schools.com/python/ref_func_map.asp
    map(<function>, <iterable(s)>)
    
filter documnetation:
    https://www.w3schools.com/python/ref_func_filter.asp  
    filter(<function that gives True or False,<iterable>)

Remeber that they both return iterable and not list. We need to convert to list if required!    
"""

#%%

def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)
print("---------------------------------")

#%%
def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)
print("---------------------------------")

#%%
things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))
print("---------------------------------")

#%%
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = map(lambda x:2*x,lst)

#%%
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper  =map(lambda x:x.upper(),abbrevs)

#%%
def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

#%
def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))

print("---------------------------------")

#%%
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
lst2 = list(filter(lambda x:"o" in x,lst))


