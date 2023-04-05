## Projet  Awalée  /  Léna et Esteban  /  Version sans interface graphique

from random import *


def cles():
    """Cette fonction ne prend pas de parametre et renvoie une listes de tuples nommées contenant les valeurs de chaques trous ainsi que les deux greniers"""

    # Liste de tuple nommé avec toutes les valeurs
    valeur={"trous_J1" : [4,4,4,4,4,4], "trous_J2": [4,4,4,4,4,4], "grenier_J1" : 0, "grenier_J2" : 0}

    return valeur


def plateau(valeur):
    """Cette fonction prend en paramètre une listes de tuple nommé avec toutes les information sur chaques trous et sur les greniers et affiche le plateau de jeu"""

    print("\nJ1   6 | 5 | 4 | 3 | 2 | 1    ",valeur['grenier_J1'])

    # permet d'afficher la ligne du joueur 1 avec les valeurs de chaques trous
    chaine = "     "
    for i in range(6):
        chaine += str(valeur["trous_J1"][-i-1]) + "   "
    print (chaine)

    print("")

    # permet d'afficher la ligne du joueur 2 avec les valeurs de chaques trous
    chaine = "     "
    for i in range(6):
        chaine += str(valeur["trous_J2"][i]) + "   "
    print(chaine)

    print("J2   1 | 2 | 3 | 4 | 5 | 6    ", valeur['grenier_J2'] , "\n")

    return


def action_joueur(joueur):
    '''Cette fonction prend en parametre un chiffre 1 ou 2 indiquant quel joueur est en train de jouer et demande le coup voulu'''

    print("C'est au tour du Joueur " + str(joueur))

    coup_jouer=int(input("Quel coup souhaitez-vous jouer (nombre entre 1 et 6) ? "))
    while coup_jouer > 6 or coup_jouer < 1:
        coup_jouer = int(input("Merci de mettre une case qui existe \n"))

    return coup_jouer




def jouer(valeur,colonne,joueur):

    """
    Cette fonction prend 3 parametres:
    - Valeur, une listes de tuple nommé avec toutes les information sur chaques trous et sur les greniers
    - Colonne, nombre entre 1 et 6 indiquant ou le joueur souhaite jouer
    - Joueur, chiffre 1 ou 2 indiquant quel joueur est en train de jouer
    Cette fonction permet de répartir les graines du trou choisi par le joueur dans tous le plateau dans le sens horaire. S'il y a plus de 11 graines à répartir, on saute la case sur laquelle on à pris les graines et on continue.
    """

    if joueur == 1:
        autrejoueur = 2
    else:
        autrejoueur = 1

    j = colonne
    # Verifie combien de points il y a à distribuer
    distribue=valeur["trous_J"+str(joueur)][colonne-1]

    # Répartie les points tant que l'on a pas tout distribué
    while distribue != 0:

        # Verifie dans quel case les points doivent etre placés
        if j < 6:
            if colonne-1 != j:
                valeur["trous_J"+str(joueur)][j] += 1
                distribue -= 1
            j += 1

        else:
            valeur["trous_J"+str(autrejoueur)][j-6] += 1
            j += 1
            distribue -= 1
        if j > 11:
            j = 0
        if j > 22:
            j = 0

    if j == 0:
        tombee = 6
        joueurtombe = autrejoueur
    elif j == 6 :
        tombee = 6
        joueurtombe=joueur
    elif j < 6:
        joueurtombe = joueur
        tombee = j
    else:
        joueurtombe = autrejoueur
        tombee = j-6

    # Met la valeur de la case de base à 0
    valeur["trous_J"+str(joueur)][colonne-1] = 0
    return valeur, tombee, joueurtombe



