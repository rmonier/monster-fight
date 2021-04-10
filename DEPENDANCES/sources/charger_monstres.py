"""
   FICHIER CHARGER_MONSTRES.PY :
     - FONCTION charger_monstres
    
   DERNIÈRE MÀJ : 11/07/2016
   CRÉÉ PAR ROMAIN MONIER POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :
       - renvoi tuple d'objets Monstre en créant ceux sauvés dans la BDD SQLite
---------------------------------------------------------------
"""

import sqlite3
import json
import os
from appdirs import *
from DEPENDANCES.sources.monstre import *
from DEPENDANCES.sources.restaurer_monstres import *

# FONCTIONS

def charger_monstres(pygame):
    
    CHEMIN_APPDATA = user_data_dir("MONSTER FIGHT")

    if not os.path.exists(CHEMIN_APPDATA):
        os.makedirs(CHEMIN_APPDATA)
    
    bdd = sqlite3.connect(CHEMIN_APPDATA + '/sauvegarde.db')
    
    monstre_existe = False
    while not monstre_existe:
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

        req.execute('SELECT nom, chemin_sprite, classe, points_vie_max, attaques, points_vie, etat FROM Monstres')

        liste_donnees_monstres = req.fetchall()

        liste_monstres = []
        for monstre in liste_donnees_monstres:
            monstre_existe = True
            attaque = json.loads(monstre[4])
            liste_monstres.append(Monstre(pygame, monstre[0], json.loads(monstre[1]), monstre[2], monstre[3], (Attaque(attaque[0]['nom'], attaque[0]['degats'], attaque[0]['classe'], attaque[0]['utilisations_max'], attaque[0]['etat'], attaque[0]['utilisations']), Attaque(attaque[1]['nom'], attaque[1]['degats'], attaque[1]['classe'], attaque[1]['utilisations_max'], attaque[1]['etat'], attaque[1]['utilisations']), Attaque(attaque[2]['nom'], attaque[2]['degats'], attaque[2]['classe'], attaque[2]['utilisations_max'], attaque[2]['etat'], attaque[2]['utilisations']), Attaque(attaque[3]['nom'], attaque[3]['degats'], attaque[3]['classe'], attaque[3]['utilisations_max'], attaque[3]['etat'], attaque[3]['utilisations'])), monstre[5], monstre[6]))

        if not monstre_existe:
            restaurer_monstres(pygame)
            
    bdd.close()
    
    return liste_monstres
