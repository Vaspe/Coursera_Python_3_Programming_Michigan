# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:42:35 2020

@author: Vasilis
"""

import PIL
from PIL import Image
from PIL import ImageEnhance

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')


images = []
for factor in [0.1,0.5,0.9] :
    #get a copy of the image and its pixels to moidify for R
    cur_image = image.copy()
    pixels = cur_image.load()
    for iwidth in range(image.width):
        for iheight in range(image.height): 
            pixels [iwidth,iheight]= (int(factor*pixels [iwidth,iheight][0]),pixels [iwidth,iheight][1],pixels [iwidth,iheight][2])
    # store the new modified image to the list
    images.append(cur_image)
    #get a copy of the image and its pixels to moidify for G
    cur_image = image.copy()
    pixels = cur_image.load()
    for iwidth in range(image.width):
        for iheight in range(image.height): 
            pixels [iwidth,iheight]= (pixels [iwidth,iheight][0],int(factor*pixels [iwidth,iheight][1]),pixels [iwidth,iheight][2])
    # store the new modified image to the list
    images.append(cur_image)
    #get a copy of the image and its pixels to moidify for B
    cur_image = image.copy()
    pixels = cur_image.load()
    for iwidth in range(image.width):
        for iheight in range(image.height): 
            pixels [iwidth,iheight]= (pixels [iwidth,iheight][0],pixels [iwidth,iheight][1],int(factor*pixels [iwidth,iheight][2]))
    # store the new modified image to the list
    images.append(cur_image)

# for i in images:
#     display(i)
    
    

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

# for img in images:
#     # Lets paste the current image into the contact sheet
#     contact_sheet.paste(img, (x, y) )
#     # Now we update our X position. If it is going to be the width of the image, then we set it to 0
#     # and update Y as well to point to the next "line" of the contact sheet.
#     if x+first_image.width == contact_sheet.width:
#         x=0
#         y=y+first_image.height
#     else:
#         x=x+first_image.width
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

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)