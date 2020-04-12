# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:39:35 2020

@author: Vasilis

Good doc:
    https://www.programiz.com/python-programming/list-comprehension

Syntax:
    [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]
 
    where the if clause is optional
"""

#%%
things = [2, 5, 9]

yourlist = [value * 2 for value in things]

print(yourlist)

"""
 The transformer expression is value * 2. The item variable is value and the sequence
 is things. This is an alternative way to perform a mapping operation. As with map, 
 each item in the sequence is transformed into an item in the new list.
"""

#%%
def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

"""
The if clause of a list comprehension can be used to do a filter operation. To perform 
a pure filter operation, the expression can be simply the variable that is bound to 
each item. 
"""

#%%
L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

lst2 = [num for num in L if num>10]

#%%

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
compri = []
for iDic in tester['info']:
    compri = compri + [iDic[item] for item in iDic if item == 'name']