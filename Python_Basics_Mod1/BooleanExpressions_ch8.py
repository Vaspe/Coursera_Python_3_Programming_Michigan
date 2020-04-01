# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:39:24 2020

@author: Vasilis
"""

# nice overview here: https://www.w3schools.com/python/python_operators.asp

print(True)
print(type(True))
print(type(False))

#%% boolean expressions
x = 5
y = 8

print ("x = "+ str(x)  )
print ("y = "+ str(y)  )

print("Expression for not equal is !=, so x!=y gives: " + str(x!=y)) # not equal
print("Expression for greater or equal is >=, so x>=y gives: " + str(x>=y)) # grater or equal
print("Expression for greater is >, so x>y gives: " + str(x>y)) # grater or equal
print("Expression for equal is ==, so x==y gives: " + str(x==y)) #  equal
print("Expression for smaller or equal is <=, so x<=y gives: " + str(x<=y)) # not equal
print("Expression for smaller  is !=, so x<y gives: " + str(x<y)) # not equal
print("--------------------------------------------")
#%% logical operators

print ("AND works with 'and', so x<y and x>10 gives: " +str(x<y and x>10 ) )
print ("OR works with 'or', so x<y or x>10 gives: " +str(x<y or x>10 ) )
print ("NOT works with 'not', so not(x<y and x>10) gives: " +str(not(x<y and x>10 )) )
print("--------------------------------------------")

#%% Membership Operators
print ("in command shows if a value, string, object is part of another object, so 9 in [3, 2, 9, 10, 9.0] gives: " +str( 9 in [3, 2, 9, 10, 9.0]))
print ("not in is the opposite of in, so 'wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing'] gives: " +str( 'wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing']))


