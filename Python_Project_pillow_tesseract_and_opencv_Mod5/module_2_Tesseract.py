# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:25:14 2020

@author: Vasilis
"""
import PIL
from PIL import Image
import pytesseract
import inspect # handy module to look at source code!
import string #native package to manipulate strings like removing non alphabetical characters


#%% get and see the image
image = Image.open("readonly/text.png")
display(image)

#%% tesseract python wrapper

# important line to make tesseract work!!!

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print(dir(pytesseract))

print("---------------------------------------------")
#help(pytesseract.image_to_string)
#help(Image.Image.resize)

# testing basic functionality of tesseract
text = pytesseract.image_to_string(image)
print(text)

#%% quick hack to look at source code of a function
src = inspect.getsource(pytesseract.image_to_string)
print(src)
print("---------------------------------------------")

#%% Using the double questionmark we can get information about the function/module

# pytesseract.image_to_string??

# print("---------------------------------------------")

#%% Noisy picture OCR
img = Image.open("readonly/Noisy_OCR.PNG")
display(img)

# trying the basic functionality with the noisy image
text = pytesseract.image_to_string(Image.open("readonly/Noisy_OCR.PNG"))
print(text)
print("---------------------------------------------")
#%% MOdifying noisy image in order to read it
img = Image.open('readonly/Noisy_OCR.PNG')
# try by resizing:
basewidth = 600 
wpercent = (basewidth / float(img.size[0])) # aspect ratio
hsize = int((float(img.size[1]) * float(wpercent))) #recovered resized height from AR
# applying antializing to make the picture clearer
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('resized_nois.png') 
display(img)

#try again to apply OCR to the resized
text2 = pytesseract.image_to_string(Image.open('resized_nois.png')) 
print(text2)
#worked a bit better but not quite
print("---------------------------------------------")

#%% second try by swutching the image to greyscale

img = img.convert('L')
# Now lets save that image
img.save('greyscale_noise.jpg')
# And run OCR on the greyscale image
text3 = pytesseract.image_to_string(Image.open('greyscale_noise.jpg')) 
print(text3)
print("---------------------------------------------")
# This worked very good!

#%% third try using binarizations meaning converting the picture to only two colors
# from the pillow 
img = Image.open('readonly/Noisy_OCR.PNG').convert('1')
# Now lets save and display that image
img.save('black_white_noise.jpg')
display(img)


# or creating our own binarization function
def binarize(image_to_transform, threshold):
    # now, lets convert that image to a single greyscale image using convert()
    output_image=image_to_transform.convert("L")
    for x in range(output_image.width):
        for y in range(output_image.height):
            
            # for the given pixel at w,h, lets check its value against the threshold
            if output_image.getpixel((x,y))< threshold: #note that the first parameter is actually a tuple object
                # lets set this to zero
                output_image.putpixel( (x,y), 0 )
            else:
                # otherwise lets set this to 255
                output_image.putpixel( (x,y), 255 )
    #now we just return the new image
    return output_image

# And testing it
for thresh in range(0,257,64):
    
    print("Trying with threshold " + str(thresh))
    

    # Lets display the binarized image inline
    display(binarize(Image.open('readonly/Noisy_OCR.PNG'), thresh))
    # And lets use tesseract on it. It's inefficient to binarize it twice but this is just for
    # a demo
    print(pytesseract.image_to_string(binarize(Image.open('readonly/Noisy_OCR.PNG'), thresh)))   
    print("---------------------------------------------")


#%% Interacting with photographs
image=Image.open('readonly/storefront.png')
display(image)
# Finally, lets try and run tesseract on that image and see what the results are
text4 = pytesseract.image_to_string(image)
print(text4)
#we see that nothing is printed

# we cant try to crop the text to assist the process
bounding_box = (315, 170, 700, 270) #xy of upper ledt and lower right corners
title_image = image.crop(bounding_box)

# Now lets display it and pull out the text
display(title_image)
text5 = pytesseract.image_to_string(title_image)
print(text5)
print("---------------------------------------------")
# now it was read succedfully

#%% Now lets try to read the little sign at the right inside thestore

#crop the image
bounding_box=(900, 420, 940, 445)
little_sign=image.crop((900, 420, 940, 445))
display(little_sign)

# first attempt by resizing the small picture
new_size=(little_sign.width*10,little_sign.height*10)
display(little_sign.resize( new_size, Image.NEAREST))
# its bigger but very bad quality!!!

# trying all the options to make the enlarged picture lsmoother
options=[Image.NEAREST, Image.BOX, Image.BILINEAR, Image.HAMMING, Image.BICUBIC, Image.LANCZOS]
for option in options:
    print(option)
    aa = little_sign.resize( new_size, option)
    display(little_sign.resize( new_size, option)) 
    txt_cur = pytesseract.image_to_string(aa)
    print(txt_cur) 
    print("---------------------------------------------")   
#We see that none can capture it

# So now lets try by binarizing theses
for option in options:
    bb = little_sign.resize( new_size, option)   
    aa = binarize(bb, 190)
    display(aa)      
    txt_cur = pytesseract.image_to_string(aa)
    print(txt_cur) 
    print("---------------------------------------------")    
# we see that also here we have no success

#%% Approach by trying all possibe binaraziation levels and thethen comparing with all possible words from a word list
eng_dict=[]
fid = open("readonly/words_alpha.txt", "r")
data = fid.read()
fid.close()
eng_dict = data.split("\n")

# Now that the lsit with all possible words is loaded we will try all thresholds for binarization
for i in range(100,200):
    strng_OCR = pytesseract.image_to_string(binarize(little_sign.resize( new_size,Image.BICUBIC)   ,i))
    strng_OCR = strng_OCR.lower()
    comparison=''
    # loop all characters and keep if they are lower case letters
    for character in strng_OCR:
        if character in string.ascii_lowercase:
            comparison = comparison + character
    # now check if this is actually a word in english or a random artifact
    if comparison in eng_dict:
        # and print it if we find it
        print(comparison)    



