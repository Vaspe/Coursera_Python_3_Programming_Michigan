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
    
    def __init__ (self, name = 'Kitty',init_hunger = random.randrange(hunger_threshold) , init_boredom =random.randrange(boredom_threshold),init_sounds = copy.deepcopy(sounds)):
        self.name = name
        self.hunger = init_hunger
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = init_sounds 