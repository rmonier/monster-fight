"""
   FICHIER MENU_OPTIONS.PY :
       - FONCTION options
       - FONCTION fenetre_restaurer

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
from DEPENDANCES.sources.gestion_options import *
from DEPENDANCES.sources.gestion_audio import *
from DEPENDANCES.sources.restaurer_monstres import *

# FENÊTRE ALERTE RESTAURATION

def fenetre_restaurer(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click):

    # CHARGEMENT DES IMAGES
    
    fenetre_alerte = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/fenetre_restaurer.png").convert()
            
    bouton_oui = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_oui.gif").convert()
    
    bouton_oui_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_oui_ok.gif").convert()
    
    bouton_non_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_non_ok.gif").convert()
    
    bouton_non = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_non.gif").convert()
    
    # CONSTANTES DE POSITIONS DES IMAGES
    
    POSITION_FENETRE_ALERTE = ((FENETRE_X / 2) - (fenetre_alerte.get_width() / 2), (FENETRE_Y / 2) - (fenetre_alerte.get_height() / 2) + 30)
    POSITION_BOUTON_OUI = (FENETRE_X - (FENETRE_X / 4) - (bouton_oui.get_width() / 2) - 30, POSITION_FENETRE_ALERTE[POSITION_Y] + (fenetre_alerte.get_height() * (3/4)) + 5)
    POSITION_BOUTON_NON = ((FENETRE_X / 4) - (bouton_non.get_width() / 2) + 30, POSITION_FENETRE_ALERTE[POSITION_Y] + (fenetre_alerte.get_height() * (3/4)) + 5)
    
    # AFFICHAGE DES IMAGES

    fenetre.blit(fenetre_alerte, POSITION_FENETRE_ALERTE)
    fenetre.blit(bouton_oui, POSITION_BOUTON_OUI)
    fenetre.blit(bouton_non, POSITION_BOUTON_NON)

    pygame.display.flip()

    # BOUCLE PRINCIPALE

    dessus_bouton = [False, False] # pour éviter la répétiton du bruit de passage au-dessus du bouton dès qu'on se déplace sur sa surface
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
            fenetre.blit(fenetre_alerte, POSITION_FENETRE_ALERTE)
            
            # ÉVÉNEMENTS DE POSITION ET DE CLIQUE
            
            # OUI ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_OUI[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_OUI[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_OUI[POSITION_Y] + bouton_oui.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_OUI[POSITION_X] + bouton_oui.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_oui_ok, POSITION_BOUTON_OUI)
                # GESTION AUDIO
                if not dessus_bouton[0]:
                    jouer_son(son_slide)
                    dessus_bouton[0] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    if(restaurer_monstres(pygame)):
                        continuer = False
            else:
                fenetre.blit(bouton_oui, POSITION_BOUTON_OUI)
                dessus_bouton[0] = False
                
            # NON ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_NON[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_NON[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_NON[POSITION_Y] + bouton_non.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_NON[POSITION_X] + bouton_non.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_non_ok, POSITION_BOUTON_NON)
                # GESTION AUDIO
                if not dessus_bouton[1]:
                    jouer_son(son_slide)
                    dessus_bouton[1] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    continuer = False
            else:
                fenetre.blit(bouton_non, POSITION_BOUTON_NON)
                dessus_bouton[1] = False
                
            pygame.display.flip()

            if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE:
                selectionner = False

# GESTION DU MENU OPTIONS

def options(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click):

    # TESTS D'INITIALISATION

    son = lire_options()["son"]
    musique = lire_options()["musique"]

    # CHARGEMENT DES IMAGES
    
    fond_options = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/menu_options.jpg").convert()
    
    titre_options = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/titre_options.png").convert()

    if(son):
        bouton_son_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_son_on_ok.gif").convert()
        bouton_son = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_son_on.gif").convert()
    else:
        bouton_son_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_son_off_ok.gif").convert()
        bouton_son = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_son_off.gif").convert()
        
    if(musique):
        bouton_musique_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_musique_on_ok.gif").convert()
        bouton_musique = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_musique_on.gif").convert()
    else:
        bouton_musique_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_musique_off_ok.gif").convert()
        bouton_musique = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_musique_off.gif").convert()
        
    bouton_restaurer = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_restaurer.gif").convert()
    
    bouton_restaurer_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_restaurer_ok.gif").convert()
            
    bouton_retour_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_retour_ok.gif").convert()
    
    bouton_retour = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_retour.gif").convert()
    
    # CONSTANTES DE POSITIONS DES IMAGES
    
    POSITION_TITRE_OPTIONS = ((FENETRE_X / 2) - (titre_options.get_width() / 2), 0)
    POSITION_BOUTON_MUSIQUE = ((FENETRE_X / 2) - (bouton_musique.get_width() / 2), (FENETRE_Y * (4/5) * (1/4) - 10))
    POSITION_BOUTON_SON = ((FENETRE_X / 2) - (bouton_son.get_width() / 2), (FENETRE_Y * (4/5) * (2/4) - 10))
    POSITION_BOUTON_RESTAURER = ((FENETRE_X / 2) - (bouton_restaurer.get_width() / 2), (FENETRE_Y * (4/5) * (3/4) - 10))
    POSITION_BOUTON_RETOUR = ((FENETRE_X / 2) - (bouton_retour.get_width() / 2), (FENETRE_Y * (4/5) * (4/4) - 10))
    
    # AFFICHAGE DES IMAGES

    fenetre.blit(fond_options, (0,0))
    fenetre.blit(titre_options, POSITION_TITRE_OPTIONS)
    fenetre.blit(bouton_musique, POSITION_BOUTON_MUSIQUE)
    fenetre.blit(bouton_son, POSITION_BOUTON_SON)
    fenetre.blit(bouton_restaurer, POSITION_BOUTON_RESTAURER)
    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)

    pygame.display.flip()

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
            fenetre.blit(fond_options, (0,0))
            fenetre.blit(titre_options, POSITION_TITRE_OPTIONS)

            # ÉVÉNEMENTS DE POSITION ET DE CLIQUE
                
            # MUSIQUE ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_MUSIQUE[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_MUSIQUE[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_MUSIQUE[POSITION_Y] + bouton_musique.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_MUSIQUE[POSITION_X] + bouton_musique.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_musique_ok, POSITION_BOUTON_MUSIQUE)
                # GESTION AUDIO
                if not dessus_bouton[0]:
                    jouer_son(son_slide)
                    dessus_bouton[0] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    musique = not(musique)
                    sauver_options(son, musique)
                    if(musique):
                        jouer_musique(pygame, -1)
                        bouton_musique_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_musique_on_ok.gif").convert()
                        bouton_musique = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_musique_on.gif").convert()
                    else:
                        pygame.mixer.music.stop()
                        bouton_musique_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_musique_off_ok.gif").convert()
                        bouton_musique = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_musique_off.gif").convert()
                    # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                    selectionner = False
                    fenetre.blit(fond_options, (0,0))
                    fenetre.blit(titre_options, POSITION_TITRE_OPTIONS)
                    fenetre.blit(bouton_musique, POSITION_BOUTON_MUSIQUE)
                    fenetre.blit(bouton_son, POSITION_BOUTON_SON)
                    fenetre.blit(bouton_restaurer, POSITION_BOUTON_RESTAURER)
                    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
            else:
                fenetre.blit(bouton_musique, POSITION_BOUTON_MUSIQUE)
                dessus_bouton[0] = False
                
            # SON ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_SON[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_SON[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_SON[POSITION_Y] + bouton_son.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_SON[POSITION_X] + bouton_son.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_son_ok, POSITION_BOUTON_SON)
                # GESTION AUDIO
                if not dessus_bouton[1]:
                    jouer_son(son_slide)
                    dessus_bouton[1] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    son = not(son)
                    sauver_options(son, musique)
                    if(son):
                        jouer_son(son_click)
                        bouton_son_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_son_on_ok.gif").convert()
                        bouton_son = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_son_on.gif").convert()
                    else:
                        pygame.mixer.stop()
                        bouton_son_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_son_off_ok.gif").convert()
                        bouton_son = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_son_off.gif").convert()
                    # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                    selectionner = False
                    fenetre.blit(fond_options, (0,0))
                    fenetre.blit(titre_options, POSITION_TITRE_OPTIONS)
                    fenetre.blit(bouton_musique, POSITION_BOUTON_MUSIQUE)
                    fenetre.blit(bouton_son, POSITION_BOUTON_SON)
                    fenetre.blit(bouton_restaurer, POSITION_BOUTON_RESTAURER)
                    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
            else:
                fenetre.blit(bouton_son, POSITION_BOUTON_SON)
                dessus_bouton[1] = False
                
            # RESTAURER ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_RESTAURER[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_RESTAURER[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_RESTAURER[POSITION_Y] + bouton_restaurer.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_RESTAURER[POSITION_X] + bouton_restaurer.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_restaurer_ok, POSITION_BOUTON_RESTAURER)
                # GESTION AUDIO
                if not dessus_bouton[2]:
                    jouer_son(son_slide)
                    dessus_bouton[2] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR) # pour ne pas perturber l'affichage on raffiche retour ici, pour l'alerte fenetre possible a l'ecran suivant
                    fenetre_restaurer(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click)
                    # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                    selectionner = False
                    fenetre.blit(fond_options, (0,0))
                    fenetre.blit(titre_options, POSITION_TITRE_OPTIONS)
                    fenetre.blit(bouton_musique, POSITION_BOUTON_MUSIQUE)
                    fenetre.blit(bouton_son, POSITION_BOUTON_SON)
                    fenetre.blit(bouton_restaurer, POSITION_BOUTON_RESTAURER)
                    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
            else:
                fenetre.blit(bouton_restaurer, POSITION_BOUTON_RESTAURER)
                dessus_bouton[2] = False
                        
            # RETOUR ---------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_RETOUR[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_RETOUR[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_RETOUR[POSITION_Y] + bouton_retour.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_RETOUR[POSITION_X] + bouton_retour.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_retour_ok, POSITION_BOUTON_RETOUR)
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
            else:
                fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
                dessus_bouton[3] = False
                
            pygame.display.flip()

            if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE:
                selectionner = False

