# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:12:25 2020

@author: Vasilis

"""



#%%
# The sort method does not return a sorted version of the list. In fact, it returns 
# the value None. But the list itself has been modified.
L1 = [1, 7, 4, -2, 3]
L2 = ["Cherry", "Apple", "Blueberry"]

L1.sort()
print(L1)
L2.sort()
print(L2)

#%% sorted function
#sorted does not change the original list. Instead, it returns a new list.
# In general prefer sorted because it does not mutate the original ibject  (list,string)

L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2) # unchanged

print("----")
L4 =L2  #because it is mutable L4 will inherit the roting done in L2
L2.sort()
print(L2)
print(L2.sort())  #return value is None

print("---------------------------------------------------------")
#%% sorted oinal arguments

str1 = 'Hello'
str2 = sorted("hello")
str3 = sorted(str1)

dic1 = {'bananas':2,'apples':5,"tomatoes":5}
dic2 = sorted(dic1)
dic3 = sorted({'bananas':2,'apples':5,"tomatoes":5})

tup1 = ('bananas','apples',"tomatoes")
tup2 =sorted (tup1)
tuo3 = sorted(('bananas','apples',"tomatoes"))

L5 = ["Cherry", "Apple", "Blueberry",6,8]
#L6 =sorted(L5) # gives an error because all elements have to have the same type!

#%% sorted oinal arguments
# see doc here :https://www.w3schools.com/python/ref_func_sorted.asp

# reverse reverses the sorting from bigger to smaller
L6 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L6, reverse=True))

L7 = [1, 7, 4, -2, 3]

print("---------------------------------------------------------")
# key defines a custom function applied during the sorting like e.g. the absolute
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L8 = sorted(L7, key=absolute)
print(L8)

#or in reverse order
print(sorted(L7, reverse=True, key=absolute))
print(sorted(L7, reverse=True, key=abs))  # same result!
print("---------------------------------------------------------")


#%%
def second_let(str1):
    out_str = str1[1]
    return out_str

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
sorted_by_second_let = sorted(ex_lst,key = second_let) 

#%%
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(str1):
    str2 = str1[-1]
    return str2
    
nums_sorted = sorted(nums,key = last_char, reverse = True)
print(nums)
print(nums_sorted)
# same with lambda funcyion
last_char2 = lambda str1:str1[-1]
nums_sorted_lambda2 = sorted(nums,key = last_char2, reverse = True)
# or equally
nums_sorted_lambda3 = sorted(nums,key = (lambda str1:str1[-1]), reverse = True)

#%%

