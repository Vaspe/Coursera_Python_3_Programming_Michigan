# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:38:41 2020

@author: Vasilis

Exercisise1 and 18-20 need revision they give an error and I dont understand
 how they work!!!!!!

"""

#%% Ex1

things = [3, 5, -4, 7]

#accum = []
#for thing in things:
#    accum.append(thing+1)
#print(accum)

test = list(map (lambda x: x+1,things ))
print(test)


#%% Ex2 manual

def lengths(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
    of strings in the input list. Use manual accumulation!"""
    # fill in this function's definition to make the test pass.
    out = []
    for i in strings:
        out = out + [len(i)]
    return(out)    
    
print (lengths(['abv', 'safgdfg', 'cvbbdfdfd']))

#%% Ex3  maps
def lengths2(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
    of strings in the input list. Use manual accumulation!"""
    # fill in this function's definition to make the test pass.
    out = list(map(lambda x: len(x), strings))
    return out

print (lengths2(['abv', 'safgdfg', 'cvbbdfdfd']))

#%% Ex 4  list comperhension
def lengths3(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
    of strings in the input list. Use manual accumulation!"""
    # fill in this function's definition to make the test pass.
    out = list(len(x) for x in strings  )
    return out

print (lengths3(['abv', 'safgdfg', 'cvbbdfdfd']))
print('-------------------------------------------')

#%% Ex5 manual
def positives_Acc(alist):
    out = []
    for i in alist:
       if i >=0:
           out = out + [i]
    return out                    
print(positives_Acc([3, 5, -4, 7]))


#%% Ex6 using filter
def positives_Fil(alist):
    out = list( filter(lambda x:x>=0, alist) )
    return out                    
print(positives_Fil([3, 5, -4, 7]))

#%% Ex7 using list comperhension
# [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]
def positives_Li_Com(alist):
    out = [x for x in alist if x>=0]
    return out     
print(positives_Li_Com([3, 5, -4, 7]))
print('-------------------------------------------')
#%% Ex 8 manual accumulation
def longwords(strings):
    """Return a shorter list of strings containing only the strings with more than
      four characters. Use manual accumulation."""
    out = []
    for i in strings:
        if len(i)>4:
            out = out + [i]
    return out        

print(longwords(["gap","banky","tt","gopro"]))
#%% Ex 9 using filter
def longwords_Fil(strings):
    """Return a shorter list of strings containing only the strings with more
    than four characters. Use the filter function."""
    out = list(filter((lambda x: len(x)>4),strings))
    return out

print(longwords_Fil(["gap","banky","tt","gopro"]))

#%% Ex 10 using list comperhension
def longwords_Li_Comp(strings):
    """Return a shorter list of strings containing only the strings with more than 
    four characters. Use a list comprehension."""
    out =[x for x in strings if len(x) > 4]
    return out

print(longwords_Li_Comp(["gap","banky","tt","gopro"]))

#%% Ex 11 using list cmprerhension
def longlengths(strings):
    out = [len(x) for x in strings if len(x)>=4]
    return out

print(longlengths(["gap","banky","tt","gopro",'Vasileios']))

#%% Ex 12 using map and filters
def longlengths2(strings):
    out = list(map(lambda x: len(x), list(filter(lambda x:len(x)>=4,strings))))
    return out

print(longlengths2(["gap","banky","tt","gopro",'Vasileios']))

#%% Ex 13 using accumulateor manually
def sumSquares(L):
    out = 0
    for i in L:
        out = out + i*i
    return out    
    
print (sumSquares([3, 2, 2, -1, 1]))

#%% Ex 14 using map and sum
def sumSquares2(L):
    out = sum(list( map(lambda x:x*x,L)  ))   
    return out
    
print (sumSquares2([3, 2, 2, -1, 1]))

#%% Ex 15 zip to get list of tuples
L1 = [1, 2, 3, 4]
L2 = [4, 3, 2, 3]
L3 = [0, 5, 0, 5]

tups = list(zip(L1,L2,L3))

print(tups)

#%% Ex 16 With zip and map ot list comperhension 
# [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]
maxs = [max(x) for x in zip(L1,L2,L3)]

print(maxs)

#%% Ex 17 
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
compri_sample = [inam['name']  for inam in tester['info'] if inam['class standing'] == 'Junior' ]

print(compri_sample)
print('-------------------------')

#%% Ex 18 the same with list comperhension PROBLEM ERROR!!!!!!
def onelist(lst):
    result = []
    for each_list in lst:
        for item in each_list:
            result.append(item)
    return result

L = [["hi", "bye"], ["hello", "goodbye"], ["hola", "adios", "bonjour", "au revoir"]]

result2 = [[x for x in L1] for L1 in L ]
result3 = [y for x in L for y in x ]
print(onelist(L))
print(result2)
print(result3)
print('-------------------------')

#%% Ex 19

#PROBLEM LOOK IT UP
tester = {'info': [
         {"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science", 'important classes': ['SI 106', 'ENGLISH 125', 'SI 110', 'AMCULT 202']},
         {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science', "important classes": ['SI 106', 'SI 410', 'PSYCH 111']},
         {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology', 'important classes': ['WOMENSTD 220', 'SOC 101', 'ENS 384']},
         {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science', "important classes": ['SOC 101', 'AMCULT 334', 'EECS 281']},
         {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History', 'important classes': ['ENGLISH 125', 'HIST 259', 'ENGLISH 130']},
         {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior', 'important classes': ['PIANO 101', 'STUDIO 300', 'THEORY 229', 'MUSC 356']}]}

class_sched  = [iDic['important classes']  for iDic in tester['info'] ]
class_sched  = [x for iDic in tester['info'] for x in iDic if x=='names' ]
print(class_sched)
print('-------------------------')
#%% Ex 20
# look at example :
# https://spapas.github.io/2016/04/27/python-nested-list-comprehensions/
# Read the explanation

nums = [[4, 3, 12, 10], [8, 7, 6], [5, 18, 15, 7, 11], [9, 4], [24, 20, 17], [3, 5]]

threes  = [y for x in nums for y in x if y%3 ==0 ]
print(threes)
print('-------------------------')
#if x%3 ==0

