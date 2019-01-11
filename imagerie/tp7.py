from utilitaire import *
from math import *
from random import *







def AmplitudeGradient(ims) :
    imd=Image.new("L",ims.size)
    width=ims.size[0]
    height=ims.size[1]
    pixs=ims.load()
    pixd=imd.load()
    for j in range(1,height-1):
        for i in range(1,width-1):
            dx=(pixs[i-1,j]-pixs[i+1,j])/2
            dy=(pixs[i,j+1]-pixs[i,j-1])/2
            pixd[i,j]=int(sqrt(dx**2+dy**2))
            

    return imd

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
def GradientC(ims) :
    imd=Image.new("L",ims.size)
    width=ims.size[0]
    height=ims.size[1]
    pixs=ims.load()
    pixd=imd.load()
    for j in range(2,height-2):
        for i in range(2,width-2):
        #for c in range(2):
            dx0=(pixs[i-2,j][0]-8*pixs[i-1,j][0]+8*pixs[i+1,j][0]-pixs[i+2,j][0])/12
            dy0=(pixs[i,j-2][0]-8*pixs[i,j-1][0]+8*pixs[i,j+1][0]-pixs[i,j+2][0])/12
            dx1=(pixs[i-2,j][1]-8*pixs[i-1,j][1]+8*pixs[i+1,j][1]-pixs[i+2,j][1])/12
            dy1=(pixs[i,j-2][1]-8*pixs[i,j-1][1]+8*pixs[i,j+1][1]-pixs[i,j+2][1])/12
            dx2=(pixs[i-2,j][2]-8*pixs[i-1,j][2]+8*pixs[i+1,j][2]-pixs[i+2,j][2])/12
            dy2=(pixs[i,j-2][2]-8*pixs[i,j-1][2]+8*pixs[i,j+1][2]-pixs[i,j+2][2])/12
            dx=(dx0+dx1+dx2)/3
            dy=(dy0+dy1+dy2)/3
            pixd[i,j]=int(sqrt(dx**2+dy**2))
            
    return imd

def GradientC1(ims) :
    imd=Image.new("RGB",ims.size)
    width=ims.size[0]
    height=ims.size[1]
    pixs=ims.load()
    pixd=imd.load()
    for j in range(2,height-2):
        for i in range(2,width-2):
        #for c in range(2):
            dx0=(pixs[i-2,j][0]-8*pixs[i-1,j][0]+8*pixs[i+1,j][0]-pixs[i+2,j][0])/12
            dy0=(pixs[i,j-2][0]-8*pixs[i,j-1][0]+8*pixs[i,j+1][0]-pixs[i,j+2][0])/12
            dx1=(pixs[i-2,j][1]-8*pixs[i-1,j][1]+8*pixs[i+1,j][1]-pixs[i+2,j][1])/12
            dy1=(pixs[i,j-2][1]-8*pixs[i,j-1][1]+8*pixs[i,j+1][1]-pixs[i,j+2][1])/12
            dx2=(pixs[i-2,j][2]-8*pixs[i-1,j][2]+8*pixs[i+1,j][2]-pixs[i+2,j][2])/12
            dy2=(pixs[i,j-2][2]-8*pixs[i,j-1][2]+8*pixs[i,j+1][2]-pixs[i,j+2][2])/12
            
            pixd[i,j]=(int(sqrt(dx0**2+dy0**2)),int(sqrt(dx1**2+dy1**2)),int(sqrt(dx2**2+dy2**2)))
            
            
    return imd
def TestGrad():
    im=ouvrir("cyto1.bmp")
    a=AmplitudeGradient(im)
    b=Gradient(im)
    affiche(a)
    affiche(b)


def Moyenneuniforme(ims):
   
    imd=Image.new("L",ims.size)
    width=ims.size[0]
    height=ims.size[1]
    pixs=ims.load()
    pixd=imd.load()
    for j in range(1,height-1):
        for i in range(1,width-1):
            pixd[i,j]=int((pixs[i+1,j]+pixs[i-1,j]+pixs[i,j+1]+pixs[i,j-1])/4)
            
    return imd

def IterMoyenneuniforme(ims,n) :
    imd=ims
    for k in range(n):
        imd=Moyenneuniforme(imd)
    return imd

def testcyto3():
    ims=ouvrir("cyto1.bmp")
    l=[2,5,10]
    for x in range (len(l)-1):
        v=randint(0,2)
        n=l[v]
        m=IterMoyenneuniforme(ims,n)
        affiche(m)


def fexponentiellex(ims, alpha): # Filtrage sur les colonnes 
  imd = Image.new('L', ims.size) 
  pixs = ims.load() 
  pixd = imd.load() 
  (width, height) = ims.size   
  for j in range(height):     
    pixd[0,j] = pixs[0,j] 
    for i in range(1,width): 
      pixd[i,j] = alpha * (pixd[i-1,j] - pixs[i,j])+ pixs[i,j] 
    for i in range(width-2, -1, -1): 
      pixd[i,j] = alpha * (pixd[i+1,j] - pixd[i,j])+ pixd[i,j] 
  return imd 

def fexponentielley(ims, alpha): #Filtrage sur les lignes 
  imd = Image.new('L', ims.size) 
  pixs = ims.load() 
  pixd = imd.load() 
  (width, height) = ims.size   
  for i in range(width):     
    pixd[i,0] = pixs[i,0] 
    for j in range(1,height): 
      pixd[i,j] = alpha * (pixd[i,j-1] - pixs[i,j])+ pixs[i,j] 
    for j in range(height-2, -1, -1): 
      pixd[i,j] = alpha * (pixd[i,j+1] - pixd[i,j])+ pixd[i,j] 
  return imd   
        
def fexponentielle(ims,alpha):
    im=fexponentiellex(ims,alpha)
    return fexponentielley(im,alpha)

def Iterexponentielle(ims,alpha,n):
    while n>0:
        ims=fexponentielle(ims,alpha)
        n-=1
    return ims

def testcyto4():
    ims=ouvrir("cyto1.bmp")
    l1=[2,5,10]
    l2=[0.1 , 0.5 , 0.8]
    for x in range (len(l1)-1):
        v=randint(0,2)
        w=randint(0,2)
        n=l1[v]
        alpha=l2[w]
        m=Iterexponentielle(ims,alpha,n)
        affiche(m)

def miniImage(ims1,ims2):
    resultat = ims1.copy()
    s=ims1.shape
    for i in range(s[0]):
        for j in range(s[1]):
            if ims1[j,i]>ims2[j,i]:
                resultat[j,i]=ims1[j,i]
            elif ims2[j,i]>ims1[j,i]:
                resultat[j,i]=ims2[j,i]
    return resultat

def diffImage(ims1,ims2):
    resultat = Image.new('L',ims1.size)
    pixs1=ims1.load()
    pixs2=ims2.load()
    pixd=resultat.load()
    (width, height) = ims1.size
    for i in range(width):     
        for j in range(height):
            #pixd[i,j]=pixs1[i,j]-pixs2[i,j]+127
            pixd[i,j]=abs(pixs1[i,j]-pixs2[i,j])
  
    return resultat      
##ims=ouvrir("cellule.jpg")
##
####affiche(GradientC1(ims))
##ims=imc2img(ims,1)
##testcyto4()
####ims=AmplitudeGradient(ims)
####ims=Gradient(ims)
####TestGrad()
###affiche(IterMoyenneuniforme(ims,20))
##ims1=ouvrir("cyto1.bmp")
##ims2=ouvrir("img.bmp")
##affiche(diffImage(ims1,ims2))




