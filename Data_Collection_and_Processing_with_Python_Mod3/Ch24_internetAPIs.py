# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:44:06 2020

@author: Vasilis

look at this guy: 
    https://en.wikipedia.org/wiki/John_Gilmore_(activist)
        https://en.wikipedia.org/wiki/Drug_policy_reform

MOdule requests can send a request to a web page using its API and ger a response 
as a text. Doc here:
    https://www.w3schools.com/python/module_requests.asp        

The produced objects are of type requests.Response and have a variety of orioerties
and methods that are summarized in the doc here"
    https://www.w3schools.com/python/ref_requests_response.asp
"""
import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=sex")
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("------")

#print("---the whole list, pretty printed---")
#print(json.dumps(x, indent=2)) # pretty print the results

#%% iseful attributes ofresponse object
tety = page.text
urly = page.url
statusy = page.status_code 
headers = page.headers
history = page.history

#%% the get attribute can automatically format the rewuest to the url so we 
# dont have to remember all the specific conventions
d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
#x1 = results.json() # turn page.text into a python object
#x1 = json.loads(results.text)
print(results.url)
print("------")

#%% another formatting exapmele using requests module

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page2 = requests.get("https://api.datamuse.com/words", params=kval_pairs)
x2 = page2.json() # turn page.text into a python object
x2b = json.loads(page2.text) # same exactly command as the previous line
print(page2.text[:150]) # print the first 150 characters
print(page2.url) # print the url that was fetched
print("------")

#%% Understanding how to use an API e.g. datamuse API
def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word
    params_diction["max"] = "5" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds], word_ds
    r#eturn word_ds # Return a python object (a list of dictionaries in this case)

print(get_rhymes("funny"))
res1,res2 = get_rhymes("funny")
print("------")

#%% testing and debuggin 1

def requestURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url

print(requestURL("http://www.myrandom.com", {'d':'paparia','koloi':'mounia'}))
print("------")

#%% testing and debuggin 2
baseurl = 'https://www.google.com/search'
d_req= {'tbm':'isch','q': '"violins and guitars"'}
print(requestURL(baseurl,d_req))
test_url = requests.get(baseurl,params = d_req)
print(test_url.url)
print(test_url.text[:100])
print("------")

#%% cching the fetched data to avoid recursive re callint of the expensive request.get() code
import requests_with_caching # tricky copy this is not a real module!!
"""
res.url
res.headers
"""
# it's not found in the permanent cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=puppy", permanent_cache_file="Files/datamuse_cache.txt")
print(res.text[:100])
print("------")
# this time it will be found in the temporary cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="Files/datamuse_cache.txt")
print("------")
# This one is in the permanent cache.
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=funny", permanent_cache_file="Files/datamuse_cache.txt")
print("------")




