"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
mois=int(input("Saisissez le mois : "))
annee=int(input("Saisissez l'année : "))
#Verifie si il s'agit d'une annee bisextile
def estBisextile(annee):
    return (annee%4==0 and annee%100!=0 or annee%400==0)
#Compte le nombre de jours dans le mois
def nbJours(mois,annee):
    if mois==2:
        if estBisextile(annee)==True:
            return 29
        else:
            return 28
    elif mois in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30
#Verifie qu'il s'agit d'une date supérieur ou égal a octobre 1752
def estValide(mois,annee):
    if annee==1752 and mois<10:
        return False
    return ((1<=mois<=12) and (annee>=1752))
#Formule de Zeller calculant le jour correspondant à la date
def zeller(jours,mois,a,c,b):
    return (int((jours+(2.6*mois-0.2)+a+(a/4)+(c/4)-2*c-(1+b)*(mois/11))%7))
#
def coderJour(jours,mois,annee):
    m=[11,12,1,2,3,4,5,6,7,8,9,10]
    mois=m[mois-1]
    c=annee//100
    a=annee%100
    b=estBisextile(annee)
    return zeller(jours,mois,a,c,b)
#Affiche le calendrier
def afficher(mois,annee):
    taille=nbJours(mois,annee)
    resultat=""
    j=["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
    for x in range(1,taille+1):
        code=coderJour(x,mois,annee)
        nom=j[code]
        resultat+=nom+str(x)
        if nom=="Dimanche":#Saut de ligne dès qu'il s'agit de Dimanche
            resultat+="\n"
        elif taille!=x:#Virgule entre chaque jour sauf en fin de ligne
            resultat+=","
    if estValide(mois,annee)==True:
        print(resultat)
    else:
        print("Erreur de saisie")


afficher(mois,annee)
