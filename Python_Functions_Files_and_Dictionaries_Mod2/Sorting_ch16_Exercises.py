# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:43:23 2020

@author: Vasilis
"""

#%%ex1,2,3,4
L = [0, 1, 6, 7, 3, 6, 8, 4, 4, 6, 1, 6, 6, 5, 4, 4, 3, 35, 4, 11]


dic_count = {}
for iEl in L:
    if iEl not in dic_count.keys():
        dic_count[iEl] = 0
    dic_count[iEl] = dic_count[iEl] +1     

print(dic_count)
sort_keys = sorted(dic_count,key = lambda x:dic_count[x],reverse=True)
print(sort_keys)
final_list = sort_keys[:5]
print(final_list)
# different result duwtp second order sorting!

#%%ex5
def freq5(str1):
    lets ={}
    for i in str1:
        if i not in lets:
            lets[i] = 0
        lets[i] = lets[i] + 1
    sort_lets = sorted(lets, reverse = True, key = (lambda x:lets[x]))         
    return sort_lets[:5]

print(freq5("babababtrtrtrtrtrtklklklklkklklkllklllm"))
