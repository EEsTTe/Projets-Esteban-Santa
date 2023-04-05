from random import *

col1 = 6
col2 = 6
col3 = 6
col4 = 6
col5 = 6
col6 = 6
col7 = 6
#Cette variable nous permet de savoir c'est a quel joueur de jouer, si elle est paire, c'est au joueur 1 de jouer, si elle est impaire c est au joueur 2
joueur = 1
#Temps que cette variable est égale à 0 la partie continue
fin_de_partie = 0


#Cette liste est notre tableau de jeu, elle est donc vide à la base
L = [[".",".",".",".",".","."],
[".",".",".",".",".","."],
[".",".",".",".",".","."],
[".",".",".",".",".","."],
[".",".",".",".",".","."],
[".",".",".",".",".","."],
[".",".",".",".",".","."]]
#Liste pour faire la verif d'une victoire
victoire_j1=["0","0","0","0"]

victoire_j2=["X","X","X","X"]

#on affiche le menu de choix
def menu():
    print("Bonjour " )
    print("*****Menu*****")
    print("1 - Nouvelle Partie")
    print("2 - Changer les pseudo")
    choix=int(input("Choisissez un menu"))
    
    #on demande d'abord au joueur si il veut jouer contre un autre joueur ou contre un robot
    if choix==1:
        print("****************")
        mode_de_jeu = int(input("mode de jeu:" + "\n" + "1) 1v1" + "\n" + "2) contre bot" + "\n"))
        if mode_de_jeu == 2:
            mode_contre_bot = int(input("niveau de difficulter: " + "\n" + "1) facile" + "\n" + "2) Moyen" + "\n" + "3) difficile" + "\n"))
    #Si le joueur à décidé de jouer contre un robot, on lui demande le niveau de dificulté qu il veut
    
    if choix==2:
        print("****************")
        Joueur1=str(input("Choisissez votre pseudo joueur 1"))
        Joueur2=str(input("Choisissez votre pseudo joueur 2"))
        print("Pseudo changé !")
        print(Joueur1)
        print(Joueur2)
        
    while choix!=1:
        return menu()
        
def mode(mode_de_jeu):
    if mode_de_jeu == 1:
        return pvp(menu,verif_la_verif_colonne,verif_la_verif_ligne_droite,verif_la_verif_ligne_gauche)
    elif mode_de_jeu == 2:
        return bot_1


def victoire(mode_de_jeu,L_verif,victoire_j1,victoire_j2,fin_de_partie,menu):
    """cette fonction verifie si un joueur a gagne.
    Parametre requis:
    -mode_de_jeu pour varier les msg de victoire en fonction du mode jeu
    -L_verif pour verifier la victoire ou non d'un joueur
    -les liste de verif d'une victoire de joueur (victoire_j1,victoire_j2)
    -fin_de_partie pour pouvoir mettre fin a la partie lorsqu'un joueur gagne"""
    if mode_de_jeu==1:

        if L_verif==victoire_j1:
            print ("Bravo ",Joueur1, " vous avez gagné!")
            fin_de_partie = 1

        if (L_verif==victoire_j2):
            print ("Bravo ",Joueur2, " vous avez gagné!")
            fin_de_partie = 1

    elif (mode_de_jeu==2):

        if L_verif==victoire_j1:
            print ("Bravo ",Joueur1, " vous avez gagné!")
            fin_de_partie = 1

        if (L_verif==victoire_j2):
            print ("La machine surpasse l'homme apparemment :)")
            fin_de_partie = 1

def verif_la_verif_ligne_gauche(a,colonne_num,victoire_j1,victoire_j2,fin_de_partie,mode_de_jeu,L):
    """elle verif si une verification est necessaire en ligne a gauche + si le joueur qui a joue gagne ou non.
    Parametre requis:
    -a pour connaitre la ligne sur laquelle le joueur a joue
    -colonne_num pour connaitre la colonne dans la laquelle le joueur a joue
    -les liste de verif d'une victoire de joueur (victoire_j1,victoire_j2)
    -fin_de_partie pour arreter la partie
    -mode_de_jeu pour savoir dans quel mode la joueur joue et donc varier les msg de victoire
    -et L (la grille de jeu) pour faire la verif """
    L_verif=[]

    if colonne_num==3 or colonne_num ==4 or colonne_num ==5 or colonne_num ==6:
    #alors calculer vers la gauche

        for i in range(0,4):

            L_verif.append(L[colonne_num-i][a])
            victoire(mode_de_jeu,L_verif,victoire_j1,victoire_j2,fin_de_partie)
        L_verif=[]

    if colonne_num==2 or colonne_num==3 or colonne_num==4 or colonne_num==5:

        for i in range(-1,3):

            L_verif.append(L[colonne_num-i][a])
            victoire(mode_de_jeu,L_verif,victoire_j1,victoire_j2,fin_de_partie)
        L_verif=[]



