# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:58:38 2020

@author: Vasilis
"""
import time
import random 
import json

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWEL_COST = 250
VOWELS = 'AEIOU'
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ'
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

def getNumberBetween(prompt, min, max):
    """
    Asks the user for a number between min & max (inclusive)
    Using a listener the input is checked for correctness
    """
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

#ee = getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10)

def requestPlayerMove(player, category, guessed):
    while True: # we're going to keep asking the player for a move until they give a valid one
        time.sleep(0.1) # added so that any feedback is printed out before the next prompt

        move = player.getMove(category, obscurePhrase(phrase, guessed), guessed)
        move = move.upper() # convert whatever the player entered to UPPERCASE
        if move == 'EXIT' or move == 'PASS':
            return move
        elif len(move) == 1: # they guessed a character
            if move not in LETTERS: # the user entered an invalid letter (such as @, #, or $)
                print('Guesses should be letters. Try again.')
                continue
            elif move in guessed: # this letter has already been guessed
                print('{} has already been guessed. Try again.'.format(move))
                continue
            elif move in VOWELS and player.prizeMoney < VOWEL_COST: # if it's a vowel, we need to be sure the player has enough
                    print('Need ${} to guess a vowel. Try again.'.format(VOWEL_COST))
                    continue
            else:
                return move
        else: # they guessed the phrase
            return move

#%% Define classes
class WOFPlayer:
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    VOWEL_COST = 250
    VOWELS = 'AEIOU'
    
    def __init__ (self,init_name):
        self.name = init_name
        self.prizeMoney = 0
        self.prizes = []
     
    def addMoney(self,amt):  
        self.prizeMoney = self.prizeMoney + amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self,prize):
        self.prizes = self.prizes + [prize]
    
    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney)
        

class WOFHumanPlayer(WOFPlayer):
    
    def getMove(self,category, obscuredPhrase, guessed):
        prompt = """
        {} has ${}

        Category: {}
        Phrase:  {}
        Guessed: {}

        Guess a letter, phrase, or type 'exit' or 'pass':
        """.format(self.name, self.prizeMoney,category,obscuredPhrase,guessed)
        userinp = input(prompt) # ask the first time
        return userinp
    
class WOFComputerPlayer(WOFPlayer):
    
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    VOWEL_COST = 250
    
    def __init__ (self,init_name,difficulty):
        WOFPlayer.__init__(self, init_name)
        self.difficulty = difficulty
      
    def smartCoinFlip(self):
        number_r = random.randint(1, 10)
        if number_r > self.difficulty:
            return True
        else:
            return False
       
    def getPossibleLetters(self,guessed):
        let_lst = [char for char in LETTERS]
        out_lst = [x for x in let_lst if (x in LETTERS and x not in guessed)]
        if not out_lst:
            out_lst = []
        return out_lst
    
    def getMove(self,category, obscuredPhrase, guessed):
        guess_let = self.getPossibleLetters(guessed)
        if not  guess_let:
            return 'pass'
        elif (all(elem in self.VOWELS for elem in guess_let) and self.prizeMoney < self.VOWEL_COST):
            return 'pass'
        else:
            if self.smartCoinFlip():
                for char in self.SORTED_FREQUENCIES[::-1]:
                    if char not in guessed and (char not in self.VOWELS and self.prizeMoney < self.VOWEL_COST) :
                        return char
            else: 
                if self.prizeMoney >= self.VOWEL_COST:
                    char2 = random.choice(self.getPossibleLetters(guessed))
                    return char2
                else:
                    new_lst = [x for x in guess_let if x not in self.VOWELS]
                    char2 = random.choice(new_lst)
                    return char2
                    
            
#%%testin'

# LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# VOWEL_COST = 250
# VOWELS = 'AEIOU'
# player = WOFComputerPlayer('tim',8)


# # # guessed = [i for i in 'BCDFGHJKLMNPQRSTYVXWZ']
# # # move = player.getMove('Places & People', '_____ _____ ____', guessed)
# # # print(move)
# # # if move in VOWELS:
# # #     anyInvalidGuesses = (move, guessed)


# resul = []
# for _ in range(100):
#     guessed = random.sample(LETTERS, 10)
#     move = player.getMove('Places & People', '_____ _____ ____', guessed)
#     resul =resul + [move]
#     if move in VOWELS:
#         anyInvalidGuesses = (move, guessed)
#         break

# ove = player.getMove('Places & People', '_____ _____ ____', LETTERS) # NO VALID GUESSES

#%% Actual game set up

# GAME LOGIC CODE
print('='*15)
print('WHEEL OF PYTHON')
print('='*15)
print('')

num_human = getNumberBetween('How many human players?', 0, 10)

# Create the human player instances
human_players = [WOFHumanPlayer(input('Enter the name for human player #{}'.format(i+1))) for i in range(num_human)]

num_computer = getNumberBetween('How many computer players?', 0, 10)

# If there are computer players, ask how difficult they should be
if num_computer >= 1:
    difficulty = getNumberBetween('What difficulty for the computers? (1-10)', 1, 10)

# Create the computer player instances
computer_players = [WOFComputerPlayer('Computer {}'.format(i+1), difficulty) for i in range(num_computer)]

players = human_players + computer_players

# No players, no game :(
if len(players) == 0:
    print('We need players to play!')
    raise Exception('Not enough players')

# category and phrase are strings.
category, phrase = getRandomCategoryAndPhrase()
# guessed is a list of the letters that have been guessed
guessed = []

# playerIndex keeps track of the index (0 to len(players)-1) of the player whose turn it is
playerIndex = 0

# will be set to the player instance when/if someone wins
winner = False


#%% GAME LOOP!

while True:
    player = players[playerIndex]
    wheelPrize = spinWheel()

    print('')
    print('-'*15)
    print(showBoard(category, obscurePhrase(phrase, guessed), guessed))
    print('')
    print('{} spins...'.format(player.name))
    time.sleep(2) # pause for dramatic effect!
    print('{}!'.format(wheelPrize['text']))
    time.sleep(1) # pause again for more dramatic effect!

    if wheelPrize['type'] == 'bankrupt':
        player.goBankrupt()
    elif wheelPrize['type'] == 'loseturn':
        pass # do nothing; just move on to the next player
    elif wheelPrize['type'] == 'cash':
        move = requestPlayerMove(player, category, guessed)
        if move == 'EXIT': # leave the game
            print('Until next time!')
            break
        elif move == 'PASS': # will just move on to next player
            print('{} passes'.format(player.name))
        elif len(move) == 1: # they guessed a letter
            guessed.append(move)

            print('{} guesses "{}"'.format(player.name, move))

            if move in VOWELS:
                player.prizeMoney -= VOWEL_COST

            count = phrase.count(move) # returns an integer with how many times this letter appears
            if count > 0:
                if count == 1:
                    print("There is one {}".format(move))
                else:
                    print("There are {} {}'s".format(count, move))

                # Give them the money and the prizes
                player.addMoney(count * wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])

                # all of the letters have been guessed
                if obscurePhrase(phrase, guessed) == phrase:
                    winner = player
                    break

                continue # this player gets to go again

            elif count == 0:
                print("There is no {}".format(move))
        else: # they guessed the whole phrase
            if move == phrase: # they guessed the full phrase correctly
                winner = player

                # Give them the money and the prizes
                player.addMoney(wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])

                break
            else:
                print('{} was not the phrase'.format(move))

    # Move on to the next player (or go back to player[0] if we reached the end)
    playerIndex = (playerIndex + 1) % len(players)

if winner:
    # In your head, you should hear this as being announced by a game show host
    print('{} wins! The phrase was {}'.format(winner.name, phrase))
    print('{} won ${}'.format(winner.name, winner.prizeMoney))
    if len(winner.prizes) > 0:
        print('{} also won:'.format(winner.name))
        for prize in winner.prizes:
            print('    - {}'.format(prize))
    time.sleep(10)        
else:
    print('Nobody won. The phrase was {}'.format(phrase))

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
