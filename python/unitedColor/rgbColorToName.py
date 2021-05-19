#! /usr/bin/env python3
# -*- coding: utf-8 -*-



def rgbColorToNameTranslate(rgbColor):
	# cette fonction retourne un tableau de noms
	
	# le fichier de correspondance des couleurs est ICI
	colorRefPath = '../../'
	colorRefName = 'color_rgb_table'
	colorRefFile = colorRefPath + colorRefName	
	
	colorAlias = []
	# lecture du fichier
	with open(colorRefFile, mode='rt') as f:
		# pour chaque ligne…
		for l in f:
			# lecture du code de la couleur, en fin de ligne
			# attention, le dernier caractère est un "saut de ligne"
			code = l[len(l) - 7:len(l) - 1]
			color = ''
			# si le code correspond à la requête…
			if code == rgbColor:
				# lecture du nom de la couleur correspondante
				end = False
				for c in l:
					if c != ':' and not end:
						color = color + c
					else:
						end = True
			# ajout de la couleur au tableau
			if len(color) != 0:
				colorAlias.append(color)
	return colorAlias



def verifyCode(rgbColor):
	# vérification de la validité de la saisie au clavier
	
	# liste des caractères autorisés pour écrire un nombre héxadécimal
	hexaDigit ='0123456789abcdef'
	# si la longueur n'est pas 6 : erreur de saisie…
	if len(rgbColor) != 6:
		print('An hexadecimal RGB color must have 6 digits!')
		return False
	# si un caractère est hors de la liste autorisée : erreur de saisie…
	for d in rgbColor:
		if not (d in hexaDigit):
			print("Authoryzed digits are '0' → '9' and 'a' → 'f'.")
			print("('A' → 'F' can be used, too.)")
			return False
	# pas d'erreur…
	return True



def readColorCode():
	# saisie au clavier du "code couleur" héxadécimal
	
	foo = False
	# tant que 'foo' est faux:
	while not foo:
		rgbColor = input('Please, enter an hexadecimal RGB color: ')
		# transformation des majuscules en minuscules
		rgbColor = rgbColor.lower()
		# vérification de la saisie : 6 "digits" hégadécimaux…
		foo = verifyCode(rgbColor)
	# 'foo' est vrai :
	# fin de la boucle
	return rgbColor



# main function
def rgbColorToName():
	myColorCode = readColorCode()
	myColorName = rgbColorToNameTranslate(myColorCode)
	print(myColorName)
	n = len(myColorName)
	if n < 1:
		msg = 'The "' + myColorCode + '" color is unnamed.'
		print(msg)
	else:
		msg = 'The "' + myColorCode + '" color is called "'
		for i in range(1, n + 1):
			print (i)
			if i == n:
				msg = msg + myColorName[i - 1] + '".'
			elif i == n - 1:
				msg = msg + myColorName[i - 1] + '" or "'
			else:
				msg = msg + myColorName[i - 1] + '", "'
		print(msg)



if __name__ == '__main__':
	rgbColorToName()
