"""
   FICHIER MENU_CREDITS.PY :
       - FONCTION credit

   DERNIÈRE MÀJ : 11/07/2016
   CRÉÉ PAR JORIS COULANGE POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :
   
---------------------------------------------------------------
"""

# RESSOURCES EXTERNES

from pygame.locals import *
from DEPENDANCES.sources.gestion_audio import *

# GESTION DU MENU CRÉDITS

def credit(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click):

    # CHARGEMENT DES IMAGES
    
    fond_credits = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/menu_credits.jpg").convert()
    
    titre_credits = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/titre_credits.png").convert()

    les_credits = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/les_credits.png").convert()
            
    bouton_retour_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_retour_ok.gif").convert()
    
    bouton_retour = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_retour.gif").convert()
    
    # CONSTANTES DE POSITIONS DES IMAGES
    
    POSITION_TITRE_CREDITS = ((FENETRE_X / 2) - (titre_credits.get_width() / 2), 0)
    POSITION_LES_CREDITS = ((FENETRE_X / 2) - (les_credits.get_width() / 2), (FENETRE_Y * (3/4) * (1/3) - 30)) # car 2x plus gros qu'un bouton  
    POSITION_BOUTON_RETOUR = ((FENETRE_X / 2) - (bouton_retour.get_width() / 2), (FENETRE_Y * (3/4) * (3/3)))
    
    # AFFICHAGE DES IMAGES

    fenetre.blit(fond_credits, (0,0))
    fenetre.blit(titre_credits, POSITION_TITRE_CREDITS)
    fenetre.blit(les_credits, POSITION_LES_CREDITS)
    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)

    pygame.display.flip()

    # BOUCLE PRINCIPALE

    dessus_bouton = [False] # pour éviter la répétiton du bruit de passage au-dessus du bouton dès qu'on se déplace sur sa surface
    selectionner = False # pour vérifier qu'on relache bien le bouton de la souris quand on clique
    continuer = True
    while continuer:
        for event in pygame.event.get():
        
            # ÉVÉNEMENT DE FERMETURE
            if event.type == QUIT:
                continuer = False
                pygame.mixer.music.fadeout(500)
                pygame.mixer.fadeout(500)
                pygame.display.quit()
                pygame.quit()
                sys.exit()
           
            # AFFICHAGE DES IMAGES
            fenetre.blit(fond_credits, (0,0))
            fenetre.blit(titre_credits, POSITION_TITRE_CREDITS)
            fenetre.blit(les_credits, POSITION_LES_CREDITS)
            
            # ÉVÉNEMENTS DE POSITION ET DE CLIQUE
            
            # RETOUR ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_RETOUR[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_RETOUR[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_RETOUR[POSITION_Y] + bouton_retour.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_RETOUR[POSITION_X] + bouton_retour.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_retour_ok, POSITION_BOUTON_RETOUR)
                # GESTION AUDIO
                if not dessus_bouton[0]:
                    jouer_son(son_slide)
                    dessus_bouton[0] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    continuer = False
            else:
                fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
                dessus_bouton[0] = False
                
            pygame.display.flip()

            if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE:
                selectionner = False
