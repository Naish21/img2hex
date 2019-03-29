#!/usr/bin/python
# img2hex.py - Convert a 212x104 image to an hex text to send to FireBeetle Covers-ePaper

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import imageio
import numpy as np
import sys

__author__  = "Jorge Aranda"
__license__ = "GNU GPLv3"
__version__ = "1.0.0"
__email__   = "jorge.aranda.moro@gmail.com"

def hextobin(hexdata, num_of_bits = 8):
    """
    hexdata = string
    Translates 'hexdata' from an hex number to binary, filling from the left
    until reaching 'num_of_bits'
    """
    scale = 16 ## equals to hexadecimal
    return bin(int(hexdata, scale))[2:].zfill(num_of_bits)

def remove0x(hex_c):
    """
    hex_c = string
    """
    return hex_c.upper().split('0X')[1]

def bin2hex(bin_num):
    """
    bin_num = string
    """
    # return hex(int(bin_num, 2))
    hexnum = hex(int(bin_num, 2))[2:].zfill(len(bin_num)//4)
    return '0X' + hexnum.upper()

def rotate90(image):
    return np.flip(image, 0).T

def imagetohex(image, invert=False):
    if image.shape[0]==104:
        image = rotate90(image)
    if invert:
        image2 = np.where(image>150, 1.0, 0)
    else:
        image2 = np.where(image>150, 0, 1.0)
    image2 = image2.astype(np.int64)
    image2 = image2.reshape((1,212*104))
    image2 = image2[0,:]

    image3 = ""
    for i in image2:
        image3 = image3 + str(i)
    
    image_hex = []
    for i in range(0,len(image3),8):
        bits8 = image3[i:i+8]
        image_hex.append(bin2hex(bits8))
    return image_hex

def exporttofile(image_hex, filename='out.txt'):
    import os
    with open(filename, 'w') as file:
        for i in image_hex:
            file.write(i + ',')
    with open(filename, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()

if __name__ == '__main__':

    argnum = len(sys.argv)

    if argnum < 2:
        print("\nConverts an image file 212x104 or 104x212 to an hex text to send to FireBeetle Covers-ePaper \n")
        print("ARGNUM imagefile [output] [-i]\n")
        print("imagefile   Specifies the image file to convert")
        print("output      Indicates a file to write the hex characters to")
        print("-i          Invert colors of the image")

    else:
        imagefile = sys.argv[1]
        try:
            outputfile = sys.argv[2]
        except:
            outputfile = 'out.txt'
        try:
            invert = sys.argv[3]
            if invert=='-i':
                invert = True
            else: 
                invert = False
        except:
            invert = False
        try:
            image = imageio.imread(imagefile)
        except:
            print('File not found!')
            sys.exit()
        try:
            image = image[:,:,1]
        except:
            pass

        try:
            image_hex = imagetohex(image, invert)
        except:
            print('Image file size is not 212x104 or 104x212')
            sys.exit()

        try:
            exporttofile(image_hex, outputfile)
        except:
            print('Error saving file (do you have writing permissions in destination?)')
            sys.exit()

        print('Output File: ' + str(outputfile))