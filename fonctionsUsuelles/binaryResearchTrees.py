# -*- coding:utf-8 -*-
"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
######################    Arbre Binaire de Recherche (ABR)   ######################

class Noeud(object):
  def __init__(self, element, ga=None, dr=None):
    self.val = element
    self.ga  = ga
    self.dr = dr

unABR=Noeud(10,Noeud(5,None,Noeud(7)),Noeud(13,Noeud(12,Noeud(11),None),Noeud(17)))
unautreABR=Noeud(11,Noeud(6,None,Noeud(8)),Noeud(14,Noeud(13,Noeud(12),None),Noeud(18)))

def voir(A,dec=1):
    "un affichage planaire de l'arbre binaire A modulo une rotation à 90°"
    if A == None:return ""
    return voir(A.dr,dec+5)+' '*dec+str(A.val)+'\n'+voir(A.ga,dec+5)

print(voir(unABR)+"\n")

# 1. Écrivez une procédure minimum(A) qui retourne un pointeur sur le noeud de valeur minimale d'un ABR A
#    (et retourne None si l'ABR est vide).
def minimum(A):
  if A==None:
    return None
  if A.ga==None:
    return A.val
  return minimum(A.ga)

# 2. Écrivez une procédure itérative present(A,x) qui, étant donné un ABR A et un élément x,
#    détermine si l'élément x est présent ou non dans l'ABR A (la procédure retourne un booléen).
def present(A,x):
  if A==None:
    return False
  while A!=None:
    if x==A.val:
      return True
    elif x>A.val:
      A=A.dr
    elif x<A.val:
      A=A.ga
  return False

# 3. Écrivez une procédure insere(A,x) qui renvoie l'ABR A où on a ajouté l'élément x.
#    La procédure ne modifie rien si x est déjà dans A.

def insere(A,x):
  if A==None:
    A=Noeud(x)
  elif x<A.val:
    if A.ga!=None:
      A.ga=insere(A.ga,x)
    else:
      A.ga=Noeud(x)
  else:
    if A.dr!=None:
      A.dr=insere(A.dr,x)
    else:
      A.dr=Noeud(x)
  return A

# 4. Écrivez une procédure affiche(A) qui affiche tous les éléments d'un ABR A
#    dans l'ordre croissant.

def affiche(A):
  if A!=None:
    affiche(A.ga)
    print(A.val)
    affiche(A.dr)

# # 5*. Écrivez une procédure afficheIntervalle(A,debut,fin)
#    qui, pour deux valeurs debut et fin supposées telles que début <= fin,
#    affiche tous les éléments x de l'ABR A qui appartiennent à l'intervalle [debut, fin].
#    Évitez les parcours de sous-arbres inutiles.
def afficheIntervalle(A,debut,fin):
  if A==None:
    return None
  if fin<A.val:
    afficheIntervalle(A.ga,debut,fin)
  if A.val<debut:
    afficheIntervalle(A.dr,debut,fin)
  if debut <=A.val<=fin:
    afficheIntervalle(A.ga,debut,A.val)
    print(A.val)
    afficheIntervalle(A.dr,A.val,fin)
#    Considérez les 4 cas suivants:
#    1) A = None : rien à afficher;
#    2) fin < A.val : appel récursif sur le sous-arbre gauche;
#    3) A.val < debut : appel récursif sur le sous-arbre droit;
#    4) debut <= A.val <= fin :
#     appel récursif sur le sous-arbre gauche et l'intervalle [debut,A.val], écrire A.val
#     puis appel récursif sur le sous-arbre droit et l'intervalle [A.val,fin]

# 6**. Écrivez une procédure rechercheKeme(A,k)
#    qui recherche le k-ème plus petit élément de l'ABR A, pour k>=1.
#
#    Le principe est d'effectuer un parcours infixé où
#    l'on décrémente k lors de la visite de chaque noeud.
#
#    Cette procédure retourne un couple: un élément et un entier.
#
#    Dans le cas où ce k-ème plus petit élément de A existe (k <= taille de l'ABR A),
#    l'élément correspond au k-ème plus petit élément de l'ABR A
#    et l'entier vaut 0.
#
#    Dans le cas où ce k-ème plus petit élément n'existe pas,
#    on donne à l'élément une valeur 'bidon', -1 par exemple,
#    et l'entier vaut k moins le nombre d'éléments de l'ABR A.

def rechercheKeme(A,k):
  pass
# 7. Écrivez une procédure coupeSelon(A,x) qui, pour un ABR A et un élément x
#    (présent ou non dans A),retourne deux ABR:
#    un ABR contenant les éléments de A strictement inférieurs à x
#    et un ABR contenant les éléments de A strictement supérieurs à x.
#    Quels noeuds de A sont visités par la procédure coupeSelon(A,x)?
def coupeSelon(A,x):
  if A==None:
    return None,None
  if A.val==x:
    return A.ga,A.dr
  if A.val>x:
    sup=A
    inf,sup.ga=coupeSelon(A.ga,x)
  else:
    inf=A
    inf.dr,sup=coupeSelon(A.dr,x)
  return inf,sup
# 8. Écrivez une procédure insereAlaRacine(A,x) qui retourne l'ABR A
#    où on ajoute l'élément x comme racine.
#    Vous utiliserez pour cela la procédure coupeSelon.
def insereAlaRacine(A,x):
  res=Noeud(x)
  res.ga,res.dr=coupeSelon(A,x)
  return res
# 9. Écrivez une procédure récursive fusion(A,B) qui retourne l'ABR
#    qui est la fusion des ABR A et B.
#    Vous utiliserez pour cela la procédure coupeSelon.
def fusion(A,B):
  if A==None:
    return B
  if B==None:
    return A
  inf,sup=coupeSelon(A,B.val)
  B.ga=fusion(inf,B.ga)
  B.dr=fusion(sup,B.dr)
  return B
