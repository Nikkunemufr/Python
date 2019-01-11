from PIL import Image
#TP 5 ex 1 Q1
def ouvrir(nomimg):
    #creer l'objet image  a partir du fichier image
    img=Image.open(nomimg)
    width=img.size[0]
    height=img.size[1]
    print ("width = %s  height = %s mode= %s" %(width,height,img.mode))
    return img

##def ouvrir():
##    nomimg=raw_input("entrer le nom de image avec extension : ")
##    #creer l'objet image  a partir du fichier image
##    img=Image.open(nomimg)
##    width=img.size[0]
##    height=img.size[1]
##    print ("width = %s  height = %s mode= %s" %(width,height,img.mode))
##    return img

def affiche(img):
        img.show()

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
def imc2rouge(imc):
    #transforme une image couleur en l'image de niveaux de gris du canal rouge
    img=Image.new("L",imc.size)
    pixc=imc.load()
    pixg=img.load()
    width=imc.size[0]
    height=imc.size[1]
    for j in range(height):
        for i in range(width):
            pixg[i,j]=pixc[i,j][0]
    img.save("img.bmp")
    return img

#TP 5 ex 1 Q2
def consvois4(ims,i,j):
    pixs=ims.load()    
    res=[pixs[i,j]]    
    if i>0:
        res=res+[pixs[i-1,j]]
    if j>0:
        res=res+[pixs[i,j-1]]
    if i<width:
        res=res+[pixs[i+1,j]]
    if j<height:
        res=res+[pixs[i,j+1]]
    return res

#TP 5 ex 1 Q3
def consvois8(ims,i,j):
    pixs=ims.load()    
    res=[]    
    width=ims.size[0]
    height=ims.size[1]
    for k in (-1,0,1):
        for m in (-1,0,1):
            if k+j in range(1,height-1) and m+i in range(1,width-1):
                res=res+[pixs[m+i,k+j]]
    return res

#TP 5 ex 1 Q4
# listes des coord des voisins de i,j
def voisinage(ims,i,j):
    vois=[]
    width=ims.size[0]
    height=ims.size[1]
    listei=[x for x in range(width)]
    listej=[x for x in range(height)]
    for k in (-1,0,1):
        for m in (-1,0,1):
            if k!=0 or m!=0:
                if i+k in listei and j+m in listej:
                    vois=vois+[[i+k,j+m]]        
    #print("\t voisinage =",i,j,vois)
    return vois
#TP 5 ex 2  aruithmétique et logique
#TP 5 ex 2 Q1
def add(img1,img2):
    imadd=Image.new("L",max(img1.size,img2.size))
    width=max(img1.size[0],img1.size[0])
    height=max(img1.size[1],img1.size[1])
    pixg1=img1.load()
    pixg2=img2.load()
    pixadd=imadd.load()
    for j in range(height):
        for i in range(width):
            pixadd[i,j]=pix1[i,j]+pix2[i,j]    
    return imadd

#TP 5 ex 2 Q2
def diff(img1,img2):
    imdiff=Image.new("L",max(img1.size,img2.size))
    width=max(img1.size[0],img1.size[0])
    height=max(img1.size[1],img1.size[1])
    pixg1=img1.load()
    pixg2=img2.load()
    pixdiff=imdiff.load()
    for j in range(height):
        for i in range(width):
            pixdiff[i,j]=pixg1[i,j]-pixg2[i,j] + 127
    return imdiff

#TP 5 ex 2 Q3
def maximg(img1,img2):
    imet=Image.new("L",max(img1.size,img2.size))
    width=max(img1.size[0],img1.size[0])
    height=max(img1.size[1],img1.size[1])
    pix1=img1.load()
    pix2=img2.load()
    pixet=imet.load()
    for j in range(height):
        for i in range(width):
            pixet[i,j]=max([pix1[i,j],pix2[i,j]])    
    return imet

#TP 5 ex 2 Q4
def minimg(img1,img2):
    imou=Image.new("L",max(img1.size,img2.size))
    width=max(img1.size[0],img1.size[0])
    height=max(img1.size[1],img1.size[1])
    pixg1=img1.load()
    pixg2=img2.load()
    pixou=imou.load()
    for j in range(height):
        for i in range(width):
            pixou[i,j]=min([pix1[i,j],pix2[i,j]])    
    return imou

#TP 5 ex 2 Q5
def minimage(img):
    width=img.size[0]
    height=img.size[1]
    pixg=img.load()
    minimum=pixg[0,0]
    for j in range(height):
        for i in range(width):
            if minimum > pixg[i,j]:
                minimum=pixg[i,j]
    return minimum

#TP 5 ex 2 Q6
def maximage(img):
    width=img.size[0]
    height=img.size[1]
    pixg=img.load()
    maximum=pixg[0,0]
    for j in range(height):
        for i in range(width):
            if maximum < pixg[i,j]:
                maximum=pixg[i,j]
    return maximum

#TP 5 ex 2 Q7
def inverse(ims):
    width=ims.size[0]
    height=ims.size[1]
    iminv=Image.new("L",ims.size)
    pix=ims.load()
    pixinv=iminv.load()
    for j in range(height):
        for i in range(width):
            pixinv[i,j]=255-pix[i,j]
    return iminv

#TP 5 ex 3 seuillage et visualisation
#TP 5 ex 3 Q1
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

#TP 5 ex 3 Q2
def binarization2(img,seuil1,seuil2):
    imgbin=Image.new("L",img.size)
    pixg=img.load()
    pixbin=imgbin.load()
    width=img.size[0]
    height=img.size[1]
    for j in range(height):
        for i in range(width):
            if pixg[i,j]>seuil1 and pixg[i,j]<seuil2:
                pixbin[i,j]=255
            else:
                pixbin[i,j]=0
    return imgbin

#TP 5 ex 3 Q3
def frontiere(ims):
    imfr=Image.new("L",ims.size)
    pixg=ims.load()
    pixfr=imfr.load()
    width=ims.size[0]
    height=ims.size[1]
    print (pixg[0,0] )#verif niveaux de gris=une seule valeur  couleur=tuple de 3 val
    for j in range(1,height-1):
        for i in range(1,width-1):
            if pixg[i,j]==255 and ( pixg[i-1,j]==0 or pixg[i+1,j]==0 or pixg[i,j-1]==0 or pixg[i,j+1]==0):
                pixfr[i,j]=255
            else:
                pixfr[i,j]=0
    return imfr
#TP 5 ex 3 Q4
def superposition(ims,imsfr):
    return maximg(ims,imsfr)

#TP 5 ex 4 Q1 q2 q3 q4
def testcyto1():
##    nomimage1="cyto1.bmp"
##    msg1=nomimage1+" 0 180"
##    nomimage2="femme.bmp"
##    msg2=nomimage2+" "
    ims=ouvrir("cellule.jpg")
    ims=imc2img(ims,1)
    iminv=inverse(ims)
    affiche(iminv)
    listeseuil=[x for x in range(70,250,20)]
    for seuil in listeseuil:
        imsbin=binarization2(ims,seuil,255)
        imfr=frontiere(imsbin)
        imvisu=superposition(ims,imfr)
        affiche(imvisu)
        
#testcyto1()
    


















