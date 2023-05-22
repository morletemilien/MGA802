# ---------------- Fichier python - Jeu du pendu - Emilien Morlet ---------------

import random

#Ouverture du fichier texte
with open ("mots_pendu.txt", 'r') as f:
# Lire le contenu du fichier
    contenu =f.readlines()

def choisir_mot(mots):
    return random.choice(mots)
# On choisit le mot aléatoire

def jeu_du_pendu():
    Nbre_chances = 6
    mot_aleatoire = choisir_mot(contenu)
    print(mot_aleatoire)
    mot = ["- "] *(len(mot_aleatoire)-1)
    lettres_deja_utilisee=""
    while Nbre_chances>0:
        lettre = str(input("Choisissez une lettre : "))
        if lettre in mot_aleatoire:
            if lettre not in lettres_deja_utilisee:
                indices_lettres=indice_lettre_dans_mot(lettre,mot_aleatoire)
                for i in indices_lettres:
                    mot[i]=lettre
                print(f"Félicitations, cette lettre est bien dans le mot, il te reste {Nbre_chances}" ' tentatives')
                print(' '.join(mot))
                lettres_deja_utilisee+=lettre
            else :
                print(f"Tu as déjà utilisé cette lettre, il te reste {Nbre_chances}" ' tentatives')
        else :
            Nbre_chances = Nbre_chances-1
            print(f"La lettre indiquée n'est pas dans le mot, il te reste {Nbre_chances}" ' tentatives')
            print(' '.join(mot))
        if mot_trouvé(mot) == True:
            print('Tu as trouvé le mot !!')
            return True
    print('Tu as perdu !')


def mot_trouvé(liste):
    for i in range(len(liste)):
        if liste[i]=="- ":
            return False
    return True


def indice_lettre_dans_mot(lettre,mot):
    indice=0
    indices_lettre=[]
    while indice<len(mot):
        if mot[indice]==lettre:
            indices_lettre.append(indice)
        indice+=1
    return indices_lettre

jeu_du_pendu()