"""
   FICHIER MENU_SELECTION.PY :
       - FONCTION selection

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
from DEPENDANCES.sources.charger_monstres import *
from DEPENDANCES.sources.combat import *

# GESTION DU MENU JOUER

def selection(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click):
    
    # CHARGEMENT DES IMAGES
    
    fond_selection = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/menu_selection.jpeg").convert()
    titre_selection = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/titre_selection.png").convert()
    bouton_monstre_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_monstre_ok.png").convert()
    bouton_monstre = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_monstre.png").convert()
    
    
    bouton_retour_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_retour_fleche_ok.png").convert()
    bouton_retour = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_retour_fleche.png").convert()
    bouton_voir_attaques = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_voir_attaques.png").convert()
    bouton_voir_attaques_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_voir_attaques_ok.png").convert()
    
    # CHARGEMENT DE LA POLICE
    
    police = pygame.font.Font(CHEMIN_DEPENDANCES + "DEPENDANCES/polices/ARJULIAN.ttf", 16)
    police2 = pygame.font.Font(CHEMIN_DEPENDANCES + "DEPENDANCES/polices/ARJULIAN.ttf", 10)

    # CHARGEMENT D'UN SON SUPPLÉMENTAIRE
    
    son_laser = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/laser.ogg")
    
    # CONSTANTES DE POSITIONS DES IMAGES
    
    POSITION_TITRE_SELECTION = ((FENETRE_X / 2) - (titre_selection.get_width() / 2), 0)
    POSITION_BOUTON_MONSTRE = []
    POSITION_BOUTON_VOIR_ATTAQUES = ((FENETRE_X - 10 - bouton_voir_attaques.get_width()), 10)
    POSITION_SPRITE = []
    POSITION_NOM = []
    POSITION_CLASSE = []
    POSITION_ETAT = []
    POSITION_VIVANT = []
    POSITION_PV = []
    POSITION_BOUTON_RETOUR = (10,10)
    TAILLE_MINIATURE = (50,50)
    COULEUR_NOIRE = (0,0,0)
    
    # AFFICHAGE DES IMAGES DE FOND

    fenetre.blit(fond_selection, (0,0))
    fenetre.blit(titre_selection, POSITION_TITRE_SELECTION)
    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
    fenetre.blit(bouton_voir_attaques, POSITION_BOUTON_VOIR_ATTAQUES)
    
    # BOUCLE DE CHARGEMENT / AFFICHAGE DES MONSTRES
    
    nombre_monstres = 0
    nombre_monstres_total = 0
    
    liste_monstres = charger_monstres(pygame)
    
    for i in liste_monstres:
        nombre_monstres_total += 1
    for i in liste_monstres:
        nombre_monstres += 1
        POSITION_BOUTON_MONSTRE.append(((FENETRE_X / 2) - (bouton_monstre.get_width() / 2), (FENETRE_Y * (4/5) * (nombre_monstres/nombre_monstres_total)) + 5))
        fenetre.blit(bouton_monstre, POSITION_BOUTON_MONSTRE[nombre_monstres-1])
        
    voir_attaques = False
    
    for i in range(nombre_monstres):
        
        # CONSTANTES DE POSITIONS
        
        POSITION_SPRITE.append((POSITION_BOUTON_MONSTRE[i][POSITION_X]+7, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+11))
        POSITION_NOM.append((POSITION_BOUTON_MONSTRE[i][POSITION_X]+60, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10))
        POSITION_VIVANT.append((POSITION_NOM[i][POSITION_X], POSITION_BOUTON_MONSTRE[i][POSITION_Y]+50))
        POSITION_CLASSE.append((POSITION_NOM[i][POSITION_X]+150, POSITION_NOM[i][POSITION_Y]))
        POSITION_PV.append((POSITION_CLASSE[i][POSITION_X]-50, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+50))
        POSITION_ETAT.append((POSITION_CLASSE[i][POSITION_X]+16, POSITION_CLASSE[i][POSITION_Y]+20))        
        
        # AFFICHAGES
        
        if not voir_attaques:            
            fenetre.blit(pygame.transform.scale(liste_monstres[i].sprite[SPRITE.HAUT.value-1], TAILLE_MINIATURE), POSITION_SPRITE[i])
            
            nom_monstre = police.render(liste_monstres[i].nom, 1, COULEUR_NOIRE)
            fenetre.blit(nom_monstre, POSITION_NOM[i])
                    
            classe_monstre = police.render("CLASSE : " + liste_monstres[i].str_classe, 1, COULEUR_NOIRE)
            fenetre.blit(classe_monstre, POSITION_CLASSE[i])
            
            etat_monstre = police.render("ÉTAT : " + liste_monstres[i].str_etat, 1, COULEUR_NOIRE)
            fenetre.blit(etat_monstre, POSITION_ETAT[i])

            if liste_monstres[i].vivant:
                vivant = police.render("VIVANT", 1, COULEUR_NOIRE)
            else:
                vivant = police.render("MORT", 1, COULEUR_NOIRE)
            fenetre.blit(vivant, POSITION_VIVANT[i])
         
            pv_monstre = police.render("PV : " + str(liste_monstres[i].pv) + "/" + str(liste_monstres[i].pv_max), 1, COULEUR_NOIRE)
            fenetre.blit(pv_monstre, POSITION_PV[i])

        else:            
            k = 0
            position_ajout = 0
            
            for attaque_actuelle in liste_monstres[i].attaques:
                position_ajout += 10
                nom_monstre = police2.render(liste_monstres[i].nom, 1, COULEUR_NOIRE)
                fenetre.blit(nom_monstre, ((FENETRE_X / 2) - (nom_monstre.get_width() / 2), POSITION_BOUTON_MONSTRE[i][POSITION_Y]+5))
                              
                degat_attaque = police2.render("DÉGATS : " + str (liste_monstres[i].attaques[k].degats), 1, COULEUR_NOIRE)
                fenetre.blit(degat_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+165, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                            
                nom_attaque = police2.render("NOM : " + liste_monstres[i].attaques[k].nom , 1, COULEUR_NOIRE)
                fenetre.blit(nom_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+10, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                            
                etat_attaque = police2.render("ÉTAT : " + liste_monstres[i].attaques[k].str_etat, 1, COULEUR_NOIRE)
                fenetre.blit(etat_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+260, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                            
                classe_attaque = police2.render("CLASSE : " + liste_monstres[i].attaques[k].str_classe, 1, COULEUR_NOIRE)
                fenetre.blit(classe_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+365, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                k+=1        

    pygame.display.flip()
    
    # BOUCLE PRINCIPALE

    dessus_bouton = [[False,False], []] # pour éviter la répétiton du bruit de passage au-dessus du bouton dès qu'on se déplace sur sa surface
    for i in range(nombre_monstres):
        dessus_bouton[1].append(False)
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
           
            # AFFICHAGE DES IMAGES DE FOND
            fenetre.blit(fond_selection, (0,0))
            fenetre.blit(titre_selection, POSITION_TITRE_SELECTION)
           
            # ÉVÉNEMENTS DE POSITION ET DE CLIQUE
                        
            # RETOUR ------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_RETOUR[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_RETOUR[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_RETOUR[POSITION_Y] + bouton_retour.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_RETOUR[POSITION_X] + bouton_retour.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_retour_ok, POSITION_BOUTON_RETOUR)
                # GESTION AUDIO
                if not dessus_bouton[0][0]:
                    jouer_son(son_slide)
                    dessus_bouton[0][0] = True
                # GESTION CLIQUES
                if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                    selectionner = True
                if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                    jouer_son(son_click)
                    continuer = False
            else:
                fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
                dessus_bouton[0][0] = False
                
            # VOIR LES ATTAQUES ------------------------------------------------------------------------
            if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_VOIR_ATTAQUES[POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_VOIR_ATTAQUES[POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_VOIR_ATTAQUES[POSITION_Y] + bouton_voir_attaques.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_VOIR_ATTAQUES[POSITION_X] + bouton_voir_attaques.get_width()):
                # GESTION AFFICHAGE
                fenetre.blit(bouton_voir_attaques_ok, POSITION_BOUTON_VOIR_ATTAQUES)
                # GESTION AUDIO
                if not dessus_bouton[0][1]:
                    jouer_son(son_slide)
                    dessus_bouton[0][1] = True
                    voir_attaques = True
            else:
                fenetre.blit(bouton_voir_attaques, POSITION_BOUTON_VOIR_ATTAQUES)
                dessus_bouton[0][1] = False
                voir_attaques = False
                
            # SÉLÉCTION ------------------------------------------------------------------------
            for i in range(nombre_monstres):
                if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_MONSTRE[i][POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_MONSTRE[i][POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_MONSTRE[i][POSITION_Y] + bouton_monstre.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_MONSTRE[i][POSITION_X] + bouton_monstre.get_width()):
                    # GESTION AFFICHAGE
                    fenetre.blit(bouton_monstre_ok, POSITION_BOUTON_MONSTRE[i])
                    # GESTION AUDIO
                    if not dessus_bouton[1][i]:
                        jouer_son(son_slide)
                        dessus_bouton[1][i] = True
                    # GESTION CLIQUES
                    if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                        selectionner = True
                    if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                        jouer_son(son_laser)
                        # GESTION NOUVELLE MUSIQUE
                        pygame.mixer.music.fadeout(2000)
                        pygame.mixer.music.load(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/musiques/combat.wav")
                        jouer_musique(pygame, -1)
                        combat(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click, son_laser, liste_monstres[i], liste_monstres, COULEUR_NOIRE)
                        pygame.mixer.music.fadeout(2000)
                        pygame.mixer.music.load(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/musiques/home.wav")
                        jouer_musique(pygame, -1)
                        # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                        selectionner = False
                        fenetre.blit(fond_selection, (0,0))
                        fenetre.blit(titre_selection, POSITION_TITRE_SELECTION)
                        fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
                        fenetre.blit(bouton_voir_attaques, POSITION_BOUTON_VOIR_ATTAQUES)
                        
                        for j in range(0, i+1, 1):                            
                            fenetre.blit(bouton_monstre, POSITION_BOUTON_MONSTRE[j])
                            fenetre.blit(pygame.transform.scale(liste_monstres[j].sprite[SPRITE.HAUT.value-1], TAILLE_MINIATURE), POSITION_SPRITE[j])
                            
                            nom_monstre = police.render(liste_monstres[j].nom, 1, COULEUR_NOIRE)
                            fenetre.blit(nom_monstre, POSITION_NOM[j])
                                    
                            classe_monstre = police.render("CLASSE : " + liste_monstres[j].str_classe, 1, COULEUR_NOIRE)
                            fenetre.blit(classe_monstre, POSITION_CLASSE[j])
                            
                            etat_monstre = police.render("ÉTAT : " + liste_monstres[j].str_etat, 1, COULEUR_NOIRE)
                            fenetre.blit(etat_monstre, POSITION_ETAT[j])

                            if liste_monstres[j].vivant:
                                vivant = police.render("VIVANT", 1, COULEUR_NOIRE)
                            else:
                                vivant = police.render("MORT", 1, COULEUR_NOIRE)
                            fenetre.blit(vivant, POSITION_VIVANT[j])
                                            
                            pv_monstre = police.render("PV : " + str(liste_monstres[j].pv) + "/" + str(liste_monstres[j].pv_max), 1, COULEUR_NOIRE)
                            fenetre.blit(pv_monstre, POSITION_PV[j])
                            
                            if not voir_attaques:
                                fenetre.blit(pygame.transform.scale(liste_monstres[i].sprite[SPRITE.HAUT.value-1], TAILLE_MINIATURE), POSITION_SPRITE[i])
                                
                                nom_monstre = police.render(liste_monstres[i].nom, 1, COULEUR_NOIRE)
                                fenetre.blit(nom_monstre, POSITION_NOM[i])
                                        
                                classe_monstre = police.render("CLASSE : " + liste_monstres[i].str_classe, 1, COULEUR_NOIRE)
                                fenetre.blit(classe_monstre, POSITION_CLASSE[i])
                                
                                etat_monstre = police.render("ÉTAT : " + liste_monstres[i].str_etat, 1, COULEUR_NOIRE)
                                fenetre.blit(etat_monstre, POSITION_ETAT[i])

                                if liste_monstres[i].vivant:
                                    vivant = police.render("VIVANT", 1, COULEUR_NOIRE)
                                else:
                                    vivant = police.render("MORT", 1, COULEUR_NOIRE)
                                fenetre.blit(vivant, POSITION_VIVANT[i])
                                                
                                pv_monstre = police.render("PV : " + str(liste_monstres[i].pv) + "/" + str(liste_monstres[i].pv_max), 1, COULEUR_NOIRE)
                                fenetre.blit(pv_monstre, POSITION_PV[i])
                            else:                                
                                k = 0
                                position_ajout = 0
                                for attaque_actuelle in liste_monstres[i].attaques:
                                    position_ajout += 10    
                                    nom_monstre = police2.render(liste_monstres[i].nom, 1, COULEUR_NOIRE)
                                    fenetre.blit(nom_monstre, ((FENETRE_X / 2) - (nom_monstre.get_width() / 2), POSITION_BOUTON_MONSTRE[i][POSITION_Y]+5))
                                                  
                                    degat_attaque = police2.render("DÉGATS : " + str (liste_monstres[i].attaques[k].degats) ,1 , COULEUR_NOIRE)
                                    fenetre.blit(degat_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+165, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                                                
                                    nom_attaque = police2.render("NOM : " + liste_monstres[i].attaques[k].nom , 1 , COULEUR_NOIRE)
                                    fenetre.blit(nom_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+10, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                                                
                                    etat_attaque = police2.render("ÉTAT : " + liste_monstres[i].attaques[k].str_etat, 1 , COULEUR_NOIRE)
                                    fenetre.blit(etat_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+260, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                                                
                                    classe_attaque = police2.render("CLASSE : " + liste_monstres[i].attaques[k].str_classe  , 1 , COULEUR_NOIRE)
                                    fenetre.blit(classe_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+365, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                                    k+=1
                else:
                    fenetre.blit(bouton_monstre, POSITION_BOUTON_MONSTRE[i]) 
                    dessus_bouton[1][i] = False
                    
                if not voir_attaques:
                    fenetre.blit(pygame.transform.scale(liste_monstres[i].sprite[SPRITE.HAUT.value-1], TAILLE_MINIATURE), POSITION_SPRITE[i])
                    
                    nom_monstre = police.render(liste_monstres[i].nom, 1, COULEUR_NOIRE)
                    fenetre.blit(nom_monstre, POSITION_NOM[i])
                            
                    classe_monstre = police.render("CLASSE : " + liste_monstres[i].str_classe, 1, COULEUR_NOIRE)
                    fenetre.blit(classe_monstre, POSITION_CLASSE[i])
                    
                    etat_monstre = police.render("ÉTAT : " + liste_monstres[i].str_etat, 1, COULEUR_NOIRE)
                    fenetre.blit(etat_monstre, POSITION_ETAT[i])

                    if liste_monstres[i].vivant:
                        vivant = police.render("VIVANT", 1, COULEUR_NOIRE)
                    else:
                        vivant = police.render("MORT", 1, COULEUR_NOIRE)
                    fenetre.blit(vivant, POSITION_VIVANT[i])
                                    
                    pv_monstre = police.render("PV : " + str(liste_monstres[i].pv) + "/" + str(liste_monstres[i].pv_max), 1, COULEUR_NOIRE)
                    fenetre.blit(pv_monstre, POSITION_PV[i])
                else:                    
                    k = 0
                    position_ajout = 0
            
                    for attaque_actuelle in liste_monstres[i].attaques:
                        position_ajout += 10
                        
                        nom_monstre = police2.render(liste_monstres[i].nom, 1, COULEUR_NOIRE)
                        fenetre.blit(nom_monstre, ((FENETRE_X / 2) - (nom_monstre.get_width() / 2), POSITION_BOUTON_MONSTRE[i][POSITION_Y]+5))
                                      
                        degat_attaque = police2.render("DÉGATS : " + str (liste_monstres[i].attaques[k].degats) ,1 , COULEUR_NOIRE)
                        fenetre.blit(degat_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+165, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                                    
                        nom_attaque = police2.render("NOM : " + liste_monstres[i].attaques[k].nom , 1 , COULEUR_NOIRE)
                        fenetre.blit(nom_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+10, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                                    
                        etat_attaque = police2.render("ÉTAT : " + liste_monstres[i].attaques[k].str_etat, 1 , COULEUR_NOIRE)
                        fenetre.blit(etat_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+260, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                                    
                        classe_attaque = police2.render("CLASSE : " + liste_monstres[i].attaques[k].str_classe  , 1 , COULEUR_NOIRE)
                        fenetre.blit(classe_attaque, (POSITION_BOUTON_MONSTRE[i][POSITION_X]+365, POSITION_BOUTON_MONSTRE[i][POSITION_Y]+10+position_ajout))
                        k+=1
                
            if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE:
                selectionner = False

            pygame.display.flip()
