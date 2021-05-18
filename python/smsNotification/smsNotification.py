#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# L'opérateur de téléphonie "Free Mobile " propose 
# une API pour s'envoyer des notifications SMS à soi-même…
# Cf. article :
# https://www.freenews.fr/freenews-edition-nationale-299/free-mobile-170/nouvelle-option-notifications-par-sms-chez-free-mobile-14817
# Remarque : l'option doit être préalablement activée dans l'espace client.
#
# Syntaxe de l'URL :
#	https://smsapi.free-mobile.fr/sendmsg?user=12345678&pass=XXXXXXXXXXXXXX&msg=Hello%20World%21
# Paramètres de l'URL à envoyer à l'API :
#	✓ user : votre login (identifiant client Free Mobile)
#	✓ pass : votre clé d’identification générée automatiquement par le service Free Mobile
#	✓ msg : le contenu du SMS encodé au format d'URL (Percent-encoding, %xx)


import http.client
from urllib.parse import quote

from myConfigurator import Config


def sendSms(myMsg):
	"""Codes de retour HTTP utilisés par l'API :
    ✓ 200 OK :               le SMS a été envoyé sur votre mobile.
    ✓ 400 Bad Request :      un des paramètres obligatoires est manquant.
    ✓ 402 Payment Required : trop de SMS ont été envoyés en trop peu de temps.
    ✓ 403 Forbidden :        le service n’est pas activé sur l’espace abonné,
                             ou l'identification (login, clé) est incorrecte.
    ✓ 500 Internal Error :   erreur côté serveur.
    
Si le serveur répond 'OK', tout va bien.
Une autre réponse provoque une erreur…
"""
	# adresse du serveur qui propose l'API
	smsSenderServer = 'smsapi.free-mobile.fr'
	# lecture des paramètres d'identification du destinataire
	dest = Config()
	# encodage en %xx des caractères spéciaux
	percentMsg = quote(myMsg, safe='/', encoding='utf-8', errors=None)
	
	# envoi de la requête (et lecture de la réponse du serveur)
	myUri = '/sendmsg?user=' + dest.userId + '&pass=' + dest.apiKey + '&msg=' + percentMsg

	myConnection = http.client.HTTPSConnection(smsSenderServer)
	myConnection.request('GET', myUri)
	serverResponse = myConnection.getresponse()
	myConnection.close()
	
	# vérification de l'envoi du SMS
	# si l'envoi du SMS n'est pas 'OK' ⇒ message d'erreur
	if serverResponse.status != 200:
		errMsg = 'HTTPError: ' + str(serverResponse.status) + ' ' + serverResponse.reason
		raise Exception(errMsg)



def test():
	myText = "Hello World!\nIt's me…\n☺"
	
	print (sendSms.__doc__)
	sendSms(myText)

if __name__ == '__main__':
	test()