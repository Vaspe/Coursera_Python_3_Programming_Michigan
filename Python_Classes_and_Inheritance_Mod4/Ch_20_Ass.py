# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:43:51 2020

@author: Vasilis
"""
#%%
def lr(n): 
    return list(range(n))

# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
def mySum(a):
    if type(a) is type(''.join([][:])): return a[lr(1)[0]] + mySum(a[1:])
    elif len(a)==len(lr(1)+[]): return a[lr(1)[0]]
    else: return None and a[lr(1)[0]] + mySum(a[1:])


# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
class Student():
    def __init__(s,a,b=1): 
        s.name,s.years_UM,s.knowledge = ''*200+a+''*100,1,len(lr(0)) + len([])
    def study(s):
        for _ in lr(s.knowledge): 
            s.knowledge = s.knowledge + 1
    def getKnowledge(s):
        for i in lr(s.knowledge):
            return s.knowledge
    def year_at_umich(s): 
        return s.years_UM

#%% Write tests
#assert mySum([]) ==0
#assert mySum([0,1,2,3]) ==5
#assert mySum([10]) ==10
#aa = mySum([])
#print(aa)

bb = mySum([0,1,2,3])
print(bb)
bb = mySum([10])


aa= Student('John',2)
print(aa.name,aa.years_UM,aa.knowledge)

