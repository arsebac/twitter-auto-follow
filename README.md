# Twitter auto following

Script utilitaire pour gérer les follow et unfollow des comptes Twitter en simulant un navigateur


# Utilisation


## Installation des dépendances

````pip install -r requirements````

## Configuration des comptes a follow

La premiere étape est de configurer la liste des comptes dans le fichier `liste_de_compte_a_follow.txt`

Il faut mettre 1 compte par ligne, sans inclure le @

## Configuration de la liste des comptes Twitter a utiliser

Chaque compte doit etre configuré dans un fichier séparé. On peut copier coller le fichier `_exemple.json` pour avoir la structure : 

```
{
  "pseudo" : "elonmusk",
  "mdp": "fuckelon2022",
  "telOuEmail": "0601020405"
}
```

Le 'pseudo' et le 'mdp' sont obligatoire et ne sont pas enregistré. Le champ telOuEmail peut etre renseigné et utilisé si Twitter nous le demande

## Configuration de Google Chrome

- Google Chrome doit etre installé et en version 103 (Pour vérifier, ouvrir chrome, puis taper : chrome://settings/help )

- Si Google Chrome n'est pas version 103, il peut y avoir des crash et faut installer la version de Chromedriver adapté à sa version. 

- le fichier chromedriver.exe des version est dispobinle ici : https://chromedriver.chromium.org/downloads , la version windows (chromedriver_win32.zip) doit etre décompréssé et installé dans le dossier courant 

# Exécution du script

Sous windows : `py main.py`

Sous linux : `python main.py`