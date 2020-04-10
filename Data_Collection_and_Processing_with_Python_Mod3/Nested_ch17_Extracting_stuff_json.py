# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:56:56 2020

@author: Vasilis
"""
import json
#%% Extracting information from nested data
"""
Very useful:
    https://jsoneditoronline.org/
    
Follow the system described below and you will have success with extracting nested data. 
The process involves the following steps:

 1. Understand the nested data object.
 2. Extract one object at the next level down.
 3. Repeat the process with the extracted object

Understand. Extract. Repeat.    
"""
# load the text from json file
fid = open("Files/twit_res.json",'r')
in_twit_json = fid.read()
fid.close()
#print(json.dumps(in_twit_json, indent=4)[:100])
#print('--------')  

# un pack json with json.loads()
dic_twit = json.loads(in_twit_json)

#check type and keys or elements: UNDERSTAND
print("----Level 1 file conents-----")
print(type(dic_twit))  # check type
print(dic_twit.keys())

#Getting the infomation you wat  EXTRACT
useful_info = dic_twit['statuses']

#Go to deeper levels. REPEAT
print("----Level 2 statuses-----")
print(type(useful_info)) # it's a list!
print(len(useful_info))

print("----Level 3: stuff in statuses----")
for res3 in useful_info: 
   print(type(res3)) # it's a dic
   print(res3.keys()) # it's a dic
   print(len(res3)) 
   
#for i in useful_info[0]:
#    print("----Level 4: stuff in "+ i +"----")
#    print(type(useful_info[1][i])) # it's a list!
#    print(useful_info[1][i])    

print("----Level 4: stuff in user----")
print(type(useful_info[0]['user']))
print(useful_info[0]['user'].keys())
us_field = useful_info[0]['user']

print("----Level 5: Screen name in user----")
print(type(us_field['screen_name'])) # finally we reached the bottom!
print(us_field['screen_name'])
print("------------------------------------------------------------")


#%%  
print ("Now we know the structure, extract allacount and creeated date:")
# extract all 'users' from all element of the list statuses
fid = open("Files/twit_res.json",'r')
twit_data = json.loads(fid.read())
fid.close()
#for iEl in   useful_info[0]:
#    us_all
#   
names_in_file = []
for iLst in twit_data['statuses']:
    names_in_file = names_in_file + [iLst['user']['screen_name'],iLst['user']['created_at']]
    print(iLst['user']['screen_name'],iLst['user']['created_at'])


