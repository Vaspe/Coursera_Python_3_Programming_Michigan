# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:49:03 2020

@author: Vasilis
"""
import random
import copy

class Pet:
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp', 'Aaarghh', 'Miauuuuu'] 
    
    def __init__ (self, name = 'Kitty',init_hunger = random.randrange(0,hunger_threshold,1) , init_boredom =random.randrange(0,boredom_threshold,1),init_sounds = copy.deepcopy(sounds)):
        self.name = name
        self.hunger = init_hunger
        self.boredom = init_boredom
        self.sounds = init_sounds 
        
    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def clock_tick(self):
        self.boredom = self.boredom + 1
        self.hunger = self.hunger + 1

    def hi(self):
        self.reduce_boredom()
        print(self.sounds[random.randrange(len(self.sounds))])
     
    def teach(self,word):
        self.sounds.append(word)
        self.reduce_boredom
        
    def feed(self):
        self.reduce_hunger()
    
    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
    
    def __str__(self):    
        state = "I'm {}. \nI feel {}.\n".format(self.name,self.mood())
        state = state + "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state

#%% Listenr loop to wrap arount the pet so that it is playable!

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched      

def play_Tamagotchi():
    animals = []
    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces_please>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>
        PetList 

        Choice: """    
    glob_err1 = "Wrong input. Please check your input again\n" 
    feedback =""
    while 1 == 1:
        
        action = input(feedback + '\n' + base_prompt)
        feedback =""
        words = action.split(" ")
        if len(words)>0:
            command = words[0]
        else:
            command = None    
            
        if command == 'Quit':
            return 'Game ended'
        elif command == 'Adopt':
            if len(words) != 2:
               feedback = feedback + glob_err1
            else:
                pet_name = whichone(animals,words[1])
                if pet_name == None:
                    animals.append(Pet(pet_name))
                    print(words[1] + " added to your pet list") 
                else:
                    feedback = feedback + 'You already have a pet with the name {}.\n'.format(pet_name)
                
                
                
                
                
                
                
            

#%% Testing our pet!
                