#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from os import listdir
from os.path import isfile, isdir, join
import Image

def resizeImage(srcImage):
    baseWidth = 1024
    wpercent = (baseWidth/float(srcImage.size[0]))
    hsize = int((float(srcImage.size[1])*float(wpercent)))
    return srcImage.resize((baseWidth,hsize), Image.ANTIALIAS)

def main():
    if(len(sys.argv) < 3):
        print("Usage: python resize.py [SRC IMAGE FOLDER][DST IMAGE FOLDER]")
        sys.exit(0)

    srcFolder = sys.argv[1]
    dstFolder = sys.argv[2]

    for imageFile in listdir(srcFolder):
        filePath = srcFolder + '/' + imageFile
        if isfile(filePath):
            srcImage = Image.open(filePath)
            rzImage = resizeImage(srcImage)
            rzImage.save(dstFolder + '/' + imageFile)

if __name__ == '__main__':
    main()    



