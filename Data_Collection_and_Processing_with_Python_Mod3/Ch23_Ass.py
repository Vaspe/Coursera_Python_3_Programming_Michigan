# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:18:13 2020

@author: Vasilis
"""

#%% Ass1
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = map(lambda x: 'Fruit: '+x,lst_check  )

#%% Ass2
countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = filter((lambda x: x[0] == 'B'),countries)

#%% Ass3
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names  = [x[1] for x in people]

#%% Ass4
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [x*2 for x in lst]


#%% Ass5
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [x[0] for x in students if x[1]>=70]

#%% Ass6
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites =list(filter(lambda x:(len(x[0])>3 and len(x[1])>3) ,zip(l1,l2)))

#%% Ass7
species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info =zip(species,population)
endangered = [x[0] for x in pop_info if x[1]<2500]

