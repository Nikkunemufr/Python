"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
#Jeu de domino

from random import randint #Importation de l'aléatoire

def somme(d): #Somme les deux parties d'un domino
    res = d[0] + d[1] #Somme les deux premiers membres du tuple
    return res #Retourne le résultat de la somme

def comptePoints(jeu): #Somme la totalité des parties de dominos
    total = 0 #Définit la variable "total"
    for n in jeu: #Parcourt le jeu
        total += somme(n) #Relance la fonction somme à chaque itération
    return total #Retourne la somme totale

def plusCher(jeu):
    maxi, k = (), 0 #maxi retient la paire de chiffres et k la valeur la plus élevée
    for n in jeu: #Parcourt le jeu
        if somme(n) >= k: #Si la fonction somme renvoie un nombre supérieur à la valeur de k
            k = somme(n) #k prend la valeur de la somme
            maxi = n #maxi prend la valeur du tuple donnant cette somme
    return maxi #renvoie la valeur maxi

def jouer(dom, plateau):
    if plateau == (): #Si le plateau est vide
        return True #Alors on peut jouer
    else: #Sinon
        deb = plateau[0][0] #deb prend la valeur du premier tuple du plateau
        fin = plateau[-1][-1] #fin prend la valeur du dernier tuple
        return dom[0] == deb or dom[1] == deb or dom[0] == fin or dom[1] == fin
        #Vérifie si le premier ou deuxième terme du tuple du domino à jouer correspond à la valeur
        #du premier ou dernier terme du plateau

def dominosJouable(jeu, plateau):
    jouable = () #Variable locale pour récupérer les dominos jouables
    for n in jeu: #Parcourt le jeu en main
        if jouer(n, plateau): #Si le domino répond True
            jouable += (n, ) #il est ajouté au tuple jouable
    return jouable #Renvoie la liste des dominos jouables

def choixOrdi(main, plateau):
    if dominosJouable(main, plateau) == (): #Si la main n'a rien répondant aux conditions de la fonction dominosJouable
        return False #Renvoie False
    else: #Sinon
        return plusCher(dominosJouable(main, plateau)) #Cherche le domino jouable correspondant à la valeur la plus chère
        #Ici, on place une fonction dans une fonction. D'abord on récupère la liste des dominos jouables,
        #puis, chaque dominos jouables passe dans la fonction plusCher et cela renvoie le domino qui a la plus grande valeur

def correct(plateau):
    k = 0 #Variable à incrémenter
    for n in range(len(plateau)-1): #Parcourt les tuples du plateau
        if plateau[n][1] == plateau[n+1][0]: #Si le dernier terme = le premier terme suivant
            k+= 2 #On additionne 2 à k
    return k != (len(plateau)) #Si l'inégalité est avérée, retourne True, sinon False

def creationJeu():
    dominos = () #Variable qui récupère la liste des dominos
    for n in range(7): #Premier terme du domino entre 0 et 6
        for m in range(n, 7): #Second terme du domino entre 0 et 6
            dominos += ((n,m),) #Ajoute chaque domino à la variable
    return dominos #Renvoie la liste des tuples de dominos

def enleve(dom, jeu):
    pioche = () #Variable qui récupère la liste des dominos
    for n in jeu: #Parcourt le jeu
        if n == dom: #Si n correspond au domino indiqué,
            pass #On passe
        else: #Sinon
            pioche += (n, ) #On ajoute le domino dans la variable
    return pioche #Renvoie la liste de tous les dominos restants

def piocher(jeu, pioche):
    domino = pioche[randint(0, len(pioche)-1)] #Choisit un domino au hasard dans la pioche
    jeu += (domino, ) #Ajoute des tuples à l'image de "jeu"
    return (jeu, enleve(domino, pioche)) #Renvoie la valeur de "jeu" et lance la fonction enleve
    #enleve récupère la liste des dominos du jeu pour les soustraire à la pioche
