# ---------------- Fichier python - Jeu du pendu - Emilien Morlet ---------------
## J'ai décidé de stocker les mots dans une liste que je change par la suite en chaîne de caractères pour l'affichage au joueur
## Car il est beaucoup plus facile d'utiliser les indices d'une liste dans ce cas la, mais nous aurions très bien pu
## utiliser directement des chaînes de caractères


import random

# Ouverture du fichier texte
with open("mots_pendu.txt", 'r') as f:
    # Lire le contenu du fichier
    contenu = f.readlines()


## Ici, on ouvre le fichier txt mots_pendu.txt et on place les lignes de celui-ci dans la variable contenu.

def choisir_mot(mots):
    return random.choice(mots)


# On choisit le mot aléatoire

def jeu_du_pendu():
    Nbre_chances = 6  ## Nombre de chances que l'on laisse à l'utilisateur
    mot_aleatoire = choisir_mot(contenu)
    # print(mot_aleatoire)                    ## Vous pouvez enlever ce commentaire pour connaître le mot choisi aléatoirement
    mot = ["- "] * (len(mot_aleatoire) - 1)
    lettres_deja_utilisee = ""  # Chaîne de caractère dans laquelle on va stocker les lettres déjà utilisées
    while Nbre_chances > 0:
        lettre = str(input("Choisissez une lettre : "))  ## L'utilisateur choisi une lettre
        if lettre in mot_aleatoire:
            if lettre not in lettres_deja_utilisee:  ## Si les 2 conditions précédentes sont validées, alors la lettre est dans le mot et pas déjà dit par le joueur
                indices_lettres = indice_lettre_dans_mot(lettre, mot_aleatoire)
                for i in indices_lettres:
                    mot[i] = lettre  ##Ici, on remplace la liste mot pour remplacer les tirets par la lettre trouvée
                print(f"Félicitations, cette lettre est bien dans le mot, il te reste {Nbre_chances}" ' tentatives')
                print(' '.join(mot))
                lettres_deja_utilisee += lettre  ## On ajoute la lettre trouvée dans la chaîne de caractère contenant toutes les lettres trouvées
            else:
                print(f"Tu as déjà utilisé cette lettre, il te reste {Nbre_chances}" ' tentatives')
        else:
            Nbre_chances = Nbre_chances - 1  ## Ici, la lettre indiquée n'est pas dans le mot, le joueur a donc une chance en moins
            print(f"La lettre indiquée n'est pas dans le mot, il te reste {Nbre_chances}" ' tentatives')
            print(' '.join(mot))  ## On change la liste en chaîne de caractères
        if mot_trouvé(mot) == True:
            print('Tu as trouvé le mot !!')
            return True
    print('Tu as perdu !')


def mot_trouvé(liste):
    for i in range(len(liste)):
        if liste[i] == "- ":
            return False
    return True


## Cette fonction permet de savoir si le mot a été trouvé en comptant le nombre de tirets restant dans le mot.


def indice_lettre_dans_mot(lettre, mot):
    indice = 0
    indices_lettre = []
    while indice < len(mot):
        if mot[indice] == lettre:
            indices_lettre.append(indice)
        indice += 1
    return indices_lettre


## Cette fonction permet de trouver l'indice de la lettre dans le mot


jeu_du_pendu()


