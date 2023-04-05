from random import *

import pygame
from pygame.locals import *
import affichage
from time import *
# Dans tout le projet, on s'attache à prendre des noms de variables de boucles "parlants" :
# c pour le numéro de colonne et l pour le numéro de ligne

# ATTENTION : pour le joueur, les colonnes vont de 1 à 7
# MAIS : dans la grille, les indices de colonnes vont de 0 à 6
# On convient donc dans chaque fonction d'utiliser les indices des colonnes
# Au programmeur du programme principal de bien passer des paramètres avec des numéros de colonnes décrémentés de 1

# Représentation des indices

# l\c : 0 1 2 3 4 5 6
# 5   :
# 4   :
# 3   :
# 2   :
# 1   :
# 0   :


class Grille:

    def __init__(self):
        # Tableau des noms des joueurs
        self.joueurs = ['bot', '', '']


        # Initialisations
        self.g = self.grille_vide()
        self.j = randint(1,2)
        print('Le tirage au sort a désigné ' + self.joueurs[self.j] + ' pour commencer...')

        self.aff = affichage.Jeu(1720,975)
        self.nbr_victoire = [0,0,0]
        
        self.mode = self.aff.affichage_mode()
        
        if self.mode == 1:
        
            self.joueurs = self.aff.affichage_nom(self.joueurs)
            
        else:
            self.difficulte = self.aff.affichage_difficulte()
            self.joueurs[1] = "Humain"
        

    ##
    
    
    def grille_vide(self):
        """Cette fonction renvoie une grille de puissance 4 modélisée de la façon suivante :
        - il s'agit d'une liste de 6 listes de 7 éléments
        - chaque liste de 7 éléments modélise une ligne de la grille-
        - la liste d'indice 0 modélise la ligne la plus en bas
        - l'élement de chaque liste d'indice 0 modélise la case la plus à gauche
        """
        return [[0 for c in range(7)] for l in range(6)]

    #
    ###
    #####
    ####################@
    #####
    ###
    #



    def coup_possible(self,c):
        """Renvoie True s'il reste une place dans la colonne c de la grille"""
        return self.g[5][c]==0

    #
    ###
    #####
    ####################@
    #####
    ###
    #

    def jouer(self,c):
        """Joue le coup c pour le joueur j dans la grille g
        On vérifie que ce coup est possible
        """
        assert self.coup_possible(c),"Ce coup est impossible : la colonne est remplie"
        l = 5
        # On décrémente l tant que la case de la ligne l est vide
        while((l >0) and (self.g[l-1][c] == 0)):
            l = l - 1
        # Ici l est la plus petite valeur pour laquelle la case de colonne c
        # et de ligne l est vide
        self.g[l][c] = self.j

    #
    ###
    #####
    ####################
    #####
    ###
    #


    def horiz(self,j,l,c):
        """Renvoie un booléen indiquant s'il y a un alignement horizontal pour le joueur j contenant la position (c,l)"""
        # Nombre de jetons de j consécutifs
        nbjetons = 0
        # Réponse à renvoyer :
        rep = False
        for col in range(max(0,c-3),min(7,c+4)):
            if (self.g[l][col]==j):
                # Un jeton identique de plus
                nbjetons = nbjetons + 1
            else:
                # On redémarre le comptage à 0
                nbjetons = 0
            if (nbjetons == 4):
                rep = True
        # S'il a rencontré au moins une fois 4 jetons j consécutifs, rep vaut True
        return rep

    #
    ###
    #####
    ####################@
    #####
    ###
    #

    def vertic(self,j,l,c):
        """Renvoie un booléen indiquant s'il y a un alignement vertical pour le joueur j contenant la position (c,l)"""
        # Nombre de jetons de j consécutifs
        nbjetons = 0
        # Réponse à renvoyer :
        rep = False
        for lig in range(max(0,l-3),min(6,l+4)):
            if (self.g[lig][c]==j):
                # Un jeton identique de plus
                nbjetons = nbjetons + 1
            else:
                # On redémarre le comptage à 0
                nbjetons = 0
            if (nbjetons == 4):
                rep = True
        # S'il a rencontré au moins une fois 4 jetons j consécutifs, rep vaut True
        return rep


    #
    ###
    #####
    ####################@
    #####
    ###
    #


    def diag(self,j,l,c):
        """Renvoie un booléen indiquant s'il y a un alignement diagonal pour le joueur j contenant la position (c,l)"""
        ## Diagonale NO-SE ( \ )
        # Nombre de jetons de j consécutifs
        nbjetons = 0

        for i in range(-3,4):
            if ((c+i >= 0) and (l-i < 6) and (c+i <7) and (l-i >=0)):
                if (self.g[l-i][c+i] == j):
                    # Un jeton identique de plus
                    nbjetons = nbjetons + 1
                else:
                    # On redémarre le comptage à 0
                    nbjetons = 0
            if (nbjetons == 4):
                return True
        # S'il a rencontré au moins une fois 4 jetons j consécutifs, rep vaut True

        ## Diagonale NE-SO ( / )
        # Nombre de jetons de j consécutifs
        nbjetons = 0
        for i in range(-3,4):
            if ((c-i >= 0) and (l-i < 6) and (c-i <7) and (l-i >=0)):
                if (self.g[l-i][c-i] == j):
                    # Un jeton identique de plus
                    nbjetons = nbjetons + 1
                else:
                    # On redémarre le comptage à 0
                    nbjetons = 0
            if (nbjetons == 4):
                return True
        # S'il a rencontré au moins une fois 4 jetons j consécutifs, rep vaut True
        return False


    def victoire(self,j):
        """Renvoie True si le joueur j a un alignement de 4 jetons dans la grille g"""
        # Il y a beaucoup plus optimal :
        # Un alignement horiz/diag passe forcemment par un jeton de la colonne centrale
        # Un alignement vertical passe forcemment par un jeton de la ligne 3 par ex.
        for l in range(6):
            for c in range(7):
                if (self.horiz(j,l,c) or self.vertic(j,l,c) or self.diag(j,l,c)) :
                    return True
        return False

    def partie_nulle(self):
        """Renvoie True si la partie est finie et qu'il n'y a pas de gagnant"""
        casesvides = 0
        for l in range(6):
            for c in range(7):
                if (self.g[l][c] == 0):
                    casesvides = casesvides + 1
        if ((casesvides == 0) and (not self.victoire(1)) and (not self.victoire(2))):
            return True
        else:
            return False





    def partie_a_deux(self):
        """Cette méthode lance une partie à deux joueurs"""
        partie = True
        while partie:

            # On débute la partie, et on joue jusqu'à un vainqueur ou une partie nulle :
            while not (self.partie_nulle() or self.victoire(1) or self.victoire(2)) :
    
        
                
                col = self.aff.affichage_partie(self.g,self.nbr_victoire, self.j,self.joueurs)+1
                # On vérifie que la saisie est correcte et possible :
                # Attention les indices des colonnes dans les fonctions vont de 0 à 6
    
                if (not self.coup_possible(col-1)):
                    print('ce coup est impossible ! La colonne est remplie')
                    col = 0
    
                print(self.j,col)
    
                # On joue le coup :
                
                
    
                # Changement de joueur :
                print(self.g)
                print(col)
                
                self.j = self.j + 1
                if (self.j == 3):
                    self.j = 1
        
                
                self.jouer(col-1)
            
            
            
            if self.partie_nulle():
                gagnant = "Partie nulle (à chier)"
            elif self.victoire(1):
                gagnant = self.joueurs[2]+" a gagné"
                self.nbr_victoire[2]+= 1
            else:
                gagnant = self.joueurs[1]+" a gagné"
                self.nbr_victoire[1]+= 1
            
            rejouer = self.aff.affichage_victoire(gagnant)
            
            if rejouer == False:
                pygame.quit()
                partie = False
                
            else:
                self.g = self.grille_vide()
                
                
    def contre_bot(self):
        pygame.quit()


son_jeu = pygame.mixer.Sound("main_music.mp3")
son_jeu.play(10)
jeu = Grille()



if jeu.mode == 1:
    jeu.partie_a_deux()
    
else:
    jeu.contre_bot()
    
