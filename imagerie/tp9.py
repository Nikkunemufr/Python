from TP8 import *

def ouverture(ims):
    ims= erosion(ims)
    ims=dilatation(ims)
    return ims

def fermeture(ims):
    ims=dilatation(ims)
    ims= erosion(ims)
    return ims

def test2nbgris():
    listeimg=  ["img.bmp", "cyto1.bmp"]
    for k in listeimg:
        img=ouvrir(k)
        #affiche(img)
        mon_ouverture_k=ouverture(img)
        affiche(mon_ouverture_k)
        #sauvegarde(mon_ouverture_k,k+"_gris'_ouverture.bmp")
        ma_fermeture_k=fermeture(img)
        affiche(ma_fermeture_k)
        #sauvegarde(ma_fermeture_k,k+"_gris_fermeture.bmp")

def test2nbcouleur():
    listeimg=  ["img.bmp", "cellule.jpg"]
    for k in listeimg:
        img=ouvrir(k)
        mon_ouverture_k=ouverture(img)
        affiche(mon_ouverture_k)
        ma_fermeture_k=fermeture(img)
        affiche(ma_fermeture_k)

def test2bin():
    listeimg=  ["lenabin.bmp", "tanbin.bmp"]
    for k in listeimg:
        img=ouvrir(k)
        mon_ouverture_k=ouverture(img)
        affiche(mon_ouverture_k)
        ma_fermeture_k=fermeture(img)
        affiche(ma_fermeture_k)

#######EXERCICE 2 ###########

def morphocyto1():
    l=[2,5,10] 
    img=ouvrir("cyto1.bmp")
    #img=imc2img(img,1)
    for n in l:
        ims=Iterexponentielle(img,0.5,n)
        affiche(ims)
    
#test2nbgris()
#test2nbcouleur()
##test2bin()
##morphocyto1()
