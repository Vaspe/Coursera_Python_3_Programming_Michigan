# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 01:13:06 2020

@author: Vasilis
"""

#%% packing tuples
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[4])
# or equivalently
julia1 = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
print(julia1[4])

#%% Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check =[]
for i in lst_tups:
    t_check = t_check + [i[2]]

#%% tuple unpack: automatic assigning left side variables to right side. The left
# side should havethe correct number of arguments    
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"

name, surname, birth_year, movie, movie_year, profession, birth_place = julia    

#%% Unpacking works also with lists!!!
alist = [0,1,2,3,4,5,6]
a1,a2,a3,a4,a5,a6,a7= alist

#%% It is useful for swapping values between variables
a = 1
b = 2
(a, b) = (b, a)
print(a, b)
print(type(a))

#%% unpacking tuples into several iterator loop variables
authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)
 
print("--------------------------------------------")    
#%% ethe enumerate functrion for tuples 
#https://www.w3schools.com/python/ref_func_enumerate.asp
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
en_list = list(enumerate(fruits))
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
print("--------------------------------------------")    

#%% Multiple assignment of vatriables
water, fire, electric,  grass =("Squirtle", "Charmander", "Pikachu", "Bulbasaur")

#%% For every key value pair, append the key to the list p_names, and append the value 
# to the list p_number. Do not use the .keys() or .values() methods
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}

## Using list and dictionary assignments
#p_names = list(pokemon.keys())
#p_number = list(pokemon.values())

# using tuple packing and unpacking
out_tup = list(pokemon.items())
p_names = []
p_number = []
#for nam,num in out_tup:
#    p_names = p_names + [nam]
#    p_number= p_number + [num]
# or equally by doing the unpacking behind the scenes:
for nam,num in pokemon.items():
    p_names = p_names + [nam]
    p_number= p_number + [num]    

#%%
track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
out_tup = list(track_medal_counts.items())
track_events = []   
for nam,num in out_tup:
    track_events = track_events + [nam]

#%% Using tuples for outputs of functions 
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
#    return c, a
#    return (c,a) #is exaclty the same!!!
    return [c,a]  # it is similar but the output will be a mutable list  which is not good

print(circleInfo(10))
circumference, area = circleInfo(10)
print("--------------------------------------------")        
#%%
def information(name,birth_year, fav_color,hometown):
    #return (name,birth_year, fav_color,hometown)
    #return name,birth_year, fav_color,hometown
    return [name,birth_year, fav_color,hometown]

a = information("Sarah",1996,"purple","St. Louis")

print (str(a))

def information(name,birth_year, fav_color,hometown):
    #return (name,birth_year, fav_color,hometown)
    return name,birth_year, fav_color,hometown
#    return [name,birth_year, fav_color,hometown]

a = information("Sarah",1996,"purple","St. Louis")

print (str(a))
print("--------------------------------------------")    
#%% unoacking multiple variable as functions inputs using the operator *
def addy(x, y):
    return x + y

print(addy(3, 4))
z = (5, 4)
print(addy(*z)) # this line will cause the values to be unpacked
print("--------------------------------------------")    









    
    
    