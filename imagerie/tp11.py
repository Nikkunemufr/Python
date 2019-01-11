from tp10 import *

def Histo_Vide():
    h=[]
    for i in range(0,256):
        h+=[0,]
    return h
#print(Histo_Vide())

def Histogramme(ims):
    h=Histo_Vide()
    pixs=ims.load()
    (width, height) = ims.size
    for i in range(width):
        for j in range(height):
            h[pixs[i,j]]+=1
    return h

def HCumule(H):
    HC=Histo_Vide()
    HC[0]=H[0]
    for i in range(0,256):
        HC[i]=HC[i-1]+H[i]
    return HC

def HPCumule(H):
    HP=Histo_Vide()
    HP[0]=H[0]
    for i in range(0,256):
        HP[i]=HP[i-1]+i*H[i]
    return HP
        
def Calculseuil(ims):
    H=Histogramme(ims)
    HC=HCumule(H)
    HP=HPCumule(H)
    maxi=0
    seuil=0
    for s in range (0,256):
        if HC[s]!=0:
            M0 =HP[s]/HC[s]
        elif HC[s]==0:
            M0=0
        if (HC[255]-HC[s])!=0:
            M1 = (HP[255]-HP[s])/(HC[255]-HC[s])
        elif (HC[255]-HC[s])==0:
            M1=0
        V=HC[s]*(HC[255]-HC[s])*((M0-M1)*(M0-M1))
        #print(V)
        if V>maxi:
            maxi=V
            seuil=s
    #print(seuil)
    return seuil

def Binarizationvariance(ims):
    seuil=Calculseuil(ims)
    return binarization(ims,seuil)






ims=ouvrir("img.bmp")
#print(Histogramme(ims))   
H=Histogramme(ims)
print(Calculseuil(ims))
affiche(Binarizationvariance(ims))
#print(HCumule(H))
#print(HPCumule(H))
