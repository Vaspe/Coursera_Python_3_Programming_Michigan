# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:12:15 2020

@author: Vasilis

Good doc:
    https://www.w3schools.com/python/ref_func_zip.asp

Syntax:
    zip(iterator1, iterator2, iterator3 ...)
    
 The zip function takes multiple lists and turns them into a list of tuples (actually,
 an iterator, but they work like lists for most practical purposes), pairing up all 
 the first items as one tuple, all the second items as a tuple, and so on    
    
    
"""

#%% Pairwise summation without zip

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

for i in range(len(L1)):
    L3.append(L1[i] + L2[i])

print(L3)

#%%% zip creates a list with all the elements in the same postioionsand we can 
# then sum them up
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = list(zip(L1, L2))

for (x1, x2) in L4:
    L3.append(x1+x2)

print(L3)

#%% Even more simplified with list comperhension
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)

#%%Or using map and not unpacking the output tuples of zip
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = list(map(lambda x: x[0] + x[1], list(zip(L1, L2))))
print(L3)

#%% example fot hangman game!
"""
#Consider a function called possible, which determines whether a word is still possible 
to play in a game of hangman, given the guesses that have been made and the current 
state of the blanked word.
"""

def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

#%% rewriting ewith zip
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

#%%
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1+x2 for (x1,x2) in list(zip(L1,L2)) if (x1>10 and x2<5)]
