"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
from tkinter import *
from random import randint
#CODE
nbr_essais_max = 10
nbr_essais = 1
borne_sup = 100
borne_inf= 1
alea_nombre = int(randint(borne_inf,borne_sup))
   
def newGame():
    global alea_nombre,nbr_essais
    nombre.delete("0",END)
    essais.delete("0.0",END)
    nbr_essais = 1
    alea_nombre = int(randint(borne_inf,borne_sup))
    essais.insert(END,"J'ai choisi un nombre entre 1 et "+str(borne_sup)+"\n")
    essais.insert(END,"A vous de le deviner en "+str(nbr_essais_max)+" tentatives au maximum !"+"\n")
    
def ok():      
    global nbr_essais
    essais.insert(END,"Essai numero "+str(nbr_essais)+"\n")
    ton_nombre=int(nombre.get())
    if ton_nombre>borne_sup or ton_nombre<borne_inf:
        essais.insert(END,str(ton_nombre)+" : Est incorrect"+"\n")
    else:
        if ton_nombre < alea_nombre:
            essais.insert(END,str(ton_nombre)+" : Est trop petit"+"\n")
        elif ton_nombre > alea_nombre:
            essais.insert(END,str(ton_nombre)+" : Est trop grand"+"\n")
        else:
            essais.insert(END,str(ton_nombre)+" : Bravo ! Vous avez trouvé "+str(alea_nombre)+" en "+str(nbr_essais)+" essai(s)"+"\n")
        nbr_essais += 1
        if nbr_essais>nbr_essais_max and ton_nombre != alea_nombre :
            essais.insert(END,str(ton_nombre)+" : Désolé, vous avez utilisé vos "+str(nbr_essais_max)+" essais en vain."+"\n")
            essais.insert(END,str(ton_nombre)+" : J'avais choisi le nombre "+str(alea_nombre)+"."+"\n")
    nombre.delete("0",END)
def bouttonPave():
    return ""
#TKINTER
#variable global
f=Tk()
pave=Frame(f)
titre=Label(f,text="Jeu du nombre mystérieux: devinez un entier compris entre 1 et 100",fg="purple",font=("comic",16,"bold"))
indication=Label(f,text="Entrez votre nombre",fg="blue",font=("comic",16,"bold"))
nombre=Entry(f)
bok=Button(f,text="OK",font=("comic",10,"bold"),command=ok)
nouvelle_partie=Button(f,text="Nouvelle Partie",font=("comic",10,"bold"),command=newGame)
quitter=Button(f,text="Quitter",font=("comic",10,"bold"),command=f.destroy)
essais=Text(f,width=80,height=20,font=("comic",16,"bold"))

for x in range(12):
    Button(pave,text=x,font=("comic",16,"bold"),command=bouttonPave)
##    deux=Button(pave,text="2",font=("comic",16,"bold"),command=ok)
##    trois=Button(pave,text="3",font=("comic",16,"bold"),command=ok)
##    quatre=Button(pave,text="4",font=("comic",16,"bold"),command=ok)
##    cinq=Button(pave,text="5",font=("comic",16,"bold"),command=ok)
##    six=Button(pave,text="6",font=("comic",16,"bold"),command=ok)
##    sept=Button(pave,text="7",font=("comic",16,"bold"),command=ok)
##    huit=Button(pave,text="8",font=("comic",16,"bold"),command=ok)
##    neuf=Button(pave,text="9",font=("comic",16,"bold"),command=ok)
##    zero=Button(pave,text="0",font=("comic",16,"bold"),command=ok)
##    effacer=Button(pave,text="C",font=("comic",16,"bold"),command=ok)
##    reponse=Button(pave,text="?",font=("comic",16,"bold"),command=ok)


#placement
titre.grid(columnspan=3)
indication.grid(row=1,column=0)
nombre.grid(row=1,column=1)
bok.grid(row=1,column=2)
essais.grid(row=2,columnspan=3)
nouvelle_partie.grid(row=3,column=2)
quitter.grid(row=4,column=2)
##un.grid(row=0,column=0)
##deux.grid(row=0,column=1)
##trois.grid(row=0,column=2)
##quatre.grid(row=1,column=0)
##cinq.grid(row=1,column=1)
##six.grid(row=1,column=2)
##sept.grid(row=2,column=0)
##huit.grid(row=2,column=1)
##neuf.grid(row=2,column=2)
##effacer.grid(row=3,column=0)
##zero.grid(row=3,column=1)
##reponse.grid(row=3,column=2)

pave.grid(row=2,column=4)
f.mainloop()
