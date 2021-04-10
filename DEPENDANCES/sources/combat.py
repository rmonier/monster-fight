"""
   FICHIER COMBAT.PY :
       - FONCTION attendre
       - FONCTION combat

   DERNIÈRE MÀJ : 11/07/2016
   CRÉÉ PAR JORIS COULANGE ET ROMAIN MONIER POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :
       - interface de combat
---------------------------------------------------------------
"""

# RESSOURCES EXTERNES

from pygame.locals import *
from DEPENDANCES.sources.gestion_audio import *
from DEPENDANCES.sources.monstre import *
import random
import time

def attendre(secondes, pygame, sys):
    temps_debut = time.time()
    while time.time() - temps_debut < secondes:
        time.sleep(0.1)
        pygame.event.post(pygame.event.Event(MOUSEMOTION)) # pour entrer dans la boucle
        for event in pygame.event.get():
            # ÉVÉNEMENT DE FERMETURE            
            if event.type == QUIT:
                continuer = False
                pygame.mixer.music.fadeout(500)
                pygame.mixer.fadeout(500)
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            pygame.event.clear()
    pygame.event.post(pygame.event.Event(MOUSEMOTION)) # pour rerentrer dans la boucle

# GESTION DE L'INTERFACE DE COMBAT

def combat(FENETRE_X, FENETRE_Y, POSITION_X, POSITION_Y, BOUTON_GAUCHE, pygame, sys, fenetre, son_slide, son_click, son_laser, monstre, liste_monstres, COULEUR_NOIRE):
    
    # CHARGEMENT DE LA POLICE
    
    police = pygame.font.Font(CHEMIN_DEPENDANCES + "DEPENDANCES/polices/ARJULIAN.ttf", 16)
    police_details = pygame.font.Font(CHEMIN_DEPENDANCES + "DEPENDANCES/polices/ARJULIAN.ttf", 13)

    # CHARGEMENT DES BRUITAGES

    son_touche = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_touche.ogg")
    son_touche_forte = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_touche_forte.ogg")
    son_touche_faible = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_touche_faible.ogg")
    
    son_normal = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_normal.ogg")
    son_eau = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_eau.ogg")
    son_feu = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_feu.ogg")
    son_electrique = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_electrique.ogg")
    son_plante = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_plante.ogg")
    son_acier = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_acier.ogg")
    son_dragon = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_dragon.ogg")
    son_insecte = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_insecte.ogg")
    son_tenebre = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_tenebre.ogg")
    son_spectre = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_spectre.ogg")
    son_psy = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_psy.ogg")
    son_vol = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_vol.ogg")
    son_sol = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_sol.ogg")
    son_roche = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_roche.ogg")
    son_poison = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_poison.ogg")
    son_combat = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_combat.ogg")
    son_glace = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_glace.ogg")
    
    son_paralyse = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_paralyse.ogg")
    son_brule = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_brule.ogg")
    son_gele = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_gele.ogg")
    son_empoisonne = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_empoisonne.ogg")
    son_endormi = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_endormi.ogg")
    son_confus = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_confus.ogg")
    
    son_gagne = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_gagne.ogg")
    son_perdu = pygame.mixer.Sound(CHEMIN_DEPENDANCES + "DEPENDANCES/audio/sons/son_perdu.ogg")

    # CHARGEMENT DES IMAGES
    
    nombre_aleatoire = random.randint(1, 4)
    if nombre_aleatoire == 1:
        fond_combat = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/combat_desert.jpg").convert()
    elif nombre_aleatoire == 2:
        fond_combat = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/combat_enfer.jpg").convert()
    elif nombre_aleatoire == 3:
        fond_combat = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/combat_jungle.jpg").convert()
    else:
        fond_combat = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/combat_spatial.png").convert()
        
    nombre_aleatoire = random.randint(0, 4)
    adversaire = Monstre(pygame, liste_monstres[nombre_aleatoire].nom, liste_monstres[nombre_aleatoire].chemin_sprite, liste_monstres[nombre_aleatoire].classe, liste_monstres[nombre_aleatoire].pv_max, (Attaque(liste_monstres[nombre_aleatoire].attaques[0].nom, liste_monstres[nombre_aleatoire].attaques[0].degats, liste_monstres[nombre_aleatoire].attaques[0].classe, liste_monstres[nombre_aleatoire].attaques[0].utilisations_max, liste_monstres[nombre_aleatoire].attaques[0].etat), Attaque(liste_monstres[nombre_aleatoire].attaques[1].nom, liste_monstres[nombre_aleatoire].attaques[1].degats, liste_monstres[nombre_aleatoire].attaques[1].classe, liste_monstres[nombre_aleatoire].attaques[1].utilisations_max, liste_monstres[nombre_aleatoire].attaques[1].etat), Attaque(liste_monstres[nombre_aleatoire].attaques[2].nom, liste_monstres[nombre_aleatoire].attaques[2].degats, liste_monstres[nombre_aleatoire].attaques[2].classe, liste_monstres[nombre_aleatoire].attaques[2].utilisations_max, liste_monstres[nombre_aleatoire].attaques[2].etat), Attaque(liste_monstres[nombre_aleatoire].attaques[3].nom, liste_monstres[nombre_aleatoire].attaques[3].degats, liste_monstres[nombre_aleatoire].attaques[3].classe, liste_monstres[nombre_aleatoire].attaques[3].utilisations_max, liste_monstres[nombre_aleatoire].attaques[3].etat)))

    zone_texte = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/zone_texte.png").convert()

    zone_monstre = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/zone_monstre.png").convert()

    fond_bouton_attaque = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/fond_bouton_attaque.png").convert()

    bouton_attaque = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_attaque.png").convert()

    bouton_attaque_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_attaque_ok.png").convert()
    
    bouton_retour_ok = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_retour_fleche_ok.png").convert()
    
    bouton_retour = pygame.image.load(CHEMIN_DEPENDANCES + "DEPENDANCES/images/menus/bouton_retour_fleche.png").convert()
    
    nom_monstre = police.render(monstre.nom, 1, COULEUR_NOIRE)
    pv_str_monstre = police.render("PV", 1, COULEUR_NOIRE)
    pv_monstre = police.render(str(monstre.pv) + "/" + str(monstre.pv_max), 1, COULEUR_NOIRE)
    etat_monstre = police.render(monstre.str_etat, 1, COULEUR_NOIRE)
    classe_str_monstre = police.render("CLASSE", 1, COULEUR_NOIRE)
    classe_monstre = police.render(monstre.str_classe, 1, COULEUR_NOIRE)
    
    nom_adversaire = police.render(adversaire.nom, 1, COULEUR_NOIRE)
    pv_str_adversaire = police.render("PV", 1, COULEUR_NOIRE)
    pv_adversaire = police.render(str(adversaire.pv) + "/" + str(adversaire.pv_max), 1, COULEUR_NOIRE)
    etat_adversaire = police.render(adversaire.str_etat, 1, COULEUR_NOIRE)
    classe_str_adversaire = police.render("CLASSE", 1, COULEUR_NOIRE)
    classe_adversaire = police.render(adversaire.str_classe, 1, COULEUR_NOIRE)

    texte = police.render("Le combat commence, " + monstre.nom + " contre " + adversaire.nom + " !", 1, COULEUR_NOIRE)

    total_attaques = 0

    nom_attaque = []
    for attaque_actuelle in monstre.attaques:
        nom_attaque.append(police.render(attaque_actuelle.nom, 1, COULEUR_NOIRE))
        total_attaques += 1
                           
    details_attaque = []
    for attaque_actuelle in monstre.attaques:
        details_attaque.append(police_details.render("DÉGATS : " + str(attaque_actuelle.degats) + "    CLASSE : " + attaque_actuelle.str_classe + "    ÉTAT : " + attaque_actuelle.str_etat, 1, COULEUR_NOIRE))
    
    # CONSTANTES ET VARIABLES DE POSITIONS DES IMAGES

    POSITION_BOUTON_RETOUR = (10,10)
    POSITION_FOND_BOUTON_ATTAQUE = (0, FENETRE_Y * (3/4) - 10)
    POSITION_ZONE_TEXTE = (0, POSITION_FOND_BOUTON_ATTAQUE[POSITION_Y] - zone_texte.get_height() + 10)
    POSITION_BOUTON_ATTAQUE = ((10, POSITION_ZONE_TEXTE[POSITION_Y] + zone_texte.get_height() + 10), (FENETRE_X - bouton_attaque.get_width() - 10, POSITION_ZONE_TEXTE[POSITION_Y] + zone_texte.get_height() + 10), (10, POSITION_ZONE_TEXTE[POSITION_Y] + bouton_attaque.get_height() + zone_texte.get_height() + 12), (FENETRE_X - bouton_attaque.get_width() - 10, POSITION_ZONE_TEXTE[POSITION_Y] + zone_texte.get_height() + bouton_attaque.get_height() + 12))
    POSITION_MONSTRE = ((FENETRE_X * (1/3)) - (monstre.sprite[SPRITE.DROITE.value-1].get_width() / 2), POSITION_ZONE_TEXTE[POSITION_Y] - monstre.sprite[SPRITE.DROITE.value-1].get_height())
    POSITION_ADVERSAIRE = ((FENETRE_X * (2/3)) - (adversaire.sprite[SPRITE.DROITE.value-1].get_width() / 2), POSITION_ZONE_TEXTE[POSITION_Y] - adversaire.sprite[SPRITE.GAUCHE.value-1].get_height())
    POSITION_ZONE_MONSTRE = (10, POSITION_ZONE_TEXTE[POSITION_Y] - zone_monstre.get_height())
    POSITION_ZONE_ADVERSAIRE = (FENETRE_X - zone_monstre.get_width() - 10, POSITION_ZONE_TEXTE[POSITION_Y] - zone_monstre.get_height())
    POSITION_TEXTE = ((POSITION_ZONE_TEXTE[POSITION_X] + (zone_texte.get_width() / 2)) - (texte.get_width() / 2), (POSITION_ZONE_TEXTE[POSITION_Y] + (zone_texte.get_height() / 2)) - (texte.get_height() / 2))
    
    POSITION_ZONE_MONSTRE_NOM = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (nom_monstre.get_width() / 2), POSITION_ZONE_MONSTRE[POSITION_Y] + 5)
    POSITION_ZONE_MONSTRE_PV_STR = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (pv_str_monstre.get_width() / 2), POSITION_ZONE_MONSTRE_NOM[POSITION_Y] + 30)
    POSITION_ZONE_MONSTRE_PV = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (pv_monstre.get_width() / 2), POSITION_ZONE_MONSTRE_PV_STR[POSITION_Y] + 20)
    POSITION_ZONE_MONSTRE_ETAT = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (etat_monstre.get_width() / 2), POSITION_ZONE_MONSTRE_PV[POSITION_Y] + 30)
    POSITION_ZONE_MONSTRE_CLASSE_STR = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (classe_str_monstre.get_width() / 2), POSITION_ZONE_MONSTRE_ETAT[POSITION_Y] + 30)
    POSITION_ZONE_MONSTRE_CLASSE = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (classe_monstre.get_width() / 2), POSITION_ZONE_MONSTRE_CLASSE_STR[POSITION_Y] + 20)
    
    POSITION_ZONE_ADVERSAIRE_NOM = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (nom_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE[POSITION_Y] + 5)
    POSITION_ZONE_ADVERSAIRE_PV_STR = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (pv_str_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE_NOM[POSITION_Y] + 30)
    POSITION_ZONE_ADVERSAIRE_PV = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (pv_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE_PV_STR[POSITION_Y] + 20)
    POSITION_ZONE_ADVERSAIRE_ETAT = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (etat_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE_PV[POSITION_Y] + 30)
    POSITION_ZONE_ADVERSAIRE_CLASSE_STR = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (classe_str_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE_ETAT[POSITION_Y] + 30)
    POSITION_ZONE_ADVERSAIRE_CLASSE = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (classe_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE_CLASSE_STR[POSITION_Y] + 20)

    POSITION_ATTAQUE_NOM = (((POSITION_BOUTON_ATTAQUE[0][POSITION_X] + (bouton_attaque.get_width() / 2)) - (nom_attaque[0].get_width() / 2), POSITION_BOUTON_ATTAQUE[0][POSITION_Y] + 5), ((POSITION_BOUTON_ATTAQUE[1][POSITION_X] + (bouton_attaque.get_width() / 2)) - (nom_attaque[1].get_width() / 2), POSITION_BOUTON_ATTAQUE[1][POSITION_Y] + 5), ((POSITION_BOUTON_ATTAQUE[2][POSITION_X] + (bouton_attaque.get_width() / 2)) - (nom_attaque[2].get_width() / 2), POSITION_BOUTON_ATTAQUE[2][POSITION_Y] + 5), ((POSITION_BOUTON_ATTAQUE[3][POSITION_X] + (bouton_attaque.get_width() / 2)) - (nom_attaque[3].get_width() / 2), POSITION_BOUTON_ATTAQUE[3][POSITION_Y] + 5))
    POSITION_ATTAQUE_DETAILS = (((POSITION_BOUTON_ATTAQUE[0][POSITION_X] + (bouton_attaque.get_width() / 2)) - (details_attaque[0].get_width() / 2), POSITION_ATTAQUE_NOM[0][POSITION_Y] + nom_attaque[0].get_height() + 2), ((POSITION_BOUTON_ATTAQUE[1][POSITION_X] + (bouton_attaque.get_width() / 2)) - (details_attaque[1].get_width() / 2), POSITION_ATTAQUE_NOM[1][POSITION_Y] + nom_attaque[1].get_height() + 2), ((POSITION_BOUTON_ATTAQUE[2][POSITION_X] + (bouton_attaque.get_width() / 2)) - (details_attaque[2].get_width() / 2), POSITION_ATTAQUE_NOM[2][POSITION_Y] + nom_attaque[2].get_height() + 2), ((POSITION_BOUTON_ATTAQUE[3][POSITION_X] + (bouton_attaque.get_width() / 2)) - (details_attaque[3].get_width() / 2), POSITION_ATTAQUE_NOM[3][POSITION_Y] + nom_attaque[3].get_height() + 2))
    
    # AFFICHAGE DES IMAGES

    fenetre.blit(fond_combat, (0,0))
    fenetre.blit(monstre.sprite[SPRITE.DROITE.value-1], POSITION_MONSTRE)
    fenetre.blit(adversaire.sprite[SPRITE.GAUCHE.value-1], POSITION_ADVERSAIRE)
    fenetre.blit(zone_monstre, POSITION_ZONE_MONSTRE)
    fenetre.blit(zone_monstre, POSITION_ZONE_ADVERSAIRE)
    fenetre.blit(fond_bouton_attaque, POSITION_FOND_BOUTON_ATTAQUE)
    fenetre.blit(zone_texte, POSITION_ZONE_TEXTE)
    fenetre.blit(texte, POSITION_TEXTE)
    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)
    
    fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
    fenetre.blit(pv_str_monstre, POSITION_ZONE_MONSTRE_PV_STR)
    fenetre.blit(pv_monstre, POSITION_ZONE_MONSTRE_PV)
    fenetre.blit(etat_monstre, POSITION_ZONE_MONSTRE_ETAT)
    fenetre.blit(classe_str_monstre, POSITION_ZONE_MONSTRE_CLASSE_STR)
    fenetre.blit(classe_monstre, POSITION_ZONE_MONSTRE_CLASSE)
    
    fenetre.blit(nom_adversaire, POSITION_ZONE_ADVERSAIRE_NOM)
    fenetre.blit(pv_str_adversaire, POSITION_ZONE_ADVERSAIRE_PV_STR)
    fenetre.blit(pv_adversaire, POSITION_ZONE_ADVERSAIRE_PV)
    fenetre.blit(etat_adversaire, POSITION_ZONE_ADVERSAIRE_ETAT)
    fenetre.blit(classe_str_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE_STR)
    fenetre.blit(classe_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE)
    
    pygame.display.flip()

    # BOUCLE PRINCIPALE

    tour_adverse = False
    temps_debut = 0
    dessus_bouton = [[False], [False, False, False, False]] # pour éviter la répétiton du bruit de passage au-dessus du bouton dès qu'on se déplace sur sa surface
    selectionner = False # pour vérifier qu'on relache bien le bouton de la souris quand on clique
    continuer = True
    attendre(3, pygame, sys)  
    pygame.event.post(pygame.event.Event(MOUSEMOTION)) # pour rentrer dans la boucle
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
            
            fenetre.blit(fond_combat, (0,0))
            fenetre.blit(monstre.sprite[SPRITE.DROITE.value-1], POSITION_MONSTRE)
            fenetre.blit(adversaire.sprite[SPRITE.GAUCHE.value-1], POSITION_ADVERSAIRE)
            fenetre.blit(zone_monstre, POSITION_ZONE_MONSTRE)
            fenetre.blit(zone_monstre, POSITION_ZONE_ADVERSAIRE)
            fenetre.blit(fond_bouton_attaque, POSITION_FOND_BOUTON_ATTAQUE)
            
            # ÉVÉNEMENTS DE POSITION ET DE CLIQUE
            
            # TOUR MONSTRE -------------------------------------------------------------------
            if not tour_adverse:
                texte = police.render("À votre " + monstre.nom + " d'attaquer !", 1, COULEUR_NOIRE)
                # ATTAQUES ------------------------------------------------------------------------
                nombre_attaques = 0
                for attaque_actuelle in monstre.attaques:
                    if pygame.mouse.get_pos()[POSITION_Y] >= POSITION_BOUTON_ATTAQUE[nombre_attaques][POSITION_Y] and pygame.mouse.get_pos()[POSITION_X] >= POSITION_BOUTON_ATTAQUE[nombre_attaques][POSITION_X] and pygame.mouse.get_pos()[POSITION_Y] < (POSITION_BOUTON_ATTAQUE[nombre_attaques][POSITION_Y] + bouton_attaque.get_height() - 13) and pygame.mouse.get_pos()[POSITION_X] < (POSITION_BOUTON_ATTAQUE[nombre_attaques][POSITION_X] + bouton_attaque.get_width()):
                        # GESTION AFFICHAGE
                        if not tour_adverse:
                            fenetre.blit(bouton_attaque_ok, POSITION_BOUTON_ATTAQUE[nombre_attaques])
                        # GESTION AUDIO
                        if not dessus_bouton[1][nombre_attaques]:
                            jouer_son(son_slide)
                            dessus_bouton[1][nombre_attaques] = True
                        # GESTION CLIQUES
                        if event.type == MOUSEBUTTONDOWN and event.button == BOUTON_GAUCHE:
                            selectionner = True
                        if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE and selectionner:
                            jouer_son(son_laser)
                            pygame.event.post(pygame.event.Event(MOUSEMOTION)) # pour rerentrer dans la boucle
                            texte = police.render("Votre " + monstre.nom + " va lancer l'attaque " + attaque_actuelle.nom + " !", 1, COULEUR_NOIRE)
                            POSITION_TEXTE = ((POSITION_ZONE_TEXTE[POSITION_X] + (zone_texte.get_width() / 2)) - (texte.get_width() / 2), (POSITION_ZONE_TEXTE[POSITION_Y] + (zone_texte.get_height() / 2)) - (texte.get_height() / 2))
                            # JOUER SON ATTAQUE
                            if attaque_actuelle.classe == CLASSE.NORMAL.value:
                                jouer_son(son_normal)
                            elif attaque_actuelle.classe == CLASSE.EAU.value:
                                jouer_son(son_eau)
                            elif attaque_actuelle.classe == CLASSE.FEU.value:
                                jouer_son(son_feu)
                            elif attaque_actuelle.classe == CLASSE.ELECTRIQUE.value:
                                jouer_son(son_electrique)
                            elif attaque_actuelle.classe == CLASSE.PLANTE.value:
                                jouer_son(son_plante)
                            elif attaque_actuelle.classe == CLASSE.ACIER.value:
                                jouer_son(son_acier)
                            elif attaque_actuelle.classe == CLASSE.DRAGON.value:
                                jouer_son(son_dragon)
                            elif attaque_actuelle.classe == CLASSE.INSECTE.value:
                                jouer_son(son_insecte)
                            elif attaque_actuelle.classe == CLASSE.TENEBRE.value:
                                jouer_son(son_tenebre)
                            elif attaque_actuelle.classe == CLASSE.SPECTRE.value:
                                jouer_son(son_spectre)
                            elif attaque_actuelle.classe == CLASSE.PSY.value:
                                jouer_son(son_psy)
                            elif attaque_actuelle.classe == CLASSE.VOL.value:
                                jouer_son(son_vol)
                            elif attaque_actuelle.classe == CLASSE.SOL.value:
                                jouer_son(son_sol)
                            elif attaque_actuelle.classe == CLASSE.ROCHE.value:
                                jouer_son(son_roche)
                            elif attaque_actuelle.classe == CLASSE.POISON.value:
                                jouer_son(son_poison)
                            elif attaque_actuelle.classe == CLASSE.COMBAT.value:
                                jouer_son(son_combat)
                            elif attaque_actuelle.classe == CLASSE.GLACE.value:
                                jouer_son(son_glace)
                            # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                            fenetre.blit(fond_combat, (0,0))
                            fenetre.blit(monstre.sprite[SPRITE.DROITE.value-1], POSITION_MONSTRE)
                            fenetre.blit(adversaire.sprite[SPRITE.GAUCHE.value-1], POSITION_ADVERSAIRE)
                            fenetre.blit(zone_monstre, POSITION_ZONE_MONSTRE)
                            fenetre.blit(zone_monstre, POSITION_ZONE_ADVERSAIRE)
                            fenetre.blit(fond_bouton_attaque, POSITION_FOND_BOUTON_ATTAQUE)
                            fenetre.blit(zone_texte, POSITION_ZONE_TEXTE)
                            fenetre.blit(texte, POSITION_TEXTE)
                            fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                            fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                            fenetre.blit(pv_str_monstre, POSITION_ZONE_MONSTRE_PV_STR)
                            fenetre.blit(pv_monstre, POSITION_ZONE_MONSTRE_PV)
                            fenetre.blit(etat_monstre, POSITION_ZONE_MONSTRE_ETAT)
                            fenetre.blit(classe_str_monstre, POSITION_ZONE_MONSTRE_CLASSE_STR)
                            fenetre.blit(classe_monstre, POSITION_ZONE_MONSTRE_CLASSE)                            
                            fenetre.blit(nom_adversaire, POSITION_ZONE_ADVERSAIRE_NOM)
                            fenetre.blit(pv_str_adversaire, POSITION_ZONE_ADVERSAIRE_PV_STR)
                            fenetre.blit(pv_adversaire, POSITION_ZONE_ADVERSAIRE_PV)
                            fenetre.blit(etat_adversaire, POSITION_ZONE_ADVERSAIRE_ETAT)
                            fenetre.blit(classe_str_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE_STR)
                            fenetre.blit(classe_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE)     
                            fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)                                        
                            pygame.display.flip()

                            attendre(2, pygame, sys)                
                            resultat_attaque, degats, efficacite, critique, touche_etat = monstre.attaquer(adversaire, attaque_actuelle)
                            texte_en_cours = ""
                            if(resultat_attaque == ATTAQUE.RECUE.value):
                                if(efficacite == EFFICACE.FORT.value):
                                    texte_en_cours += "C'est super efficace ! "
                                    jouer_son(son_touche_forte)
                                elif(efficacite == EFFICACE.FAIBLE.value):
                                    texte_en_cours += "Ce n'est pas très efficace... "
                                    jouer_son(son_touche_faible)
                                else:
                                    jouer_son(son_touche)
                                if(critique):
                                    texte_en_cours += "Coup critique ! "
                                texte_en_cours += adversaire.nom + " ennemi reçoit " + str(int(degats)) + " dégats !"
                            elif(resultat_attaque == ATTAQUE.RATE_MALCHANCE.value):
                                texte_en_cours += "Votre " + monstre.nom + " rate son attaque..."
                            elif(resultat_attaque == ATTAQUE.RATE_PARALYSE.value):
                                texte_en_cours += "Votre " + monstre.nom + " est paralysé, il n'arrive pas à attaquer !"
                                jouer_son(son_paralyse)
                            elif(resultat_attaque == ATTAQUE.RATE_GELE.value):
                                texte_en_cours += "Votre " + monstre.nom + " est gelé, il ne peut pas attaquer !"
                                jouer_son(son_gele)
                            elif(resultat_attaque == ATTAQUE.RATE_ENDORMI.value):
                                texte_en_cours += "Votre " + monstre.nom + " est endormi, et il continue à dormir..."
                                jouer_son(son_endormi)
                            elif(resultat_attaque == ATTAQUE.RATE_NON_EFFICACE.value):
                                texte_en_cours += adversaire.nom + " ennemi n'est pas affecté..."
                            elif(resultat_attaque == ATTAQUE.RATE_CONFUS.value):
                                texte_en_cours += "Votre " + monstre.nom + " est confus ! Il se blesse dans sa confusion et perd " + str(int(degats)) + "PV !"
                                monstre.pv -= degats
                                jouer_son(son_confus)
                                jouer_son(son_touche)
                            elif(resultat_attaque == ATTAQUE.RATE_ESQUIVE.value):
                                texte_en_cours += adversaire.nom + " ennemi esquive l'attaque !"
                                
                            texte = police.render(texte_en_cours, 1, COULEUR_NOIRE)
                            POSITION_TEXTE = ((POSITION_ZONE_TEXTE[POSITION_X] + (zone_texte.get_width() / 2)) - (texte.get_width() / 2), (POSITION_ZONE_TEXTE[POSITION_Y] + (zone_texte.get_height() / 2)) - (texte.get_height() / 2))
                            # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                            fenetre.blit(fond_combat, (0,0))
                            fenetre.blit(monstre.sprite[SPRITE.DROITE.value-1], POSITION_MONSTRE)
                            fenetre.blit(adversaire.sprite[SPRITE.GAUCHE.value-1], POSITION_ADVERSAIRE)
                            fenetre.blit(zone_monstre, POSITION_ZONE_MONSTRE)
                            fenetre.blit(zone_monstre, POSITION_ZONE_ADVERSAIRE)
                            fenetre.blit(fond_bouton_attaque, POSITION_FOND_BOUTON_ATTAQUE)
                            fenetre.blit(zone_texte, POSITION_ZONE_TEXTE)
                            fenetre.blit(texte, POSITION_TEXTE)
                            fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                            fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                            fenetre.blit(pv_str_monstre, POSITION_ZONE_MONSTRE_PV_STR)
                            fenetre.blit(pv_monstre, POSITION_ZONE_MONSTRE_PV)
                            fenetre.blit(etat_monstre, POSITION_ZONE_MONSTRE_ETAT)
                            fenetre.blit(classe_str_monstre, POSITION_ZONE_MONSTRE_CLASSE_STR)
                            fenetre.blit(classe_monstre, POSITION_ZONE_MONSTRE_CLASSE)                            
                            fenetre.blit(nom_adversaire, POSITION_ZONE_ADVERSAIRE_NOM)
                            fenetre.blit(pv_str_adversaire, POSITION_ZONE_ADVERSAIRE_PV_STR)
                            fenetre.blit(pv_adversaire, POSITION_ZONE_ADVERSAIRE_PV)
                            fenetre.blit(etat_adversaire, POSITION_ZONE_ADVERSAIRE_ETAT)
                            fenetre.blit(classe_str_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE_STR)
                            fenetre.blit(classe_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE)   
                            fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)                                
                            pygame.display.flip()
                            
                            attendre(2, pygame, sys)   

                            if(touche_etat):
                                texte_en_cours = adversaire.nom + " ennemi est désormais " + adversaire.str_etat + " !"
                                texte = police.render(texte_en_cours, 1, COULEUR_NOIRE)
                                POSITION_TEXTE = ((POSITION_ZONE_TEXTE[POSITION_X] + (zone_texte.get_width() / 2)) - (texte.get_width() / 2), (POSITION_ZONE_TEXTE[POSITION_Y] + (zone_texte.get_height() / 2)) - (texte.get_height() / 2))
                                # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                                fenetre.blit(fond_combat, (0,0))
                                fenetre.blit(monstre.sprite[SPRITE.DROITE.value-1], POSITION_MONSTRE)
                                fenetre.blit(adversaire.sprite[SPRITE.GAUCHE.value-1], POSITION_ADVERSAIRE)
                                fenetre.blit(zone_monstre, POSITION_ZONE_MONSTRE)
                                fenetre.blit(zone_monstre, POSITION_ZONE_ADVERSAIRE)
                                fenetre.blit(fond_bouton_attaque, POSITION_FOND_BOUTON_ATTAQUE)
                                fenetre.blit(zone_texte, POSITION_ZONE_TEXTE)
                                fenetre.blit(texte, POSITION_TEXTE)
                                fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                                fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                                fenetre.blit(pv_str_monstre, POSITION_ZONE_MONSTRE_PV_STR)
                                fenetre.blit(pv_monstre, POSITION_ZONE_MONSTRE_PV)
                                fenetre.blit(etat_monstre, POSITION_ZONE_MONSTRE_ETAT)
                                fenetre.blit(classe_str_monstre, POSITION_ZONE_MONSTRE_CLASSE_STR)
                                fenetre.blit(classe_monstre, POSITION_ZONE_MONSTRE_CLASSE)                            
                                fenetre.blit(nom_adversaire, POSITION_ZONE_ADVERSAIRE_NOM)
                                fenetre.blit(pv_str_adversaire, POSITION_ZONE_ADVERSAIRE_PV_STR)
                                fenetre.blit(pv_adversaire, POSITION_ZONE_ADVERSAIRE_PV)
                                fenetre.blit(etat_adversaire, POSITION_ZONE_ADVERSAIRE_ETAT)
                                fenetre.blit(classe_str_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE_STR)
                                fenetre.blit(classe_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE)
                                fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)                                
                                pygame.display.flip()

                                attendre(2, pygame, sys)
                                
                            if monstre.etat == ETAT.BRULE.value:
                                nombre_aleatoire = random.randint(1, 100)
                                monstre.pv -= nombre_aleatoire
                                texte = police.render("Pendant ce temps, votre " + monstre.nom + " est en train de brûler et il perd " + str(nombre_aleatoire) + "PV !", 1, COULEUR_NOIRE)
                                jouer_son(son_brule)
                                jouer_son(son_touche)
                            if monstre.etat == ETAT.EMPOISONNE.value:
                                nombre_aleatoire = random.randint(1, 100)
                                monstre.pv -= nombre_aleatoire
                                texte = police.render("Pendant ce temps, votre " + monstre.nom + " est empoisonné et il perd " + str(nombre_aleatoire) + "PV !", 1, COULEUR_NOIRE)
                                jouer_son(son_empoisonne)
                                jouer_son(son_touche)
                            if monstre.etat == ETAT.BRULE.value or monstre.etat == ETAT.EMPOISONNE.value:
                                POSITION_TEXTE = ((POSITION_ZONE_TEXTE[POSITION_X] + (zone_texte.get_width() / 2)) - (texte.get_width() / 2), (POSITION_ZONE_TEXTE[POSITION_Y] + (zone_texte.get_height() / 2)) - (texte.get_height() / 2))
                                # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                                fenetre.blit(fond_combat, (0,0))
                                fenetre.blit(monstre.sprite[SPRITE.DROITE.value-1], POSITION_MONSTRE)
                                fenetre.blit(adversaire.sprite[SPRITE.GAUCHE.value-1], POSITION_ADVERSAIRE)
                                fenetre.blit(zone_monstre, POSITION_ZONE_MONSTRE)
                                fenetre.blit(zone_monstre, POSITION_ZONE_ADVERSAIRE)
                                fenetre.blit(fond_bouton_attaque, POSITION_FOND_BOUTON_ATTAQUE)
                                fenetre.blit(zone_texte, POSITION_ZONE_TEXTE)
                                fenetre.blit(texte, POSITION_TEXTE)
                                fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                                fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                                fenetre.blit(pv_str_monstre, POSITION_ZONE_MONSTRE_PV_STR)
                                fenetre.blit(pv_monstre, POSITION_ZONE_MONSTRE_PV)
                                fenetre.blit(etat_monstre, POSITION_ZONE_MONSTRE_ETAT)
                                fenetre.blit(classe_str_monstre, POSITION_ZONE_MONSTRE_CLASSE_STR)
                                fenetre.blit(classe_monstre, POSITION_ZONE_MONSTRE_CLASSE)                            
                                fenetre.blit(nom_adversaire, POSITION_ZONE_ADVERSAIRE_NOM)
                                fenetre.blit(pv_str_adversaire, POSITION_ZONE_ADVERSAIRE_PV_STR)
                                fenetre.blit(pv_adversaire, POSITION_ZONE_ADVERSAIRE_PV)
                                fenetre.blit(etat_adversaire, POSITION_ZONE_ADVERSAIRE_ETAT)
                                fenetre.blit(classe_str_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE_STR)
                                fenetre.blit(classe_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE)     
                                fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)                                        
                                pygame.display.flip()

                                attendre(2, pygame, sys)
                           
                            temps_debut = time.time()
                            tour_adverse = True
                    else:
                        if not tour_adverse:
                            fenetre.blit(bouton_attaque, POSITION_BOUTON_ATTAQUE[nombre_attaques])
                        dessus_bouton[1][nombre_attaques] = False
                        
                    nombre_attaques+=1
                    
                if not tour_adverse:
                    for i in range(total_attaques):
                        fenetre.blit(nom_attaque[i], POSITION_ATTAQUE_NOM[i])
                        fenetre.blit(details_attaque[i], POSITION_ATTAQUE_DETAILS[i])

            # TOUR ADVERSAIRE -------------------------------------------------------------------
            else:
                texte = police.render("Au " + adversaire.nom + " ennemi d'attaquer !", 1, COULEUR_NOIRE)
                if time.time() - temps_debut > 3:
                    nombre_aleatoire = random.randint(0, 3)
                    texte = police.render(adversaire.nom + " ennemi va lancer l'attaque " + adversaire.attaques[nombre_aleatoire].nom + " !", 1, COULEUR_NOIRE)
                    POSITION_TEXTE = ((POSITION_ZONE_TEXTE[POSITION_X] + (zone_texte.get_width() / 2)) - (texte.get_width() / 2), (POSITION_ZONE_TEXTE[POSITION_Y] + (zone_texte.get_height() / 2)) - (texte.get_height() / 2))
                    # JOUER SON ATTAQUE
                    if adversaire.attaques[nombre_aleatoire].classe == CLASSE.NORMAL.value:
                        jouer_son(son_normal)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.EAU.value:
                        jouer_son(son_eau)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.FEU.value:
                        jouer_son(son_feu)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.ELECTRIQUE.value:
                        jouer_son(son_electrique)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.PLANTE.value:
                        jouer_son(son_plante)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.ACIER.value:
                        jouer_son(son_acier)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.DRAGON.value:
                        jouer_son(son_dragon)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.INSECTE.value:
                        jouer_son(son_insecte)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.TENEBRE.value:
                        jouer_son(son_tenebre)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.SPECTRE.value:
                        jouer_son(son_spectre)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.PSY.value:
                        jouer_son(son_psy)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.VOL.value:
                        jouer_son(son_vol)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.SOL.value:
                        jouer_son(son_sol)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.ROCHE.value:
                        jouer_son(son_roche)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.POISON.value:
                        jouer_son(son_poison)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.COMBAT.value:
                        jouer_son(son_combat)
                    elif adversaire.attaques[nombre_aleatoire].classe == CLASSE.GLACE.value:
                        jouer_son(son_glace)
                    # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                    fenetre.blit(fond_combat, (0,0))
                    fenetre.blit(monstre.sprite[SPRITE.DROITE.value-1], POSITION_MONSTRE)
                    fenetre.blit(adversaire.sprite[SPRITE.GAUCHE.value-1], POSITION_ADVERSAIRE)
                    fenetre.blit(zone_monstre, POSITION_ZONE_MONSTRE)
                    fenetre.blit(zone_monstre, POSITION_ZONE_ADVERSAIRE)
                    fenetre.blit(fond_bouton_attaque, POSITION_FOND_BOUTON_ATTAQUE)
                    fenetre.blit(zone_texte, POSITION_ZONE_TEXTE)
                    fenetre.blit(texte, POSITION_TEXTE)
                    fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                    fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                    fenetre.blit(pv_str_monstre, POSITION_ZONE_MONSTRE_PV_STR)
                    fenetre.blit(pv_monstre, POSITION_ZONE_MONSTRE_PV)
                    fenetre.blit(etat_monstre, POSITION_ZONE_MONSTRE_ETAT)
                    fenetre.blit(classe_str_monstre, POSITION_ZONE_MONSTRE_CLASSE_STR)
                    fenetre.blit(classe_monstre, POSITION_ZONE_MONSTRE_CLASSE)                            
                    fenetre.blit(nom_adversaire, POSITION_ZONE_ADVERSAIRE_NOM)
                    fenetre.blit(pv_str_adversaire, POSITION_ZONE_ADVERSAIRE_PV_STR)
                    fenetre.blit(pv_adversaire, POSITION_ZONE_ADVERSAIRE_PV)
                    fenetre.blit(etat_adversaire, POSITION_ZONE_ADVERSAIRE_ETAT)
                    fenetre.blit(classe_str_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE_STR)
                    fenetre.blit(classe_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE)     
                    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)                                        
                    pygame.display.flip()

                    attendre(2, pygame, sys)                

                    resultat_attaque, degats, efficacite, critique, touche_etat = adversaire.attaquer(monstre, adversaire.attaques[nombre_aleatoire])
                    texte_en_cours = ""
                    if(resultat_attaque == ATTAQUE.RECUE.value):
                        if(efficacite == EFFICACE.FORT.value):
                            texte_en_cours += "C'est super efficace ! "
                            jouer_son(son_touche_forte)
                        elif(efficacite == EFFICACE.FAIBLE.value):
                            texte_en_cours += "Ce n'est pas très efficace... "
                            jouer_son(son_touche_faible)
                        else:
                            jouer_son(son_touche)
                        if(critique):
                            texte_en_cours += "Coup critique ! "
                        texte_en_cours += "Votre " + monstre.nom + " reçoit " + str(int(degats)) + " dégats !"
                    elif(resultat_attaque == ATTAQUE.RATE_MALCHANCE.value):
                        texte_en_cours += adversaire.nom + " ennemi rate son attaque..."
                    elif(resultat_attaque == ATTAQUE.RATE_PARALYSE.value):
                        texte_en_cours += adversaire.nom + " ennemi est paralysé, il n'arrive pas à attaquer !"
                        jouer_son(son_paralyse)
                    elif(resultat_attaque == ATTAQUE.RATE_GELE.value):
                        texte_en_cours += adversaire.nom + " ennemi est gelé, il ne peut pas attaquer !"
                        jouer_son(son_gele)
                    elif(resultat_attaque == ATTAQUE.RATE_ENDORMI.value):
                        texte_en_cours += adversaire.nom + " ennemi est endormi, et il continue à dormir..."
                        jouer_son(son_endormi)
                    elif(resultat_attaque == ATTAQUE.RATE_NON_EFFICACE.value):
                        texte_en_cours += "Votre " + monstre.nom + " n'est pas affecté..."
                    elif(resultat_attaque == ATTAQUE.RATE_CONFUS.value):
                        texte_en_cours += adversaire.nom + " ennemi est confus ! Il se blesse dans sa confusion et perd " + str(int(degats)) + "PV !"
                        adversaire.pv -= degats
                        jouer_son(son_confus)
                        jouer_son(son_touche)
                    elif(resultat_attaque == ATTAQUE.RATE_ESQUIVE.value):
                        texte_en_cours += "Votre " + monstre.nom + " esquive l'attaque !"
                                
                    texte = police.render(texte_en_cours, 1, COULEUR_NOIRE)
                    POSITION_TEXTE = ((POSITION_ZONE_TEXTE[POSITION_X] + (zone_texte.get_width() / 2)) - (texte.get_width() / 2), (POSITION_ZONE_TEXTE[POSITION_Y] + (zone_texte.get_height() / 2)) - (texte.get_height() / 2))
                    # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                    fenetre.blit(fond_combat, (0,0))
                    fenetre.blit(monstre.sprite[SPRITE.DROITE.value-1], POSITION_MONSTRE)
                    fenetre.blit(adversaire.sprite[SPRITE.GAUCHE.value-1], POSITION_ADVERSAIRE)
                    fenetre.blit(zone_monstre, POSITION_ZONE_MONSTRE)
                    fenetre.blit(zone_monstre, POSITION_ZONE_ADVERSAIRE)
                    fenetre.blit(fond_bouton_attaque, POSITION_FOND_BOUTON_ATTAQUE)
                    fenetre.blit(zone_texte, POSITION_ZONE_TEXTE)
                    fenetre.blit(texte, POSITION_TEXTE)
                    fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                    fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                    fenetre.blit(pv_str_monstre, POSITION_ZONE_MONSTRE_PV_STR)
                    fenetre.blit(pv_monstre, POSITION_ZONE_MONSTRE_PV)
                    fenetre.blit(etat_monstre, POSITION_ZONE_MONSTRE_ETAT)
                    fenetre.blit(classe_str_monstre, POSITION_ZONE_MONSTRE_CLASSE_STR)
                    fenetre.blit(classe_monstre, POSITION_ZONE_MONSTRE_CLASSE)                            
                    fenetre.blit(nom_adversaire, POSITION_ZONE_ADVERSAIRE_NOM)
                    fenetre.blit(pv_str_adversaire, POSITION_ZONE_ADVERSAIRE_PV_STR)
                    fenetre.blit(pv_adversaire, POSITION_ZONE_ADVERSAIRE_PV)
                    fenetre.blit(etat_adversaire, POSITION_ZONE_ADVERSAIRE_ETAT)
                    fenetre.blit(classe_str_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE_STR)
                    fenetre.blit(classe_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE)   
                    fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)                                
                    pygame.display.flip()
                            
                    attendre(2, pygame, sys)   

                    if(touche_etat):
                        texte_en_cours = "Votre " + monstre.nom + " est désormais " + monstre.str_etat + " !"
                        texte = police.render(texte_en_cours, 1, COULEUR_NOIRE)
                        POSITION_TEXTE = ((POSITION_ZONE_TEXTE[POSITION_X] + (zone_texte.get_width() / 2)) - (texte.get_width() / 2), (POSITION_ZONE_TEXTE[POSITION_Y] + (zone_texte.get_height() / 2)) - (texte.get_height() / 2))
                        # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                        fenetre.blit(fond_combat, (0,0))
                        fenetre.blit(monstre.sprite[SPRITE.DROITE.value-1], POSITION_MONSTRE)
                        fenetre.blit(adversaire.sprite[SPRITE.GAUCHE.value-1], POSITION_ADVERSAIRE)
                        fenetre.blit(zone_monstre, POSITION_ZONE_MONSTRE)
                        fenetre.blit(zone_monstre, POSITION_ZONE_ADVERSAIRE)
                        fenetre.blit(fond_bouton_attaque, POSITION_FOND_BOUTON_ATTAQUE)
                        fenetre.blit(zone_texte, POSITION_ZONE_TEXTE)
                        fenetre.blit(texte, POSITION_TEXTE)
                        fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                        fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                        fenetre.blit(pv_str_monstre, POSITION_ZONE_MONSTRE_PV_STR)
                        fenetre.blit(pv_monstre, POSITION_ZONE_MONSTRE_PV)
                        fenetre.blit(etat_monstre, POSITION_ZONE_MONSTRE_ETAT)
                        fenetre.blit(classe_str_monstre, POSITION_ZONE_MONSTRE_CLASSE_STR)
                        fenetre.blit(classe_monstre, POSITION_ZONE_MONSTRE_CLASSE)                            
                        fenetre.blit(nom_adversaire, POSITION_ZONE_ADVERSAIRE_NOM)
                        fenetre.blit(pv_str_adversaire, POSITION_ZONE_ADVERSAIRE_PV_STR)
                        fenetre.blit(pv_adversaire, POSITION_ZONE_ADVERSAIRE_PV)
                        fenetre.blit(etat_adversaire, POSITION_ZONE_ADVERSAIRE_ETAT)
                        fenetre.blit(classe_str_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE_STR)
                        fenetre.blit(classe_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE)
                        fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)                                
                        pygame.display.flip()

                        attendre(2, pygame, sys)
                                
                    if adversaire.etat == ETAT.BRULE.value:
                        nombre_aleatoire = random.randint(1, 100)
                        adversaire.pv -= nombre_aleatoire
                        texte = police.render("Pendant ce temps, " + adversaire.nom + " ennemi est en train de brûler et il perd " + str(nombre_aleatoire) + "PV !", 1, COULEUR_NOIRE)
                        jouer_son(son_brule)
                        jouer_son(son_touche)
                    if adversaire.etat == ETAT.EMPOISONNE.value:
                        nombre_aleatoire = random.randint(1, 100)
                        adversaire.pv -= nombre_aleatoire
                        texte = police.render("Pendant ce temps, " + adversaire.nom + " ennemi est empoisonné et il perd " + str(nombre_aleatoire) + "PV !", 1, COULEUR_NOIRE)
                        jouer_son(son_empoisonne)
                        jouer_son(son_touche)
                    if adversaire.etat == ETAT.BRULE.value or adversaire.etat == ETAT.EMPOISONNE.value:
                        POSITION_TEXTE = ((POSITION_ZONE_TEXTE[POSITION_X] + (zone_texte.get_width() / 2)) - (texte.get_width() / 2), (POSITION_ZONE_TEXTE[POSITION_Y] + (zone_texte.get_height() / 2)) - (texte.get_height() / 2))
                        # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                        fenetre.blit(fond_combat, (0,0))
                        fenetre.blit(monstre.sprite[SPRITE.DROITE.value-1], POSITION_MONSTRE)
                        fenetre.blit(adversaire.sprite[SPRITE.GAUCHE.value-1], POSITION_ADVERSAIRE)
                        fenetre.blit(zone_monstre, POSITION_ZONE_MONSTRE)
                        fenetre.blit(zone_monstre, POSITION_ZONE_ADVERSAIRE)
                        fenetre.blit(fond_bouton_attaque, POSITION_FOND_BOUTON_ATTAQUE)
                        fenetre.blit(zone_texte, POSITION_ZONE_TEXTE)
                        fenetre.blit(texte, POSITION_TEXTE)
                        fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                        fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                        fenetre.blit(pv_str_monstre, POSITION_ZONE_MONSTRE_PV_STR)
                        fenetre.blit(pv_monstre, POSITION_ZONE_MONSTRE_PV)
                        fenetre.blit(etat_monstre, POSITION_ZONE_MONSTRE_ETAT)
                        fenetre.blit(classe_str_monstre, POSITION_ZONE_MONSTRE_CLASSE_STR)
                        fenetre.blit(classe_monstre, POSITION_ZONE_MONSTRE_CLASSE)                            
                        fenetre.blit(nom_adversaire, POSITION_ZONE_ADVERSAIRE_NOM)
                        fenetre.blit(pv_str_adversaire, POSITION_ZONE_ADVERSAIRE_PV_STR)
                        fenetre.blit(pv_adversaire, POSITION_ZONE_ADVERSAIRE_PV)
                        fenetre.blit(etat_adversaire, POSITION_ZONE_ADVERSAIRE_ETAT)
                        fenetre.blit(classe_str_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE_STR)
                        fenetre.blit(classe_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE)     
                        fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)                                        
                        pygame.display.flip()

                        attendre(2, pygame, sys)
                           
                    tour_adverse = False
                pygame.event.post(pygame.event.Event(MOUSEMOTION)) # pour rerentrer dans la boucle
                
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
                
            # RÉCUPÉRATION DES NOUVELLES VALEURS
            
            nom_monstre = police.render(monstre.nom, 1, COULEUR_NOIRE)
            pv_str_monstre = police.render("PV", 1, COULEUR_NOIRE)
            pv_monstre = police.render(str(monstre.pv) + "/" + str(monstre.pv_max), 1, COULEUR_NOIRE)
            etat_monstre = police.render(monstre.str_etat, 1, COULEUR_NOIRE)
            classe_str_monstre = police.render("CLASSE", 1, COULEUR_NOIRE)
            classe_monstre = police.render(monstre.str_classe, 1, COULEUR_NOIRE)
            
            nom_adversaire = police.render(adversaire.nom, 1, COULEUR_NOIRE)
            pv_str_adversaire = police.render("PV", 1, COULEUR_NOIRE)
            pv_adversaire = police.render(str(adversaire.pv) + "/" + str(adversaire.pv_max), 1, COULEUR_NOIRE)
            etat_adversaire = police.render(adversaire.str_etat, 1, COULEUR_NOIRE)
            classe_str_adversaire = police.render("CLASSE", 1, COULEUR_NOIRE)
            classe_adversaire = police.render(adversaire.str_classe, 1, COULEUR_NOIRE)
            
            nom_attaque = []
            for attaque_actuelle in monstre.attaques:
                nom_attaque.append(police.render(attaque_actuelle.nom, 1, COULEUR_NOIRE))
                                   
            details_attaque = []
            for attaque_actuelle in monstre.attaques:
                details_attaque.append(police_details.render("DÉGATS : " + str(attaque_actuelle.degats) + "    CLASSE : " + attaque_actuelle.str_classe + "    ÉTAT : " + attaque_actuelle.str_etat, 1, COULEUR_NOIRE))

            POSITION_TEXTE = ((POSITION_ZONE_TEXTE[POSITION_X] + (zone_texte.get_width() / 2)) - (texte.get_width() / 2), (POSITION_ZONE_TEXTE[POSITION_Y] + (zone_texte.get_height() / 2)) - (texte.get_height() / 2))
            POSITION_ZONE_MONSTRE_NOM = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (nom_monstre.get_width() / 2), POSITION_ZONE_MONSTRE[POSITION_Y] + 5)
            POSITION_ZONE_MONSTRE_PV_STR = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (pv_str_monstre.get_width() / 2), POSITION_ZONE_MONSTRE_NOM[POSITION_Y] + 30)
            POSITION_ZONE_MONSTRE_PV = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (pv_monstre.get_width() / 2), POSITION_ZONE_MONSTRE_PV_STR[POSITION_Y] + 20)
            POSITION_ZONE_MONSTRE_ETAT = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (etat_monstre.get_width() / 2), POSITION_ZONE_MONSTRE_PV[POSITION_Y] + 30)
            POSITION_ZONE_MONSTRE_CLASSE_STR = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (classe_str_monstre.get_width() / 2), POSITION_ZONE_MONSTRE_ETAT[POSITION_Y] + 30)
            POSITION_ZONE_MONSTRE_CLASSE = ((POSITION_ZONE_MONSTRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (classe_monstre.get_width() / 2), POSITION_ZONE_MONSTRE_CLASSE_STR[POSITION_Y] + 20)
            
            POSITION_ZONE_ADVERSAIRE_NOM = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (nom_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE[POSITION_Y] + 5)
            POSITION_ZONE_ADVERSAIRE_PV_STR = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (pv_str_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE_NOM[POSITION_Y] + 30)
            POSITION_ZONE_ADVERSAIRE_PV = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (pv_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE_PV_STR[POSITION_Y] + 20)
            POSITION_ZONE_ADVERSAIRE_ETAT = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (etat_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE_PV[POSITION_Y] + 30)
            POSITION_ZONE_ADVERSAIRE_CLASSE_STR = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (classe_str_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE_ETAT[POSITION_Y] + 30)
            POSITION_ZONE_ADVERSAIRE_CLASSE = ((POSITION_ZONE_ADVERSAIRE[POSITION_X] + (zone_monstre.get_width() / 2)) - (classe_adversaire.get_width() / 2), POSITION_ZONE_ADVERSAIRE_CLASSE_STR[POSITION_Y] + 20)

            POSITION_ATTAQUE_NOM = (((POSITION_BOUTON_ATTAQUE[0][POSITION_X] + (bouton_attaque.get_width() / 2)) - (nom_attaque[0].get_width() / 2), POSITION_BOUTON_ATTAQUE[0][POSITION_Y] + 5), ((POSITION_BOUTON_ATTAQUE[1][POSITION_X] + (bouton_attaque.get_width() / 2)) - (nom_attaque[1].get_width() / 2), POSITION_BOUTON_ATTAQUE[1][POSITION_Y] + 5), ((POSITION_BOUTON_ATTAQUE[2][POSITION_X] + (bouton_attaque.get_width() / 2)) - (nom_attaque[2].get_width() / 2), POSITION_BOUTON_ATTAQUE[2][POSITION_Y] + 5), ((POSITION_BOUTON_ATTAQUE[3][POSITION_X] + (bouton_attaque.get_width() / 2)) - (nom_attaque[3].get_width() / 2), POSITION_BOUTON_ATTAQUE[3][POSITION_Y] + 5))
            POSITION_ATTAQUE_DETAILS = (((POSITION_BOUTON_ATTAQUE[0][POSITION_X] + (bouton_attaque.get_width() / 2)) - (details_attaque[0].get_width() / 2), POSITION_ATTAQUE_NOM[0][POSITION_Y] + nom_attaque[0].get_height() + 2), ((POSITION_BOUTON_ATTAQUE[1][POSITION_X] + (bouton_attaque.get_width() / 2)) - (details_attaque[1].get_width() / 2), POSITION_ATTAQUE_NOM[1][POSITION_Y] + nom_attaque[1].get_height() + 2), ((POSITION_BOUTON_ATTAQUE[2][POSITION_X] + (bouton_attaque.get_width() / 2)) - (details_attaque[2].get_width() / 2), POSITION_ATTAQUE_NOM[2][POSITION_Y] + nom_attaque[2].get_height() + 2), ((POSITION_BOUTON_ATTAQUE[3][POSITION_X] + (bouton_attaque.get_width() / 2)) - (details_attaque[3].get_width() / 2), POSITION_ATTAQUE_NOM[3][POSITION_Y] + nom_attaque[3].get_height() + 2))
            
                
            # AFFICHAGE DES IMAGES RESTANTES
            
            fenetre.blit(zone_texte, POSITION_ZONE_TEXTE)
            fenetre.blit(texte, POSITION_TEXTE)
            fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
            fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
            fenetre.blit(pv_str_monstre, POSITION_ZONE_MONSTRE_PV_STR)
            fenetre.blit(pv_monstre, POSITION_ZONE_MONSTRE_PV)
            fenetre.blit(etat_monstre, POSITION_ZONE_MONSTRE_ETAT)
            fenetre.blit(classe_str_monstre, POSITION_ZONE_MONSTRE_CLASSE_STR)
            fenetre.blit(classe_monstre, POSITION_ZONE_MONSTRE_CLASSE)
            
            fenetre.blit(nom_adversaire, POSITION_ZONE_ADVERSAIRE_NOM)
            fenetre.blit(pv_str_adversaire, POSITION_ZONE_ADVERSAIRE_PV_STR)
            fenetre.blit(pv_adversaire, POSITION_ZONE_ADVERSAIRE_PV)
            fenetre.blit(etat_adversaire, POSITION_ZONE_ADVERSAIRE_ETAT)
            fenetre.blit(classe_str_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE_STR)
            fenetre.blit(classe_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE)
                
            pygame.display.flip()

            # TESTS DE FIN DE PARTIE ---------------------------------------------------------------------------------------
            if not monstre.vivant:            
                texte_en_cours = "Votre " + monstre.nom + " est MORT ! Vous avez perdu !"
                jouer_son(son_perdu)
            elif not adversaire.vivant:
                texte_en_cours = adversaire.nom + " ennemi est MORT ! Vous avez gagné !"
                jouer_son(son_gagne)
            if not monstre.vivant or not adversaire.vivant:
                texte = police.render(texte_en_cours, 1, COULEUR_NOIRE)
                POSITION_TEXTE = ((POSITION_ZONE_TEXTE[POSITION_X] + (zone_texte.get_width() / 2)) - (texte.get_width() / 2), (POSITION_ZONE_TEXTE[POSITION_Y] + (zone_texte.get_height() / 2)) - (texte.get_height() / 2))
                # RETOUR -> rafraichir l'affichage du menu qui redevient neutre
                fenetre.blit(fond_combat, (0,0))
                fenetre.blit(monstre.sprite[SPRITE.DROITE.value-1], POSITION_MONSTRE)
                fenetre.blit(adversaire.sprite[SPRITE.GAUCHE.value-1], POSITION_ADVERSAIRE)
                fenetre.blit(zone_monstre, POSITION_ZONE_MONSTRE)
                fenetre.blit(zone_monstre, POSITION_ZONE_ADVERSAIRE)
                fenetre.blit(fond_bouton_attaque, POSITION_FOND_BOUTON_ATTAQUE)
                fenetre.blit(zone_texte, POSITION_ZONE_TEXTE)
                fenetre.blit(texte, POSITION_TEXTE)
                fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                fenetre.blit(nom_monstre, POSITION_ZONE_MONSTRE_NOM)
                fenetre.blit(pv_str_monstre, POSITION_ZONE_MONSTRE_PV_STR)
                fenetre.blit(pv_monstre, POSITION_ZONE_MONSTRE_PV)
                fenetre.blit(etat_monstre, POSITION_ZONE_MONSTRE_ETAT)
                fenetre.blit(classe_str_monstre, POSITION_ZONE_MONSTRE_CLASSE_STR)
                fenetre.blit(classe_monstre, POSITION_ZONE_MONSTRE_CLASSE)                            
                fenetre.blit(nom_adversaire, POSITION_ZONE_ADVERSAIRE_NOM)
                fenetre.blit(pv_str_adversaire, POSITION_ZONE_ADVERSAIRE_PV_STR)
                fenetre.blit(pv_adversaire, POSITION_ZONE_ADVERSAIRE_PV)
                fenetre.blit(etat_adversaire, POSITION_ZONE_ADVERSAIRE_ETAT)
                fenetre.blit(classe_str_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE_STR)
                fenetre.blit(classe_adversaire, POSITION_ZONE_ADVERSAIRE_CLASSE)
                fenetre.blit(bouton_retour, POSITION_BOUTON_RETOUR)                                
                pygame.display.flip()

                attendre(3, pygame, sys)
                continuer = False
                pygame.event.clear()
                break

            if event.type == MOUSEBUTTONUP and event.button == BOUTON_GAUCHE:
                selectionner = False
