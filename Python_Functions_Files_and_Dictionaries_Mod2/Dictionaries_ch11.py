# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:12:12 2020

@author: Vasilis
Nice overview of the dictionaries and their methods:
    https://www.w3schools.com/python/python_dictionaries.asp
    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict


Method	Description

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get() 	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	      Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
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
print("Using the command del as del inventory['pears'], gives:  " +str(inventory))
len(inventory)
print("Using the command len gives the amount of key-value pairs in a dictionary, len(inventpry):  " +str(len(inventory)))

print("-------------------------------------------------------")
#%% main methods

print("----------------MAIN METHODS--- keys,values,items,in,not in, get, update------------------------")

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

key_list = list(inventory.keys()) # the method keys() its self does not produce a list!!!!!
print ("in order to see all keys in a dicitonary I need to do list(inventory.keys()): which gives"+ str(key_list))

# using a loop:
for k in inventory: # or equally: for k in inventory.keys"
    print("Key is "+ k)

# method values returns all the values:
dic_val = list(inventory.values())
print ("in order to see all values in a dicitonary I need to do list(inventory.values()): which gives"+ str(dic_val))

# method items return a list with tuples including in each tuple a key-value pair
dic_item = list(inventory.items() )
print ("in order to see all key-value pairs in a dictionary I need to do list(inventory.items() ): which gives"+ str(dic_item))

if 'mangos' in inventory:
    print(inventory['bananas'])
else:
    print("We have no mangos")
    
# If I want to check i fa key exist the dictionary["keyname"] will produce an error
# We can do it with get method which gives a none if the key doesn't exist and continues
print("Asking for an existing value with inventory.get('bananas'): " + str(inventory.get('bananas')))    
print("Asking for a non-existing value with inventory.get('mangos'): " + str(inventory.get('mangos')))    
# If the value does not exis I can include a second argument in get to assign a values:
print("Asking for a non-existing value with inventory.get('mangos',0): " + str(inventory.get('mangos',0)))    

places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
places.get("Brazil",2016)
places.update({"Brazil":2016})
print("We can add a new key pair value with the update method.places.update({'Brazil':2016}): " +str(places))

print("-------------------------------------------------------")
#%% mutability of dictionaries:

opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites # now alias refers to the same dictionary pbject as opposites

print(alias is opposites) # is is valid also for dicitonaries to see if they refer to same object isinde python

alias['right'] = 'left'
print(opposites['right'])
