# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:58:38 2020

@author: Vasilis
"""
import time
import random 
import json

#%%




#%% Time module example 
# time.sleep(x) delays code execution for x seconds

for x in range(2, 6):
    print('Sleep {} seconds..'.format(x))
    time.sleep(1) # "Sleep" for x seconds
print('Done!')

#%% Random module example
# random.randint(min, max) generates a random number between min and max (inclusive)
# random.choice(L) selects a random item from the list L

random.choice(L) selects a random item from the list L
rand_number = random.randint(1, 10)
print('Random number between 1 and 10: {}'.format(rand_number))

letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
rand_letter = random.choice(letters)
print('Random letter: {}'.format(rand_letter))

#%%



