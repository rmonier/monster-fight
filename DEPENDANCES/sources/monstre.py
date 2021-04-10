"""
   FICHIER MONSTRE.PY :
       - CLASSE Attaque
       - CLASSE Monstre

   DERNIÈRE MÀJ : 11/07/2016
   CRÉÉ PAR ROMAIN MONIER POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :
       - faire en sorte que quand gelé par exemple, plus de chances de plus l'etre aub fur et a mesure
       - rajouter un parametre pour indiquer quand on veut prendre en compte CHEMIN_DEPENDANCES pour le retour du chemin des sprites
---------------------------------------------------------------
"""

# RESSOURCES EXTERNES
from enum import Enum
from DEPENDANCES.sources.monstre_fonctions import *
import json
import random
import sys

# VÉRIFICATION CHEMIN
if getattr(sys, 'frozen', False):
    CHEMIN_DEPENDANCES = sys._MEIPASS + "/"
else:
    CHEMIN_DEPENDANCES = ""

# DÉFINITION DES ENUMS DE CLASSE DU MONSTRE ET D'ATTAQUES
CLASSE = Enum('Classe', 'NORMAL EAU FEU ELECTRIQUE PLANTE ACIER DRAGON INSECTE TENEBRE SPECTRE PSY VOL SOL ROCHE POISON COMBAT GLACE')

# DÉFINITION DES ENUMS D'ÉTAT DU MONSTRE ET D'ATTAQUES
ETAT = Enum('Etat', 'NORMAL PARALYSE BRULE GELE EMPOISONNE ENDORMI CONFUS')

# DÉFINITION DES ENUMS D'ATTAQUES DU MONSTRE
ATTAQUE_NUM = Enum('AttaqueNum', 'PREMIERE DEUXIEME TROISIEME QUATRIEME')

EFFICACE = Enum('Efficace', 'NORMAL FORT FAIBLE NON')

ATTAQUE = Enum('AttaqueEtat', 'ERREUR RECUE RATE_NON_EFFICACE RATE_MALCHANCE RATE_ESQUIVE RATE_PARALYSE RATE_CONFUS RATE_GELE RATE_ENDORMI')

RATIO_DEGATS_FORTS = 1.5
RATIO_DEGATS_FAIBLES = 0.5

# DÉFINITION DES ENUMS DE SPRITE DU MONSTRE
SPRITE = Enum('Sprite', 'HAUT GAUCHE DROITE')

CHEMIN_SPRITE_DEFAUT_HAUT = "DEPENDANCES/images/sprites/defaut/haut.gif"
CHEMIN_SPRITE_DEFAUT_GAUCHE = "DEPENDANCES/images/sprites/defaut/gauche.gif"
CHEMIN_SPRITE_DEFAUT_DROITE = "DEPENDANCES/images/sprites/defaut/droite.gif"

