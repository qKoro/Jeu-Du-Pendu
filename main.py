from getpass import getpass
from time import *

mot = getpass("Entrez votre mot\n")

liste = []
votre_liste = []

for x in mot:
    liste.append(x)
    votre_liste.append('*')

print("".join(votre_liste))

nb_erreur = 0
while nb_erreur < 9 :
    lettre = input("Entrez votre lettre\n")

    if len(lettre)>1:
        if lettre == mot:
            print("Vous avez trouvé")
            sleep(3)
            break

    elif lettre in liste:
        for (index,x) in enumerate(liste):
            if x == lettre:
                votre_liste[index] = x
        v = "".join(votre_liste)
        print("Bonne lettre ",v)
    else:
        nb_erreur += 1
        print("Mauvaise lettre, il vous reste %s essais"%(9-nb_erreur))


if nb_erreur == 9:
    print("Vous avez perdu")
