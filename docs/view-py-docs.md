# Documentation de la structure de views.py

## But du programme

Ce programme a pour but de visualiser les données générées par le programme `tvideos.py` dans une fentre graphique.

## Bibliothèques utilisées

- `tkinter.ttk` : utilisée pour créer des widgets stylisés.
- `sqlite3` : utilisée pour gérer des bases de données SQLite.
- `customtkinter` : utilisée pour créer des widgets personnalisés.

## classes définies


### Classe `FourChoiceFrame`

Cette classe est utilisée pour créer un widget personnalisé qui affiche quatre choix de réponse.

### Classe `App`

Cette classe est utilisée pour créer une fenêtre graphique qui affiche les données générées par le programme `tvideos.py`.


## utilisation de la classe `FourChoiceFrame`

### Méthode `__init__()`

-on exécute la méthode `super().__init__()` pour appeler le constructeur de la classe mère `CTkFrame`

-on crée un widget `radio` pour enregistrer la réponse de l'utilisateur
- on definit une police de caractère pour le titre
- on crée un widget `label` pour afficher le titre
- on crée un dictonnaire `table_choices` pour associer les choix de réponse à leur valeur
- dans une boucle on crée les choix de réponse et on les place dans le widget `radio`

## utilisation de la classe `App`

on crée une constante `table` pour associer les widgets aux table de la base de données

### Méthode `__init__()`

-on exécute la méthode `super().__init__()` pour appeler le constructeur de la classe mère `CTkFrame`
- on crée la fenêtre graphique


### Méthode `submit()`




