# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:32:16 2020

@author: Vasilis
"""

#%% Ex 1
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}

credits1 = 0 # credits is a keyword in python 3.7!
for i in Junior:
    credits1 = credits1 + Junior[i]

    
#%%

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for i in str1:
    if i not in freq:
        freq[i] = 0
    freq[i] = freq[i] + 1

#%%\
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
words = str1.split(' ')
freq_words = {}
for i in words:
    if i not in freq_words:
        freq_words[i] = 0
    freq_words[i] = freq_words[i] + 1
    

#%%
sally = "sally sells sea shells by the sea shore"

freq = {}
for i in sally:
    if i not in freq:
        freq[i] = 0
    freq[i] = freq[i] + 1

characters = freq
keylist = characters.keys()
best_char = keylist[0]
for i in characters:
    if characters[i] > characters[best_char]:
        best_char = i
    
#%%
sally = "sally sells sea shells by the sea shore and by the road"

freq = {}
for i in sally:
    if i not in freq:
        freq[i] = 0
    freq[i] = freq[i] + 1

characters = freq
keylist = characters.keys()
worst_char = keylist[0]
for i in characters:
    if characters[i] < characters[worst_char]:
        worst_char = i
    
#%%
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."

freq = {}
for i in string1:
    i = i.lower()
    if i not in freq:
        freq[i] = 0
    freq[i] = freq[i] + 1

letter_counts  = freq

#%%
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

string1 = p
freq = {}
for i in string1:
    i = i.lower()
    if i not in freq:
        freq[i] = 0
    freq[i] = freq[i] + 1

low_d   = freq

        

    
    