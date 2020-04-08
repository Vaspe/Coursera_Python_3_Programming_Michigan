# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:50:52 2020

@author: Vasilis
"""

#%% Ass 1
olympics=("Beijing", "London", "Rio", "Tokyo")


#%% Ass 2
tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]

country = []
for itup in tuples_lst:
    country = country + [itup[1]]


#%% Ass 3
olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp    


#%%
def info(name, gender, age, bday_month,hometown):
    return (name, gender, age, bday_month,hometown)

ret_val =info('Sue', 'Female', 20, 'March', 'Ann Arbor') 


#%%
gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals =[]
for itup in gold.items():
    num_medals =num_medals + [itup[1]]
#or equqlaly
dic_list =list(gold.items())
num_medals2 =[]
for nam,num in dic_list:
    num_medals2 = num_medals2 +[num] 
    


