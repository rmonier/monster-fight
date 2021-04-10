"""
   FICHIER MENU.PY :
       - FONCTION lancer_menu
       - SCRIPT D'AFFICHAGE PRINCIPAL

   DERNIÈRE MÀJ : 11/07/2016
   CRÉÉ PAR ROMAIN MONIER ET JORIS COULANGE POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :
       - Finaliser les menus externes
---------------------------------------------------------------
"""

# RESSOURCES EXTERNES

from pygame.locals import *

from DEPENDANCES.sources.menu_jouer import *
from DEPENDANCES.sources.menu_options import *
from DEPENDANCES.sources.menu_credits import *
from DEPENDANCES.sources.gestion_options import *
from DEPENDANCES.sources.gestion_audio import *

def lancer_menu(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click):

    # CHARGEMENT DES IMAGES

    fond = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/menu.jpg").convert()

    titre = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/titre.gif").convert()

    bouton_jouer = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_jouer.gif").convert()

    bouton_options = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_options.gif").convert()

    bouton_credits = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_credits.gif").convert()

    bouton_quitter = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_quitter.gif").convert()

    bouton_jouer_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_jouer_ok.gif").convert()

    bouton_options_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_options_ok.gif").convert()

    bouton_credits_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_credits_ok.gif").convert()

    bouton_quitter_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_quitter_ok.gif").convert()

    # CONSTANTES DE POSITIONS DES IMAGES

    POSITION_TITRE = ((FENETRE_X / 2) - (titre.get_width() / 2), 0)
    POSITION_BOUTON_JOUER = ((FENETRE_X / 2) - (bouton_jouer.get_width() / 2), (FENETRE_Y * (4/5) * (1/4)) - 10)
    POSITION_BOUTON_OPTIONS = ((FENETRE_X / 2) - (bouton_options.get_width() / 2), (FENETRE_Y * (4/5) * (2/4)) - 10)
    POSITION_BOUTON_CREDITS = ((FENETRE_X / 2) - (bouton_credits.get_width() / 2), (FENETRE_Y * (4/5) * (3/4)) - 10)
    POSITION_BOUTON_QUITTER = ((FENETRE_X / 2) - (bouton_quitter.get_width() / 2), (FENETRE_Y * (4/5) * (4/4)) - 10)

    # AFFICHAGE DES IMAGES

    fenetre.blit(fond, (0,0))
    fenetre.blit(titre, POSITION_TITRE)
    fenetre.blit(bouton_jouer, POSITION_BOUTON_JOUER)
    fenetre.blit(bouton_options, POSITION_BOUTON_OPTIONS)
    fenetre.blit(bouton_credits, POSITION_BOUTON_CREDITS)
    fenetre.blit(bouton_quitter, POSITION_BOUTON_QUITTER)

    pygame.display.flip()

    # LANCEMENT DE LA MUSIQUE

    jouer_musique(pygame, -1)

    # BOUCLE PRINCIPALE

    dessus_bouton = [False, False, False, False] # pour éviter la répétiton du bruit de passage au-dessus du bouton dès qu'on se déplace sur sa surface
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
            fenetre.blit(fond, (0,0))
            fenetre.blit(titre, POSITION_TITRE)

            # ÉVÉNEMENTS DE POSITION ET DE CLIQUE
            
            # JOUER ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_JOUER[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_JOUER[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_JOUER[POSITION_Y] + bouton_jouer.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_JOUER[POSITION_X] + bouton_jouer.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_jouer_ok, POSITION_BOUTON_JOUER)
                # GESTION AUDIO
                if not dessus_bouton[0]:
                    jouer_son(son_slide)
                    dessus_bouton[0] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    jouer(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click)
                    # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                    selectionner = False
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(titre, POSITION_TITRE)
                    fenetre.blit(bouton_jouer, POSITION_BOUTON_JOUER)
                    fenetre.blit(bouton_options, POSITION_BOUTON_OPTIONS)
                    fenetre.blit(bouton_credits, POSITION_BOUTON_CREDITS)
                    fenetre.blit(bouton_quitter, POSITION_BOUTON_QUITTER)
                    
            else:
                fenetre.blit(bouton_jouer, POSITION_BOUTON_JOUER)
                dessus_bouton[0] = False
                
            # OPTIONS ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_OPTIONS[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_OPTIONS[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_OPTIONS[POSITION_Y] + bouton_options.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_OPTIONS[POSITION_X] + bouton_options.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_options_ok, POSITION_BOUTON_OPTIONS)
                # GESTION AUDIO
                if not dessus_bouton[1]:
                    jouer_son(son_slide)
                    dessus_bouton[1] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    options(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click)
                    # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                    selectionner = False
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(titre, POSITION_TITRE)
                    fenetre.blit(bouton_jouer, POSITION_BOUTON_JOUER)
                    fenetre.blit(bouton_options, POSITION_BOUTON_OPTIONS)
                    fenetre.blit(bouton_credits, POSITION_BOUTON_CREDITS)
                    fenetre.blit(bouton_quitter, POSITION_BOUTON_QUITTER)
            else:
                fenetre.blit(bouton_options, POSITION_BOUTON_OPTIONS)
                dessus_bouton[1] = False
                
            # CRÉDITS ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_CREDITS[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_CREDITS[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_CREDITS[POSITION_Y] + bouton_credits.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_CREDITS[POSITION_X] + bouton_credits.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_credits_ok, POSITION_BOUTON_CREDITS)
                # GESTION AUDIO
                if not dessus_bouton[2]:
                    jouer_son(son_slide)
                    dessus_bouton[2] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    credit(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click)
                    # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                    selectionner = False
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(titre, POSITION_TITRE)
                    fenetre.blit(bouton_jouer, POSITION_BOUTON_JOUER)
                    fenetre.blit(bouton_options, POSITION_BOUTON_OPTIONS)
                    fenetre.blit(bouton_credits, POSITION_BOUTON_CREDITS)
                    fenetre.blit(bouton_quitter, POSITION_BOUTON_QUITTER)
            else:
                fenetre.blit(bouton_credits, POSITION_BOUTON_CREDITS)
                dessus_bouton[2] = False
                
            # QUITTER ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_QUITTER[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_QUITTER[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_QUITTER[POSITION_Y] + bouton_quitter.get_height()) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_QUITTER[POSITION_X] + bouton_quitter.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_quitter_ok, POSITION_BOUTON_QUITTER)
                # GESTION AUDIO
                if not dessus_bouton[3]:
                    jouer_son(son_slide)
                    dessus_bouton[3] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    continuer = False
                    pygame.mixer.music.fadeout(500)
                    pygame.mixer.fadeout(500)
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
            else:
                fenetre.blit(bouton_quitter, POSITION_BOUTON_QUITTER)
                dessus_bouton[3] = False
                
            pygame.display.flip()

            if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE:
                selectionner = False

