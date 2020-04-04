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

#%%
olympicsfile = open("Files/olympics.txt", "r")

for aline in olympicsfile.readlines():
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olympicsfile.close()

print ("----------------------------------------------------------")
#%%
olympicsfile = open("Files/olympics.txt", "r")
 # we cana avoid readlines as python does it aurtomatically in loops. This is faste thanmreadlines
for aline in olympicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olympicsfile.close()

#%% Using with for files
with open('Files/mydata.txt', 'r') as md:
    for line in md:
        print(line)
# with automates the close of the file since md is a file object and makes sure we clsose the file at the end

#%%
fid = open ("Files/squared_numbers.txt",'w')

for i in range(13):
    square = i*i
    fid.write(str(square)+"\n")

fid.close()

print ("----------------------------------------------------------")
#%% CSV files
fid = open("Files/olympics.txt", "r")
lines = fid.readlines()
header = lines[0]
field_names = header.strip().split(',') # we need to remove also white spaces around the variables!!!
print("The field names are: " + str(field_names))
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA": # only show athletes with medals
        print("{}: {}; {}".format(vals[0],vals[4],vals[5]))
fid.close()
print ("----------------------------------------------------------")
#%%
fid = open("Files/SP500.txt")

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


#%% Writing a CSV
olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("Files/reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()    
        
#%%
olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("Files/reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
