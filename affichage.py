import pygame
from random import *
from pygame.locals import *
from time import *

pygame.init()


class Jeu:

    def __init__(self,x,y):
        self.fenetre = pygame.display.set_mode([x,y])
        self.larg = x
        self.haut = y
        self.nom_fenetre = pygame.display.set_caption("puissance4")
        self.pos = pygame.mouse.get_pos()
        
        self.musique_victoire = pygame.mixer.Sound("win.mp3")
        self.son_clic = pygame.mixer.Sound("clic.mp3")
        
        
        
        self.police = pygame.font.SysFont("Arial",75)
        self.petite_police = pygame.font.SysFont("Arial",35)
        
       
        
        self.menu = True
        self.partie =True

        self.carre_choix = self.carre_choix()
        
        
    
    def carre_choix(self):
        carre_choix = {}
        x=450 + 25//2
        for i in range(7):
            carre_choix[str(i)] = pygame.Rect([x,800,100,100])
            x+= 125
        return carre_choix

        
    def affichage_nom(self,joueurs):
        nom_j = 0
        while True:
            """Cette fonction ne prend pas de paramètre et affiche les rectangles ou sont demander les noms des joueurs et le bouton et qui ammène au jeu"""
        
            self.fenetre.fill([28,41,57])
        
            # dessine le cadre du joueur 1 pour qu'il rentre son nom
            pygame.draw.rect(self.fenetre, ("yellow"),  pygame.Rect(300,150,500,100), 4,border_radius=10)
        
            # dessine le cadre du joueur 2 pour qu'il rentre son nom
            pygame.draw.rect(self.fenetre, ("red"),  pygame.Rect(300,550,500,100), 4,border_radius=10)
        
            # variable du nom du joueur 1
            nom_j1 = self.police.render(joueurs[1],True,("yellow"))
        
            # variable du nom du joueur 2
            nom_j2 = self.police.render(joueurs[2],True,("red"))
        
            # dessine nom joueur 1 au dessus du cadre pour le prénom du joueur 1
            place_nom_j1 = self.police.render("nom joueur 1",True,("yellow"))
            self.fenetre.blit(place_nom_j1,(300,50))
        
            # dessine nom joueur 2 au dessus du cadre pour le prénom du joueur 2
            place_nom_j2 = self.police.render("nom joueur 2",True,("red"))
            self.fenetre.blit(place_nom_j2,(300,450))
        
            # affiche l'écriture du nom du joueur 1 dans son cadre
            self.fenetre.blit(nom_j1,(325,150))
        
            # affiche l'écriture du nom du joueur 2 dans son cadre
            self.fenetre.blit(nom_j2,(325,550))
        
            # dessine le cadre du bouton jouer
            pygame.draw.rect(self.fenetre, ('blue'), pygame.Rect(740,750,250,100),5, border_radius=10)
            
            valide = self.police.render("Jouer",True,('blue'))
            
            rect_valide = valide.get_rect()
            rect_valide.center =(865,800)
            
            self.fenetre.blit(valide, rect_valide)    

            pygame.display.flip() 
            
            

            
                
            for event in pygame.event.get():
                # clic sur 'échap'
                if event.type == pygame.MOUSEBUTTONDOWN:
    
                 
                    if pygame.Rect(300,150,500,100).collidepoint(pygame.mouse.get_pos()):
        
                        nom_j = 1
                        self.son_clic.play()
        
                    if pygame.Rect(300,550,500,100).collidepoint(pygame.mouse.get_pos()):
        
                        nom_j = 2
                        self.son_clic.play()
        
                
        
            
                    if pygame.Rect(740,750,250,100).collidepoint(pygame.mouse.get_pos()) and len(joueurs[1])>=1 and len(joueurs[2])>=1:
                        self.son_clic.play()
                        return joueurs
                        
                     
                if event.type ==pygame.KEYDOWN:
                
                    # si un touche du clavier est appuyer et quelle est égale à la touche 'Retour arrière'
                    if event.key == pygame.K_BACKSPACE:

                        # on enlève le dernier caractère du nom
                        joueurs[nom_j] = joueurs[nom_j][:-1]

                    else:
                        joueurs[nom_j]+= event.unicode

                    if len(joueurs[nom_j])> 12:
                        joueurs[nom_j] = joueurs[nom_j][:-1]

                if event.type == pygame.QUIT:
    
                    pygame.quit()
                
    def affichage_difficulte(self):
        while True:
            self.fenetre.fill([28,41,57])
            self.fenetre.blit(self.police.render("Quelle difficulté?",True,("white")),(600,300))
            
            dif = [' facile','normal',' Victor']
            
            y = 500
            
            for e in dif:
                pygame.draw.rect(self.fenetre, ('red'),(700,y,200,100),4, border_radius=10)
                
                self.fenetre.blit(self.police.render(e,True,("white")), (710,y+10,500,100))
                
                y+= 150
                
            pygame.display.flip()
            
            for event in pygame.event.get():
              
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(700,500,200,100).collidepoint(pygame.mouse.get_pos()):
                        self.son_clic.play()
                        return 1
                        
                    
                    #Ce bloque permet de proposer de cliquer pour choisir le mode '1v1'
                    if pygame.Rect(700,650,200,100).collidepoint(pygame.mouse.get_pos()):
                        self.son_clic.play()
                        return 2
                        
                    if pygame.Rect(700,800,200,100).collidepoint(pygame.mouse.get_pos()):
                        self.son_clic.play()
                        return 3
        
            
                    
    
                if event.type == pygame.QUIT:
    
                    pygame.quit()
        
    
    
    def affichage_mode(self):
        while True:
            
            self.fenetre.fill([28,41,57])
    
            self.fenetre.blit(self.police.render("A quel mode voulez-vous jouer ?",True,("white")),(425,300))
    
            choix = "1v1"
            cadre = "cadre_oui"
            x = 450
            #création des 2 boutons
            for i in range(2):
    
                pygame.draw.rect(self.fenetre, ('red'),(x,700,200,100),4, border_radius=10)
                
                self.fenetre.blit(self.police.render(choix,True,("white")), (x+50,705,500,100))
    
                x += 500
                choix = "Bot"
                cadre = "cadre_non"
    
            pygame.display.flip()
            
         
       
            
            for event in pygame.event.get():
              
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(450,700,200,100).collidepoint(pygame.mouse.get_pos()):
                        self.son_clic.play()
                        return 1
                        
                    
                    #Ce bloque permet de proposer de cliquer pour choisir le mode '1v1'
                    if pygame.Rect(950,700,200,100).collidepoint(pygame.mouse.get_pos()):
                        self.son_clic.play()
                        return 2
                        
        
            
                    
    
                if event.type == pygame.QUIT:
    
                    pygame.quit()
        


    def affichage_partie(self,grille,nbr_victoire,j,joueur):
       
        while True:
            self.fenetre.fill([28,41,57])
            
            if j == 1:
                self.fenetre.blit(self.police.render("C'est à "+joueur[1],True,("yellow")),(10,100))
                
            elif j == 2:
                self.fenetre.blit(self.police.render("C'est à "+joueur[2],True,("red")),(10,100))
                
            
            
            x = 450
            pygame.draw.rect(self.fenetre,(0,0,150),(x,30,870,765), border_radius = 5)  # cadre jeu
            pygame.draw.rect(self.fenetre,("grey"),(x,30,875,765), 5, border_radius = 10)
    
            x += 25//2
            for i in range(7):
                pygame.draw.rect(self.fenetre,("white"),(x,820,100,130), 2, border_radius = 10) #case
                self.fenetre.blit(self.police.render(str(i+1),True,([249,19,19])),(x+30,845)) #chiffre dans case
    
                x +=125
            
            x =500+ 25//2
            y=725
            for i in range(6):

                for l in range(7):
                    if grille[i][l] == 2:
                        pygame.draw.circle(self.fenetre,([255,193,15]),(x,y),50)  #jeton jaune
                        pygame.draw.circle(self.fenetre,("grey"),(x,y),50, 3 )
    
                    elif grille[i][l] == 1:
                        pygame.draw.circle(self.fenetre,([249,19,19]),(x,y),50) #jeton rouge
                        pygame.draw.circle(self.fenetre,("grey"),(x,y),50, 3 )
    
                    else:
                        pygame.draw.circle(self.fenetre,("blue"),(x,y),50) #intérieur p4
                        pygame.draw.circle(self.fenetre,("grey"),(x,y),50, 3 )
                    
                    x += 125
                x=500+ 25//2
                y -=125
                
                
            pygame.draw.rect(self.fenetre,(0,0,150),(1400,30,300,400), border_radius = 5)  # cadre jeu
            pygame.draw.rect(self.fenetre,("grey"),(1400,30,300,400), 5, border_radius = 10)
            self.fenetre.blit(self.petite_police.render("Nombre de victoire :",True,("white")),(1420,70))
           
            y = 150
            for i in range(1,len(nbr_victoire)):
               
                self.fenetre.blit(self.petite_police.render(joueur[i] +" :"+ str(nbr_victoire[i]),True,("white")),(1450,y))
                y += 90
            
            
            
            
            pygame.display.flip()
            
            
    
            
            for event in pygame.event.get():
              
                if event.type == pygame.MOUSEBUTTONDOWN:
    
                   
                    for i in range(7):

                        if self.carre_choix[str(i)].collidepoint(pygame.mouse.get_pos()):
                            self.son_clic.play()
                
                            return i
                if event.type == pygame.QUIT:
    
                    pygame.quit()
                       
            
    def affichage_victoire(self,gagnant):
        self.musique_victoire.play()
        while True:
            
            pygame.draw.rect(self.fenetre,(28,41,57),(400,200,970,500), border_radius = 5)  # cadre jeu
            pygame.draw.rect(self.fenetre,("grey"),(400,200,970,500), 5, border_radius = 10)
            
            self.fenetre.blit(self.police.render(gagnant,True,("white")),(500,250))
            
            self.fenetre.blit(self.police.render("Voulez-vous rejouer?",True,("white")),(550,400))
    
            choix = "Oui"

            x = 500
            #création des 2 boutons
            for i in range(2):
    
                pygame.draw.rect(self.fenetre, ('red'),(x,550,200,100),4, border_radius=10)
                
                self.fenetre.blit(self.police.render(choix,True,("white")), (x+30,550,200,100))
    
                x += 500
                choix = "Non"

    
            pygame.display.flip()
            
            
            
            
            
            
            for event in pygame.event.get():
              
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(500,550,200,100).collidepoint(pygame.mouse.get_pos()):
        
                        return True
                    
                    #Ce bloque permet de proposer de cliquer pour choisir le mode '1v1'
                    if pygame.Rect(1000,550,200,100).collidepoint(pygame.mouse.get_pos()):
                        
                        return False
        
            
                    
    
                if event.type == pygame.QUIT:
    
                    pygame.quit()




    



