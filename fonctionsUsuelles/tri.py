"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""

def triCroissant (l):
    """Retourne une copie, triée par ordre croissant, d'une liste donnée."""
    copieLocale=l[:]
    for i in range(len(copieLocale)):
        indiceMinCourant=0
        for j in range(len(copieLocale)):
            if copieLocale[j]<copieLocale[indiceMinCourant]:
                indiceMinCourant=j
        resultatTri.append(copieLocale[indiceMinCourant])
        copieLocale[indiceMinCourant:indiceMinCourant+1]=[]
    return resultatTri

def triDecroissant (l):
    """Retourne une copie, triée par ordre décroissant, d'une liste donnée."""
    res=[]
    for i in range(len(l)):
        indiceMaxCourant=0
        for j in range(len(l)):
            if l[j]>l[indiceMaxCourant]:
                indiceMaxCourant=j
        res.append(l[indiceMaxCourant])
        l[indiceMaxCourant:indiceMaxCourant+1]=[]
    return res