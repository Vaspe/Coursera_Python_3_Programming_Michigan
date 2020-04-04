# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 23:50:48 2020

@author: Vasilis
Useful refeerences:
https://www.w3schools.com/python/python_file_handling.asp
https://www.w3schools.com/python/python_ref_file.asp
"""



#%% 
'''
We have to open a file with a reference name like fileref (or fid) using the open command

The input of the text file name is a string and the second argument is the 
 r for read , w for writem, a for append and x to create a file. Additionally we can add t or 
 b for habdling as text or binary.
 
At the end the file has to be closed with the xxx.close() method. Always close the file!
'''
#fileref = open("Files/olympics.txt", "r")
### other code here that refers to variable fileref
#contents = fileref.read()
#fileref.close()


#%% file methods https://www.w3schools.com/python/python_ref_file.asp
fileref = open("Files/olympics.txt", "r")

#fileref.flush()
com_readline = fileref.readline() #reads the next line
com_readable = fileref.readable()
com_seekable = fileref.seekable()
com_tell = fileref.tell()
com_writable = fileref.writable()
com_readlines = fileref.readlines() # reads whole klines the narguments is the number of charactes which is ceiled up to include the full lastline. If empty returns a listi conataining each line as an element
com_read = fileref.read(5) # argument is the number of characters to be read. If empry reads the whole file in one variable
fileref.close()

'''
A common error that novice programmers make is not realizing that all these ways of 
reading the file contents, use up the file. After you call readlines(), if you call 
it again you’ll get an empty list.
'''

#%% testing writing
fileref = open("Files/TestFile1.txt","w") 
fileref.write("This is my first text!!") 

fileref.close()

#%%
fileref = open("Files/school_prompt2.txt","r") 
whole_file = fileref.read()
numchar = len(whole_file)

fileref.close()

#%%
fileref = open("Files/travel_plans2.txt","r") 
file_lines = fileref.readlines()
num_lines = len(file_lines)

fileref.close()
#%%
fileref = open("Files/emotion_words2.txt","r") 
input_str= fileref.read(40)
fileref.close()

fid = open ("Files/first_forty.txt","w")
fid.write(input_str)
fid.close


