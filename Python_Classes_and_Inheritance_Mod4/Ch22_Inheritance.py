# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:57:07 2020

@author: Vasilis

It works by defining a new class, and using a special syntax to show what the new
sub-class inherits from a super-class. In the definition of the inherited class,
you only need to specify the methods and instance variables that are different
from the parent class (the parent class, or the superclass, is what we may call
the class that is inherited from.  
"""

#%%
#Adding sub vlasses based on the type of pet that will share aome common methods

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
#        self.sounds = init_sounds  This does not work with inheritance be very carefull!!
        self.sounds = self.sounds
        
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

#%%
"""
In the definition of the class Cat, we only need to define the things that are 
different from the ones in the Pet class.
"""
# Here's the new definition of class Cat, a subclass of Pet.
class Cat(Pet): # the class name that the new class inherits from goes in the parentheses, like so.
    sounds = ['Meow']

    def chasing_rats(self):
        return "What are you doing, Pinky? Taking over the world?!"

#%% We can go multiple levels. Noew a new class will inherit from cat
class Cheshire(Cat): # this inherits from Cat, which inherits from Pet

    def smile(self): # this method is specific to instances of Cheshire
        print(":D :D :D")
        
#%% testin'
p1 = Pet("Fido")
print(p1) # we've seen this stuff before!

p1.feed()
p1.hi()
print(p1)

cat1 = Cat("Fluffy")
print(cat1) # this uses the same __str__ method as the Pets do

cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi()
print(cat1)

print(cat1.chasing_rats())

#print(p1.chasing_rats()) # This line will give us an error. The Pet class doesn't have this method!

print('-------------------------')
# Let's try it with instances.
cat1 = Cat("Fluffy")
cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi() # Uses the special Cat hello.
print(cat1)

print(cat1.chasing_rats())

new_cat = Cheshire("Pumpkin") # create a Cheshire cat instance with name "Pumpkin"
new_cat.hi() # same as Cat!
new_cat.chasing_rats() # OK, because Cheshire inherits from Cat
new_cat.smile() # Only for Cheshire instances (and any classes that you make inherit from Cheshire)

# cat1.smile() # This line would give you an error, because the Cat class does not have this method!

# None of the subclass methods can be used on the parent class, though.
p1 = Pet("Teddy")
p1.hi() # just the regular Pet hello
#p1.chasing_rats() # This will give you an error -- this method doesn't exist on instances of the Pet class.
#p1.smile() # This will give you an error, too. This method does not exist on instances of the Pet class.
