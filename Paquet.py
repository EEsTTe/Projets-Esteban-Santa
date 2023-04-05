from Pile import *
from random import *
from Joueur import *

valeur=[2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi","as"]
couleur=["♥", "♦", "♣", "♠"]

class Paquet:
    def __init__(self,nbr):
        import random
        Liste_carte=valeur*4*nbr
        Longueur=52*nbr
        carte=randint(1,Longueur)
        paquet = Pile(52*nbr)


        for i in range(52*nbr):
            paquet.empile(Liste_carte[carte])
            carte=randint(1,Longueur) #1 ou 0
            Longueur=Longueur-1
        #paquet.affichePile() #a cacher
        self.paquet=paquet

    def pioche(self):
        Paquet=self.paquet
        Carte_pioche=Paquet.depile()

        if Carte_pioche == "valet" or Carte_pioche == "dame" or Carte_pioche == "roi" :
            print(Carte_pioche)
            Carte_pioche=10

        if Carte_pioche == "as":
            if self.valeur_cartes < 11:
                Carte_pioche=11
            else :
                Carte_pioche=1





        return Carte_pioche
        #print(Carte_pioche , couleur[randint(0,3)])"""








##
def test():
    test=Paquet(4)

def test1(nbr):
    import random
    Liste_carte=valeur*4*nbr
    Longueur=len(Liste_carte)
    return Liste_carte


def test():
    J1=Joueur(50,"J1")
    test=Paquet(4)
    for i in range(4):
        carte_pioche=test.pioche()
        J1.valeur_cartes= J1.valeur_cartes + carte_pioche
    J1.Affiche_info()


# A faire :
#-Commentaire + docstring

