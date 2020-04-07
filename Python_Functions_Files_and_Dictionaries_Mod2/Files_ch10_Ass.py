# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:20:11 2020

@author: Vasilis
"""
#%%
fid = open("Files/travel_plans2.txt")
text = fid.read() 
fid.close
num = len(text)     

#%%
# 1st attempt is wrong because it does not see the line change as space
fid = open("Files/emotion_words2.txt")
text2 = fid.read() 
fid.close
words2 = text2.split(" ")
num_words2= len(words2) 

num_words = 0
fid = open("Files/emotion_words2.txt")
for i in fid:
    print(i)
    num_words = num_words + len(i.split(" ")) 
fid.close
num_words = num_words 

#%% 
fid = open("Files/school_prompt2.txt")
lines = fid.readlines()
fid.close
num_lines = len(lines)

#%%
fid = open("Files/school_prompt2.txt")
beginning_chars = fid.read(30)
fid.close   


#%% 
fid = open("Files/school_prompt2.txt")
lines = fid.readlines()
fid.close
three = []
for i in lines:
    words = i.split(" ")
    three = three + [words[2]]
    
#%%
emotions = []    
fid = open("Files/emotion_words2.txt")
for i in fid:

    emotions = emotions + [i.split(" ")[0] ]
fid.close    

#%%
fid = open("Files/travel_plans2.txt")
first_chars = fid.read(33)
fid.close   

#%%
words3 =[]
fid = open("Files/school_prompt2.txt")
for i in fid.readlines():
    words3 = words3 + i.strip().split(" ")
fid.close
p_words_len = 0
p_words = []
for i in words3:
    if "p" in i:
#        if i[-1] == ',' or i[-1]==".":
#            endm1 = len(i)-1
#            i = i[0:endm1]    
        if i[-2:] == '\n':
            endm1 = len(i)-2
            i = i[0:endm1]      
        p_words_len = p_words_len +1
        p_words = p_words + [i]

#%%

fid = open("Files/SP500.txt","r")

lines = fid.readlines()
fid.close()
header = lines[0]
labels_nam = header.split(",")
ind1 = labels_nam.index("SP500")
ind2 = labels_nam.index("Long Interest Rate")

cnt = 0 
cnt2 = 0 
SP_val_tot = 0
max_interest = 0
SP_val = []
interest_val = []

for i in lines[1:]:
    curline = i
    curline = curline.split(",")
    SP_val = SP_val + [curline[ind1]]
    interest_val = interest_val+ [float(curline[ind2])]
    if cnt >=5 and cnt<=16:
        SP_val_tot =  SP_val_tot + float(SP_val[cnt])
        if max_interest< float(interest_val[cnt]): 
            max_interest = float(interest_val[cnt])
        cnt2 = cnt2 +1
    cnt =cnt+1;
    
mean_SP = SP_val_tot/cnt2        
        


