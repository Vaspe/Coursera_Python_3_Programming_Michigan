# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:26:37 2020

@author: Vasilis
"""

#%% Write code to assign the string "You can apply to SI!" to output if the string "SI 106"
# is in the list courses. If it is not in courses, assign the value "Take SI 106!" to the variable output.
courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]

if ("SI 106" in courses) :
    output = "You can apply to SI!"
else:
    output = "Take SI 106"
    
# unary selection is when the if is followed by no else so it is basically only does something if one option is valid
# binary selection is when we use both if and else statements (no else if!)
#  chained conditional is when we have more than two options in the flow of the conditional e.g. if elif else
        
#%%
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]

resps= []

for i in percent_rain:
    if i > 90: # temretaure about 90
        resps = resps + ["Bring an umbrella."] 
    elif i > 80: # temperature between 80 and 90
        resps = resps + ["Good for the flowers?"] 
    elif i>50: # temperature between 50 and 80
        resps = resps + ["Watch out for clouds!"] 
    else: # temperature under 50
        resps = resps +["Nice day!"]    
        
#%%
x = 64
output = []

if x > 63:
    output.append(True)
elif x > 55:
    output.append(False)
else:
    output.append("Neither")

if x > 67:
    output.append(True)
else:
    output.append(None)        
    
#%%  
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []

for i in words:
    if i[-1] == 'e':
        past_tense = past_tense +[i + 'd']
    else:
        past_tense = past_tense +[i + 'ed']
    
print (past_tense)    
 
 #%%
num_lst = [3, 20, -1, 9, 10]
is_odd =[]
for i in num_lst:
    if i%2 == 0:
        is_odd.append(True)
    else:
        is_odd.append(False)