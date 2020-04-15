# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:45:43 2020

@author: Vasilis
"""
import requests
import json

#%% Ass1
def get_movies_from_tastedive(mvie_str):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {}
#    params_diction["api_key"] = 'a9e655842a66983c8f0bbb23ceae3bf2' # from the above global variable
    params_diction["q"] = mvie_str 
    params_diction["type"] = "movies"
    params_diction["limit"] = '5'
    #tastedive_resp = requests_with_caching.get(baseurl, params = params_diction, permanent_cache_file="Files/flickr_cache.txt")
    tastedive_resp = requests.get(baseurl, params = params_diction)
    taste_dive_dat = tastedive_resp.json()
    out_lst = [dic1['Name'] for dic1 in taste_dive_dat['Similar']['Results']   ]
    out_dic = {}
    out_dic['Similar'] = out_lst
#    for i in out_lst:
#        out_dic['Similar'] = out_dic['Similar'] + [i]
    # Useful for debugging: print the url! Uncomment the below line to do so.
    print(tastedive_resp.url) # Paste the result into the browser to check it out...
    return out_dic,taste_dive_dat

def extract_movie_titles(dic_in):
    return dic_in['Similar']

def get_related_titles(str_lst):
    outlst = []
    for iStr in str_lst:
        (output_dic,data) = get_movies_from_tastedive(iStr)
        cur_lst = extract_movie_titles(output_dic)
        for iTit in cur_lst:
            if iTit not in outlst:
                outlst = outlst + [iTit]
    return  outlst           

def get_movie_data (mov_str):
    baseurl = "http://www.omdbapi.com/"
    params_diction = {}
    params_diction["apikey"] = '7f2db103' # from registration
    params_diction["t"] = mov_str 
    params_diction["r"] = "json"
    #omdb_resp = requests_with_caching.get(baseurl, params = params_diction)
    omdb_resp = requests.get(baseurl, params = params_diction)
   # print(omdb_resp.url)
    omdb_dat = omdb_resp.json()
    return omdb_dat

def get_movie_rating(dic_in):
    all_rat = dic_in['Ratings']
    rot_rat = 0 
    for iDic in all_rat:
        if iDic['Source'] == 'Rotten Tomatoes':
            rot_rat = int(iDic['Value'][0:2])
    return rot_rat    

def get_sorted_recommendations(str_lst):
    out_lst1 = get_related_titles(str_lst)
    out_lst2 = sorted(out_lst1,key = lambda x:(get_movie_rating(get_movie_data(x)),x[0]), reverse = True )
    return out_lst2
        
        
        
#%% Testing baby
#(output_test,data) = get_movies_from_tastedive("Black Panther")
#out_test2 = extract_movie_titles(output_test)
#out_test3 = get_related_titles(["Black Panther", "Captain Marvel"])
#out_test4 = get_movie_data("Venom")
#out_test_5 = get_movie_rating(get_movie_data("Deadpool 2"))
out_test6 = get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
