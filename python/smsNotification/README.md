L'opérateur de téléphonie **Free Mobile** propose une API pour s'envoyer des
notifications par SMS à soi-même… Cette fonctionalité est décrite dans un 
article du site **Free News** à lire
[ICI](https://www.freenews.fr/freenews-edition-nationale-299/free-mobile-170/nouvelle-option-notifications-par-sms-chez-free-mobile-14817).

##### Remarque :
l'option doit être préalablement activée dans
l'[espace client](https://mobile.free.fr/account/) du site **Free Mobile**.
> Espace abonné   
> → Mon forfait mobile → Mes options → Notifications par SMS → ✅

#### Mode d'emploi de l'API
Il suffit d'envoyer la requète grâce à une `URL` dont la syntaxe est :   
`https://smsapi.free-mobile.fr/sendmsg?user=12345678&pass=XXXXXXXXXXXXXX&msg=Hello%20World%21`   
pour recevoir le SMS :
> Hello World!

Les paramètres de l'`URL` sont :
- `user` : votre login (identifiant client **Free Mobile** à 8 chiffres)
- `pass` : votre clé d’identification générée automatiquement par le service
**Free Mobile** et visible sur votre espace abonné, au niveau de l'option
*Notifications par SMS*
- `msg` : le contenu du SMS encodé au format `URL` (Percent-encoding, caractères
*spéciaux* et *étendus* représentés sous la forme %xx)

---

Ce petit programme modulaire nécessite les bibliothèques standards :
- `http.client`
- `urllib.parse`

ainsi que la bibliothèque `yaml` (projet **PyYaml** disponible sur
[GitHub: yaml/pyyaml](https://github.com/yaml/pyyaml))

### Fichier *smsNotification.py*
Ce fichier est auto-documenté.   
Le [fichier de configuration](#fichier-configyaml) doit être préalablement complété à
partir de vos informations personnelles ([login & clé API](#mode-demploi-de-lapi))

L'exécution de la commande `./smsNotification.py` sur la console affiche le mode d'emploi
« interne » (auto-documentation  de la fonction `sendSms()`) et vous envoie le SMS :
> Hello World!   
> It's me…  
> 🙂

Construit comme un module, ce fichier peut être utilisé depuis un autre script en python :
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smsNotification

# ...

smsNotification.sendSms("That's all Folks...")

# ...

```


### Fichier *myConfigurator.py*
Ce fichier est auto-documenté.   
Le module extrait mes informations de [login & clé API](#mode-demploi-de-lapi) du
fichier de confguration.

L'exécution de la commande `./smsNotification.py` sur la console lit le fichier de
configuration et affiche le mode d'emploi « interne » (auto-documentation de la
classe `Config`). Elle ne fait rien des données lues… elle pourrait les imprimer ; 
cependant, les 2 lignes de l'impression sont *commentées* et réservées à 
l'*instrumentation* (tests de vérification du bon fonctionnement du programme).
```python
# ...
	# Instrumentation:
	#print(dest.userId)
	#print(dest.apiKey)
# ...
```
⚠️ Les variables `dest.usrId` et `dest.apiKey` contiennent des données sensibles !


### Fichier *config.yaml*
Contenu du fichier :
```yaml
# nom du fichier : config.yaml

# configuration pour :
#    sendSms() — module smsNotification.py
send_sms:
  user_id: "12345678"        # remplacer 12345678       par votre propre login
  api_key: "XXXXXXXXXXXXXX"  # remplacer XXXXXXXXXXXXXX par votre propre clé API

# juste pour compliquer les choses…
# … ou pouvoir ajouter des fonctionnalités plus tard
misc:

```
⚠️ Ce fichier contient des données sensibles !

