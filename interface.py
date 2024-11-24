import pygame
import math
import random
import time

FENETRE_LARGEUR = 1024
FENETRE_HAUTEUR = 512

pygame.init()

screen = pygame.display.set_mode((FENETRE_LARGEUR, FENETRE_HAUTEUR))

running = True

boule_rouge=pygame.image.load("boule rouge.png").convert()
boule_bleu=pygame.image.load("boule bleu.png").convert()
boule_verte=pygame.image.load("boule verte.png").convert()
boule_jaune=pygame.image.load("boule jaune.png").convert()
fiole=pygame.image.load("fiole.png").convert()

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