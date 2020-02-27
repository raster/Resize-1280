#!/usr/local/bin/python3
#
# Pete Prodoehl <pete@2xlnetworks.com>
# 
# Rezies images to 1280x960
# Assuming 4032x3024 images as source
# (Which is the size of photos from my phone...)
#

from PIL import Image
import glob
import getopt
import sys
import os

# read command line arguments first
fullCmdArguments = sys.argv

# then read further arguments
argumentList = fullCmdArguments[1:]

# loop through files, resizing each one
for infile in argumentList:
    file, ext = os.path.splitext(infile)
    img = Image.open(infile)
    newimg = img.resize((1280, 960))
    newimg.convert('RGB').save(file + ".jpg","JPEG",Optimize=True)

