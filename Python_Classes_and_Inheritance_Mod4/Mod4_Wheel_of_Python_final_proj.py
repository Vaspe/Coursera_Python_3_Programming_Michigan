# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:58:38 2020

@author: Vasilis
"""
import time
import random 
import json

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#%% Define functions
def spinWheel():
    """
    returns a random dictionary from all the possible wheel cases
    with type, text,value and prize keys. No input required
    # Examples:
   { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
   { "type": "bankrupt", "text": "Bankrupt", "prize": false },
   { "type": "loseturn", "text": "Lose a turn", "prize": false }
    """
    fid = open("Files/wheel.json", 'r')
    wheel = json.loads(fid.read())
    fid.close()    
    return random.choice(wheel)

# aa = spinWheel()

def getRandomCategoryAndPhrase():  
    """
    Gives a random category and phrase from a list
    The output is a tuple with the firs part being the category
    and the second the phrse.
    """
    with open("Files/phrases.json", 'r') as fid:        
        phrases = json.loads(fid.read())
        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        
        return (category, phrase.upper())

# bb = getRandomCategoryAndPhrase()

def obscurePhrase(phrase, guessed):
    """
    Given a phrase and a list of guessed letters, returns an obscured version
    Example:
        guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
        phrase:  "GLACIER NATIONAL PARK"
        returns> "_L___ER N____N_L P_RK"    
    """
    rv = ''
    for s in phrase:
        if (s.upper() in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv

# cc = obscurePhrase('murder and crime',['r','d'])

def showBoard(category, obscuredPhrase, guessed):
    """
    It returns a string representing the current state of the game
    """
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))

# print (showBoard('Singer', "S__ S___n",['S']))


#%% Define classes




#%% Time module example 
# time.sleep(x) delays code execution for x seconds

# for x in range(2, 6):
#     print('Sleep {} seconds..'.format(x))
#     time.sleep(1) # "Sleep" for x seconds
# print('Done!')

#%% Random module example
# random.randint(min, max) generates a random number between min and max (inclusive)
# random.choice(L) selects a random item from the list L

# random.choice(L) selects a random item from the list L
# rand_number = random.randint(1, 10)
# print('Random number between 1 and 10: {}'.format(rand_number))

# letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
# rand_letter = random.choice(letters)
# print('Random letter: {}'.format(rand_letter))

#%%



