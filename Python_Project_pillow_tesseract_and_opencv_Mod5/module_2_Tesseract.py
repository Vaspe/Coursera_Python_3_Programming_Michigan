# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:25:14 2020

@author: Vasilis
"""

from PIL import Image
import pytesseract
import inspect # handy module to look at source code!


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

#%% quick hack to look at source code of a function
src = inspect.getsource(pytesseract.image_to_string)
print(src)
print("---------------------------------------------")

#%% Using the double questionmark we can get information about the function/module

pytesseract.image_to_string??

print("---------------------------------------------")


