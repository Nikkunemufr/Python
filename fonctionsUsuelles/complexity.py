# -*- coding:utf-8 -*-
"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
# psyco est un module basé sur les techniques de "compilation à la volée"
# et permet ainsi d'accélérer l'exécution des programmes.
try:
    import psyco
    psyco.full()
except:
    pass

from random import randrange
from time import time

compteur = 0

def tirageAleatoire(taille,rang=30):
    """retourne un tableau de taille entiers dont les valeurs
    sont tirées aléatoirement dans l'intervalle [0,rang-1]"""
    res=[0]*taille
    for i in range(taille):
        res[i]=randrange(rang)
    return res

###########################   TRI RAPIDE   ###########################

def partition(tableau,g,d):
    "partition du tableau dans l'intervalle [g,d]"
    pivot=tableau[g]
    courg=g+1
    courd=d
    while True:
        while courg<d and tableau[courg]<=pivot:
            courg=courg+1
        while tableau[courd]>pivot:
            courd=courd-1
        if courg < courd:
            tableau[courg],tableau[courd]=tableau[courd],tableau[courg]
        else:
            tableau[g],tableau[courd]=tableau[courd],tableau[g]
            return courd

def triRapide(tableau,g,d):
    "tri du tableau dans l'intervalle [g,d], donc tri de tableau[g:d+1]"
    global compteur
    compteur += 1
    if g<d:
        i=randrange(g,d+1)
        tableau[g],tableau[i]=tableau[i],tableau[g]
        m=partition(tableau,g,d)
        triRapide(tableau,g,m-1)
        triRapide(tableau,m+1,d)

print("Un exemple d'execution de triRapide:"); print
L=[5,3,4,7,4,1]; print("la liste initiale:", L)
print
triRapide(L,0,5); print("la meme liste, mais triee:", L)

##########################   TRI SELECTION   #########################

## 1) Ecrire la fonction TriSelection

def triSelection(tableau):
    global compteur
    for x in range(0,len(tableau)-1):
        indiceDuMin=x
        for k in range(x+1,len(tableau)) :
            compteur += 1
            if tableau[k]<tableau[indiceDuMin] :
                indiceDuMin=k
            if indiceDuMin !=x :
                tableau[x],tableau[indiceDuMin]=tableau[indiceDuMin],tableau[x]
    return tableau



##########################   TRI FUSION   #########################

## 2) Ecrire la fonction fusion

def fusion(tab1,tab2):
    """ retourne le tableau résultant de la fusion
    des deux tableaux triés tab1 et tab2 """
    i=0
    j=0
    res=[]
    global compteur

    while i<len(tab1) or j<len(tab2):
        if i == len(tab1):
            res.extend(tab2[:len(tab2)])
            return res
        elif j == len(tab2):
            res.extend(tab1[:len(tab1)])
            return res
        if tab1[i]<tab2[j]:
            res.append(tab1[i])
            i+=1
        else:
            res.append(tab2[j])
            j+=1
        compteur += 1

    return res


def triFusion(tableau,g,d):
    if g<d:
        m=(g+d)//2
        triFusion(tableau,g,m)
        triFusion(tableau,m+1,d)
        tableau[g:d+1]=fusion(tableau[g:m+1],tableau[m+1:d+1])


##########################   TEST   #########################

## 3) Tester les temps d'exécution des différents tris
##        pour différentes tailles: 10, 100, 1000,
##        et, si on peut: 10 000, 100 000, 1 000 0000

def test(n):
    global compteur
    print("Mon test pour:", n)
    monTab=tirageAleatoire(n,n)
    print("*"*20); print("taille = "),; print(n)
    tonTab=monTab[:]
    t1=time()
    triRapide(tonTab,0,len(tonTab)-1)
    t2=time()
    print("compteur:",compteur)
    compteur = 0
    print("temps du tri rapide: "); print(t2-t1)
##    triSelection(tonTab)
##    t3=time()
##    print("compteur:",compteur)
##    compteur = 0
##    print("temps du tri selection: "); print(t3-t1)
    triFusion(tonTab, 0, len(tonTab))
    t4=time()
    print("compteur:",compteur)
    compteur = 0
    print("temps du tri fusion: "); print(t4-t1)
    tonTab.sort()
    t5=time()
    print("temps du tri fusion: "); print(t5-t1)


for el in [10,100,1000,10000,100000,1000000]:
    test(el)
    print


## 4) Pour chacun des tris, introduire une variable compteur (globale)
##      pour compter le nombre de comparaisons entre paires d'éléments du tableau.
##
##    Pour chacun des tris, répondre à la question suivante:
##    Quand on multiplie la taille par 10, par combien est multiplié le temps? le nombre de comparaisons?
