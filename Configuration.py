import json
import os
class Configuration:
    """Récupère les informations depuis les fichiers à exécuter"""
    @staticmethod
    def liste_des_comptes_a_follow():
        with open('liste_de_compte_a_follow.txt') as fichier:
            liste = []
            for ligne in fichier:
                liste.append(ligne.strip())
            return liste
    """Récupère les informations des comptes à exécuter"""
    @staticmethod
    def liste_des_compte_twitter():
        comptes_twitter = []
        comptes = os.listdir("comptes")
        for compte in comptes:
            if compte == '_exemple.json':
                continue # On ignore l'exemple
            with open('comptes/' + compte) as fichier:
                compte_json = json.load(fichier)
                compte_json['fichier'] = os.getcwd() + '/comptes/' + compte
                comptes_twitter.append(compte_json) # On lit le fichier json
        return comptes_twitter
