# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:39:29 2020

@author: Vasilis

The assignment grading is very simple, if you create something that looks like the
two sample outputs (searching for "Chris" in the small images and "Mark" in the
large images) you get full points! If you fail to handle the case where some pages
have the text but no faces (with the Mark search) you can still pass the assignment,
but I know you can do better!
 
Wworkaround to post the final project's source code for grading, while Coursera 
is fixing that weird textbox which messes up formatting and makes it unreadable 
and unrunnable.

If you first double each end-of-line (i.e. make CRLF (\r\n) to be CRLFCRLF (\r\n\r\n)) 
and then paste the result to that text box and save - the formatting is retained.
Looks a bit weird (longer than it should be), but the code is readable and can
be copy-pasted to .py file or Jupiter for running. 

Course material here:
    https://drive.google.com/file/d/1gzySVKYpc6UtxXNhzcW6i11wtRoq_iNq/view
"""

import zipfile

import PIL
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
from io import BytesIO
# import time 

#%%

# zip_name = "D:/Github/small_img.zip"
zip_name = "D:/Github/images.zip"

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')


# RCreating zipfile object 
myzip = zipfile.ZipFile(zip_name, 'r')
#info_list = myzip.infolist()
#Taking all the file names in the zip 
fl_names = myzip.namelist()

#Creating a dictionary wtih keys the image names and values a li st with first element the image object itself
img_dict = {}
for i in fl_names:
    img_dict[i] = [Image.open(BytesIO(myzip.read(i)))]

#%% Get the text of each page and add it to the dictionary    


#%% Get the pictures/faces of each page and add them to the dictionary


#%% Chack in which images the text appears


#%% make a collage with the text and all the faces in a  contact shit

# PIL.Image.thumbnail 


#%% Rest stuff not used

# t = time.time()
# elapsed = time.time() - t
# print(elapsed)
    
# for i in info_list:
#     print (i.orig_filename)
#     im_file = myzip.read(i.orig_filename)
#     cur_img = Image.open(BytesIO(im_file) )
    # display(cur_img)
    # Image.open(im_file)

# cc = myzip.getinfo('a-0.png')
# data1 = myzip.read('a-0.png')
# aa = zipfile.ZipInfo(filename=zip_name)


