"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
from turtle import *
#0.Menu
print("triang1(n)")
print("triang2(n)")
print("carre(a)")
print("ligne_de_carres(a,n)")
print("carres_croissants(a,n)")
print("ligne_figure(fonction,nombre,taille)")
print("ligne_figure_croissant")
print("rayons(n,d)")
print("def polygone(a,n)")
print("etoile(a)")
print("etoile_croissant_decroissant(a,n)")
print("etoile6(a)")
print("spirale_figure(a,n)")
print("carres_emb(n,a)")
print("rayons_cercle(n,d,a)")

#1.Triangles
def triang1(n):
    speed("fastest")
    title("triangle haut")
    for x in range(3):
        forward(n)
        left(120)


def triang2(n):
    speed("fastest")
    title("triangle bas")
    for x in range(3):
        forward(n)
        right(120)

#2.Carres
def carre(a):
    speed("fastest")
    title("carre")
    for x in range(4):
        forward(a)
        right(90)
    

def ligne_de_carres(a,n):
    speed("fastest")
    title("lignede carres")
    for x in range(n):
        up()
        forward(a+10)
        down()
        carre(a)


def carres_croissants(a,n):
    speed("fastest")
    title("carres croissants")
    for x in range(n):
        up()
        forward(a+(a/4))
        down()
        carre(a)
        a=a*1.25

#3.Programmation d'ordre supérieur
def ligne_figure(fonction,nombre,taille):
    speed("fastest")
    for x in range(nombre):
        fonction(taille)
        up()
        forward(taille+(taille/4))
        down()
        
    
def ligne_figure_croissant(fonction,nombre,taille,taux):
    speed("fastest")
    for x in range(nombre):
        up()
        forward(taille+(taille/4))
        down()
        fonction(taille)
        taille=taille*taux
    
#4.Les polygones et les étoiles
def rayons(n,d):
    speed("fastest")
    rayon=0
    for x in range(n):
        rayon=360/n
        forward(d)
        backward(d)
        right(rayon)

def polygone(a,n):
    speed("fastest")
    for x in range(n):
        forward(a)
        right(360/n)
        forward(a)


def etoile(a):
    speed("fastest")
    for x in range(5):
        forward(a)
        right(180-180/5)

def etoile_croissant_decroissant(a,n):
    speed("fastest")
    for x in range(n//2):
        etoile(a)
        up()
        forward(a+a/2)
        down()
        a=a*1.25
    if n%2==0:
        a=a*0.75
        for x in range(n//2):
            etoile(a)
            up()
            forward(a+a/2)
            down()
            a=a*0.75
    else:
         for x in range(n//2+1):
            etoile(a)
            up()
            forward(a+a/2)
            down()
            a=a*0.75
            

def etoile6(a):
    speed("fastest")
    triang1(a)
    up()
    left(90)
    forward(3*a/5)
    right(90)
    down()
    triang2(a)


def spirale_figure(a,n):
    speed("fastest")
    bgcolor("black")
    for x in range(n):
        if x%2==0:
            color("blue")
            ligne_figure(etoile,1,a)
            color("red")
            ligne_figure(triang1,1,a)
        if x%2!=0:
            color("cyan")
            ligne_figure(etoile6,1,a)
            color("purple")
            ligne_figure(carre,1,a)
            left(70)
        if x%4==0:
            a=a*1.25
#5.Les carrés emboités
def carres_emb(n,a):
    speed("fastest")
    for x in range(n):
        carre(a)
        up()
        backward(a/2)
        left(90)
        backward(a/2)
        down()
        right(45)
        a=a*(2**0.5)


#6.des morceaux de cercles ou des cercles
def rayons_cercle(n,d,a):
    speed("fastest")
    bgcolor("black")
    color("white")
    for x in range(n+1):
        rayon=360/n
        down()
        circle(d, a)
        up()
        goto(0,0)
        down()
        setheading(rayon*x)
        up()


def coeur(a):
    color("red","pink")
    begin_fill()
    left(45)
    forward(a)
    circle(a/2, 180)
    right(90)
    circle(a/2, 180)
    forward(a)
    end_fill()
    hideturtle()
    up()
    forward(a/2)
    left(90)
    forward(a/4)
    down()
    write("JE T'AIME MON PAPA D'AMOUR", move=False, align="center", font=("Arial", 50, "normal"))
