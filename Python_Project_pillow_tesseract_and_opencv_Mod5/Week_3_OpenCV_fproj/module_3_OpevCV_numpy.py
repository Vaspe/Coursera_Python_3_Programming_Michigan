# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 22:32:27 2020

@author: Vasilis

See docs:
    docs.opencv.org
"""

import cv2 as cv
import inspect
from PIL import Image
import numpy as np

#%%
#read the image with openCV
img = cv.imread('readonly/floyd.jpg')
# convert to grweyscale read the docs for the commands
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# seethe object is anumpy ndarray and not a picure
inspect.getmro(type(gray))
print(gray)

# we canconvert the ndarray back to a visible image using the PIL again with fromaarray command
image = Image.fromarray(gray, "L") #array of data with a given color format and convert this into a PIL object
display(image)

print("--------------------------------------")


#%% short  intro to numpy
single_dim = np.array([25, 50 , 25, 10, 10])
double_dim = np.array([single_dim])

print(double_dim)
print("--------------------------------------")

display(Image.fromarray(double_dim, "L")) # weconvert to image and dis;ay it. Its only a line of pixels with different evels of blacj

# the shape numpy function shows as the dimension of an ndarray 
print(single_dim.shape)
print(double_dim.shape)
print(img.shape) #it is 256x256x256 = 16e6 color which is called  24bit color. It means that each of the 415x415 pixels has a combination of the 24bit color
print("--------------------------------------")
#back to the image
first_pixel = img[0][0]
print(first_pixel)
print("--------------------------------------")
# using reshape
print("Original image")
print(gray)
print("New image")

# first parameter of reshapr is the original matrixand the second is the new dimension we need
image1d = np.reshape(gray,(1,gray.shape[0]*gray.shape[1]))
print(image1d)
print("--------------------------------------")

# slicing matrices to get submatrixes of ndarray 

# load the two column picture from before and make it gray scale with opencv
img = cv.imread('readonly/two_col.png')
gray2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# indexing mulidimenstional arrays in numpy ndaarray objects
test1 = gray2[2:4,1:3]
print(test1)
print("--------------------------------------")

#non-zero command retutns the ammount of elemtns elements that are not zero 
test2 = np.count_nonzero(gray[2:4,1:3])
print(test2)

#%% Example of using matrix manipulation to create a line or something in a image

white_matrix=np.full((12,12),255,dtype=np.uint8)
display(Image.fromarray(white_matrix,"L")) # it is just 12x12 white pixels
print(white_matrix)

# add a blck column as we needed before:
white_matrix[:,6] = np.full((1,12),0,dtype=np.uint8) # switchinhg all middle pixels to 0
display(Image.fromarray(white_matrix,"L"))
white_matrix    


#%% Back to images and open cv

