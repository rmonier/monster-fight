"""
   FICHIER MENU_JOUER.PY :
       - FONCTION jouer
       
   DERNIÈRE MÀJ : 11/07/2016
   CRÉÉ PAR ROMAIN MONIER ET JORIS COULANGE POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :

---------------------------------------------------------------
"""

# RESSOURCES EXTERNES

from pygame.locals import *
from DEPENDANCES.sources.gestion_audio import *
from DEPENDANCES.sources.menu_selection import *

# GESTION DU MENU JOUER

def jouer(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click):

    # CHARGEMENT DES IMAGES
    
    fond_jouer = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/menu_jouer.png").convert()
    
    titre_jouer = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/titre_jouer.png").convert()

    bouton_creation_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_creation_ok.gif").convert()
    
    bouton_creation = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_creation.gif").convert()
            
    bouton_selection_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_selection_ok.gif").convert()
    
    bouton_selection = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_selection.gif").convert()
            
    bouton_retour_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_retour_ok.gif").convert()
    
    bouton_retour = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_retour.gif").convert()
    
    # CONSTANTES DE POSITIONS DES IMAGES
    
    POSITION_TITRE_JOUER = ((FENETRE_X / 2) - (titre_jouer.get_width() / 2), 0)
    POSITION_BOUTON_SELECTION = ((FENETRE_X / 2) - (bouton_creation.get_width() / 2), (FENETRE_Y * (3/4) * (1/3)))
    POSITION_BOUTON_CREATION = ((FENETRE_X / 2) - (bouton_selection.get_width() / 2), (FENETRE_Y * (3/4) * (2/3)))
    POSITION_BOUTON_RETOUR = ((FENETRE_X / 2) - (bouton_retour.get_width() / 2), (FENETRE_Y * (3/4) * (3/3)))
    
    # AFFICHAGE DES IMAGES

    fenetre.blit(fond_jouer, (0,0))
    fenetre.blit(titre_jouer, POSITION_TITRE_JOUER)
    fenetre.blit(bouton_creation, POSITION_BOUTON_CREATION)
    fenetre.blit(bouton_selection, POSITION_BOUTON_SELECTION)
    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)

    pygame.display.flip()

    # BOUCLE PRINCIPALE

    dessus_bouton = [False, False, False] # pour éviter la répétiton du bruit de passage au-dessus du bouton dès qu'on se déplace sur sa surface
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
            fenetre.blit(fond_jouer, (0,0))
            fenetre.blit(titre_jouer, POSITION_TITRE_JOUER)

            # ÉVÉNEMENTS DE POSITION ET DE CLIQUE
                
            # SÉLÉCTIONNER ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_SELECTION[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_SELECTION[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_SELECTION[POSITION_Y] + bouton_selection.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_SELECTION[POSITION_X] + bouton_selection.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_selection_ok, POSITION_BOUTON_SELECTION)
                # GESTION AUDIO
                if not dessus_bouton[0]:
                    jouer_son(son_slide)
                    dessus_bouton[0] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    selection(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click)
                    # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                    selectionner = False
                    fenetre.blit(fond_jouer, (0,0))
                    fenetre.blit(titre_jouer, POSITION_TITRE_JOUER)
                    fenetre.blit(bouton_creation, POSITION_BOUTON_CREATION)
                    fenetre.blit(bouton_selection, POSITION_BOUTON_SELECTION)
                    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
            else:
                fenetre.blit(bouton_selection, POSITION_BOUTON_SELECTION)
                dessus_bouton[0] = False
        
            # CRÉER -----------------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_CREATION[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_CREATION[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_CREATION[POSITION_Y] + bouton_creation.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_CREATION[POSITION_X] + bouton_creation.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_creation_ok, POSITION_BOUTON_CREATION)
                # GESTION AUDIO
                if not dessus_bouton[1]:
                    jouer_son(son_slide)
                    dessus_bouton[1] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    print("CRÉER")
                    # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                    selectionner = False
                    fenetre.blit(fond_jouer, (0,0))
                    fenetre.blit(titre_jouer, POSITION_TITRE_JOUER)
                    fenetre.blit(bouton_creation, POSITION_BOUTON_CREATION)
                    fenetre.blit(bouton_selection, POSITION_BOUTON_SELECTION)
                    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
            else:
                fenetre.blit(bouton_creation, POSITION_BOUTON_CREATION)
                dessus_bouton[1] = False
                
            # RETOUR ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_RETOUR[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_RETOUR[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_RETOUR[POSITION_Y] + bouton_retour.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_RETOUR[POSITION_X] + bouton_retour.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_retour_ok, POSITION_BOUTON_RETOUR)
                # GESTION AUDIO
                if not dessus_bouton[2]:
                    jouer_son(son_slide)
                    dessus_bouton[2] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    continuer = False
            else:
                fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
                dessus_bouton[2] = False
                
            pygame.display.flip()

            if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE:
                selectionner = False
