"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
from stockage import *
from datetime import *
def chercheNom(nom):
    for x in repertoire:
        if nom == repertoire[x][0]:
            return x
    #recherche d un perso par nom ou prenom , et renvoie toute les info sur cette perso
def cherchePrenom(Prenom):
    for x in repertoire:
        if nom == repertoire[x][1]:
            return x

#cherche toutes les personnes ayant un num et les met dans une liste
def cherchenums():
    persoNums = []
    for x in repertoire:
        if  getPrenom(x)  != "":
            persoNums += [x,]
    return persoNums

#cette fonction retourne une liste qui contient les perso qui ont leurs anniversaire le mois courant
def chercheAnnif():
    Annif_Ce_mois =[]
    today = date.today()
    moisactu = today.month
    for x in repertoire:
        if existeDate(x) != -1:
            m= getDate(x)[1]
            if moisactu == m :
                Annif_Ce_mois += [x,]
    return Annif_Ce_mois
