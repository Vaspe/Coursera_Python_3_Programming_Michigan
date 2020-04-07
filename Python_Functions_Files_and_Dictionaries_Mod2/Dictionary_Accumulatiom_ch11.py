# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:23:49 2020

@author: Vasilis
"""
#%% Accumulation of multiple outputs in a dictionary
fid = open('Files/scarlet.txt', 'r')
txt = fid.read()
fid.close()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        # we have not seen this character before, so initialize a counter for it
        x[c] = 0

    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1

print("a: " + str(x['a']) + " occurrences")
keylist= list(x.keys())
#keylist = keylist.sort()
#%%
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
words_all = sentence.split(" ")
word_counts = {}
for i in words_all:
    if  i not in word_counts:
        word_counts[i] = 0
    word_counts[i] = word_counts[i]+1

#%%
stri = "what can I do"
char_d = {}
for i in stri:
    if i not in char_d:
        char_d[i] = 0
    char_d[i] = char_d[i]+1
    
#%%
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0
for i in travel:
    
    total = total+ travel[i]

#%%
schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
total_credits=0
for i in schedule:
    total_credits =total_credits+ schedule[i]
        
#%%
d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
best_key_so_far = 'a'
for key in ks:
    if d[key] > d[best_key_so_far]:
        best_key_so_far =key
        

print("key " + str(best_key_so_far) + " has the highest value, " + str(d[best_key_so_far]))

#%%
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d={}
for i in placement:
    if i not in d:
        d[i] = 0
    d[i] = d[i] + 1

ks = list(d.keys())
min_val_key = ks[0]
for i in ks:
    if d[i] < d[min_val_key]:
        min_val_key = i
#d["min_value"] = d[min_val_key]    
min_value = min_val_key

#%%#
product = "iphone and android phones"
lett_d ={}
for i in product:
    if i not in lett_d:
        lett_d[i] = 0
    lett_d[i] = lett_d[i] +1

keysy = list(lett_d.keys())
max_value_key = keysy[0]
for i in keysy:
    if lett_d[i] > lett_d[max_value_key]:
        max_value_key = i
#d["min_value"] = d[min_val_key]    
max_value = max_value_key


    











    