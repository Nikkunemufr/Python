"""
     :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
     Calendrier réalisé en Python avec possibilité de choix du type du calendrier : Grégorien ou Julien
"""
from math import *
mois=int(input("Saisissez le mois : "))
annee=int(input("Saisissez l'année : "))
jul=int(input("[0] pour officiel [1] pour francais [2] pour anglais"))
#Test si julien
def testerJulien(jours,mois,annee,jul):
    """
        Cette fonction permet de tester si la date saisie correspond au calendrier Julien en fonction du type de calendrier choisie, 0 pour officiel, 1 pour francais, 2 pour anglais
        :param jours : le jour
        :type jours : int
        :param mois: le mois
        :type mois : int
        :param annee: l'année
        :type annee: int
        :param n : 0 pour calendrier officiel, 1 pour calendrier francais, 2 pour calendrier anglais
        :type n: int
        :return: True si la date est Julienne et False si la date n'est pas Julienne
        :rtype : boolean
    """
    if jul==0:
        if annee<=1582:#Date officiel
            if jours<=4:
                if mois<=10:
                    return True
    if jul==1:
        if annee<=1582:#Date francaise
            if jours<=9:
                if mois<=12:
                    return True
    if jul==2:
        if annee<=1752:#Date anglaise
            if jours<=2:
                if mois<=9:
                    return True
    else:
        return False
#Verifie si il s'agit d'une annee bisextile
def estBisextile(annee,jul):
    """
      Cette fonction permet de voir si une année est bissextile ou non
      :param annee: l'annee à definir comme bissextile ou non
      :type annee: int
      :param jul : 0 pour calendrier officiel, 1 pour calendrier francais, 2 pour calendrier anglais
      :type jul: int
      :return: retourne True si l'année est bissextile sinon elle retourne False
      :rtype: boolean
    """
    if jul==1:
        if annee%4==0:
            return True
        else:
            return False
    if jul==0:        
        if annee%4==0 and annee%100!=0 or annee%400==0:
            return True
        else:
            return False
#Compte le nombre de jours dans le mois
def nbJours(mois,annee,jul):
    """
        Cette fonction permet d'associer le mois d'une année à son nombre de jour . Si l'année est bissextile le mois 2 contient
        29 jours , sinon il ne contient que 28 jours , les autres mois restent inchangés
        :param mois: le mois où l'on veux connaitre son nombre de jours ( 1<=mois<=12 )
        :type mois: int
        :param annee: l'année
        :type annee: int
        :param jul : 0 pour calendrier officiel, 1 pour calendrier francais, 2 pour calendrier anglais
        :type jul: int
        :return: retourne le nombre de jours dans le mois en fonction de l'année et du type de calendrier voulu
        :rtype: int
    """
    if mois==2:
        if estBisextile(annee,jul)==True:
            return 29
        else:
            return 28
    elif mois in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30
#Formule de Zeller calculant le jour correspondant à la date
def zeller(jours,m,a,c,b,mois,annee,jul):
    """
      La formule de zeller permet de determiner le jour de la semaine selon la date voulu.
      cette formule s'écrit de deux maniéres , selon si la date appartient au calendrier Julien ou Grégorien
      elle retourne un entier entre 0 et 6 où
      0 désigne Dimanche
      1 désigne Lundi
      2 désigne Mardi
      3 désigne Mercredi
      4 désigne Jeudi
      5 désigne Vendredi
      6 désigne Samedi
      :param jours: le jour du mois , 1<=jours<=31
      :type jours : int
      :param m: code le mois avec mars comme premier mois
      :type m: int
      :param a: code les dizaines de l'année
      :type a: int
      :param c : code les centaines de l'année
      :type c: int
      :param b: vérifie si l'année est bissextile ou non
      :type b : boolean
      :param mois: code la valeur du mois
      :type  mois: int
      :param annee: l'annee
      :type annee: int
      :param jul: 0 pour calendrier officiel, 1 pour calendrier francais, 2 pour calendrier anglais
      :type jul: int
      :return: retourne une valeur comprise entre 0 et 6
      :rtype: int
      .. note: Afin de définir m,a,c et b nous appellerons cette fonction par coderJour().
    """
    if testerJulien(jours,mois,annee,jul):
        return (floor(a/4)+a+(floor(2.6*m-0.2)-(1+b)*floor(m/11)-2)+jours+6*c)%7
    else:
        return (floor(a/4)+a+(floor(2.6*m-0.2)-(1+b)*floor(m/11)-2)%7+jours+5*c+floor(c/4)+2)%7
#Code les jours
def coderJour(j,mois,annee,jul):
    """
     Cette fonction s'occupe de définir et de calculer les paramètres manquant de la fonction de Zeller c'est à dire m,a,c et b
     m : définie Mars comme premier mois
     a : calcul l'année dans le siecle
     c : calcul les centaines de l'année
     b : vérifie s'il s'agit d'une année bissextile ou 
     :param jours: le jour
     :type jours: int
     :param mois: mois de l'année avec Mars comme premier mois
     :type mois: int
     :param annee: l'année
     :type annee: int
     :param jul: 0 pour calendrier officiel, 1 pour calendrier francais, 2 pour calendrier anglais
     :type jul: int
     :return: retourne une valeur comprise entre 0 et 6
     :rtype: int
    """
    l=[11,12,1,2,3,4,5,6,7,8,9,10]
    m=l[mois-1]
    c=annee//100
    a=annee%100
    b=estBisextile(annee,jul)
    return zeller(j,m,a,c,b,mois,annee,jul)
#Affiche le calendrier
def afficher(mois,annee,jul):
    """
      Affiche le calendrier du mois demandé selon l'année et le type du calendrier demandé
      :param mois : le mois
      :type mois : int
      :param annee: l'année
      :type annee : int
      :param jul : 0 pour calendrier officiel, 1 pour calendrier francais, 2 pour calendrier anglais
      :type jul: entier
      :return : le calendrier du mois
      :rtype : chaine de caractère
    """
    taille=nbJours(mois,annee,jul)
    resultat=""
    j=["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
    jours=1
    while(jours<=taille):
        code=coderJour(jours,mois,annee,jul)
        nomJours=j[code]
        if nomJours=="Dimanche":
            resultat+=nomJours+" "+str(jours)+"\n"
        else:
            resultat+=nomJours+" "+str(jours)+","
        if (annee==1582 and mois==10 and jours==4 and jul==0 ) or (annee==1582 and mois==12 and jours==9 and jul==1) or (annee==1752 and mois==9 and jours==2 and jul==2):
            jours+=1+3*floor((annee-400)/400)+floor((100+(annee%400))/100)
        else:
           jours+=1
    print(resultat)

afficher(mois,annee,jul)
