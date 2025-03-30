# Projet Théorie des langages

## Introduction
Le projet a lieu dans le cadre du cours de théories des langages réalisé au Semestre 2 de la deuixème année de Licence Sciences du Numérique. 
Il a été réalisé par Candice Giami et Clément Szewczyk. 

L'objectif du projet est d'implémenter une bibliotèque de fonction sur les automates en **python**. 

Les étapes du projet : 
- modélisation d’un automate.
- de charger la description d’un automate sous forme d’un fichier texte (texte brut, json, xml…) dont vous définirez
le format
- de sauvegarder la description d’un automate sous forme d’un fichier texte dont le format respecte celui en lecture
- d’afficher l’automate à l’écran ou de générer un fichier image.
- Réaliser des opérations élémentaires sur les automates (union, concaténation et répétition)
- Synchroniser un automate (suppression des 𝜖-transitions) **(BONUS)**
- Construire un automate à partir d’une expression régulière **(BONUS)**
- Compléter/Déterminiser/Minimiser un automate
- Reconnaitre une adresse mail à l’aide d’un automate

Les étapes sont découpé en 4 parties :
1. Modélisation d'un automate
2. Opérations sur les automates
3. Expressions régulières verd Automates (Bonus)
4. Finalisation


## Importation

Le projet utilise disgraph pour générer des images d'automates. Pour cela vous devez l'installer 

```bash
pip install disgraph
```


## Lancement  :

Pour avoir un visuel complet, veuillez regarder le fichier suivant : [Fichier Jupiter Notebook](./rapport/rapport.ipynb)

Si vous voullez lancer une fonctionnalité en particulier, vous pouvez dans un terminal en allant dans le dossier qui vous intéresse. 

```bash
cd partie1
python modelisation.py
```

