"""
   FICHIER MONSTER FIGHT.PY :
       - FICHIER DE DÉMARRAGE / CHARGEMENT DU JEU

   DERNIÈRE MÀJ : 11/07/2016
   CRÉÉ PAR ROMAIN MONIER POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :
       
---------------------------------------------------------------
"""

# RESSOURCES EXTERNES

import sys
import pygame
from DEPENDANCES.sources.menu import *

# VÉRIFICATION CHEMIN
if getattr(sys, 'frozen', False):
    CHEMIN_DEPENDANCES = sys._MEIPASS + "/"
else:
    CHEMIN_DEPENDANCES = ""

# CONSTANTES PRINCIPALES

FENETRE_X = 800
FENETRE_Y = 440
POSITION_X = 0
POSITION_Y = 1
BOUTON_GAUCHE = 1

# INITIALISATION DE PYGAME

pygame.init()

pygame.display.set_caption("MONSTER FIGHT")
pygame.display.set_icon(pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/icone.ICO"))

fenetre = pygame.display.set_mode((FENETRE_X, FENETRE_Y))

# CHARGEMENT DES SONS

son_slide = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/slide.ogg")
son_click = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/click.ogg")

# CHARGEMENT DE LA MUSIQUE

pygame.mixer.music.load(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/musiques/home.wav")

# LANCEMENT DU MENU

lancer_menu(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click)