# DÉFINITION DE LA CLASSE Attaque ---------------------------------------------------------------------------------------------
class Attaque:
    """Classe Attaque"""

    # CONSTRUCTEUR (initialisation des attributs en mode privé) ---------------------------------------------------------------------------------------------
    
    def __init__(self, nom='VIDE', degats='NULL', classe=CLASSE.NORMAL.value, utilisations_max=1, etat=ETAT.NORMAL.value, utilisations=-1):
        attaque_existe = True
        # NOM
        if nom:
            self.__nom = nom
        else:
            self.__nom = 'NULL'

        # DÉGATS
        if(isinstance(degats, str)):
            if(degats == 'NULL'):
                self.__attaque_existe = False
                self.__nom = 'VIDE'
                attaque_existe = False
        else:
            self.__attaque_existe = True
            self.__degats = degats
            
        # CLASSE
        classe_existe = False
        for i in CLASSE:
            i = i.value
            if(classe == i):
                classe_existe = True
                break;
        if(classe_existe):
            self.__classe = classe
        else:
            self.__classe = CLASSE.NORMAL.value

        # ÉTAT
        etat_existe = False
        for i in ETAT:
            i = i.value
            if(etat == i):
                etat_existe = True
                break;
        if(etat_existe):
            self.__etat = etat
        else:
            self.__etat = ETAT.NORMAL.value
                
        # UTILISATIONS MAX
        if(utilisations_max <= 0):
            utilisations_max = 1
        self.__utilisations_max = utilisations_max
            
        # UTILISATIONS
        if(utilisations == -1):
            utilisations = utilisations_max
        if(utilisations < 0):
            utilisations = 0
        if(utilisations > utilisations_max):
            utilisations = utilisations_max
        self.__utilisations = utilisations

        # UTILISABLE
        if(utilisations > 0):
            self.__utilisable = True
        else:
            self.__utilisable = False

    # MÉTHODES GETTER --------------------------------------------------------------------------------------------

    def _getNom(self):
        return self.__nom
    def _getDegats(self):
        return self.__degats
    def _getClasse(self):
        return self.__classe
    def _getStrClasse(self):
        return str(nom_classe_str(CLASSE, self.__classe))
    def _getEtat(self):
        return self.__etat
    def _getStrEtat(self):
        return str(nom_etat_str(ETAT, self.__etat))
    def _getUtilisations(self):
        return self.__utilisations
    def _getUtilisationsMax(self):
        return self.__utilisations_max
    def _getUtilisable(self):
        return self.__utilisable
    def _getAttaqueExiste(self):
        return self.__attaque_existe

    # MÉTHODES SETTER --------------------------------------------------------------------------------------------

    
    def _setNom(self, nom):
        if nom:
            self.__nom = nom

    def _setDegats(self, degats):
        self.__degats = degats
        
    def _setClasse(self, classe):
        classe_existe = False
        for i in CLASSE:
            i = i.value
            if(classe == i):
                classe_existe = True
                break;
        if(classe_existe):
            self.__classe = classe
        
    def _setEtat(self, etat):
        etat_existe = False
        for i in ETAT:
            i = i.value
            if(etat == i):
                etat_existe = True
                break;
        if(etat_existe):
            self.__etat = etat
        
    def _setUtilisationsMax(self, points_vie_max):
        if(utilisations_max <= 0):
            utilisations_max = 1
        self.__utilisations_max = utilisations_max
        if(self.__utilisations > utilisations_max):
            self.__utilisations = utilisations_max
            
    def _setUtilisations(self, points_vie):
        if(utilisations <= 0):
            utilisations = 0
            self.__utilisable = False
        else:
            self.__utilisable = True
        if(utilisations > utilisations_max):
            utilisations = utilisations_max
        self.__utilisations = utilisations
        
    # LINK DES GETTERS ET SETTERS AUX ATTRIBUTS ---------------------------------------------------------------------------------------------
    
    nom = property(_getNom, _setNom)
    classe = property(_getClasse, _setClasse)
    degats = property(_getDegats, _setDegats)
    etat = property(_getEtat, _setEtat)
    str_classe = property(_getStrClasse)
    str_etat = property(_getStrEtat)
    utilisations = property(_getUtilisations, _setUtilisations)
    utilisations_max = property(_getUtilisationsMax, _setUtilisationsMax)
    attaque_existe = property(_getAttaqueExiste)
    utilisable = property(_getUtilisable)
    
        
