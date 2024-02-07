# Indexeur Web Minimal
# Auteur : AOUACHRI OMAR

Ce projet consiste à créer un indexeur web minimal en utilisant des données extraites d'URLs au format JSON. L'objectif est de construire un index non positionnel des titres des pages web en les tokenisant et en calculant certaines statistiques sur les documents. En bonus, nous pouvons également appliquer un traitement de données plus avancé comme l'utilisation d'un stemmer et créer un index positionnel.

## Structure du Projet

- `main.py`: Ce fichier contient le code principal du projet. Il extrait les données des URLs au format JSON, construit l'index web, calcule les statistiques des documents et écrit les résultats dans des fichiers JSON.
- `Build_index.py`: Ce module contient les fonctions nécessaires pour construire l'index web et l'index avec traitement de données avancé.
- `Statistique.py`: Ce module contient la fonction pour calculer les statistiques des documents.
- `compare_stemmer.py`: Ce fichier contient une comparaison de plusieurs stemmers de NLTK sur des phrases de test.
- `requirements.txt`: Ce fichier contient la liste des dépendances Python nécessaires pour exécuter le projet.

## Exécution du Projet

1. git clone 
2. Installez les dépendances en exécutant la commande suivante dans votre terminal :

```
pip install -r requirements.txt
```
3. Supprimer tout les fichiers index_exemples.json et metadata.json parce que c'est l'execution du main qui va les générer.
3. Exécutez le script principal `main.py` 


4. Le script va extraire les données des URLs, construire l'index, calculer les statistiques des documents et écrire les résultats dans des fichiers JSON.

## Explications Additionnelles

- Les résultats seront écrits dans les fichiers `metadata.json`, `title.non_pos_index.json`, `mon_stemmer.title.non_pos_index.json`, et `title.pos_index.json`.

--- 

