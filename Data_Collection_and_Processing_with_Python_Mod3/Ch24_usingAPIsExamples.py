# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:16:51 2020

@author: Vasilis
"""

import requests
import requests_with_caching
import json
import webbrowser


#%% itunes api

base_itune = 'https://itunes.apple.com/search'

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests_with_caching.get(base_itune, params = parameters,permanent_cache_file="Files/itunes_cache.txt")
iTunes_response2 = requests.get(base_itune, params = parameters)
print(iTunes_response2.text)
print('-----------------')
py_data = json.loads(iTunes_response2.text)
print(iTunes_response2.url)
print('-----------------')
for r in py_data['results']:
    print(r['trackName'])
print('-----------------')
def fet_itunes_data(s_term, entity ="podcast" ):
    base_itune = 'https://itunes.apple.com/search'
    term = s_term
    params_dic_itune = {}
    params_dic_itune['terms'] =  term
    params_dic_itune['terms'] =  entity
    iTunes_res = requests.get(base_itune, params = parameters)
    print (iTunes_res.url)
    return iTunes_res.json()
        
test_itune_Ann = fet_itunes_data("Ann Arbor",'podcast')
print('-----------------')

#%% flickr api

# apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
# paste the key (not the secret) as the value of the variable flickr_key
flickr_key = 'a9e655842a66983c8f0bbb23ceae3bf2'

def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = 'a9e655842a66983c8f0bbb23ceae3bf2' # from the above global variable
    params_diction["tags"] = tags_string # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
#    flickr_resp = requests_with_caching.get(baseurl, params = params_diction, permanent_cache_file="Files/flickr_cache.txt")
    flickr_resp = requests.get(baseurl, params = params_diction)

    # Useful for debugging: print the url! Uncomment the below line to do so.
    print(flickr_resp.url) # Paste the result into the browser to check it out...
    return flickr_resp.json()

result_river_mts = get_flickr_data("river,mountains")
print('-----------------')

# post processing
# Some code to open up a few photos that are tagged with the mountains and river tags...

photos = result_river_mts['photos']['photo']
for photo in photos:
    owner = photo['owner']
    photo_id = photo['id']
    url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id)
    print(url)
#    webbrowser.open(url)

print('-----------------')

#%% Non-english characters
print('χψζωνβψωισγφω')
print('-----------------')

'''
When we fetch a webpage that is in json format, the webpage will have a header 
called ‘content-type’ that will say something like application/json; charset=utf8. 
If it specifies the utf8 character set in that way, the requests module will 
automatically decode the contents into unicode: requests.get('that web page').text 
will yield a string, with each of those sequences of one to four bytes coverted 
into a single character.

If, for some reason, you get json-formatted text that is utf-encoded but the requests
module hasn’t magically decoded it for you, the json.loads() function call can 
take care of the decoding for you. loads() takes an optional parameter, encoding. 
E.g.: encoding='utf-8' is the defautl kwarg 

When we want to wtite to a file or to command windowthere can be a problem as the
default is ascii. One solution is to use the Python method to encode the string,
using a format such as utf-8. For example, s.encode('utf-8') will encode string
s as utf-8. That will encode non-ASCII characters with multiple character sequences 
that are difficult for people to read but can decoded back into single Unicode characters.

Another quick-and-dirty option, if you just have a few stray characters that are
getting in your way, is to replace any non-ASCII characters with question marks.
For example, s.encode('ascii', 'replace').
'''