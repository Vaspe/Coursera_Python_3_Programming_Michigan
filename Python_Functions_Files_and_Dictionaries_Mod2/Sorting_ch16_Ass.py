# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:11:34 2020

@author: Vasilis
"""

#%%ASS1

letters = "alwnfiwaksuezlaeiajsdl"

sorted_letters = sorted(letters,reverse=True)

#%%ASS2

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)

#%%ASS3
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners = sorted(winners)

#%%ASS4
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners1 = sorted(winners,reverse=True)

#%%ASS55
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners2 = sorted(winners,reverse=False,key = (lambda x:x.split(" ")[-1]))

#%%ASS6
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)

#%%ASS7
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three = sorted(medals,reverse= True, key = lambda x:medals[x])[:3]

#%%ASS8

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries,reverse = True,key = lambda x:groceries[x])

#%%ASS9
def last_four(x):
    aa = str(x)
    bb = aa[-4:]
    return int(bb)

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted (ids,key = last_four)

#%%ASS10
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted (ids,key = lambda x:int(str(x)[-4:])) # Very hard to read and ubderstand!

#%%ASS11
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst,key = lambda x:x[1])




