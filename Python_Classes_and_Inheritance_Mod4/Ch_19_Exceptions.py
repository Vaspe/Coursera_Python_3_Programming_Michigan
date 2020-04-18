# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:18:38 2020

@author: Vasilis

Good docs for errors and exceptions:
    https://docs.python.org/3/tutorial/errors.html

try:
   <try clause code block>
except <ErrorType>:
   <exception handler code block>
"""

#%% try except is the same as try catch in matlab:
# the except part can takeeither a specifi exception(error class)
# or we can define except Exception: which handel all tyoes of errors 

try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception:
    print("got an error")

print("continuing")

try:
    x = 5
    y = x/0
    print("This won't print, either")
except ZeroDivisionError:
    print("error 2")

print("continuing again")
print("-----------------------------")

# we can also print the error:
    
try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception as e:
    print("got an error")
    print(e)

print("continuing")    
print("-----------------------------")
try:
    for i in range(5):
        print(1.0 / (3-i))
except Exception as error_inst:
    print("Got an error", error_inst)
print("-----------------------------")

#%%

students = [('Timmy', 95, 'Will pass'), ('Martha', 70), ('Betty', 82, 'Will pass'), ('Stewart', 50, 'Will not pass'), ('Ashley', 68), ('Natalie', 99, 'Will pass'), ('Archie', 71), ('Carl', 45, 'Will not pass')]

passing = {'Will pass': 0, 'Will not pass': 0}
for tup in students:
    try:
        if tup[2] == 'Will pass':
            passing['Will pass'] += 1
        elif tup[2] == 'Will not pass':
            passing['Will not pass'] += 1
    except Exception:
        pass
    
#%%
nums = [5, 9, '4', 3, 2, 1, 6, 5, '7', 4, 3, 2, 6, 7, 8, '0', 3, 4, 0, 6, 5, '3', 5, 6, 7, 8, '3', '1', 5, 6, 7, 9, 3, 2, 5, 6, '9', 2, 3, 4, 5, 1]

plus_four = []

for num in nums:
    try:
        plus_four.append(num+4)
    except Exception:
        plus_four.append('Error')

#%% Ch 19.5 Ex 1
blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in blog_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        post['Likes'] = 0
        

#%% Ch 19.5 Ex 2
food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except KeyError:
        print("I got a key error")
        pass    
    except IndexError:
        print("I got an index error")
        pass

# We can hace multiple excepts one after the other too!