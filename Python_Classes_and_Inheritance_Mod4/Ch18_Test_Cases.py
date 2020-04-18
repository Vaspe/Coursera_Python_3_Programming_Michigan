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
#for item in lst2:
#    assert type(item) == first_type

#%% check length of a variable
lst = ['a', 'b', 'c']

assert len(lst) < 10    

#%% function test

def accumulator(lst):
    accum = 0   
    for w in lst:
        accum = accum + w
    return accum
    
assert accumulator([1,2,3]) == 6    
# assert accumulator([]) == None   # gives 0 instead og the expected 0!!!!

#%%  Testing possible combination of outputs of functions
"""
#1 Functionality with 'normal' expec ted inputs
#2 Testing edge cases like numbers or types of inputs that are extreme
#3 Testing side effects like mutations of lists or other stuf that are not directly 
#   connected to the functionality
#4 Test outputs like files written outside the environment
"""                

# functionality and edge tests
def square(x):
    return x*x

assert square(3) == 9
assert square(4) ==16
assert square(0) ==0
assert square(-3)==9

# side effect tests:
def update_counts(letters, counts_d):
    for c in letters:
        if c not in counts:
            counts_d[c] = 0
        if c in counts_d:
            counts_d[c] = counts_d[c] + 1


counts = {'a': 3, 'b': 2}
update_counts("aaab", counts)
# 3 more occurrences of a, so 6 in all
assert counts['a'] == 6  # cretes an error!
# 1 more occurrence of b, so 3 in all
assert counts['b'] == 3   

# The same for optional parametrs.
assert sorted([1, 7, 4]) == [1, 4, 7]
assert sorted([1, 7, 4], reverse=True) == [7, 4, 1]    

#%% When doing development unit test for each increment change should be done 
# before the implementation itself. This is a good practice to make sure
# we have a clear scope and added functionality does not break the previous
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

assert distance(1, 2, 1, 2) == 0
assert distance(1,2, 4,6) == 5
assert distance(0,0, 1,1) == 2**0.5

"""
1. Make sure you know what you are trying to accomplish. Then you can write appropriate unit tests.

2. Start with a working skeleton program and make small incremental changes. At any
 point, if there is an error, you will know exactly where it is.

3. Use temporary variables to hold intermediate values so that you can easily inspect
 and check them.

4. Once the program is working, you might want to consolidate multiple statements 
 into compound expressions, but only do this if it does not make the program more 
 difficult to read.

"""

#%% In the same way we can also create test cases for classes!

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


#testing class constructor (__init__ method)
p = Point(3, 4)
assert p.y == 4
assert p.x == 3

#testing the distance method
p = Point(3, 4)
assert p.distanceFromOrigin() == 5.0

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
assert p.x == 1
assert p.y == 7
