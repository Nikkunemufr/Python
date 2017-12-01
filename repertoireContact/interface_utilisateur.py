"""
     :Authors : MORTELIER Alexis
     Répertoire de contact
"""

from stockage import *
from recherche import *
from tkinter import*
from tkinter.filedialog import askopenfilename

def ajouterPerso():
    """
     Cette fonction gère l'interface pour ajouter un contact au répertoire
    """
    ajout=Toplevel(fen)

    Label(ajout,text="nom").pack()
    nomEntry=Entry(ajout)
    nomEntry.pack()

    Label(ajout,text="prenom").pack()
    prenomEntry=Entry(ajout)
    prenomEntry.pack()

    Label(ajout,text="Numero Fixe").pack()
    num1Entry=Entry(ajout)
    num1Entry.pack()

    Label(ajout,text="Numero Portable").pack()
    num2Entry=Entry(ajout)
    num2Entry.pack()

    Label(ajout,text="Adresse numero 1").pack()
    adresse1Entry=Entry(ajout)
    adresse1Entry.pack()

    Label(ajout,text="Adresse numero 2").pack()
    adresse2Entry=Entry(ajout)
    adresse2Entry.pack()

    Label(ajout,text="E-Mail").pack()
    mailEntry=Entry(ajout)
    mailEntry.pack()

    Label(ajout,text="Date de naissance (JJ/MM/AAAA)").pack()
    annivEntry=Entry(ajout)
    annivEntry.pack()


    Button(ajout,text="Ajouter le contact", command=addPerso(nomEntry.get(),prenomEntry.get(),num1Entry.get(),num2Entry.get(),adresse1Entry.get(),adresse2Entry.get(),mailEntry.get(),annivEntry.get())).pack()
    Button(ajout,text="Quitter", command=ajout.destroy).pack()
    ajout.mainloop()



def supprimerPerso():
    """
     Cette fonction gère l'interface pour supprimer un contact au répertoire
    """
    suppr=Toplevel(fen)

    Label(suppr,text="Rang du contact").pack()
    rangEntry=Entry(suppr)
    rangEntry.pack()

    val=rangEntry.get()
    Button(suppr,text="Supprimer le contact", command=delPerso(val)).pack()
    Button(suppr,text="Quitter", command=suppr.destroy).pack()
    suppr.mainloop()

def modifierPerso():
    """
     Cette fonction gère l'interface pour modifier un contact du répertoire
    """
    modifie=Toplevel(fen)

    Label(modifie,text="Rang du contact").pack()
    rangEntry=Entry(modifie)
    rangEntry.pack()

    Label(modifie,text="nom").pack()
    nomEntry=Entry(modifie)
    nomEntry.pack()

    Label(modifie,text="prenom").pack()
    prenomEntry=Entry(modifie)
    prenomEntry.pack()

    Label(modifie,text="Numero Fixe").pack()
    num1Entry=Entry(modifie)
    num1Entry.pack()

    Label(modifie,text="Numero Portable").pack()
    num2Entry=Entry(modifie)
    num2Entry.pack()

    Label(modifie,text="Adresse numero 1").pack()
    adresse1Entry=Entry(modifie)
    adresse1Entry.pack()

    Label(modifie,text="Adresse numero 2").pack()
    adresse2Entry=Entry(modifie)
    adresse2Entry.pack()

    Label(modifie,text="E-Mail").pack()
    mailEntry=Entry(modifie)
    mailEntry.pack()

    Label(modifie,text="Date de naissance (JJ/MM/AAAA)").pack()
    annivEntry=Entry(modifie)
    annivEntry.pack()

    Button(modifie,text="Modifier le contact", command=modifierContact(rangEntry.get(),nomEntry.get(),prenomEntry.get(),num1Entry.get(),num2Entry.get(),adresse1Entry.get(),adresse2Entry.get(),mailEntry.get(),annivEntry.get())).pack()
    Button(modifie,text="Quitter", command=modifie.destroy).pack()
    ajout.mainloop()

def modifierContact(rang,nom,prenom,num1,num2,adresse1,adresse2,mail,anniv):
    """
     Cette fonction sert a appeller les deux fonctions de stockage delPerso qui supprime le personnage au rang donnée puis rajoute le contacte au répertoire
    """
    delPerso(rang)
    addPerso(nom,prenom,num1,num2,adresse1,adresse2,mail,anniv)

def rechercheAnniv():
    """
     Cette fonction gère l'interface pour rechercher un contact par rapport a son anniversaire
    """
    anniv=Toplevel(fen)
    Button(anniv,text="Rechercher", command=chercheAnnif).pack()
    Button(anniv,text="Quitter", command=anniv.destroy).pack()
    anniv.mainloop()

def rechercheNom():
    """
     Cette fonction gère l'interface pour rechercher un contact par rapport a son nom
    """
    searchNom=Toplevel(fen)

    Label(searchNom,text="Nom du contact").pack()
    nomEntry=Entry(searchNom)
    nomEntry.pack()

    Button(searchNom,text="Rechercher", command=nom(nomEntry.get())).pack()
    Button(searchNom,text="Quitter", command=searchNom.destroy).pack()
    searchNom.mainloop()

