# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:31:00 2020

@author: Vasilis
"""

##%% Ex1
#d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']
#m_list = []
#for i in d:
#    if type(i)==str:
#        if 'm'in i:
#           m_list = m_list +[i]
#    elif   type(i)==list:  
#        for el in i:
#            if 'm' in el:
#                m_list = m_list +[el]
#            elif   type(el)==list:
#                for el2 in el:
#                    if 'm' in el2:
#                        m_list = m_list +[el2]
#
##%% Ex 2
#pokemon = {'Trainer1':
#          {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
#          'Trainer2':
#          {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
#          'Trainer3':
#          {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
#          'Trainer4':
#          {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}}}
#r = 0
#p = 0
#d = 0
#    
#for ikey1 in pokemon:
#    dic1 = pokemon[ikey1]
#    for ikey2 in dic1:
#        dic2 = dic1[ikey2]
#        for ikey3 in dic2:
#            if ikey3 =='rattatas':
#                r = r + dic2[ikey3]
#            elif ikey3 =='ditto':
#                d = d + dic2[ikey3]
#            elif ikey3 =='pidgey':
#                p = p + dic2[ikey3]   
#        
##%% Ex 3
#big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]
#word_counts = {}
#
#for i1 in big_list:
#    if type(i1)==str:
#        if i1 not in word_counts:
#           word_counts[i1] = 0
#        word_counts[i1] = word_counts[i1] +1   
#    elif   type(i1)==list:  
#        for i2 in i1:
#            if type(i2)==str:
#                if i2 not in word_counts:
#                    word_counts[i2] = 0
#                word_counts[i2] = word_counts[i2] +1  
#            elif  type(i2)==list:   
#                for i3 in i2:
#                    if type(i3)==str:
#                        if i3 not in word_counts:
#                            word_counts[i3] = 0
#                    word_counts[i3] = word_counts[i3] +1      
#        
#%% Ex4   
pokemon_go_data = {'bentspoon':
                  {'Rattata': 203, 'Pidgey': 120, 'Drowzee': 89, 'Squirtle': 35, 'Pikachu': 3, 'Eevee': 34, 'Magikarp': 300, 'Paras': 38},
                  'Laurne':
                  {'Pidgey': 169, 'Rattata': 245, 'Squirtle': 9, 'Caterpie': 38, 'Weedle': 97, 'Pikachu': 6, 'Nidoran': 44, 'Clefairy': 15, 'Zubat': 79, 'Dratini': 4},
                  'picklejarlid':
                  {'Rattata': 32, 'Drowzee': 15, 'Nidoran': 4, 'Bulbasaur': 3, 'Pidgey': 56, 'Weedle': 21, 'Oddish': 18, 'Magmar': 6, 'Spearow': 14},
                  'professoroak':
                  {'Charmander': 11, 'Ponyta': 9, 'Rattata': 107, 'Belsprout': 29, 'Seel': 19, 'Pidgey': 93, 'Shellder': 43, 'Drowzee': 245, 'Tauros': 18, 'Lapras': 18}}
pok_vals = {}
for ikey1 in pokemon_go_data:
    idic2 = pokemon_go_data[ikey1]
    for ikey2 in idic2:
        if ikey2 not in pok_vals:
            pok_vals[ikey2] = 0
        pok_vals[ikey2] = pok_vals[ikey2] +1        

most_common_pokemon = sorted(pok_vals, key = (lambda x:(pok_vals[x],len(x)) ))[-1]
                      
        
        
        