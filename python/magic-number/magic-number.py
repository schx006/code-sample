#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Programme "magic-number.py"
# Version 1.0
#
# Auteur : Xavier Schoepfer
#
# GNU General Public License v3.0


import random as rdm




def main():
	"""SYNOPSIS :
	magic-number.py

DESCRIPTION :
Générer un "nombre magique" (Magic Number) aléatoire de 8 octets en hexadécimal.
"""
	mn = ''
	i  = 0

	sysAgCheck()

	while i < 8:
		# tirage au sort d'un nombre entre 0 et 255
		myDigit = int(abs(rdm.random() * 255))
		# conversion en héxadécimal, entre '0x0' et '0xff'
		myCode = str(hex(myDigit))
		# Si 'code < 0x10' ...
		if len(myCode) == 3:
			# ajout d'un '0' devant le chiffre significatif 
			# suppression du préfixe '0x'
			myCode = '0' + myCode[-1]
		else:
			# suppression du préfixe '0x'
			myCode = myCode[-2:]
		# concaténation		
		mn += myCode
		i += 1
	# impression du "Magic Number"
	print('The Magic Number is:')
	print(mn)




if __name__ == '__main__':
	main()
