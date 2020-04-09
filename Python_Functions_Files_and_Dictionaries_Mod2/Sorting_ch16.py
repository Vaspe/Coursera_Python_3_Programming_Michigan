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
# IMPRTANT: . The key function passed  must always take just one parameter!!!!
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
print("---------------------------------------------------------")

#%% sorting dictionaries
# by default it sort based on the keys:
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
y = sorted(d.keys())
for k in y:
    print("{} appears {} times".format(k, d[k]))
y1 = sorted(d)
print(y)
print(y1)


# if we want to sprt based on other property of the key like its value or a part
# of it we have to define a key function in the sorted. Usually done as a lambda
# anonymoys function

y2 = sorted(d, key=lambda k: d[k], reverse=True)
for k in y2:
    print("{} appears {} times".format(k, d[k]))
print(y2)
print("---------------------------------------------------------")    

#%% small exercise!
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values = sorted(dictionary,key = lambda x:dictionary[x], reverse=True)

#%% Second order sorting or what happens when two values are the same in a sorting sequence
# By defautl python will retutn them in the ordr encountered if no second layer exists
# for a list of tuples it will go to the next element of the tuplkes to do the second order soring 
tups = [('A', 3, 2),
        ('C', 1, 4),
        ('B', 3, 1),
        ('A', 2, 4),
        ('C', 1, 2),
       ('B', 3, 1,8)]
for tup in sorted(tups):
    print(tup)
print("---------------------------------------------------------")    

# we can also define the prder our selves:
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
for fruit in fruits:
    print(fruit)
print("---------------------------------------------------------")    
for fruit in new_order:
    print(fruit)
print("---------------------------------------------------------")    

# to change the order of the first order sort but keepo the second we can 
# do a trick of chnaging the sign of the numerical values that are sorted so now 
# we have reverse numerical sorting and regulkar alphabetic sorting:
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)    
print("---------------------------------------------------------")    
 
#%% when anonymous function is too much!
def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))
