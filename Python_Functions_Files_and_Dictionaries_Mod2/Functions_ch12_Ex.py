# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:27:57 2020

@author: Vasilis
"""
import random
#%% Ex1
def num_test(in_num):
    if in_num>10:
        out_mess = "Greater than 10."
    elif in_num ==10:
        out_mess = "Equal to 10."
    else:
        out_mess = "Less than 10."
    return    out_mess 
        
print(num_test(10))    

#%% Ex2 Write a function that will return the number of digits in an integer.
def numDigits(n):
      return len(str(n))
  
#%%
def reverse(astring):
    out_str = astring[::-1]
    return out_str

reverse('ass')      

#%% Ex4
def mirror(mystr):
    # your code here
    revstr= mystr[::-1]
    out_str= mystr+revstr
    return out_str

#%% Ex 5
def remove_letter(theLetter, theString):
    # your code here
    outstr = ""
    for i in theString:
        if i !=theLetter:
            outstr = outstr +i
    return outstr  
print(remove_letter("n","banana")            )

#%% Ex 6 !!!!!
def county(alist,y):
    cnt = 0
    for i in alist:
        if i == y:
            cnt = cnt +1
    return cnt    

def iny (alist,y):
    a = 0
    for i in alist:
        if i==y:
            a = a +1
    if a>0:
        out = True
    else:
        out = False
    return out    

def reversey (alist):
    out = alist[::-1]
    return out

def indexy (alist,y):
    pos1 = 0
    for i in alist:        
        if i == y:
            return pos1
        pos1 = pos1 +1
            
def inserty (alist,y,pos):
    outlst = []
    cnt = 0
    for i in alist:
        if cnt == pos:
            outlst = outlst +[y]
        else:
            outlst = outlst +[i]
        cnt =cnt +1        
    return outlst        
        
lst = [0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
print(county(lst,0))
print(iny(lst,4))
print(reversey(lst))
print(indexy(lst,2))
print(inserty( lst,'cat', 5))        
     
        
print("--------------------------------------")
#%% Ex7 Write a function replace(s, old, new) that replaces all occurences of old
# with new in a string s: HARD!!!
s= 'Mississippi'
old = "si"
new = "SI"
if old in s: 
    sz = len(old)
    letters = 5
else:
    out_str = s    

#%%Ex8
ran_list = []
for i in range(0,100):
    ran_list = ran_list + [random.randrange(0,1000)]
def mymax(list_in):
    ymax = list_in[0]
    for i in list_in:
        if i>ymax:
            ymax = i
    return ymax

print('The max of the list is ' + str(mymax(ran_list)))            
    
#%% Ex9
def sum_of_squares(xs):
    sqr_sum =0
    for i in xs:
        sqr_sum=sqr_sum+i*i
    return sqr_sum

#%% Ex 10
def countOdd(lst):
    odd_cnt = 0
    for i in lst:
        if i%2==1:
            odd_cnt=odd_cnt+1
    return odd_cnt
    
#%% Ex11
def sumEven(lst):
    even_sum = 0
    for i in lst:
        if i%2==0:
            even_sum=even_sum+i
    return even_sum
   
sumEven([0,2,4,5])   
    
#%% Ex 12
def sumNegatives(lst):
    neg_sum = 0
    for i in lst:
        if i <0:
            neg_sum = neg_sum + i
    return neg_sum    

#%% Ex 13
def findHypot(a,b):
    hypt = (a**2+b**2)**0.5
    return hypt    
    
#%%Ex 14
def is_even(n):
    if n%2==0:
        out_str = True
    else:
        out_str = False
    return out_str

#%% Ex 15
def is_rightangled(a, b, c):
    x = a**2 + b**2
    y = c**2
    if abs(x-y)< 0.001:
        out = True
    else:
        out = False
    return out     