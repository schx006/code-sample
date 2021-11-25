#!/usr/bin/env python3
# coding=utf-8

# file: caesar.py

import io
import unicodedata
import argparse


def codeChar(encode, key, char):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # uniformisation de la casse
    char = char.upper()
    myChar = char

    for i in range(26):
        if char == alphabet[i]:
            if encode == True:
                myChar = alphabet[(i + key) % 26]
            else:
                myChar = alphabet[(i - key) % 26]
            return(myChar)


def caesar(encode, key, workFile):

    """Julius Caesar's code

syntax:
    caesar.py encode|decode key fileToProcess.txt
    with key: integer between 1 and 25
    output: standard output
"""

    if key < 1 or key > 25:
        raise syntax_error
    out = ''

    with open(workFile, "rt", encoding="utf-8") as f:
        data = f.read()
        if encode:
            # retrait des accents du texte à crypter
            data = ''.join((c for c in unicodedata.normalize('NFD', data) if unicodedata.category(c) != 'Mn'))
        for c in data:
            # le code 'Jules César' n'encrypte que les lettres, pas les nombres, ni la ponctuation
            if c.isalpha():
                cc = codeChar(encode, key, c)
            else:
                cc = c
            out += cc
    f.closed
    return(out)


def prog():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices = ['encode', 'decode'])
    parser.add_argument('key', type=int, choices=range(1, 26))
    parser.add_argument('fileName', type=str)
    args = parser.parse_args()

    # 'Vrai' pour crypter, 'Faux' pour décrypter
    if args.action == 'encode':
        myAction = True
    else:
        myAction = False
    myKey = args.key
    myFile = args.fileName
    
    print(caesar(myAction, myKey, myFile))



# ------------------------

if __name__ == '__main__':
    prog()
