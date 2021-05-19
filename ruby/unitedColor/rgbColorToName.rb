#!/usr/bin/env ruby -w
# -*- coding: utf-8 -*-



def rgbColorToNameTranslate(rgbColor)
	# cette méthode retourne un tableau de noms
	
	# le fichier de correspondance des noms est ICI
	colorRefPath = '../../'
	colorRefName = 'color_rgb_table'
	colorRefFile = colorRefPath + colorRefName
	
	colorAlias = []
	# lecture du fichier
	f = File.new(colorRefFile, 'rt')
	l = f.readlines()
	n = l.length
	for i in (0..n-1) do
		# lecture du code de la couleur, en fin de ligne
		# attention, le dernier caractère est un "saut de ligne"
		j = l[i].length
		code = l[i][j-7..j-2]
		color = ''
		# si le code correspond à la requête…
		if code == rgbColor
			# lecture du nom de la couleur correspondante
			foo = false
			for k in (0..j-8) do
				c = l[i][k]
				if c != ':' and not foo
					color += c
				else
					foo = true
				end
			end
		end
		# ajout de la couleur au tableau
		if color.length != 0
			colorAlias.push(color)
		end
	end
	return colorAlias
end



def verifyCode(rgbColor)
	# liste des caractères autorisés pour écrire un nombre héxadécimal
	hexaDigit = '0123456789abcdef'
	# si la longueur n'est pas 6 : erreur de saisie…
	if rgbColor.length() != 6
		puts('An hexadecimal RGB color must have 6 digits!')
		# erreur :
		return true
	end
	# si un caractère est hors de la liste autorisée : erreur de saisie…
	rgbColor.each_char do |d|
		if hexaDigit.match?(d) == false
			puts('Authorized digits are \'0\’ → \'9\' and \'a\' → \'f\'.')
			puts('(\'A\' → \'F\' can be used, too.)')
			# erreur :
			return true
		end
	end
	# pas d'erreur :
	return false
end



def readColorCode()
	# saisie au clavier du "code couleur" héxadécimal
	
	err = true
	while err
		puts('Please, enter an hexadecimal RGB color:')
		rgbColor = gets.chomp
		# transformation des majuscules en minuscules
		rgbColor = rgbColor.downcase()
		# vérification de la saisie : 6 "digits"
		err = verifyCode(rgbColor)
	end
	# pas d'erreur
	# fin de la boucle
	return rgbColor
end



# main method • méthode principale
def rgbColorToName()
	myColorCode = readColorCode()
	myColorName = rgbColorToNameTranslate(myColorCode)
	n = myColorName.length()
	if n < 1
		msg = 'The "' + myColorCode + '" color is unnamed.'
		puts(msg)
	else
		msg = 'The "' + myColorCode + '" color is called "'
		(1..n).each do |i|
			if i == n
				msg = msg + myColorName[i - 1] + '".'
			elsif i == n - 1
				msg = msg + myColorName[i - 1] + '" or "'
			else
				msg = msg + myColorName[i - 1] + '", "'
			end
		end
		puts(msg)
	end
end


if __FILE__ == $0
	rgbColorToName()
end
