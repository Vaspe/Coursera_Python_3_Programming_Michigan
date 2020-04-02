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
print("----------------------------------------------")        
#%%Write code that asks the user to enter a numeric score (0-100). In response,
#it should print out the score and corresponding letter grade, according to the table below.

usr_in = 20 #input("Define a score")

if float(usr_in) >= 90:
    print ('Score is: ' + str(usr_in) + " Grade is: A")     
elif float(usr_in) >= 80:
    print ('Score is: ' + str(usr_in) + " Grade is: B")        
elif float(usr_in) >= 70:
    print ('Score is: ' + str(usr_in) + " Grade is: C")        
elif float(usr_in) >= 60:
    print ('Score is: ' + str(usr_in) + " Grade is: D")            
elif float(usr_in) < 60:
    print ('Score is: ' + str(usr_in) + " Grade is: F")
print("----------------------------------------------")

#%%A year is a leap year if it is divisible by 4. If the year can be evenly divided by 100, 
#it is NOT a leap year, unless the year is also evenly divisible by 400. Then it is a
#leap year. Write code that asks the user to input a year and output True if it’s a leap year,
#or False otherwise
    
year_in = 2000 #input("Give a year")
year = int(year_in)

if (year%4 ==0 and not(year%100==0)  ):
    print('True')
elif ( (year%100==0) and year%400==0):
    print('True')
else:
    print("False")

print("----------------------------------------------")    


#%%
num_lst = [3, 20, -1, 9, 10]
is_even = []
for i in num_lst:
    if i%2==0:
        is_even=is_even+["True"]
    else:
        is_even=is_even+["False"]

#%%
#Implement the calculator for the date of Easter.The following algorithm computes the date
#for Easter Sunday for any year between 1900 to 2099.The algorithm can give a date in 
#April. You will know that the date is in April if the calculation gives you an answer
#greater than 31. (You’ll need to adjust) Also, if the year is one of four special years
#(1954, 1981, 2049, or 2076) then subtract 7 from the date.Your program should print
#an error message if the user provides a date that is out of range.

year_in = 2020 #input("Give a year")

year = int(year_in)
april_flag = False

# check acceptable date range limits
if year<1900 or year>2099:
    print('Error. Please choose a year between 1900 and 2099 inclusive')
else:
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dateofeaster = 22 + d + e
    if dateofeaster >31: # check if it is april and remove 31 (days of March!)
        dateofeaster = dateofeaster-31
        april_flag = True
    if year in [1954, 1981, 2049, 2076]: # for 'special year remove 7'
        dateofeaster = dateofeaster -7
    if  april_flag:       
        print ("Date of easter for the year " + str(year_in) + ' is April ' + str(dateofeaster) )        
    else    :
        print ("Date of easter for the year " + str(year_in) + ' is March ' + str(dateofeaster) )  

print("----------------------------------------------")  
#%% Palindrome check
in_str = "racecar" #input("Give a string as input"

rev_str = in_str[::-1]

if rev_str==in_str:
    print(True)
else:
    print(False)
    