def nom(name):
    """
     Cette fonction insére dans l'affichage du répertoire les contacts prenant le nom indiqué
     :param name : nom du contact
    """
    lRep.delete(0,END)
    for x in range(len(repertoire)):
        if name==repertoire[x].split()[0]:
            val=repertoire[x].split()[0]+" "+repertoire[x].split()[1]
            lRep.insert(END,val)

def recherchePrenom():
    """
     Cette fonction gère l'interface pour rechercher un contact par rapport a son prénom
    """
    searchPrenom=Toplevel(fen)

    Label(searchPrenom,text="Prenom du contact").pack()
    prenomEntry=Entry(searchPrenom)
    prenomEntry.pack()

    Button(searchPrenom,text="Rechercher", command=prenom).pack()
    Button(searchPrenom,text="Quitter", command=searchPrenom.destroy).pack()
    searchPrenom.mainloop()

def prenom(prename):
    """
     Cette fonction insére dans l'affichage du répertoire les contacts prenant le prénom indiqué
     :param name : prenom du contact
    """
    lRep.delete(0,END)
    for x in range(len(repertoire)):
        if prename==repertoire[x].split()[1]:
            val=repertoire[x].split()[0]+" "+repertoire[x].split()[1]
            lRep.insert(END,val)

def chercheAnnif():
    """
     Cette fonction insére dans l'affichage du répertoire les contacte ayant leur anniversaire dans le mois
    """
    lRep.delete(0,END)
    today = date.today()
    moisactu = today.month
    for x in range(len(repertoire)):
        if repertoire[x].split()[7][3]=="0":
            moisNaissance=int(repertoire[x].split()[7][4])
        else:
            moisNaissance=int(repertoire[x].split()[7][3]+repertoire[x].split()[7][4])

        if moisNaissance==moisactu:
            val=repertoire[x].split()[0]+" "+repertoire[x].split()[1]
            lRep.insert(END,val)

def load():
    """
     Cette fonction appelle le fichier texte faisant office de répertoire
    """
    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
    global rep
    rep=filename
    chargeRep()

def chargeRep():
    """
     Cette fonction charge le répertoire et l'affiche dans la listbox
    """
    global repertoire
    lRep.delete(0,END)
    repertoire=[]
    fichier = open(rep, "r")
    for l in fichier:
        repertoire+=[l]
        x=l.split()
        val=x[0]+" "+x[1]
        lRep.insert(END,val)
    fichier.close()

def save():
    """
     Cette fonction sauvegarde le répertoire
    """
    sauv=Toplevel(fen)
    Label(sauv,text="Nom du fichier :").pack()
    nomFichier = Entry(sauv)
    nomFichier.pack()
    val=nomFichier.get()
    Button(sauv,text="Sauvegarde du repertoire", command = clicked(val)).pack()
    Button(sauv,text="Quitter", command = sauv.destroy).pack()
    sauv.mainloop()

def clicked(Input):
    """
     Cette fonction sauvegarde le repertoire dans un fichier texte
     :param Input: nom du fichier
    """
    fichier = open(str(Input + ".txt"),"w")
    for x in range(len(repertoire)):
        fichier.write(str(repertoire[x])+"\n")
    fichier.close()

def info():
    """
     Cette fonction affiche une fenetre d'aide
    """
    about=Toplevel(fen)
    Label(about,text="Repertoire de contact créer par Alexis Mortelier").pack()

def voirContact():
    """
     Cette fonction affiche toute les informations du contact selectionné
    """
    global repertoire
    index=lRep.curselection()[0]
    infocontact.set(repertoire[index])


rep=""

fen=Tk()
fen.geometry("800x600")
fen.title("Repertoire")

menubar = Menu(fen)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Importer", command=load)
menu1.add_command(label="Exporter", command=save)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Ajouter", command=ajouterPerso)
menu2.add_command(label="Modifier", command=modifierPerso)
menu2.add_command(label="Supprimer", command=supprimerPerso)
menubar.add_cascade(label="Contact", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Recherche prenom", command=recherchePrenom)
menu3.add_command(label="Recherche nom", command=rechercheNom)
menu3.add_command(label="Anniversaire dans le mois", command=rechercheAnniv)
menubar.add_cascade(label="Rechercher", menu=menu3)

menu4 = Menu(menubar, tearoff=0)
menu4.add_command(label="A propos", command=info)
menubar.add_cascade(label="Aide", menu=menu4)

fen.config(menu=menubar)

# frame 1
Frame1 = Frame(fen)
Frame1.grid(row=0, column=0)
# frame 2
Frame2 = Frame(fen)
Frame2.grid(row=0, column=1)
# frame 3
Frame3 = Frame(fen)
Frame3.grid(row=1, column=1)

infocontact=StringVar()
infocontact.set("Aucun contact selectionné")

lInfo=Label(Frame1,textvariable=infocontact)
lInfo.pack()
lRep = Listbox(Frame2)
lRep.pack()
lReload=Button(Frame3,text="Recharger Repertoire",command=chargeRep)
lReload.pack()
lQuit=Button(Frame3,text="Voir",command=voirContact)
lQuit.pack()
lVoir=Button(Frame3,text="Quitter",command=fen.destroy)
lVoir.pack()

fen.mainloop()
