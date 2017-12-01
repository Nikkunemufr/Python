"""
    authors:MORTELIER Alexis
"""
#=================================== Variable global ===================================
jean={"nom":"jean","jeu1":120, "jeu3":75, "jeu4":50,"jeu5":240} 
pierre={"nom":"pierre","jeu1":100, "jeu5":140, "jeu2":55,"jeu10":85} 
alain={"nom":"alain","jeu2":75,"jeu1":90} 
luc={"nom":"luc", "jeu2":45, "jeu5":110,"jeu1":100} 
liste1=[jean,pierre,alain,luc]
jean={"nom":"jean","jeu1":120, "jeu3":75, "jeu4":50,"jeu5":240} 
jean2={"nom":"jean","jeu1":110, "jeu2":60,"jeu3":95, "jeu5":240}

def combien_jeux(d):
    res=0
    for x in d:
        if x!="nom":
            res+=1
    return res


def score_moyen(d):
    res=0
    for x in d:
        if x!="nom":
            res+=d[x]
    return (res/combien_jeux(d))

def qui(jeu,ld):
    res=[]
    for x in ld:
        if jeu in x:
            res+=[x["nom"]]
    return res


def champion(jeu,ld):
    score=0
    winner=""
    for x in ld:
        if jeu in x and x[jeu]>score:
            winner=x["nom"]
            score=x[jeu]
    return winner,score

def fusionne(d1,d2):
    for x in d2:
        if x not in d1:
            d1[x]=d2[x]
        elif d1[x]>d2[x]:
            d1[x]=d2[x]
    return d1

def tousLesJeux(d):
    l=[]
    for x in d:
        for y in x:
            if y!="nom" and y not in l:
                l+=[y]
    return l

def dicoDesChampions(d):
    dicoChamp={}
    jeux=tousLesJeux(d)
    for x in jeux:
        dicoChamp[x]=champion(x,d)
    return dicoChamp
