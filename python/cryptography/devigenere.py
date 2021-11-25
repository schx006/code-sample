#!/usr/bin/env python3
# coding=utf-8

# file: devigenere.py

import io
import unicodedata
import argparse


def codeChar(encode, key, char, index):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # uniformisation de la casse
    char = char.upper()
    lk = len(key)
    keyChar = key[index % lk]

    for i in range(26):
        if keyChar == alphabet[i]:
            row = i
    for i in range(26):
        if char == alphabet[i]:
            if encode:
                myChar = alphabet[(i + row) % 26]
            else:
                myChar = alphabet[(i - row) % 26]
            return(myChar)

 
def devigenere(encode, key, workFile):

    """Blaise de Vigenère's code

syntax:
    devigenere.py encode|decode key fileToProcess.txt
    with key: key word (alphabetical string without space)
    output: standard output
"""

    # la clé ne doit pas contenir de caractères accentués…
    key = ''.join((c for c in unicodedata.normalize('NFD', key) if unicodedata.category(c) != 'Mn'))
    # … doit être alphabétique…
    if not key.isalpha():
        raise syntax_error
    # … et être en majuscule (uniformisation de la casse).
    key = key.upper()
    out = ''
    counter = 0

    with open(workFile, "rt", encoding="utf-8") as f:
        data = f.read()
        if encode:
            # retrait des accents du texte à crypter
            data = ''.join((c for c in unicodedata.normalize('NFD', data) if unicodedata.category(c) != 'Mn'))
        for c in data:
            # le code 'de Vigenère' n'encrypte que les lettres, pas les chiffres, ni la ponctuation
            if c.isalpha():
                cc = codeChar(encode, key, c, counter)
                counter += 1
            else:
                cc = c
            out += cc
    f.closed
    return(out)


def prog():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices = ['encode', 'decode'])
    parser.add_argument('key', type=str)
    parser.add_argument('fileName', type=str)
    args = parser.parse_args()
 
    # 'Vrai' pour crypter, 'Faux' pour décrypter
    if args.action == 'encode':
        myAction = True
    else:
        myAction = False
    myKey = args.key
    myFile = args.fileName
    
    print(devigenere(myAction, myKey, myFile))


    
# ------------------------

if __name__ == '__main__':
    prog()
