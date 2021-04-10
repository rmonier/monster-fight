"""
   FICHIER MONSTRE_FONCTIONS.PY :
       - FONCTION efficacite_classes
       - FONCTION nom_classe_str
       - FONCTION nom_etat_str

   DERNIÈRE MÀJ : 03/05/2016
   CRÉÉ PAR ROMAIN MONIER POUR LE PROJET D'ISN
   MAINTENU PAR ROMAIN MONIER
   2015/2016
---------------------------------------------------------------
   INFOS :
       - compare deux types et dit ce qu'il en ressort (super ou pas efficace etc)
       - renvoi les chaines de noms de classe
---------------------------------------------------------------
"""

# FONCTIONS

def nom_etat_str(ETAT, etat):
    if(etat == ETAT.NORMAL.value):
        return "NORMAL"
    elif(etat == ETAT.PARALYSE.value):
        return "PARALYSÉ"
    elif(etat == ETAT.BRULE.value):
        return "BRÛLÉ"
    elif(etat == ETAT.GELE.value):
        return "GELÉ"
    elif(etat == ETAT.EMPOISONNE.value):
        return "EMPOISONNÉ"
    elif(etat == ETAT.ENDORMI.value):
        return "ENDORMI"
    elif(etat == ETAT.CONFUS.value):
        return "CONFUS"
    else:
        return "ERREUR"
    
def nom_classe_str(CLASSE, classe):
    if(classe == CLASSE.NORMAL.value):
        return "NORMAL"
    elif(classe == CLASSE.COMBAT.value):
        return "COMBAT"
    elif(classe == CLASSE.EAU.value):
        return "EAU"
    elif(classe == CLASSE.FEU.value):
        return "FEU"
    elif(classe == CLASSE.ELECTRIQUE.value):
        return "ÉLECTRIQUE"
    elif(classe == CLASSE.PLANTE.value):
        return "PLANTE"
    elif(classe == CLASSE.ACIER.value):
        return "ACIER"
    elif(classe == CLASSE.DRAGON.value):
        return "DRAGON"
    elif(classe == CLASSE.INSECTE.value):
        return "INSECTE"
    elif(classe == CLASSE.TENEBRE.value):
        return "TÉNÈBRE"
    elif(classe == CLASSE.SPECTRE.value):
        return "SPECTRE"
    elif(classe == CLASSE.PSY.value):
        return "PSY"
    elif(classe == CLASSE.VOL.value):
        return "VOL"
    elif(classe == CLASSE.SOL.value):
        return "SOL"
    elif(classe == CLASSE.ROCHE.value):
        return "ROCHE"
    elif(classe == CLASSE.POISON.value):
        return "POISON"
    elif(classe == CLASSE.GLACE.value):
        return "GLACE"
    else:
        return "ERREUR"

def efficacite_classes(EFFICACE, CLASSE, attaque, adversaire):

    # NORMAL
    if(attaque == CLASSE.NORMAL.value):
        if(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.SPECTRE.value):
            return EFFICACE.NON.value
        elif(adversaire == CLASSE.ROCHE.value):
            return EFFICACE.FAIBLE.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # EAU
    elif(attaque == CLASSE.EAU.value):
        if(adversaire == CLASSE.EAU.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.FEU.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.PLANTE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.DRAGON.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.SOL.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.ROCHE.value):
            return EFFICACE.FORT.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # FEU
    elif(attaque == CLASSE.FEU.value):
        if(adversaire == CLASSE.EAU.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.FEU.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.PLANTE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.DRAGON.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.INSECTE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.ROCHE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.GLACE.value):
            return EFFICACE.FORT.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # ELECTRIQUE
    elif(attaque == CLASSE.ELECTRIQUE.value):
        if(adversaire == CLASSE.ELECTRIQUE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.PLANTE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.DRAGON.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.VOL.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.SOL.value):
            return EFFICACE.NON.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # PLANTE
    elif(attaque == CLASSE.PLANTE.value):
        if(adversaire == CLASSE.EAU.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.FEU.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.PLANTE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.DRAGON.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.INSECTE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.VOL.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.SOL.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.ROCHE.value):
            return EFFICACE.FORT.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # ACIER
    elif(attaque == CLASSE.ACIER.value):
        if(adversaire == CLASSE.EAU.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.FEU.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.ELECTRIQUE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.ROCHE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.COMBAT.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.GLACE.value):
            return EFFICACE.FORT.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # DRAGON
    elif(attaque == CLASSE.DRAGON.value):
        if(adversaire == CLASSE.DRAGON.value):
            return EFFICACE.FORT.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # INSECTE
    elif(attaque == CLASSE.INSECTE.value):
        if(adversaire == CLASSE.FEU.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.PLANTE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.INSECTE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.TENEBRE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.SPECTRE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.PSY.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.VOL.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.SOL.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.ROCHE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.POISON.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.COMBAT.value):
            return EFFICACE.FAIBLE.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # TENEBRE
    elif(attaque == CLASSE.TENEBRE.value):
        if(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.TENEBRE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.SPECTRE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.PSY.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.COMBAT.value):
            return EFFICACE.FAIBLE.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # SPECTRE
    elif(attaque == CLASSE.SPECTRE.value):
        if(adversaire == CLASSE.NORMAL.value):
            return EFFICACE.NON.value
        elif(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.TENEBRE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.SPECTRE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.PSY.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.COMBAT.value):
            return EFFICACE.FAIBLE.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # PSY
    elif(attaque == CLASSE.PSY.value):
        if(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.TENEBRE.value):
            return EFFICACE.NON.value
        elif(adversaire == CLASSE.PSY.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.POISON.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.COMBAT.value):
            return EFFICACE.FORT.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # VOL
    elif(attaque == CLASSE.VOL.value):
        if(adversaire == CLASSE.PLANTE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.INSECTE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.ROCHE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.COMBAT.value):
            return EFFICACE.FORT.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # SOL
    elif(attaque == CLASSE.SOL.value):
        if(adversaire == CLASSE.ELECTRIQUE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.PLANTE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.INSECTE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.VOL.value):
            return EFFICACE.NON.value
        elif(adversaire == CLASSE.SOL.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.ROCHE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.POISON.value):
            return EFFICACE.FORT.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # ROCHE
    elif(attaque == CLASSE.ROCHE.value):
        if(adversaire == CLASSE.FEU.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.VOL.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.SOL.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.ROCHE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.COMBAT.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.GLACE.value):
            return EFFICACE.FORT.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # POISON
    elif(attaque == CLASSE.POISON.value):
        if(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.SPECTRE.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.POISON.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.COMBAT.value):
            return EFFICACE.FAIBLE.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # COMBAT
    elif(attaque == CLASSE.COMBAT.value):
        if(adversaire == CLASSE.NORMAL.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.TENEBRE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.SPECTRE.value):
            return EFFICACE.NON.value
        elif(adversaire == CLASSE.PSY.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.VOL.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.ROCHE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.POISON.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.GLACE.value):
            return EFFICACE.FORT.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
        
    # GLACE
    elif(attaque == CLASSE.GLACE.value):
        if(adversaire == CLASSE.EAU.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.FEU.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.PLANTE.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.ACIER.value):
            return EFFICACE.FAIBLE.value
        elif(adversaire == CLASSE.DRAGON.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.VOL.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.SOL.value):
            return EFFICACE.FORT.value
        elif(adversaire == CLASSE.GLACE.value):
            return EFFICACE.FAIBLE.value
        else:
            for actuelle_classe in CLASSE:
                if(adversaire == actuelle_classe.value):
                    return EFFICACE.NORMAL.value
            return False
    else:
        return False
