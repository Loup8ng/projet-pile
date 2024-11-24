import pygame
import math
import random
import time

pygame.init()

# affichage de la fenêtre

FENETRE_LARGEUR = 1024
FENETRE_HAUTEUR = 512

pygame.init()

screen = pygame.display.set_mode((FENETRE_LARGEUR, FENETRE_HAUTEUR))

running = True

boule_rouge=pygame.image.load("projet pile/boule rouge.png").convert()
boule_bleu=pygame.image.load("projet pile/boule bleu.png").convert()
boule_verte=pygame.image.load("projet pile/boule verte.png").convert()
boule_jaune=pygame.image.load("projet pile/boule jaune.png").convert()
fiole=pygame.image.load("projet pile/fiole.png").convert()

def dessin_fiole(nb_fioles):
    x=0
    for i in range(nb_fioles):
        
        x+=200
        screen.blit(fiole, (x, 150))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    dessin_fiole(4)
    pygame.display.flip()

# partie fonctionnement : 
class Pile ():
    def __init__(self):
        self.pile=[]

    def empiler(self,valeur):
        self.pile.append(valeur)

    def depiler(self):
        return self.pile.pop()

    def est_vide(self,valeur):
        return self.pile==[]
pile=Pile()

class Boules():
    
    def __init__(self):
        """
        définie le début de notre class
        """
        self.boules= self
    def couleur(self):
        """
        donne les couleurs pour un groupe de trois et en aléatoire. (et peut leurs donner une valeur pour la reconnaissance dans le programme).
        """
        li="R","V","B","J"
        return li[random.randint(0,3)]
boule=Boules()

class Fiole ():
    
    def __init__ (self):       
        """
        définie le début de notre class
        """
        self.fiole= Pile()
    

    def est_vide2(self):
        """
        vérifie si la fiole est vide
        """
        return self.fiole.est_vide
        
    def est_remplie(self):
        """
        vérifie si la fiole contient qqch 
        """
        if self.fiole.est_vide2==False:
            return True
fiole=Fiole()
  


def test_Fiole (): 
    print ("Test de la classe Fiole")
    assert fiole.est_remplie()
    assert fiole.est_vide2()
    assert fiole.__init__()

def test_tous(): 
    print("Test de toutes les fonctions")
    print(" ")

