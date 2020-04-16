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
        self.hunger =self.hunger + 1

    def hi(self):
        self.reduce_boredom()
        print(sounds[random.randrange(len(sounds))])
     
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
                