# DÉFINITION DE LA CLASSE Monstre ---------------------------------------------------------------------------------------------
class Monstre:
    """Classe Monstre"""
    
    # CONSTRUCTEUR (initialisation des attributs en mode privé) ---------------------------------------------------------------------------------------------
    
    def __init__(self, pygame, nom='NULL', chemin_sprite=(CHEMIN_SPRITE_DEFAUT_HAUT, CHEMIN_SPRITE_DEFAUT_GAUCHE, CHEMIN_SPRITE_DEFAUT_DROITE), classe=CLASSE.NORMAL.value, points_vie_max=1, attaques=(Attaque(), Attaque(), Attaque(), Attaque()), points_vie=-1, etat=ETAT.NORMAL.value):
        # NOM
        if nom:
            self.__nom = nom
        else:
            self.__nom = 'NULL'

        # CLASSE 
        classe_existe = False
        for i in CLASSE:
            i = i.value
            if(classe == i):
                classe_existe = True
                break;
        if(classe_existe):
            self.__classe = classe
        else:
            self.__classe = CLASSE.NORMAL.value

        # ÉTAT
        etat_existe = False
        for i in ETAT:
            i = i.value
            if(etat == i):
                etat_existe = True
                break;
        if(etat_existe):
            self.__etat = etat
        else:
            self.__etat = ETAT.NORMAL.value

        # PV MAX
        points_vie_max = int(points_vie_max)
        if(points_vie_max <= 0):
            points_vie_max = 1
        self.__points_vie_max = points_vie_max

        # PV
        points_vie = int(points_vie)
        if(points_vie == -1):
            points_vie = points_vie_max
        if(points_vie < 0):
            points_vie = 0
        if(points_vie > points_vie_max):
            points_vie = points_vie_max
        self.__points_vie = points_vie

        # SPRITE  => faire tests voir si on arrive à charger, sinon charger ceux par défaut
        haut = pygame.image.load(CHEMIN_DEPENDANCES + chemin_sprite[SPRITE.HAUT.value-1]).convert()
        gauche = pygame.image.load(CHEMIN_DEPENDANCES + chemin_sprite[SPRITE.GAUCHE.value-1]).convert()
        droite = pygame.image.load(CHEMIN_DEPENDANCES + chemin_sprite[SPRITE.DROITE.value-1]).convert()
        self.__chemin_sprite = chemin_sprite
        self.__sprite = (haut, gauche, droite)

        # ATTAQUES
        self.__attaques = attaques

        # VIVANT
        if(points_vie > 0):
            self.__vivant = True
        else:
            self.__vivant = False
        
    # MÉTHODES GETTER --------------------------------------------------------------------------------------------
    
    def _getNom(self):
        return self.__nom
    def _getClasse(self):
        return self.__classe
    def _getStrClasse(self):
        return str(nom_classe_str(CLASSE, self.__classe))
    def _getEtat(self):
        return self.__etat
    def _getStrEtat(self):
        return str(nom_etat_str(ETAT, self.__etat))
    def _getPV(self):
        return self.__points_vie
    def _getPVMax(self):
        return self.__points_vie_max
    def _getSprite(self):
        return self.__sprite
    def _getCheminSprite(self):
        return self.__chemin_sprite
    def _getAttaques(self):
        return self.__attaques
    def _getVivant(self):
        return self.__vivant

    # MÉTHODES SETTER ---------------------------------------------------------------------------------------------
    
    def _setNom(self, nom):
        if nom:
            self.__nom = nom
        
    def _setClasse(self, classe):
        classe_existe = False
        for i in CLASSE:
            i = i.value
            if(classe == i):
                classe_existe = True
                break;
        if(classe_existe):
            self.__classe = classe
        
    def _setEtat(self, etat):
        etat_existe = False
        for i in ETAT:
            i = i.value
            if(etat == i):
                etat_existe = True
                break;
        if(etat_existe):
            self.__etat = etat
        
    def _setPVMax(self, points_vie_max):
        points_vie_max = int(points_vie_max)
        if(points_vie_max <= 0):
            points_vie_max = 1
        self.__points_vie_max = points_vie_max
        if(self.__points_vie > points_vie_max):
            self.__points_vie = points_vie_max
            
    def _setPV(self, points_vie):
        points_vie = int(points_vie)
        if(points_vie > self.__points_vie_max):
            points_vie = self.__points_vie_max
        if(points_vie <= 0):
            points_vie = 0
            self.__vivant = False
        else:
            self.__vivant = True
        self.__points_vie = points_vie
        
    def _setSprite(self, sprite):
        self.__sprite = sprite
        
    def _setCheminSprite(self, chemin_sprite):
        haut = pygame.image.load(CHEMIN_DEPENDANCES + chemin_sprite[SPRITE.HAUT.value-1]).convert()
        gauche = pygame.image.load(CHEMIN_DEPENDANCES + chemin_sprite[SPRITE.GAUCHE.value-1]).convert()
        droite = pygame.image.load(CHEMIN_DEPENDANCES + chemin_sprite[SPRITE.DROITE.value-1]).convert()
        sprite = (haut, gauche, droite)
        self.__chemin_sprite = chemin_sprite
        self._setSprite(sprite)
        
    def _setAttaques(self, attaques):
        self.__attaques = attaques
    
    # LINK DES GETTERS ET SETTERS AUX ATTRIBUTS ---------------------------------------------------------------------------------------------
    
    nom = property(_getNom, _setNom)
    classe = property(_getClasse, _setClasse)
    etat = property(_getEtat, _setEtat)
    str_classe = property(_getStrClasse)
    str_etat = property(_getStrEtat)
    pv = property(_getPV, _setPV)
    pv_max = property(_getPVMax, _setPVMax)
    sprite = property(_getSprite, _setSprite)
    chemin_sprite = property(_getCheminSprite, _setCheminSprite)
    attaques = property(_getAttaques, _setAttaques)
    vivant = property(_getVivant)

    # MÉTHODES D'ACTIONS ---------------------------------------------------------------------------------------------
    
    def attaquer(self, adversaire, attaque):
        
        # TEST DE RÉUSSITE
        nombre_aleatoire = random.randint(1, 100)
        if(nombre_aleatoire > 95): # 5% de chances de rater l'attaque
            return ATTAQUE.RATE_MALCHANCE.value, 0, 0, False, False

        # TESTS D'ÉTATS
        if(self.etat == ETAT.PARALYSE.value):
            nombre_aleatoire = random.randint(1, 100)
            if(nombre_aleatoire > 20): # 80% de chances de rater l'attaque
                return ATTAQUE.RATE_PARALYSE.value, 0, 0, False, False
        if(self.etat == ETAT.GELE.value):
            nombre_aleatoire = random.randint(1, 100)
            if(nombre_aleatoire > 10): # 90% de chances de rater l'attaque
                return ATTAQUE.RATE_GELE.value, 0, 0, False, False
        if(self.etat == ETAT.ENDORMI.value):
            nombre_aleatoire = random.randint(1, 100)
            if(nombre_aleatoire > 40): # 60% de chances de rater l'attaque
                return ATTAQUE.RATE_ENDORMI.value, 0, 0, False, False
        if(self.etat == ETAT.CONFUS.value):
            nombre_aleatoire = random.randint(1, 100)
            if(nombre_aleatoire > 50): # 50% de chances de rater l'attaque
                return ATTAQUE.RATE_CONFUS.value, nombre_aleatoire, 0, False, False
        
        # TEST DE PUISSANCE
        degats = attaque.degats        
        efficacite = efficacite_classes(EFFICACE, CLASSE, attaque.classe, adversaire.classe)
        if(efficacite == EFFICACE.NORMAL.value):
            degats = degats
        elif(efficacite == EFFICACE.FORT.value):
            degats *= RATIO_DEGATS_FORTS
        elif(efficacite == EFFICACE.FAIBLE.value):
            degats *= RATIO_DEGATS_FAIBLES
        elif(efficacite == EFFICACE.NON.value):
            return ATTAQUE.RATE_NON_EFFICACE.value, 0, 0, False, False
        else:
            return ATTAQUE.ERREUR.value, 0, 0, False, False

        # TEST DE COUP CRITIQUE
        nombre_aleatoire = random.randint(1, 100)
        critique = False
        if(nombre_aleatoire <= 5): # 5% de chances de faire un coup critique
            critique = True
            if(nombre_aleatoire == 1):
                degats *= 3
            elif(nombre_aleatoire == 2):
                degats *= 2.75
            elif(nombre_aleatoire == 3):
                degats *= 2.5
            elif(nombre_aleatoire == 4):
                degats *= 2.25
            elif(nombre_aleatoire == 5):
                degats *= 2

        return adversaire.recevoir_attaque(degats, attaque, efficacite, critique)

    def recevoir_attaque(self, degats, attaque, efficacite, critique):
        
        # TESTS D'ÉTATS POUR ESQUIVES
        if(self.etat == ETAT.PARALYSE.value):
            nombre_aleatoire = random.randint(1, 100)
            if(nombre_aleatoire > 0): # 0% de chances d'esquiver
                self.pv -= degats
            else:
                return ATTAQUE.RATE_ESQUIVE.value, 0, 0, False, False
        elif(self.etat == ETAT.GELE.value):
            nombre_aleatoire = random.randint(1, 100)
            if(nombre_aleatoire > 0): # 0% de chances d'esquiver
                self.pv -= degats
            else:
                return ATTAQUE.RATE_ESQUIVE.value, 0, 0, False, False
        elif(self.etat == ETAT.ENDORMI.value):
            nombre_aleatoire = random.randint(1, 100)
            if(nombre_aleatoire > 0): # 0% de chances d'esquiver
                self.pv -= degats
            else:
                return ATTAQUE.RATE_ESQUIVE.value, 0, 0, False, False
        elif(self.etat == ETAT.CONFUS.value):
            nombre_aleatoire = random.randint(1, 100)
            if(nombre_aleatoire < 95): # 5% de chances d'esquiver
                self.pv -= degats
            else:
                return ATTAQUE.RATE_ESQUIVE.value, 0, 0, False, False
        else:
            nombre_aleatoire = random.randint(1, 100)
            if(nombre_aleatoire < 90): # 10% de chances d'esquiver
                self.pv -= degats
            else:
                return ATTAQUE.RATE_ESQUIVE.value, 0, 0, False, False

        # TESTS DE RÉCÉPTION D'ÉTATS
        nombre_aleatoire = random.randint(1, 100)
        touche_etat = False
        if(nombre_aleatoire > 50 and attaque.etat != ETAT.NORMAL.value): # 50% de chances de recevoir l'état
            touche_etat = True
            self.etat = attaque.etat        

        return ATTAQUE.RECUE.value, degats, efficacite, critique, touche_etat

    def recevoir_vie(self, vie):
        self.pv += vie
