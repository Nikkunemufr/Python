from PIL import Image
from math import *

def imc2img(imc,n):
    #transforme une image couleur en une image de niveaux de gris
    img=Image.new("L",imc.size)
    pixc=imc.load()
    pixg=img.load()
    width=imc.size[0]
    height=imc.size[1]
    for j in range(height):
        for i in range(width):
            pixg[i,j]=pixc[i,j][n]
    img.save("img.bmp")
    return img

def ouvrir(nomimg):
    #creer l'objet image  a partir du fichier image
    img=Image.open(nomimg)
    width=img.size[0]
    height=img.size[1]
    print ("width = %s  height = %s mode= %s" %(width,height,img.mode))
    return img

def affiche(img):
        img.show()

def Histo_Vide():
    h=[]
    for i in range(0,256):
        h+=[0,]
    return h

def Histogramme(ims):
    h=Histo_Vide()
    pixs=ims.load()
    (width, height) = ims.size
    for i in range(width):
        for j in range(height):
            h[pixs[i,j]]+=1
    return h

def histonormalise(ims):
    h=Histogramme(ims)
    (width, height) = ims.size
    for x in h:
        x = x/(width*height)
    return h

def HCumule(H):
    HC=Histo_Vide()
    HC[0]=H[0]
    for i in range(0,256):
        HC[i]=HC[i-1]+H[i]
    return HC

def HCumulFin(H):
    HCF = Histo_Vide()
    HCF[-1] = H[-1]
    for i in range(-2,-255,-1):
        HCF[i]=HCF[i+1]+H[i]
    return HCF

def histoNlog(H):
    HN = H
    HNlog = Histo_Vide()
    HNlog[0]=HN[0]
    for i in range(0,255):
        if HN[i] > 0:
            HNlog[i]=HN[i]*log(HN[i])
    return HNlog
                               
def seuilentropie(ims):
    Histo_N=Histogramme(ims)
    P=HCumule(Histo_N)
    HN = histoNlog(Histo_N)
    H1=HCumule(Histo_N)
    H2 = HCumulFin(Histo_N)
    maxi=0
    seuil=0
    for s in range (0,256):
        if P[s]>0 and 1 - P[s] > 0: 
            TE=log(P[s]*(1-P[s]))- H1[s]/P[s] - H2[s+1]/(1 - P[s])
        elif P[s]==0:
            M0=0
        if (P[255]-P[s])!=0:
            M1 = (H1[255]-H1[s])/(P[255]-P[s])
        elif (P[255]-P[s])==0:
            M1=0
        M0 = 0
        V=P[s]*(P[255]-P[s])*((M0-M1)*(M0-M1))
        #print(V)
        if V>maxi:
            maxi=V
            seuil=s
    #print(seuil)
    return seuil

def binarization(img,seuil):
    imgbin=Image.new("L",img.size)
    pixg=img.load()
    pixbin=imgbin.load()
    width=img.size[0]
    height=img.size[1]
    for j in range(height):
        for i in range(width):
            if pixg[i,j]>seuil:
                pixbin[i,j]=255
            else:
                pixbin[i,j]=0
    return imgbin

def Binarisationentropie(ims):
    seuil=seuilentropie(ims)
    return binarization(ims,seuil)

def list_image():
    liste = ["texte.bmp", "cyto1.bmp", "tangram.bmp", "lena.bmp"]
    for ims in liste:
        im = ouvrir(ims)
        if im.mode == "RGB":
            im=imc2img(im,1)
        affiche(Binarisationentropie(im))

ims = ouvrir("cyto1.bmp")
list_image()

def Gradient(ims) :
    imd=Image.new("L",ims.size)
    width=ims.size[0]
    height=ims.size[1]
    pixs=ims.load()
    pixd=imd.load()
    for j in range(2,height-2):
        for i in range(2,width-2):
            dx=(pixs[i-2,j]-8*pixs[i-1,j]+8*pixs[i+1,j]-pixs[i+2,j])/12
            dy=(pixs[i,j-2]-8*pixs[i,j-1]+8*pixs[i,j+1]-pixs[i,j+2])/12
            
            pixd[i,j]=int(sqrt(dx**2+dy**2))
    return imd

def list_imageEx2():
    liste = ["cyto1.bmp", "tangram.bmp", "lena.bmp"]
    for ims in liste:
        im = ouvrir(ims)
        if im.mode == "RGB":
            im=imc2img(im,1)
        affiche(Gradient(im))


