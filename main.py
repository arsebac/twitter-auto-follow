from Navigateur import Navigateur
from Configuration import Configuration

comptes_twitter = Configuration.liste_des_compte_twitter()
comptes_a_follow = Configuration.liste_des_comptes_a_follow()
nb_compte_a_follow = str(len(comptes_a_follow))
print("Lancement du script avec " + str(len(comptes_twitter)) + " comptes twitter")
for compte_twitter in comptes_twitter:
    navigateur = Navigateur()
    navigateur.demarrer()
    reussi = navigateur.connection_twitter(compte_twitter)
    if not reussi:
        continue  # on passe au prochain compte

    print("Connection réussi, on commence à follow les " + nb_compte_a_follow + " comptes a follow")

    for compte_a_follow in comptes_a_follow:
        print("Follow ", compte_a_follow)
        navigateur.follow(compte_a_follow)
