 #coding:utf-8
"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
# On utilise une classe pour définir le type pointeur sur noeud.
class Noeud(object):
    def __init__(self,val,suiv=None):
        """initialisateur de classe
        permet l'allocation de la mémoire requise pour stocker le noeud
        et l'initialisation de ses attributs val et suiv"""
        self.val=val
        self.suiv=suiv

# Quelques exemples de listes avec représentation simplement chaînée.
# a) la liste vide :
listeVide=None

# b) une liste réduite à l'élément 5 :
listeSingleton=Noeud(5)
# listeSingleton=Noeud(5) => appel de la fonction __init__ de Noeud
# avec comme paramètres : self=listeSingleton, val=5 et suiv=None
#
# Cette simple instruction correspond en pseudo-code à la séquence :
#     listeSingleton : pointeur sur noeud     # déclaration de type
#     Nouveau(listeSingleton)                 # allocation de la mémoire
#     listeSingleton->val=5                   # initialisation du champ val
#     listeSingleton->suiv=None               # initialisation du champ suiv


# c) la liste 2,5,8,10:
maliste=Noeud(2,Noeud(5,Noeud(8,Noeud(10))))
maliste2=Noeud(2,Noeud(5))



# Exo 1. A partir de la liste maliste=Noeud(2,Noeud(5,Noeud(8,Noeud(10))))
# écrivez l'instruction nécessaire pour afficher le 1er élément de maliste (l'élément 2)
# puis l'instruction nécessaire pour afficher le 3ème élément (ici 8).
print("exo 1-A")
print (maliste.val)
print("exo 1-B")
print (maliste.suiv.suiv.val)

# Exo 2. En utilisant les procédures données ci-dessous (essayez d'abord de bien les comprendre),
# écrivez les instructions nécessaires pour :
# a) afficher tous les éléments de maliste;
# b) ajouter l'élément 7 en début de maliste et afficher à nouveau maliste;
# c) ajouter l'élément 3 en fin de maliste et afficher à nouveau maliste;
# d) déterminer si l'élément 8 est ou non dans maliste.

def affiche(debut):
    while debut!=None:
        print(debut.val,end=" ")
        debut=debut.suiv
    print()


def insere_debut(debut,x):
    return Noeud(x,debut)

def insere_fin_it(debut,x):
    if debut==None:
        return Noeud(x)
    cour=debut
    while cour.suiv!=None:
        cour=cour.suiv
    cour.suiv=Noeud(x)
    return debut

def recherche_rec(debut,x):
    if debut==None:
        return False
    if debut.val==x:
        return True
    return recherche_rec(debut.suiv,x)

#a)
print("exo 2-A")
affiche(maliste)
#b)
print("exo 2-B")
maliste=insere_debut(maliste,7)
affiche(maliste)
#c)
print("exo 2-C")
maliste=insere_fin_it(maliste,3)
affiche(maliste)
#d)
print("exo 2-D")
print(recherche_rec(maliste,8))
# Exo 3. Donnez une version récursive de la procédure insere_fin(debut,x)
# qui prend en entrée deux arguments (debut qui est une référence
# sur le premier noeud d'une liste et x un élément)
# et qui insère x à la fin de la liste.
print("exo 3")
def insere_fin_rec(debut,x):
    if debut==None:
        return Noeud(x)
    else:
        debut.suiv=insere_fin_rec(debut.suiv,x)
    return debut
maliste=insere_fin_rec(maliste,10)
affiche(maliste)
# Exo 4. Donnez une version itérative de la procédure recherche(debut,x)
# qui prend en entrée deux arguments (debut une référence
# sur le premier noeud d'une liste et x un élément) et
# qui détermine si x est ou non dans la liste.
print("exo 4")
def recherche_it(debut,x):
    while debut !=None:
        if debut.val==x:
            return True
        debut=debut.suiv
    return False

# Exo 5. Écrivez une procédure inverse(debut)
# qui prend en entrée debut une référence sur le premier noeud d'une liste
# et qui retourne une référence sur le premier noeud de la liste inversée.
print("exo 5")
def inverse(debut):
    tete=debut
    if debut==None:
        return None
    tete=inverse(debut.suiv)
    tete=insere_fin_it(tete,debut.val)
    return tete

affiche(inverse(maliste))
# Exo 6. Une liste L1 est une sous-liste d'une liste L2 si L1 est obtenue à partir de L2 en supprimant zéro, un ou plusieurs éléments de la liste L2.
# Exemple: la liste 3,5,10 est une sous-liste de la liste 2,3,5,5,7,10.
# Écrivez une procédure sousListe(L1,L2)
# qui prend en entrée deux listes L1 et L2 et qui retourne True si L1 est une sous-liste de L2.
# On supposera que L1 et L2 sont des listes d'entiers triés dans l'ordre croissant (au sens large).
print("exo 6")
def sousListe(l1=maliste,l2=maliste2):
    compteur=0
    init=0
    while l1!=None:
        l3=l2
        while l3!=None:
            if l1.val==l3.val:
                compteur+=1
            l3=l3.suiv
        init+=1
        l1=l1.suiv
    if init==compteur:
        return True
    print(init)
    print(compteur)
    return False
sousListe()

# Exos un peu plus difficiles (avec *):

# Exo 7. Écrivez une procédure insere_apres(L,x,y)
# qui insère un élément y après la première occurrence de l'élément x dans une liste L
# (ne fait rien en l'absence de x) et retourne la liste ainsi modifiée.
print("exo 7")
# Exo 8. Écrivez une procédure insere_avant(L,x,y)
# qui insère un élément y avant la première occurrence de l'élément x dans une liste L
# (ne fait rien en l'absence de x) et retourne la liste ainsi modifiée.
print("exo 8")

## Test
print("TEST")
debut=None
for i in range(3):
    debut=insere_fin_it(debut,i)
affiche(debut)
