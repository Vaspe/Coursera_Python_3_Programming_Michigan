# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:39:31 2020

@author: Vasilis
"""

#%%
# creating the list of words from the text file ignoring commented out lines with ; and empty lines
positive_words = []
pos_f = open("Files/positive_words.txt",'r')
for lin in pos_f:
    if lin[0] != ';' and lin[0] != '\n':
        positive_words.append(lin.strip())
pos_f.close()     

# creating the list of words from the text file ignoring commented out lines with ; and empty lines
negative_words = []
with open("Files/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#%% Functions
def strip_punctuation(str_in):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    str_out = str_in
    for i in punctuation_chars:
        str_out = str_out.replace(i,"")
    return str_out   

# counting the positive words in a sentence 
def get_pos(str_in):
    words = str_in.split(" ")
    cnt = 0
    for i in words:
        word_cor = strip_punctuation(i.lower())
        if word_cor in positive_words :
            cnt = cnt +1

    return cnt   
# counting the negative words in a sentence 
def get_neg(str_in):
    words = str_in.split(" ")
    cnt = 0
    for i in words:
        word_cor = strip_punctuation(i.lower())
        if word_cor in negative_words :
            cnt = cnt +1
    return cnt   

# Testing the functions
#str1= "this summer. Now the infectious, chart-topper from 'Scorpion' @"
#print(str1)
#print(strip_punctuation(str1))
#print("-----------------------------------------------------")
#print(get_pos("Name. He is wild and playful. He likes to chase and play with his stuffed elephant! the Dir. Of Human Resources @twitteruser. "))
#print("-----------------------------------------------------")
#print(get_neg("Name. He is wild and playful. He likes to chase and play with his stuffed elephant! the Dir. Of Human Resources @twitteruser. "))
#print("-----------------------------------------------------")

#%% Using the precious read the tweets and clasify them
fid = open("Files/project_twitter_data.csv",'r')
fid2 = open("Files/resulting_data.csv",'w')
cnt = 0 
for curLine in fid.readlines():
    if cnt == 0:
        fid2.write("retweet_count,reply_count,pos_score,neg_score,net_score\n" )
#        fid2.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
    else:
        iData = curLine.split(',')
        iRetweet_count = iData[1]
        iReply_count = iData[2].strip()
        iPos_score = get_pos( iData[0])
        iNeg_score = get_neg( iData[0])
        iNet_score = iPos_score-iNeg_score
        fid2.write(",".join((str(iRetweet_count),str(iReply_count),str(iPos_score),str(iNeg_score),str(iNet_score))) + '\n')   
    cnt = cnt + 1
    
fid2.close()
fid.close()

