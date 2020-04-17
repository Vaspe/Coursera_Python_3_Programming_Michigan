# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 00:03:34 2020

@author: Vasilis

Important resouces not covered in the course abut modules unittest and doctest:
    https://docs.python.org/3/library/unittest.html
    https://docs.python.org/3/library/doctest.html#module-doctest

Asser statement:
    https://docs.python.org/3/reference/simple_stmts.html#assert

Other good docs:
    https://realpython.com/python-testing/      
"""

#%%
assert 5==5

print('I passd')

#%% checking the type
assert type(9//5) == int
#assert type(9.0//5) == int


#%% checking if list elements are the same
lst = ['a', 'b', 'c']

first_type = type(lst[0])
for item in lst:
    assert type(item) == first_type

lst2 = ['a', 'b', 'c', 17]
first_type = type(lst2[0])
for item in lst2:
    assert type(item) == first_type

#%% check length of a variable
lst = ['a', 'b', 'c']

assert len(lst) < 10    
    