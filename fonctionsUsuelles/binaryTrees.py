# -*- coding: utf-8 -*-
"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
###########################    Arbre Binaire    ###########################


class Noeud(object):
  def __init__(self, element, ga=None, dr=None):
    self.val = element
    self.ga  = ga
    self.dr = dr

def hauteur(A):
    "fonction qui calcule la hauteur d'un arbre binaire A"
    if A ==None:
      return -1
    return 1+max(hauteur(A.ga),hauteur(A.dr))

def voir(A,dec=1):
  "un affichage planaire de l'arbre A modulo une rotation à 90°"
  if A == None:return ""
  return voir(A.dr,dec+5)+' '*dec+str(A.val)+'\n'+voir(A.ga,dec+5)

# Un exemple d'arbre binaire :
B=Noeud(4,Noeud(1,None,Noeud(9)),Noeud(3,Noeud(2,Noeud(5),None),Noeud(7)))

print(voir(B)+"\n")


# 1. Écrire une fonction affichePrefixe(A) qui affiche les éléments d'un arbre binaire A
#    dans l'ordre préfixé, une fonction qui affiche les éléments
#    d'un arbre binaire dans l'ordre infixé et une fonction qui
#    affiche les éléments d'un arbre binaire dans l'ordre postfixé.
def affiche_prefixe(A):
  if A!=None:
    print (A.val, end=" ")
    affiche_prefixe(A.ga)
    affiche_prefixe(A.dr)

def affiche_infixe(A):
  if A!=None:
    affiche_prefixe(A.ga)
    print (A.val, end=" ")
    affiche_prefixe(A.dr)

def affiche_suffixe(A):
  if A!=None:
    affiche_prefixe(A.ga)
    affiche_prefixe(A.dr)
    print (A.val, end=" ")

# 2. Écrire une fonction interne(A) qui retourne le nombre de noeuds internes
#    (i.e. les noeuds qui ne sont pas des feuilles) d'un arbre binaire A.
def affiche_noeud(A):
  if A!=None:
    return 0
  return 1+affiche_noeud(A.ga)+affiche_noeud(A.dr)

# 3. Écrire une fonction filiforme(A) qui détermine si un arbre binaire A est dégénéré
#    (c'est-à-dire, tel que tout noeud a au plus un fils).
def filiforme(A):
  if A==None:
    return False
  elif A.dr==None and A.ga==None:
    return False
  elif A.ga==None:
    filiforme(A.dr)
  elif A.dr==None:
    filiforme(A.ga)
  return True
# 4. Écrire une fonction combien(A,k) qui retourne le nombre de noeuds
#    de l'arbre binaire A qui sont à la profondeur k.
#    (cas possibles : i) A est vide ou k<0,
#                     ii) A est non vide et k=0,
#                     iii) A est non vide et k>0)
def combien(A,k):
  if A==None or k<0:
    return 0
  if k==0:
    return 1
  if k>0:
    return combien(A.ga,k=-1)+combien(A.dr,k=-1)
# 5. La longueur de cheminement d'un arbre binaire est
#    la somme des profondeurs de tous les noeuds de cet arbre.
#    Écrire une fonction long_chemin(A,p=0) qui calcule la longueur de cheminement
#    d'un arbre binaire A. (p indique la profondeur du noeud racine de A).
def long_chemin(A,p=0):
  if A==None:
    return 0
  return p+long_chemin(A.dr,p+1) + long_chemin(A.ga,p+1)
# 6. Un arbre binaire est équilibré si en tout noeud de l'arbre
#    la différence des hauteurs de ses deux sous-arbres gauche et droit est d'au plus 1.
#    Écrire une fonction equilibre(A) qui retourne un booléen et un entier:
#    le booléen vaut vrai et l'entier indique la hauteur de l'arbre
#    si l'arbre est équilibré, le booléen vaut faux et l'entier indique
#    une valeur bidon (par exemple -2) sinon.
def equilibre(A):
  if A==None:
    return True,0
  equilibreG,hauteurG=equilibre(A.ga)
  equilibreD,hauteurD=equilibre(A.dr)
  if hauteurG>hauteurD+1 or hauteurD>hauteurG+1:
    return False, 69
  if equilibreG==False or equilibreD==False:
    return False, 69
  return True, max(hauteurD,hauteurG)+1
