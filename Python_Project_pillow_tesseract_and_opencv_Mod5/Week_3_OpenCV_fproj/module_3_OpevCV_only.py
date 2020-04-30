# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:18:10 2020

@author: Vasilis

https://docs.opencv.org/
"""

import cv2 as cv
from PIL import Image
from PIL import ImageDraw


#%%

#load xml based classifiers for faces and eyes
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('readonly/haarcascade_eye.xml')

#reding the usual picture and making it grayscale
img = cv.imread('readonly/floyd.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# using the face cascade we loaded to detect a face in the greayed pic. the output is a box in the form x,y,x,y of UL,LR corners in an ndarray
faces = face_cascade.detectMultiScale(gray)
# theoutput is an ndarray 
print(faces)

# we can convert the ndarray to list using tolist
aa = faces.tolist()[0]
print(faces.tolist()[0])


# create a PIL image object
pil_img = Image.fromarray(gray,mode="L")
drawing = ImageDraw.Draw(pil_img)
#a list with the rextangel to be given as input to the drawing function
rec = faces.tolist()[0]
# draw a rectangle around the bounds
drawing.rectangle(rec, outline="white")
display(pil_img)
# the result is wrong because we get the wrong values for the rencangltr
# looking at the docs of opencv the ouput is : (x,y,w,h)

#So we have to modify from (x,y,w,h) to (x1,y1,x2,y2):

# first reload the draw cancas picture
pil_img = Image.fromarray(gray,mode="L")
drawing = ImageDraw.Draw(pil_img)
# now draw the rectangele by adding width and height to the values
drawing.rectangle((rec[0],rec[1],rec[0]+rec[2],rec[1]+rec[3]), outline="white")
display(pil_img)


#%% More complicated example using the recruitment image

# Firstly opencv does not read gifs. So we need to convert to a BW png 
pil_img = Image.open('readonly/msi_recruitment.gif')
# now lets convert it to greyscale for opencv, and get the bytestream
open_cv_version = pil_img.convert("L")
# now lets just write that to a file
open_cv_version.save("msi_recruitment.png")

# now read this file with opencv and get faces
cv_img = cv.imread('msi_recruitment.png')
faces = face_cascade.detectMultiScale(cv_img)

# we still have our PIL color version in a gif to draw on
pil_img=Image.open('readonly/msi_recruitment.gif')

drawing=ImageDraw.Draw(pil_img)
# For each item in faces, lets surround it with a box
for x,y,w,h in faces:
    drawing.rectangle((x,y,x+w,y+h), outline="white")
display(pil_img)

#the recognitiojn is kiond of corecet but the colors are generally fucked up
# this is because of the gif format
# so we need to convert to rgb mode:
pil_img=Image.open('readonly/msi_recruitment.gif')
pil_img = pil_img.convert("RGB")
print(pil_img.mode)

# and back to faces:
drawing = ImageDraw.Draw(pil_img)
for x,y,w,h in faces:
    drawing.rectangle((x,y,x+w,y+h), outline="white")
display(pil_img)
#the result is much better but still missing some    


#%% Solving this:

# just a quich function to show the pic again    
def show_rects(faces):
    #Lets read in our gif and convert it
    pil_img=Image.open('readonly/msi_recruitment.gif').convert("RGB")
    # Set our drawing context
    drawing=ImageDraw.Draw(pil_img)
    # And plot all of the rectangles in faces
    for x,y,w,h in faces:
        drawing.rectangle((x,y,x+w,y+h), outline="white")
    #Finally lets display this
    display(pil_img)

   
# native opencv native binarization
cv_img_bin = cv.threshold(cv_img,90,255,cv.THRESH_BINARY)[1] # returns a list, we want the second value
# display(Image.fromarray(cv_img_bin))
#  the actual face detection
faces = face_cascade.detectMultiScale(cv_img_bin)
show_rects(faces)

# this doesnt really work so we need to go to and check other parameters of the function:
faces = face_cascade.detectMultiScale(cv_img,1.05)
show_rects(faces)

faces = face_cascade.detectMultiScale(cv_img,1.15)
show_rects(faces)

faces = face_cascade.detectMultiScale(cv_img,1.25)
show_rects(faces)

# Timit is like tic toc but more advanced!
%timeit face_cascade.detectMultiScale(cv_img,1.05)
%timeit face_cascade.detectMultiScale(cv_img,1.15)