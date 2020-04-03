# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:47:45 2020

@author: Vasilis
"""

verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]

for i in range(len(verbs)):
    verbs[i] = verbs[i]+"ing"
    
#%%

classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
upper = []
lower = []
for i in classes:
    if int(i[-3:])>=200:
        upper = upper + [i]
    else:
        lower = lower +[i]

#%%
myList = [76, 92.3, 'hello', True, 4, 76]
myList.append("apple")  
myList.append(76)  
myList.insert(2,"cat")
myList.insert(0,99)
myList.index("hello")
myList.count(76)
myList.remove(76)
myList.pop(myList.index(True))

#%%
import keyword
test = ["else", "integer", "except", "elif"]
keyword_test = []

for i in test:
    keyword_test = keyword_test +[keyword.iskeyword(i)]

#%%
import string
nums = string.digits
chars = ['h', '1', 'C', 'i', '9', 'True', '3.1', '8', 'F', '4', 'j']
cnt = 0
is_num = []
for i in chars:
    is_num = is_num + [(i,i in nums)]
    cnt = cnt +1
    
#%%
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
words = org.split(" ")
acro = ""
for i in words:
    if not(i in stopwords):
        acro = acro + i.upper()[0]    

#%%
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
words = sent.split(" ")
acro = ''

for i in words:
    if not(i in stopwords):
        acro = acro + i.upper()[0] + i.upper()[1] + ". "  

acro = acro[0:len(acro)-2]        

#%%
p_phrase = "was it a car or a cat I saw"

r_phrase = p_phrase[::-1]

print(p_phrase==r_phrase)

#%%
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]


for i in inventory:
    items = i.split(", ")
    print ("The store has {} {}, each for {} USD".format(items[1],items[0],items[2]))
