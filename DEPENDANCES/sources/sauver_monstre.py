"""
   FICHIER SAUVER_MONSTRE.PY :
       - FONCTION sauver_monstre

   DERNIÈRE MÀJ : 11/07/2016
   CRÉÉ PAR ROMAIN MONIER POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :
       - PLUS TARD -> il faut lui envoyer une liste d'objets Monstre
       - il faut envoyer un objet Monstre et l'id du monstre à remplacer
       - enregistre 1 monstre (ou modifie le précédent) / PLUS TARD -> des nouveaux monstres
       - PLUS TARD -> pour attaques faire un lien avec l'autre table
---------------------------------------------------------------
"""

# RESSOURCES EXTERNES

import sqlite3
import json
import os
from appdirs import *

# FONCTIONS

def sauver_monstre(monstre, id_choisi):
    
    if not monstre:
        return False
    
    CHEMIN_APPDATA = user_data_dir("MONSTER FIGHT")

    if not os.path.exists(CHEMIN_APPDATA):
        os.makedirs(CHEMIN_APPDATA)
    
    bdd = sqlite3.connect(CHEMIN_APPDATA + '/sauvegarde.db')

    req = bdd.cursor()

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
            
    req.execute('UPDATE Monstres SET nom = ?, chemin_sprite = ?, classe = ?, points_vie_max = ?, attaques = ?, points_vie = ?, etat = ? WHERE id = ?', (monstre.nom, json.dumps(liste_chemins), monstre.classe, monstre.pv_max, json.dumps(liste_attaques), monstre.pv, monstre.etat, id_choisi))
    bdd.commit()
    
    bdd.close()

    return True
