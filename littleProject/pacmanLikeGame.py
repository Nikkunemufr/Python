"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
from tkinter import *
from random import *
# variables globales 

c=35 # dimension d'une case supposée carrée
x0,y0=50,50  #coordonnées du point en haut à gauche

#fonctions sur la grille

def creegrille(n, x):
    res=[0]*n
    for i in range(n):
        res[i]= [x]*n
    return res


def taille(grille):
    return len(grille)

# creation aléatoire de grilles avec tresors

def aleagrille(n,p):  # n taile de la grille p nombre d'objets
    m=creegrille(n,'_')
    cases=[(x,y) for x in range(n) for y in range(n) if x!=0 or y!=0]
    objets=sample (cases, p)
    for (i,j) in objets:
        m[i][j]=randint(0,1)
    m[0][0]='*'
    return m


# fonctions sur les déplacements

def deplacement(m,d, i,j):# deplacement de d à partir de la position i j
    n=taille(m)
    x,y,p=i,j,0
    if d=="H":
        x=i-1
    elif d=='B':
        x+=1
    elif d=='G':
        y-=1
    else:
        y+=1
    if x in range(0,n) and y in range(0,n):
        m[i][j]='_'
        if m[x][y]==0:
            p=5
            changeScore(p)
        elif m[x][y]==1:
            p=-10
            changeScore(p)
        m[x][y]='*'
        return (x,y,p)
    else:
        changeScore(-2)
        return (i,j,-2)

# avec le changement de score pour la version TKinter
def changeScore(p):
    pts=txt.get("0.0", END)[:-1]
    if pts:
        pts=p+int(pts)
    else:
        pts=p
    txt.delete("0.0", END)
    txt.insert(END, str(pts))


#  fonctions Tkinter
def monquitter():
    dessin.quit()
    dessin.destroy()
    
def H():
    global pos
    res=deplacement(m, 'H', pos[0], pos[1])
    pos=res[0:2]
    dessineGrille(m)
    finDeJeu()
    
def D():
    global pos
    res=deplacement(m, 'D', pos[0], pos[1])
    pos=res[0:2]
    dessineGrille(m)
    finDeJeu()
    
def G():
    global pos
    res=deplacement(m, 'G', pos[0], pos[1])
    pos=res[0:2]
    dessineGrille(m)
    finDeJeu()
def B():
    global pos
    res=deplacement(m, 'B', pos[0], pos[1])
    pos=res[0:2]
    dessineGrille(m)
    finDeJeu()
    
def dessineGrille(m):
    
    can.delete(ALL)
    n=len(m)
    for i in range(n+1):
        can.create_line(x0+c*i, y0,x0+c*i,y0 + n*c)
        can.create_line(x0, y0+c*i,x0+n*c ,y0+c*i)

    for i in range(n):
        for j in range(n):
            x=m[i][j]
            if x==1:
                can.create_image(x0+x0/3 +c*j,y0+y0/3+c*i,image=fantome)        
            elif x==0:
                can.create_image(x0+x0/3 +c*j,y0+y0/3+c*i,image=tresor)
            elif x=='*':
                can.create_image(x0+x0/3+c*j,y0+y0/3+c*i,image=pacman)
            elif i==n-1 and j==n-1:
                can.create_image(x0+x0/3+c*j,y0+y0/3+c*i,image=arrive)

def finDeJeu():
    global pos,m
    n=len(m)
    if pos==(n-1,n-1):
        BH.configure(state=DISABLED)
        BG.configure(state=DISABLED)
        BD.configure(state=DISABLED)
        BB.configure(state=DISABLED)
        fin=Label(dessin,text="LA PARTIE EST FINIE",font=("Ubuntu",20,"bold"))
        fin.pack(side=BOTTOM)
        texte.set("VAS Y FRANCKY C'EST BON")
        bdem.configure(state=NORMAL)
        
m=""
pos=0,0
def new():
    global m
    global pos
    m=aleagrille(10,15)
    pos=0,0
    dessineGrille(m)
    cadre.pack(side=TOP)
    BH.configure(state=NORMAL)
    BG.configure(state=NORMAL)
    BD.configure(state=NORMAL)
    BB.configure(state=NORMAL)
    bdem.configure(state=DISABLED)
    texte.set("Allez Francky !")
    
    


            
## et les widgets
    
dessin=Tk()
pacman=PhotoImage(file="pacman35.gif")
tresor=PhotoImage(file="tresor35.gif")
fantome=PhotoImage(file="fantome35.gif")
arrive=PhotoImage(file="arrivee35.gif")
Label(dessin,text="Jeu ",font=("Ubuntu",20,"bold")).pack()


can= Canvas(dessin,height=600,width=600,bg="white")
can.pack(side=LEFT)

texte=StringVar()
texte.set("Ridick Francky ?")

bdem=Button(dessin,textvariable=texte,command=new,font=("Ubuntu",20,"bold"))
bdem.pack(side=TOP)

cadre=Frame(dessin, pady=50, width=160)

BH=Button(cadre, command=H, text='H',font=("Ubuntu",20,"bold"))
BH.pack()
cadremilieu=Frame(cadre)
cadremilieu.pack()
BG=Button(cadremilieu, command=G, text='G',font=("Ubuntu",20,"bold"))
BD=Button(cadremilieu, command=D, text='D',font=("Ubuntu",20,"bold"))
BB=Button(cadre, command=B, text='B',font=("Ubuntu",20,"bold"))


BG.pack(side=LEFT)
BD.pack(side=LEFT)
BB.pack()

bq=Button(dessin,text="Quitter",command=monquitter,font=("Ubuntu",20,"bold"))
bq.pack(side=BOTTOM)  

cadreScore=Frame(dessin, pady=50, padx=20)
cadreScore.pack(side=BOTTOM)
lab=Label(cadreScore, text= "votre score",font=("Ubuntu",20,"bold"))
txt=Text(cadreScore, height=1, width=4,font=("Ubuntu",20,"bold"))
lab.pack(side=LEFT)
txt.pack(side=LEFT)


 


dessin.mainloop()
