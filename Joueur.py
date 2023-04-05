from Paquet import *
from Pile import *
from random import *

class Joueur :

    def __init__(self,nbr_de_jetons,nom):
        self.nom=nom
        self.jeton=nbr_de_jetons
        self.valeur_cartes=0

    def Affiche_info(self):
        print("Le joueur",self.nom,"en est à",self.valeur_cartes)

    def Banque(self):
        self.jeton=999999
        self.valeur_banque=0







def test():
    J1=Joueur(50,"J1")
    test=Paquet(4)
    for i in range(4):
        carte_pioche=test.pioche()
        J1.valeur_cartes= J1.valeur_cartes + carte_pioche
    J1.Affiche_info()


def test2():
    J1=Joueur(50,"J1")
    J1.Banque()
    return J1.valeur_banque , J1.jeton

