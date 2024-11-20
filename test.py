import pygame
import math
import random

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






def affichage (nb_fioles=4,nb_boules=3): 
    b=[]
    for i in range (nb_fioles):
        print(b)
        b=[] 
        for j in range (nb_boules):
            b.append(boule.couleur())
    return b
    
    
def test_Fiole (): 
    print ("Test de la classe Fiole")
    assert Fiole.est_remplie()
    assert Fiole.est_vide2()
    assert Fiole.__init__()

def test_tous(): 
    print("test de toutes les fonctions")
    assert test_Fiole()
    assert affichage()  




a=affichage()
