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
    if len(animals) == 0:
        return None
    else:    
        for pet in petlist:
#            print(pet.name)
            if pet.name == name:
#                print('found')
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
        CheckMood <petname>
        Info <petname>
        
    
        Choice: """    
    glob_err1 = "Wrong input. Please check your input again\n" 
    feedback ="\n"
    while 1 == 1:
#        print(str(animals))
        action = input('\n' + feedback + '\n' + base_prompt)
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
    #            print(pet_name)
                if pet_name is None :
                    animals.append(Pet(words[1]))
                    feedback = feedback + words[1] + " added to your pet list\n"
#                    print(str(animals))
                else:
                    feedback = feedback + 'You already have a pet with the name {}.\n'.format(words[1])
        elif command == 'Greet':
            if len(words) != 2:
               feedback = feedback + glob_err1  
            else:   
                pet_name = whichone(animals,words[1])
                if pet_name is None :
                     feedback = feedback + words[1] + " is not in your pet list \n"
                else:
                    pet_name.hi()
        elif command == 'Teach':
            if len(words) != 3:
               feedback = feedback + glob_err1  
            else:   
                pet_name = whichone(animals,words[1])
                if pet_name is None :
                     feedback = feedback + words[1] + " is not in your pet list \n"
                else:
                    if words[2] not in pet_name.sounds:
                        pet_name.teach(words[2])
                    else:
                        feedback = feedback + words[1] + " already knows " + words[2]
        elif command == 'Feed':
            if len(words) != 2:
               feedback = feedback + glob_err1  
            else:   
                pet_name = whichone(animals,words[1])
                if pet_name is None :
                     feedback = feedback + words[1] + " is not in your pet list \n"
                else:
                    pet_name.feed()            
        elif command == 'PetList':
            if len(words) != 1:
                feedback = feedback + glob_err1  

            else:
                if len(animals) != 0:
                    feedback = feedback + 'You have the following pets in your list: '  + str([x.name for x in animals])                
                else:
                    feedback = feedback + 'Your pet list is currently empty. You can adopt a pet!'
        elif command == 'CheckMood':
            if len(words) != 2:
               feedback = feedback + glob_err1  
            else:   
                pet_name = whichone(animals,words[1])
                if pet_name is None :
                     feedback = feedback + words[1] + " is not in your pet list \n"
                else:
                    feedback = feedback +pet_name.name + ' is now ' + pet_name.mood()  
        elif command == 'Info':
            if len(words) != 2:
               feedback = feedback + glob_err1  
            else:   
                pet_name = whichone(animals,words[1])
                if pet_name is None :
                     feedback = feedback + words[1] + " is not in your pet list \n"
                else:
                    feedback = feedback +pet_name.name + ' info is \n' + pet_name.__str__()  
        else:
            feedback = feedback + glob_err1  
            
        for ipet in animals:
            ipet.clock_tick()
#            feedback += "\n" + pet.__str__()                        
                    
play_Tamagotchi()                
                
                
                
                
            

#%% Testing our pet!
                