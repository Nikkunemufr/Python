from tp7 import *
from math import *

def consvois(ims,i,j,taille):
    vois=[]
    pixs=ims.load()
    width=ims.size[0]
    height=ims.size[1]
    listei=[x for x in range(width)]
    listej=[x for x in range(height)]
    for k in range(-taille,taille+1):
        for m in (-taille,taille+1):
            if k!=0 or m!=0:
                if i+k in listei and j+m in listej:
                    vois=vois+[pixs[i+k,j+m]]        
    #print("\t voisinage =",i,j,vois)
    return vois

def erosion1(ims,taille):
    imd=Image.new('L',ims.size)
    pixs=ims.load()
    pixd=imd.load()
    (width,height)=ims.size
    for j in range (height):
        for i in range (width):
            pixd[i,j]=min(consvois(ims,i,j,taille))
    return imd

def erosionIte1(ims,n,taille):
    for k in range(n):
        ims=erosion1(ims,taille)
    return(ims)


def dilatation1(ims,taille):
    imd=Image.new('L',ims.size)
    pixs=ims.load()
    pixd=imd.load()
    (width,height)=ims.size
    for j in range (height):
        for i in range (width):
            pixd[i,j]=max(consvois(ims,i,j,taille))
    return imd

def dilatationIte1(ims,n,taille):
    for k in range(n):
        ims=dilatation1(ims,taille)
    return(ims)

def erosion(ims):
    imd=Image.new('L',ims.size)
    pixs=ims.load()
    pixd=imd.load()
    (width,height)=ims.size
    for j in range (height):
        for i in range (width):
            pixd[i,j]=min(consvois8(ims,i,j))
    return imd

def erosionIte(ims,n):
    for k in range(n):
        ims=erosion(ims)
    return(ims)


def dilatation(ims):
    imd=Image.new('L',ims.size)
    pixs=ims.load()
    pixd=imd.load()
    (width,height)=ims.size
    for j in range (height):
        for i in range (width):
            pixd[i,j]=max(consvois8(ims,i,j))
    return imd

def dilatationIte(ims,n):
    for k in range(n):
        ims=dilatation(ims)
    return(ims)

def borderimage(ims,taille):
    imd=Image.new('L',ims.size)
    pixs=ims.load()
    pixd=imd.load()
    (width,height)=ims.size
    for j in range (taille,height-taille):
        for i in range (taille,width-taille):
            if pixs[i,j]==255: # and (pixs[i,j-1]==0 or pixs[i-1,j]==0 or pixs[i-1,j-1]==0):
                #{l=consvois8(ims,i,j)
                l=consvois(ims,i,j,taille)
                for x in l:
                    if x==0:
                        pixd[i,j]=255

            
    return imd

##ims=ouvrir('img.bmp')
####imse=erosionIte(ims,5)
##imse=dilatationIte1(ims,2,2)
##affiche(imse)
####imsbin=binarization(imse,150)
#####affiche(imsbin)
####affiche(borderimage(imsbin,3))
