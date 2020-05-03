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
import io
import PIL
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
from io import BytesIO
# import time 

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#%%

#Define the zip file name with the pngs
zip_name = "D:/Github/small_img.zip"
# zip_name = "D:/Github/images.zip"
# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# Creating zipfile object 
myzip = zipfile.ZipFile(zip_name, 'r')

#take the info from thefile
info_list = myzip.infolist() # not useful...
# print(info_list)

#Taking all the file names in the zip 
fl_names = myzip.namelist()

#Creating a dictionary wtih keys the image names and values a li st with first element the image object itself
img_dict = {}
images_arr = []
for i in fl_names:
    img_dict[i] = [Image.open(BytesIO(myzip.read(i)))]
    img_dict[i] = img_dict[i] + [np.asarray(img_dict[i][0])]
    # display(img_dict[i][0])
    # images_arr = images_arr + [np.asarray.img_dict[i][0]]
    # img_dict[i] = [np.asarray(Image.open(myzip.read(i)))]
    #display(Image.open(BytesIO(myzip.read(i))))
    # images_arr  = np.asarray(Image.open(BytesIO(myzip.read(i)))) 
myzip.close()
 
# display(Image.fromarray(img_dict[i],"L"))
#display(Image.open(BytesIO(myzip.read(fl_names[0]))))

#%% Get the text of each page and add it to the dictionary 
for i in img_dict:
    img_dict[i] = img_dict[i] + [pytesseract.image_to_string(img_dict[i][0])]

#Image.open()

#%% Get the pictures/faces of each page and add them to the dictionary

cc = cv.cvtColor(img_dict[i][1],cv.COLOR_BGR2HSV)

# data1 = np.asarray(img_dict[i][0])
# data = img_dict[i][0]
# img = cv.imdecode(np.frombuffer(data, np.uint8), 1)    

# bytes_io = io.BytesIO(img_dict[i][1])

# pil_img = Image.open(img_dict[i][0])
# rgb = img.convert('rgb')
# # now lets convert it to greyscale for opencv, and get the bytestream
# open_cv_version = pil_img.convert("L")



# # now read this file with opencv and get faces
# cv_img = cv.imread(pil_img)

# img = cv.imread(img_dict[i][0])
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # using the face cascade we loaded to detect a face in the greayed pic. the output is a box in the form x,y,x,y of UL,LR corners in an ndarray
# faces = face_cascade.detectMultiScale(gray)


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


