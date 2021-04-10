"""
   FICHIER RESTAURER_MONSTRES.PY :
       - FONCTION restaurer_monstres

   DERNIÈRE MÀJ : 11/07/2016
   CRÉÉ PAR ROMAIN MONIER POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :
       - restaurer les monstres par défaut
---------------------------------------------------------------
"""

# RESSOURCES EXTERNES

import sqlite3
from appdirs import *
import json
import os
from DEPENDANCES.sources.monstre import *

# FONCTIONS

def restaurer_monstres(pygame):

    CHEMIN_APPDATA = user_data_dir("MONSTER FIGHT")

    if not os.path.exists(CHEMIN_APPDATA):
        os.makedirs(CHEMIN_APPDATA)
    
    bdd = sqlite3.connect(CHEMIN_APPDATA + '/sauvegarde.db')

    req = bdd.cursor()
    req.execute('''
    CREATE TABLE IF NOT EXISTS Monstres(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         nom VARCHAR(30) NOT NULL,
         chemin_sprite VARCHAR(255),
         classe SMALLINT UNSIGNED,
         points_vie_max SMALLINT UNSIGNED NOT NULL,
         attaques TEXT,
         points_vie SMALLINT UNSIGNED,
         etat SMALLINT UNSIGNED
    )
    ''')
    
    bdd.commit()

    req.execute('DELETE FROM Monstres')
    bdd.commit()

    # Monstres par défauts :
    liste_monstres = [Monstre(pygame, 'BRUTALIZATOR',('DEPENDANCES/images/sprites/brutalizator/haut.gif', 'DEPENDANCES/images/sprites/brutalizator/gauche.gif', 'DEPENDANCES/images/sprites/brutalizator/droite.gif'), CLASSE.COMBAT.value, 1000, (Attaque("COUP DE POING", 50, CLASSE.COMBAT.value, 35), Attaque("EXPLOSION CRÂNIENNE", 100, CLASSE.SOL.value, 5, ETAT.CONFUS.value), Attaque("FIGHTER PUNCH", 250, CLASSE.ROCHE.value, 1, ETAT.CONFUS.value), Attaque("COUPURE", 20, CLASSE.INSECTE.value, 20))), Monstre(pygame, 'POURFENDATOR',('DEPENDANCES/images/sprites/pourfendator/haut.gif', 'DEPENDANCES/images/sprites/pourfendator/gauche.gif', 'DEPENDANCES/images/sprites/pourfendator/droite.gif'), CLASSE.INSECTE.value, 800, (Attaque("TORRENT", 100, CLASSE.EAU.value, 10), Attaque("BOURDONNEMENT", 50, CLASSE.INSECTE.value, 35, ETAT.CONFUS.value), Attaque("APPEL DE LA NATURE", 20, CLASSE.PLANTE.value, 35, ETAT.EMPOISONNE.value), Attaque("PULSION CANNIBALE", 300, CLASSE.DRAGON.value, 1))), Monstre(pygame, 'DEZINGATOR',('DEPENDANCES/images/sprites/dezingator/haut.gif', 'DEPENDANCES/images/sprites/dezingator/gauche.gif', 'DEPENDANCES/images/sprites/dezingator/droite.gif'), CLASSE.PSY.value, 600, (Attaque("PSYCHO EFFECT", 80, CLASSE.PSY.value, 20, ETAT.CONFUS.value), Attaque("IMPULSION", 0, CLASSE.ELECTRIQUE.value, 20, ETAT.PARALYSE.value), Attaque("LAME D'ARGENT", 250, CLASSE.ACIER.value, 3), Attaque("EXPULSION", 650, CLASSE.SPECTRE.value, 1))), Monstre(pygame, 'BURNATOR',('DEPENDANCES/images/sprites/burnator/haut.gif', 'DEPENDANCES/images/sprites/burnator/gauche.gif', 'DEPENDANCES/images/sprites/burnator/droite.gif'), CLASSE.FEU.value, 500, (Attaque("SALUTATIONS", 10, CLASSE.NORMAL.value, 100), Attaque("DOOMED LIGHT", 250, CLASSE.FEU.value, 10, ETAT.BRULE.value), Attaque("FEU FOLLET", 50, CLASSE.FEU.value, 35, ETAT.CONFUS.value), Attaque("ENTAILLE", 20, CLASSE.VOL.value, 20))), Monstre(pygame, 'TENEBRATOR',('DEPENDANCES/images/sprites/tenebrator/haut.gif', 'DEPENDANCES/images/sprites/tenebrator/gauche.gif', 'DEPENDANCES/images/sprites/tenebrator/droite.gif'), CLASSE.TENEBRE.value, 1500, (Attaque("END OF THE WORLD", 950, CLASSE.TENEBRE.value, 2, ETAT.BRULE.value), Attaque("MORT RÊVEUSE", 400, CLASSE.TENEBRE.value, 2, ETAT.ENDORMI.value), Attaque("CONDAMNATION", 250, CLASSE.GLACE.value, 100, ETAT.GELE.value), Attaque("LAME FUNESTE", 42, CLASSE.POISON.value, 42, ETAT.EMPOISONNE.value)))]

    liste_monstres_a_restaurer = []
    for monstre in liste_monstres:
        liste_attaques = []
        liste_chemins = []
        for attaque in monstre.attaques:
            attaque_str = {}
            attaque_str['nom'] = attaque.nom
            attaque_str['degats'] = attaque.degats
            attaque_str['classe'] = attaque.classe
            attaque_str['utilisations_max'] = attaque.utilisations_max
            attaque_str['etat'] = attaque.etat
            attaque_str['utilisations'] = attaque.utilisations
            liste_attaques.append(attaque_str)
        for chemin in monstre.chemin_sprite:
            liste_chemins.append(chemin)
            
        liste_monstres_a_restaurer.append((monstre.nom, json.dumps(liste_chemins), monstre.classe, monstre.pv_max, json.dumps(liste_attaques), monstre.pv, monstre.etat))
        
    req.executemany('INSERT INTO Monstres (nom,chemin_sprite,classe,points_vie_max,attaques,points_vie,etat) VALUES (?,?,?,?,?,?,?)', liste_monstres_a_restaurer)
    bdd.commit()
 
    bdd.close()

    return True
