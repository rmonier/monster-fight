"""
   FICHIER GESTION_OPTIONS.PY :
       - FONCTION sauver_options
       - FONCTION lire_options

   DERNIÈRE MÀJ : 11/07/2016
   CRÉÉ PAR ROMAIN MONIER POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :
       - enregistre les options envoyées
       - retourne liste des options
---------------------------------------------------------------
"""

# RESSOURCES EXTERNES

import sqlite3
import sys
import os
from appdirs import *

# VÉRIFICATION CHEMIN
if getattr(sys, 'frozen', False):
    CHEMIN_DEPENDANCES = sys._MEIPASS + "/"
else:
    CHEMIN_DEPENDANCES = ""

# FONCTIONS

def sauver_options(son, musique):
    
    CHEMIN_APPDATA = user_data_dir("MONSTER FIGHT")

    if not os.path.exists(CHEMIN_APPDATA):
        os.makedirs(CHEMIN_APPDATA)
    
    bdd = sqlite3.connect(CHEMIN_APPDATA + '/sauvegarde.db')

    req = bdd.cursor()
            
    req.execute('UPDATE Options SET son = ?, musique = ?', (int(son), int(musique)))
    bdd.commit()
    
    bdd.close()

    return True

def lire_options():
    
    CHEMIN_APPDATA = user_data_dir("MONSTER FIGHT")

    if not os.path.exists(CHEMIN_APPDATA):
        os.makedirs(CHEMIN_APPDATA)
    
    bdd = sqlite3.connect(CHEMIN_APPDATA + '/sauvegarde.db')

    req = bdd.cursor()

    req = bdd.cursor()
    req.execute('''
    CREATE TABLE IF NOT EXISTS Options(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         son SMALLINT UNSIGNED,
         musique SMALLINT UNSIGNED
    )
    ''')
    
    bdd.commit()

    req.execute('SELECT son, musique FROM Options')

    liste_donnees_options = req.fetchone()

    if not liste_donnees_options:
        req.execute('INSERT INTO Options (son, musique) VALUES (?,?)', (1,1))
        bdd.commit()
        son = True
        musique = True
    else:
        son = bool(int(liste_donnees_options[0]))
        musique = bool(int(liste_donnees_options[1]))
        
    bdd.close()

    liste_options = {}
    liste_options["son"] = son
    liste_options["musique"] = musique

    return liste_options
