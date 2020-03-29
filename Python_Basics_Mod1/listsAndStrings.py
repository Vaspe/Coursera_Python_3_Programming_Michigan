# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:20:46 2020

@author: Vasilis
"""

#%% Definitions

"""
string: A single variable which is a concatenation of single strings (nubers,letters,
        symbols, etc,,,). Empty string is also a single character. They are marked with quotes
        Example: 'I am a string'. "I'm also a string", '''She said, "I 'm also a string" and left''' 
        Strings are immutable, cannot be changed after creation
list:  A list of any data type (string,int,float,list, etc...). All can be mixed 
       in there although is not recommended as best practice they are marked with
       [] and the (possibly mixed) variables are comma separated
       Example: ["hello", 2.0, 5, [10, 20]] 
       Lists are mutable, CAN be changed after creation
tuples: It is the same idea with the list and can contain any type of comma separated
        elements. They are marked with (). Tuples can contain lists   
        Example ("hello", 2.0, 5, [10, 20]) 
        Tuples are immutable, CANNOT be changed after creation. Although internal elements 
        like list mainteain their mutable nature
"""

#%% String definition examples

aa = 'I am a string'
print(aa)
bb = "I'm also a string"
print(bb)
cc = '''She said, "I 'm also a string" and left''' 
print(cc)
dd = ''' 
I am a multiple 
line string
defined with 3'
'''
print(dd)
ee = """
I am a second multiple
line string
defined with triple "
"""
print(ee)
ff =" "
print (ff)
gg=""
print(gg)


#%% List definition examples
hh = ["Hello", " ", "I", 'am', 'a random list', "of strings only"]
print (hh)
ii = ["hello", 2.0, 5, [10, 20], "I am a random list which includes another random list"] 
print(ii)
ii1 = [5]
print(ii1)
#%% Tuples definition examples
jj = ("hello", 2.0, 5, [10, 20], "I am a random tuple which includes a random list")
print(jj)
kk=(5,)
print(kk)

#%% INDEXING OPERATOR IN PYTHON IS []     (same to () in matlab...)
# Indexing starts at 0!!!! 
# Last value is not inclusive when defining a range!!!!
print("-----------------------------")

sString = 'Pyhton'
lList = ['one',2,'three']
tTuple = ("hello", 2.0, 5, [10, 20], "I am a random tuple which includes a random list")

for i in range (len(sString)):
    print('The character i = '+str(i) +' in the string is ' +(sString[i]))
    
for i in range (len(tTuple)):
    print ('The item i = '+str(i) +' in the tuple is ' + str(tTuple[i]) )
    
for i in range (len(lList)):
    print ('The item i = '+str(i) +' in the list is ' + str(lList[i]))
print("-----------------------------")

L = [0.34, '6', 'SI106', 'Python', -2]
print ('L is the list:'+ str(L))
print('the length of L[1:-1] is '+str(len(L[1:-1])) + ' beacuse the first element is ncluded but the last one is excluded. Python FTW!')
print('Return of L[:4] is '+str((L[:4])) + ' .This the slice operator property where blank in the beginning means 0')
print('Return of L[-3:] is '+str((L[-3:])) + ' .This the slice operator property where blank at the end means start from last value (-1)')
print('The symbol : means take all. Return of L(:) is ' + str(L[:]))
L[3]='Takis'
print("Changing an elment works with L[3]='Takis' is " + str(L[:]))

print("-----------------------------")

T = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print ('T is the tuple:'+ str(T))
print ('T[2:4] is: '+ str(T[2:4]))
T=T[:4] + ('Takis',) + T[5:]
print("As we cannot mutate a tuple we have to reassign the whole thing in order to change the values. E.g. T=T[:4] + ('Takis',) + T[5:] gives:" +str(T))

print("-----------------------------")

#%% concatenation and repetition

print ("Using + we can concatenate lists. With * we can repaeat items. Combining bith also works")

fruit = ["apple","orange","banana","cherry"]
print('the list fruit contains: ' + str(fruit))
a = fruit +[1,32,666,69]
print([1,2] + [3,4])
print('Concataning two list like a = a = fruit +[1,32,666,69] gives a new list a: ' + str(a))
b =a[1:5]*2
print('Repeating selected values of a list like eg b =[a[1:5]*2] gives: ' +str(b) )
print("-----------------------------")


#%% Count and index
# Look here for an overview of list methods: https://www.w3schools.com/python/python_ref_list.asp
print('Count is a method of strings and lists that counts the occurence of a character or set of characters appear in a string/list')
SS = "This is my test string that I have created. Ha ha ha!"
SSha = SS.count("ha") 
print('my string is: '+ SS + ' the count of ha is SS.count("ha"): ' + str(SSha) ) 
print('If the character/string we are looking does not exist count returns 0')
print("-----------------------------")
SSindha = SS.index('ha')
print('Index is a method of strings and lists that find the first index where a character or set of characters appear in a string/list')
print('my string is: '+ SS + ' the count of ha is SSindha = SS.index("ha"): ' + str(SSindha) ) 
print('If the character/string we are looking does not exist python gives an error instead of empty output...')
print("-----------------------------")
L2 = [0.34, '6', 'SI106', 'Python', -2,6]
L2_6 = L2.count(6)
print('my list is: '+ str(L2) + ' the count of 6 is L2.count(6): ' + str(L2_6) ) 
print('If the character/string we are looking does not exist count returns 0')
print("-----------------------------")
L2_ind6 = L2.index(6)
print('my list is: '+ str(L2) + ' the first index of 6 is L2.index(6): ' + str(L2_ind6) ) 
print('If the character/string we are looking does not exist index throws errror!')
print("-----------------------------")

# 
        

