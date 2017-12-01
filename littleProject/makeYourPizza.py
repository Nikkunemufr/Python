'''
    Ce super programme de piza yolo va vous permettre de faire les meilleurs pizza du monde !
    Ce super programme trop génial vous ai proposez par Alexis MORTELIER
'''
from random import randint

#Partie 1
def saisie():
    rep=()
    ingredient=""
    while ingredient != "1":
        ingredient=input("Entrez un ingrédient ou 1 quand vous avez finie: ")
        if ingredient!=1:
            rep+=(ingredient, )
    return rep


#Partie 2
def choix(l,n):
    choix=('tomates', 'champignons', 'mozzarella', 'jambon')
    newchoix=()
    x=0
    while x<n:
        random=randint(1,len(l))
        if l[random] not in choix:
            newchoix+=(l[random], )
            x+=1
    return newchoix

#Partie 3
def affiche(t):
    res="Votre pizza : "
    for k in range(0,len(t)):
        res+=t[k]+" "
    return res

#Partie 4
def lesPizzas():
    ingredient=saisie()
    rep=0
    n=int(input("Choisissez vos nombre d'ingredients : "))
    while rep !=1:
        prop=choix(ingredient,n)
        print(prop)
        rep=int(input("Tapez 1 pour arreter, tapez 0 pour continuer : "))

lesPizzas()
