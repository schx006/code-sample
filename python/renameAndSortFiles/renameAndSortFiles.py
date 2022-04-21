#!/usr/bin/env python3
# coding=utf-8

# File:     renameSortedFiles.py
# Author:   Xavier Schoepfer


#   Cette fonction copie des fichiers d'images JPEG d'un répertoire 
#   ('./filesToSort/') vers un autre ('./sortedFiles/'), de sorte que
#   les noms dans le répertoire d'arrivée forment une liste 
#   de 'IMG_0001.jpeg' à 'IMG_0xyz.jpeg' ('xyz' est le nombre de 
#   fichiers présents dans le répertoire).


import os


inDir = "./filesToSort/"
outDir = "./sortedFiles/"

fName = "IMG_"
fSuffix = ".jpeg"
i = 1

with os.scandir(inDir) as it:
    for f in it:
        if i < 10:
            zero = "000"
        elif i < 100:
            zero = "00"
        elif i < 1000:
            zero = "0"
        else:
            zero = ""
        oldName = os.fsdecode(f)
        newName = outDir + fName + zero + str(i) + fSuffix
        os.rename(oldName, newName)
        i += 1