def capture(valeur, trou, joueur, joueurtombe):
    '''Cette fonction prend 3 paramètre
    valeur = une listes de tuple nommé avec toutes les information sur chaques trous et sur les greniers
    joueur = chiffre 1 ou 2 indiquant quel joueur est en train de jouer
    trou = chiffre entre 1 et 6, qui est l'indice de la dernière case sur laquelle on dépose des graines
    joueurtombe = chiffre 1 ou 2 qui indique si la dernière graine qui est déposée se situe dans un trou appartenant au joueurn 1 ou bien au joueur 2

    Cette fonction permet de capturer les graines présente dans la dernière case, Si la dernière graine qui est déposée dans un trou         de l’adversaire comportant déjà 2 ou 3 graines.
    Les graines capturées sont déposée dans le grenier du joueur et le trou est laissé vide.'''

    trou -= 1  #on enlève 1 pour avoir une valeur entre 1 et 5 et non entre 1 et 6
    test=1

    if joueur != joueurtombe: # permet d'éviter de valider des points si le trou appartient au même joueur

        while test == 1: #tant que test==1

            if joueur == 1:

                #si la valeur du trou est égale à 2 ou 3
                if valeur['trous_J2'][trou] == 2 or valeur['trous_J2'][trou] == 3:

                    #on ajoute le nombre de graine présente dans le trou dans le grenier de J1
                    valeur['grenier_J1'] = int(valeur['grenier_J1']) + int(valeur['trous_J2'][trou])

                    #on vide le trou
                    valeur['trous_J2'][trou] = 0

                    #permet d'éviter une erreur (out of range) et de finir la boucle
                    if trou == 0:
                        test = 0
                    #permet de tester le trou d'avant une fois les graines récupérer
                    else:
                        trou -= 1

                else:
                    #on sort de la boucle while
                    test = 0

            else:

                #si la valeur du trou est égale à 2 ou 3
                if valeur['trous_J1'][trou] == 2 or valeur['trous_J1'][trou] == 3:

                    #on ajoute le nombre de graine présente dans le trou dans le grenier de J2
                    valeur['grenier_J2'] = int(valeur['grenier_J2']) + int(valeur['trous_J1'][trou])
                    #on vide le trou
                    valeur['trous_J1'][trou] = 0

                    #permet d'éviter une erreur (out of range) et de finir la boucle
                    if trou == 0:
                        test = 0
                    #permet de tester le trou d'avant une fois les graines récupérer
                    else:
                        trou -= 1


                else:
                    #on sort de la boucle while
                    test = 0


def bot(valeur):
    '''Cette fonction prend en paramètre
    valeur = une listes de tuple nommé avec toutes les information sur chaques trous et sur les greniers

    et renvoie le coup souhaiter (nombre entre 1 et 6)

    Cette fonction permet de créer un bot, qui joue de manière intelligente à la place du joueur 2.
    Le bot jouera si possible un coup qui lui permet de récuperer le plus de graine possible, sinon il jouera de façon aléatoire.'''

    #Liste avec toutes les valeurs de chaques trous contenant 1 ou 2 graines
    Liste=[]

    boucle=[2,1]

    for p in boucle:

        #permet de tester les 6 trous
        for i in range(6):

            #si la valeur du trou est égale à 2 ou sinon 1
            if valeur['trous_J1'][i] == p:

                # on ajoute la valeur du trou dans la Liste
                Liste.append(i)


    for i in Liste:

        #test s'il est possible de récuperer les graines du trou i
        for p in range(6):
            if valeur['trous_J2'][p]-(5-p)==i+1:

                #renvoie le coup à jouer
                return(p+1)

    else:
        #s'il est impossible de récuperer des graines en face, on joue de façon aléatoire
        return(randint(1,6))


def jeu():
    '''Cette fonction initialise le jeu sans interface graphique à l'aide de toute les fonctions précédentes'''
    valeur = cles()
    joueur = randint(1,2)


    bot_joue=int(input("Voulez-vous jouer avec un bot ? (0 : non ou 1 : oui) "))

    #la boucle s'arrête lorsque la partie est fini
    while valeur['grenier_J1'] <= 24 and valeur['grenier_J2'] <= 24 and valeur['grenier_J1'] + valeur['grenier_J2'] != 48:

        plateau(valeur)



        if joueur==2:

            #s'il y a un bot, on le fait jouer à la place du joueur 2
            if bot_joue==1:
                coup=bot(valeur)
                print("Le bot a joué en ",coup)

            else:
                coup = action_joueur(joueur)

        else:
            coup=action_joueur(joueur)

        #joue le coup souhaiter par le joueur et change les valeurs des variables valeur, tombee et joueur_tombe
        valeur, tombee, joueurtombe = jouer(valeur, coup, joueur)

        #capture les graines présente dans la dernière case et éventuelements les cases précédentes et met à jour le grenier
        capture(valeur, tombee, joueur, joueurtombe)

        #si tous les trous d'un joueurs sont vide on ajoute les graines encore présente sur le plateau de jeu dans le grenier du joueur n'ayant plus de graine
        if valeur['trous_J1'] == [0 for i in range(6)]:
            for i in range(6): valeur['grenier_J2'] += valeur['trous_J2'][i]
        elif valeur['trous_J2'] == [0 for i in range(6)]:
            for i in range(6): valeur['grenier_J1'] += valeur['trous_J1'][i]

        #change de joueur
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1


    #Envoie un message si la partie est terminée qui indique quel joueur à gagné
    if valeur['grenier_J1']>=25:
        return "Le Joueur 1 a gagné !"

    elif valeur['grenier_J2']>=25:

        if bot_joue==1:
           return ("Le bot (joueur 2) a gagné !")
        else:
            return ("Le joueur 2 a gagné !")
    else:
        return ("Ce match se termine sur une égalité ! ")

    return valeur


Partie=int(input("Voulez-vous jouer à l'Awalée ? (1 : oui) "))
if Partie ==1:
    jeu()