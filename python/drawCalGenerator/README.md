# drawCalGenerator.py

Ce programme liste les dates de tirage du Loto®[^1] (ou de l'Euromillions®[^2]) pour une année de référence donnée.

### Utilisation du script

1. Pour créer un fichier des dates de tirage `drawCalendar.txt`, utiliser la commande :    
   ```bash
   python3 drawCalGenerator.py > ./drawCalendar.txt
   ```
2. Pour redéfinir l'année de référence, éditer le fichier du progrmamme `drawCalGenerator.py` et
   modifier la variable globale `year` :
   ```python
   ⫶
   
   # global variables
   # reference year
   year = 2023
   ⫶
   ```
3. Pour obtenir la liste des tirages d'Euromillions® (au lieu du loto®), et vive-versa,
   déplacer le `#` de commentaire dans les variables globales pour intervertir les valeurs de `isoDrawDay`.    
   Pour les dates de tirage du Loto® :
   ```python
   ⫶
   
   # global variables
   ⫶
   # draw days for the game
   isoDrawDay = (1, 3, 6)	# ISO format, Loto® draws : Monday, Wednesday, Saturday
   #isoDrawDay = (2, 4)	# ISO format, Euromillions® draws : Tuesday, Friday
   ⫶
   ```
   Pour les dates de tirage de l'Euromillions® :
   ```python
   ⫶
   
   # global variables
   ⫶
   # draw days for the game
   #isoDrawDay = (1, 3, 6)	# ISO format, Loto® draws : Monday, Wednesday, Saturday
   isoDrawDay = (2, 4)	# ISO format, Euromillions® draws : Tuesday, Friday
   ⫶
   ```

[^1]: *Loto®* est une marque déposée de la société **Française des Jeux (*FDJ*)**.
[^2]: *Euromillions®* est une marque déposée de la société **Française des Jeux (*FDJ*)**.