def verif_la_verif_ligne_droite(a,colonne_num,victoire_j1,victoire_j2,fin_de_partie,mode_de_jeu,L):
    """elle verif si une verification est necessaire en ligne a droite + si le joueur qui a joue gagne ou non.
    Parametre requis:
    -a pour connaitre la ligne sur laquelle le joueur a joue
    -colonne_num pour connaitre la colonne dans la laquelle le joueur a joue
    -les liste de verif d'une victoire de joueur (victoire_j1,victoire_j2)
    -fin_de_partie pour arreter la partie
    -mode_de_jeu pour savoir dans quel mode la joueur joue et donc varier les msg de victoire
    -et L (la grille de jeu) pour faire la verif """
    L_verif=[]

    if colonne_num == 0 or colonne_num ==1 or colonne_num ==2 or colonne_num ==3:
    #alors calculer vers la droite

        for i in range(0,4):

            L_verif.append(L[colonne_num+i][a])
            victoire(mode_de_jeu,L_verif,victoire_j1,victoire_j2,fin_de_partie)
        L_verif=[]

    if colonne_num==1 or colonne_num==2 or colonne_num==3 or colonne_num==4:

        for i in range(-1,3):

            L_verif.append(L[colonne_num+i][a])
            victoire(mode_de_jeu,L_verif,victoire_j1,victoire_j2,fin_de_partie)
        L_verif=[]

def verif_la_verif_colonne(a,colonne_num,mode_de_jeu,victoire_j1,victoire_j2,fin_de_partie,L):
    """elle verif si une verification est necessaire en ligne. Parametre requis:
    -a pour connaitre la ligne sur laquelle le joueur a joue
    -colonne_num pour connaitre la colonne dans la laquelle le joueur a joue
    -mode_de_jeu pour varier les msg de victoire en fonction du mode jeu
    -les liste de verif d'une victoire de joueur (victoire_j1,victoire_j2)
    -fin_de_partie pour pouvoir mettre fin a la partie lorsqu'un joueur gagne
    -et L (la grille de jeu) pour faire la verif """
    L_verif=[]
    if a <3:
    #alors calcule vers le bas
        for i in range(4):
            L_verif.append(L[colonne_num][a+i])
            victoire(mode_de_jeu,L_verif,victoire_j1,victoire_j2,fin_de_partie)
        L_verif=[]


def  affichage():
    """Cette fonction ne prend pas de paramêtre en entrer et elle renvoie:
    - Le tableau de jeu au cour de la partie"""
    #on renvoie d'abord les numeros au dessus des colonne du tableau
    print("1/2/3/4/5/6/7")
    #on rnevoie ensuite les 6 lignes du tableau
    for i in range(6):
        print (L[0][i],L[1][i],L[2][i],L[3][i],L[4][i],L[5][i],L[6][i])



def chang(a):
    """Cette fonction prend en paramêtre un nombre comprit entre 0 et 6 et:
    - Modifie l'élément de "L" demandé en fonction du joueur"""
    #si c'est au joueur 1 de jouer, la liste va être modifiée par un "0"
    if joueur%2 == 0:
        L[colonne_num][a] = "0"
    #si c'est au joueur 2 de jouer, la liste va être modifiée par un "X"
    if joueur%2 != 0:
        L[colonne_num][a] = "X"


#On affiche une première fois le tableau vide
menu()
affichage()
mode(menu)

