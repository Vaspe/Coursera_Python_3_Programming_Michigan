# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:28:02 2020

@author: Vasilis
"""

#%% lists can have multiple levels nested
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h',[0,1,2,['k','k','k']]]]
print(nested1[0])
print(len(nested1))
nested1.append(['i'])
print("-------")
for L in nested1:
    print(L)
    
#levels are seen with indexing with []. Problem is you should know all the levels a priori    
print(str(nested1[2][3][3][1]))    
print(str(nested1[2][3][3][1][0][0][0])) # we can add infinite o at the end it points to the same always
#print(nested1)
print("-------")

#%% All types of objects are allowed in nested lists:
nested2 = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"},(1,2,3,'k','l')]

print(nested2[2])
print(nested2[3])
print(nested2[2]['b'])
print(nested2[3][4])
print(list(nested2[2].keys()))
nested2[2]['c'] = 'no'
print(nested2[2]['c'])

print("-------")

#%% Also functions can be part of these snested lists
def square(x):
    return x*x

L = [square, abs, lambda x: x+1]

print("****names****")
for f in L:
    print(f)

print("****call each of them****")
for f in L:
    print(f(-2))

print("****just the first one in the list****")
print(L[0])
print(L[0](3))
print("-------")

#%% Nested dictionaries are also allowed

info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

color = info['personal_data']['physical_features']['color']
print(color)
info['personal_data']['physical_features']['color'] = "I can change this!"
color = info['personal_data']['physical_features']['color']
print(color)
print("-------")

#%% JSON format using the json module
"""
 good doc: https://www.w3schools.com/python/python_json.asp

 - From python to JSON use the method json.dumps() --> any object can become a json
 - From JSON to python use the method json.loads() --> dictionary
 - in general think of yaml,json,and xml as text base data file formats and h5 
   and pandas as binary data file formats
 
#import yaml
#import io
#import xml
#import pandas

"""
import json
#a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
#print(a_string)
fid =open("Files/first_json.json")
a_string2 = fid.read()
fid.close()
# loads method creates a dictionary from a string (or file) formattes as json 
d = json.loads(a_string2)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount']) # gives an error because it is just a string
print("-------")

# dumps creates the json from a python structure
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))
print('--------')

#%% nested iterations
nested3 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested3:
    print("level1: ")
    for y in x:
        print("     level2: " + y)

#%%
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = []
for iLst in info:
    last_names = last_names + [iLst[1]] 

#%%
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]

b_strings = []
for iLst in L:
    for iWrd in iLst:
        if "b" in iWrd:
            b_strings = b_strings + [iWrd]
print('--------')           
#%% DEEP AND SHALLOW COPIES
# DEEP completely decoupled in all levels from the original object
# Shallow is coupled in all levels (except the highest?)

# Shallow
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:] # shallow copy with all the nested data copied and mutable
print(copied_version)
print(copied_version is original)
print(copied_version == original)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_version)            
            
print('--------')   

#DEEPv1 cloning elements
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = []
    for item in inner_list:
        copied_inner_list.append(item) #deep copy we clone all stuff but they dont refer to same object
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)
  
print('--------')   
        
# Shallow v2 using slices
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = inner_list[:] #deep copy we clone all stuff but they dont refer to same object
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)

print('--------')  

#%% Using the copy module
import copy
# doc her e: https://docs.python.org/3.7/library/copy.html
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version)

print('--------')  









