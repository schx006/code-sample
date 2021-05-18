#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import yaml


class Config:
	"""Structure du fichier de configuration (YAML) :
send_sms:
   user_id: "123456788"
   api_key: "XXXXXXXXXX"
misc:

Après lecture du fichier par une instance de la classe "Config",
les données de configurations sont sous la forme :
 {'send_sms': {'user_id': '12345678', 'api_key': 'XXXXXXXXXX'}, 'misc': None}

Les paramètres utiles de l'instance sont :
	obj.userId
	obj.apiKey
"""
    
	def __init__(self):
	
		# le fichier de configuration est ICI
		configPath = './'
		configName = 'config.yaml'
		configFile = configPath + configName

		# lecture du fichier
		with open(configFile, mode='rt') as f:
			configData = yaml.load(f, Loader=yaml.SafeLoader)
			# extraction des paramètres de la structure de données
			self.userId = configData['send_sms']['user_id']
			self.apiKey = configData['send_sms']['api_key']



def test():
	print(Config.__doc__)
	dest = Config()
	#print(dest.userId)
	#print(dest.apiKey)

if __name__ == '__main__':
	test()
