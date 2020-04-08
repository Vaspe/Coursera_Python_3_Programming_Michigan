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
