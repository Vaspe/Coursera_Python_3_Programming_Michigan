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
# import io
# import PIL
from PIL import Image
from PIL import ImageDraw
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

def get_imdict(zip_name):
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
    size = 128, 128
    for i in fl_names:
        img_dict[i] = [Image.open(BytesIO(myzip.read(i)))]
        img_dict[i] = img_dict[i] + [np.asarray(img_dict[i][0])]
        #display(img_dict[i][0])    
        
        # get the text of each page
        img_dict[i] = img_dict[i] + [pytesseract.image_to_string(img_dict[i][0])]
        
        #find the faces,crop them,  and store them in a list
        cv_im = cv.cvtColor(img_dict[i][1],cv.COLOR_BGR2HSV)
        faces = face_cascade.detectMultiScale(cv_im,1.2,4)
        small_faces = []
        pil_img = img_dict[i][0]
        for x,y,w,h in faces:
            cur_im = pil_img.copy()
            #crop the face
            aa = cur_im.crop((x,y,x+w,y+h))
            # resize cropped to 128x128
            aa.thumbnail(size)
            # display(aa)
            #add to the list of faces
            small_faces = small_faces + [aa]
        img_dict[i] =img_dict[i] + [small_faces]
    myzip.close()
    

    return img_dict     

#%% logic:

img_dict = get_imdict(zip_name)
wrd = 'Christopher'

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if y+first_image.height == contact_sheet.height:
        x=x+first_image.width
        y=0
    else:
        y=y+first_image.height        


# for i in img_dict['a-0.png'][3]:
#     display(i)

for i in  img_dict:
    # check for word in the text
    if wrd in img_dict[i][2]:
        print('Results found in ' + i)
        if img_dict[i][3]:
            for ii in img_dict['a-0.png'][3]:
                display(ii)
        else:
            print('But there were no faces in that file')        
    else:
        print('No results found in ' + i)
        continue
    
    



