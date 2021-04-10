"""
   FICHIER GESTION_AUDIO.PY :
       - FONCTION jouer_son
       - FONCTION jouer_musique

   DERNIÈRE MÀJ : 16/04/2016
   CRÉÉ PAR ROMAIN MONIER POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :
   
---------------------------------------------------------------
"""

# RESSOURCES EXTERNES

from pygame.locals import *
from DEPENDANCES.sources.gestion_options import *

# FONCTIONS AUDIO

def jouer_son(son):
    if(lire_options()["son"]):
        son.play()

def jouer_musique(pygame, rep):
    if(lire_options()["musique"]):
        pygame.mixer.music.play(rep)