## Mode de jeu contre bot
def bot_1(verif_la_verif_colonne,verif_la_verif_ligne_droite,verif_la_verif_ligne_gauche,menu):
    if mode_de_jeu == 2 and mode_contre_bot == 1:
        while fin_de_partie == 0:
            joueur += 1
    
            if joueur%2 == 0:
                colonne_num = int(input("Joueur 1 c'est à toi : "))-1
    
            if joueur % 2 != 0:
                print("c'est au tour du bot")
                colonne_num = randint(0, 6)
    
    
            # assert colonne_num > 0 or colonne_num < 8, "nombre trop grand choisi"
            if colonne_num < 0 or colonne_num > 6:
                print("nombre trop grand")
                joueur -= 1
    
            if colonne_num == 0:
                col1 = col1 - 1
                a = col1
                chang(a)
                affichage()
                if col1 < 0:
                    print("impossible rejoue")
                    joueur-= 1
    
    
            if colonne_num == 1:
                col2 -= 1
                a = col2
                chang(a)
                affichage()
                if col2 < 0:
                    print("impossible rejoue")
                    joueur-= 1
    
    
            if colonne_num == 2:
                col3 -= 1
                a = col3
                chang(a)
                affichage()
                if col3 < 0:
                    print("impossible rejoue")
                    joueur-= 1
    
    
            if colonne_num == 3:
                col4 -= 1
                a = col4
                chang(a)
                affichage()
                if col4 < 0:
                    print("impossible rejoue")
                    joueur-= 1
    
    
            if colonne_num == 4:
                col5 -= 1
                a = col5
                chang(a)
                affichage()
                if col5 < 0:
                    print("impossible rejoue")
                    joueur-= 1
    
    
            if colonne_num == 5:
                col6 -= 1
                a = col6
                chang(a)
                affichage()
                if col6 < 0:
                    print("impossible rejoue")
                    joueur-= 1
    
    
            if colonne_num == 6:
                col7 -= 1
                a = col7
                chang(a)
                affichage()
                if col7 < 0:
                    print("impossible rejoue")
                    joueur-= 1
    
            verif_la_verif_ligne_gauche(a,colonne_num,victoire_j1,victoire_j2,fin_de_partie,mode_de_jeu,L)
            if fin_de_partie != 1:
                verif_la_verif_ligne_droite(a,colonne_num,victoire_j1,victoire_j2,fin_de_partie,mode_de_jeu,L)
            
            verif_la_verif_colonne(a,colonne_num,mode_de_jeu,victoire_j1,victoire_j2,fin_de_partie,L)
    
            if col1 <= 0 and col2 <= 0 and col3 <= 0 and col4 <= 0 and col5 <= 0 and col6 <= 0 and col7 <= 0:
                print("égalité, fin de partie")
                fin_de_partie = 1

def bot_2(verif_la_verif_colonne,verif_la_verif_ligne_droite,verif_la_verif_ligne_gauche,menu):
    if mode_de_jeu == 2 and mode_contre_bot == 2:
        print("en dev")


## Mode de jeu 1v1


def pvp (menu,verif_la_verif_colonne,verif_la_verif_ligne_droite,verif_la_verif_ligne_gauche):
    while fin_de_partie == 0:
        joueur += 1

        if joueur%2 == 0:
            colonne_num = int(input(Joueur1," c'est à toi : "))-1

        if joueur % 2 != 0:
            colonne_num = int(input(Joueur2," c'est à toi : "))-1



        if colonne_num < 0 or colonne_num > 6:
            print("nombre trop grand")
            joueur -= 1



        if colonne_num == 0:
            col1 = col1 - 1
            a = col1
            chang(a)
            affichage()
            if col1 < 0:
                print("impossible rejoue")
                joueur-= 1


        if colonne_num == 1:
            col2 -= 1
            a = col2
            chang(a)
            affichage()
            if col2 < 0:
                print("impossible rejoue")
                joueur-= 1


        if colonne_num == 2:
            col3 -= 1
            a = col3
            chang(a)
            affichage()
            if col3 < 0:
                print("impossible rejoue")
                joueur-= 1


        if colonne_num == 3:
            col4 -= 1
            a = col4
            chang(a)
            affichage()
            if col4 < 0:
                print("impossible rejoue")
                joueur-= 1


        if colonne_num == 4:
            col5 -= 1
            a = col5
            chang(a)
            affichage()
            if col5 < 0:
                print("impossible rejoue")
                joueur-= 1


        if colonne_num == 5:
            col6 -= 1
            a = col6
            chang(a)
            affichage()
            if col6 < 0:
                print("impossible rejoue")
                joueur-= 1


        if colonne_num == 6:
            col7 -= 1
            a = col7
            chang(a)
            affichage()
            if col7 < 0:
                print("impossible rejoue")
                joueur-= 1


        verif_la_verif_ligne_gauche(a,colonne_num,victoire_j1,victoire_j2,fin_de_partie,mode_de_jeu,L)
        if fin_de_partie != 1:
            verif_la_verif_ligne_droite(a,colonne_num,victoire_j1,victoire_j2,fin_de_partie,mode_de_jeu,L)
        
        verif_la_verif_colonne(a,colonne_num,mode_de_jeu,victoire_j1,victoire_j2,fin_de_partie,L)


        if col1 <= 0 and col2 <= 0 and col3 <= 0 and col4 <= 0 and col5 <= 0 and col6 <= 0 and col7 <= 0:
            print("égalité, fin de partie")
            fin_de_partie = 1