# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:27:13 2020

@author: Vasilis
"""

#%% Write a program that extracts the last three items in the list sports and assigns it
# to the variable last. Make sure to write your code so that it works no matter how many items are in the list.

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last2 = []
for i in range (-3,0,1):
    #print(i)
    #print(sports[i])
    last2 = last2+[sports[i]]

last = sports[-3:]
#print(str(last))

#%% Write code that combines the following variables so that the sentence “You are 
# doing a great job, keep it up!” is assigned to the variable message. Do not edit
# the values assigned to by, az, io, or qy.

by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

ioplus = "".join([io,","])
ioplusplus = "".join([az, ioplus])
message2 = " ".join([by,ioplusplus,qy])
message = " ".join([by, "".join([az, "".join([io,","])]),qy])
print(message)

#%% Write code to determine how many 9’s are in the list nums and assign that value 
# to the variable how_many. Do not use a for loop to do this.
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

how_many = nums.count(9)

#%% Write code that uses slicing to get rid of the the second 8 so that here are 
#only two 8’s in the list bound to the variable nums.
nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

nums = nums[:4]+nums[5:]
print (str(nums))

#%% Assign the last element of lst to the variable end_elem. Do this so that it works no matter how long lst is.
lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

end_elem = lst[-1]

#%% Assign the number of elements in lst to the variable num_lst.
lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

num_lst = len(lst)

#%% Create a variable called wrds and assign to it a list whose elements are the 
# words in the string sent. Do not worry about punctuation.
sent = "The bicentennial for our university was in 2017"
wrds = sent.split()

