# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:12:12 2020

@author: Vasilis
Nice overview of the dictionaries and their methods:
    https://www.w3schools.com/python/python_dictionaries.asp

"""
#%% creating a dictionary, starting from an emoty one
eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'
print(eng2sp)

#%% dictionary from scratch
eng2sp_2 = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
print(eng2sp_2)

#%% accessing valus in a dictionary from the keys

value = eng2sp['two']
print(value)
print(eng2sp['one'])

#%% my first dictionary
medals = {'gold':33, "bronze":12, "silver":17}
print (medals)

# or

olympics = {'gold':8}
olympics['silver'] = 7
olympics['bronze'] =6
print("-------------------------------------------------------")
#%% the del keyword deletes a key value pair. Yhe key should be iused as inpout of the dictionary
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print (inventory)
del inventory['pears']
print(inventory)






