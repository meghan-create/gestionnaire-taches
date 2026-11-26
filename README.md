# Gestionnaire de tâches (Python + JSON)

Petit programme en ligne de commande pour gérer une liste de tâches.
Les tâches sont enregistrées dans un fichier `taches.json`, elles sont donc conservées entre deux lancements.

## Fonctionnalités
- Afficher la liste des tâches
- Ajouter une tâche
- Marquer une tâche comme terminée
- Supprimer une tâche

## Lancer le programme
Python 3 doit être installé. Dans un terminal, depuis le dossier du projet :

```
python taches.py
```

## Ce que j'ai appris
- Lire et écrire un fichier JSON avec le module `json`
- Manipuler des listes et des dictionnaires en Python
- Découper un programme en fonctions
- Gérer les erreurs de saisie avec `try / except`

## Exemple de fichier `taches.json`
```json
[
  { "titre": "Réviser le cours de SQL", "terminee": true },
  { "titre": "Envoyer ma candidature", "terminee": false }
]
```
