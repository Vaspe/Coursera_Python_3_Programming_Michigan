# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:10:11 2020

@author: Vasilis
"""

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)
    
    def opponent(self):
        if self.p_type == 'Grass':
            return ('Fire','Water')
        if self.p_type == 'Ghost':
            return ('Dark','Psychic')
        if self.p_type == 'Fire':
            return ('Water','Grass')
        if self.p_type == 'Flying':
            return ('Electric','Fighting')
        
#%%
class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]
     
    def action(self):
        print("{} knows a lot of different moves!".format(self.name))
    
    def attack_up(self):
        if self.level > 10:
            self.attack = self.attack + self.attack_boost
            return self.attack    

#%%
class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3

#%%
class Fire_Pokemon(Pokemon):
    p_type = "Fire"

#%%
class Flying_Pokemon(Pokemon):
    p_type = "Flying" 
           
#%% Actions
p1 = Grass_Pokemon("Belle")
p1.action()

p2 = Grass_Pokemon("Bulby")
p3 = Grass_Pokemon("Pica")

for i in range(6):
    p3.train()
print(p2)    
print(p2.attack)