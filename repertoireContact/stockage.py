"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
from os.path import exists

repertoire =[]
DATE_Inconnu=-1

def creerEntree(nom,prenom,num1,num2,adresse1,adresse2,email,date):
     return (nom,prenom,num1,num2,adresse1,adresse2,email,date)

def addPerso(nom,prenom,num1,num2,adresse1,adresse2,email,date):
    global repertoire
    repertoire += [creerEntree(nom,prenom,num1,num2,adresse1,adresse2,email,date),]

def delPerso(x):
    global repertoire
    del(repertoire[int(x)])
    chargeRep()

def getPerso(y):
    return repertoire[y]


def getNom(p):
    return p[0]

def getPrenom(p):
    return p[1]
    #perso = getPerso(y)  prenom = perso[1] return prenom

def getNums(p):
     return p[2]

def getadresses(p):
     return p[3]

def getEmail(p):
     return p[4]

def getDate(p):
     return p[5]

def existeDate(p):
    #perso = getPerso(y)
    if p[5] == "":
        return DATE_Inconnu
