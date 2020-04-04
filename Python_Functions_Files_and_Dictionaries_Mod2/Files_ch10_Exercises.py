# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:49:41 2020

@author: Vasilis
"""

#%% Ex1

fid = open("Files/studentdata.txt","r")

for i in fid:
    curline = i.split(" ")
    if len(curline)>7:
        print (str(curline[0]))
fid.close        
        
#%% Ex2

fid = open("Files/travel_plans2.txt","r")

destination = []
for i in fid:
    if ":" in i:
       destination = destination + [i] 
    
        
fid.close        

#%% Ex3 
fid = open("Files/emotion_words2.txt","r")
whole_text = fid.read()        
fid.close   

j_emotions = []

words = whole_text.split(" ")
for i in words:
    if i[0] == 'j':
        j_emotions = j_emotions +[i]
     
   
