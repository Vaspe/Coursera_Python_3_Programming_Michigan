# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:27:29 2020

@author: Vasilis
"""

#%%
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num_rainy_months = 0
pure_rainfall_mi = rainfall_mi.split(",")
for i in pure_rainfall_mi:
    if float(i) > 3.0:
        num_rainy_months = num_rainy_months + 1
print (num_rainy_months)


#%%

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
words = sentence.split(" ")
same_letter_count = 0

for i in words:
    if i[0]==i[-1]:
       same_letter_count = same_letter_count+1 

#%%%
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0

for i in items:
    if 'w' in i:
        acc_num = acc_num + 1
        
#%%
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

words = sentence.split(" ")
num_a_or_e = 0

for i in words:
    if ("a" in i or "e" in i):
        num_a_or_e = num_a_or_e +1        
        
#%%
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = 0

for i in s :
    if i in vowels:
        num_vowels = num_vowels + 1        

#%%
w = "Friendship is a wonderful human experience!"

if "Friendly" in w:
    wrd = "Friendly is here!"
elif "Friend" in w:
    wrd = "Friend is here!"
else:
    wrd = "No variation of friend is in here."

#%%



#%%
    
    
    
    
#%%    











