from tp9 import *

def DiffusionLineaire(ims,n,tau):
    imd0 = Image.new('F', ims.size) 
    imd1 = Image.new('F', ims.size) 
    pixs = ims.load() 
    pixd0 = imd0.load() 
    (width, height) = ims.size 
    for j in range(height): 
        for i in range(width): 
            pixd0[i,j] = pixs[i,j] 
    for n_i in range(n): 
        pixd0 = imd0.load() 
        pixd1 = imd1.load() 
        for j in range(1,height-1): 
            for i in range(1,width-1): 
                Lap= pixd0[i,j+1] + pixd0[i,j-1]+ pixd0[i-1,j]+ pixd0[i+1,j]-4*pixd0[i,j]
                pixd1[i,j] = pixd0[i,j] + tau * Lap 
                (imd0, imd1) = (imd1, imd0) 
    return imd0

def dn1_g(x,k):
    return 1/((x/k)**2+1)



def DiffusionNonLineaire(ims,k): 
    imd = Image.new('F', ims.size)  
    pixs = ims.load() 
    pixd = imd.load() 
    (width, height) = ims.size 

    for j in range(1,height-1): 
        for i in range(1,width-1):
            diff_c1=abs(pixs[i+1,j]-pixs[i,j])
            diff_c2=abs(pixs[i-1,j]-pixs[i,j])
            diff_c3=abs(pixs[i,j+1]-pixs[i,j])
            diff_c4=abs(pixs[i,j-1]-pixs[i,j])
            c1 = dn1_g(diff_c1,k)
            c2 = dn1_g(diff_c2,k) 
            c3 =  dn1_g(diff_c3,k)
            c4 =  dn1_g(diff_c4,k)
            s =  (diff_c1 + diff_c2 + diff_c3 + diff_c4)
            if s !=0:
                tau=1 / s
            else:
                tau=1
            pixd[i,j] = pixs[i,j] + tau*(c1*diff_c1+c2*diff_c2+c3*diff_c3+c4*diff_c4)   
    return imd
def IterDiffusionNonLineaire(ims,n,k):
    for n_i in range(n):
        ims = DiffusionNonLineaire(ims,k)
    return ims

##def DiffusionNonLineaire1(ims,n,k): 
##    imd0 = Image.new('F', ims.size) 
##    imd1 = Image.new('F', ims.size) 
##    pixs = ims.load() 
##    pixd0 = imd0.load() 
##    (width, height) = ims.size 
##    for j in range(height): 
##        for i in range(width): 
##            pixd0[i,j] = pixs[i,j] 
##    for n_i in range(n): 
##        #print ('Iteration', n_i) 
##        pixd0 = imd0.load() 
##        pixd1 = imd1.load() 
##        for j in range(1,height-1): 
##            for i in range(1,width-1):
##                diff_c1=abs(pixd0[i+1,j]-pixd1[i,j])
##                diff_c2=abs(pixd0[i-1,j]-pixd1[i,j])
##                diff_c3=abs(pixd0[i,j+1]-pixd1[i,j])
##                diff_c4=abs(pixd0[i,j-1]-pixd1[i,j])
##                c1 = dn1_g(diff_c1,k)
##                c2 = dn1_g(diff_c2,k) 
##                c3 =  dn1_g(diff_c3,k)
##                c4 =  dn1_g(diff_c4,k)
##                s =  (diff_c1 + diff_c2 + diff_c3 + diff_c4)
##                if s !=0:
##                    tau=1 / s
##                else:
##                    tau=1
##                pixd1[i,j] = pixd0[i,j] + tau*(c1*diff_c1+c2*diff_c2+c3*diff_c3+c4*diff_c4)   
##        (imd0, imd1) = (imd1, imd0) 
##    return imd0


ims = ouvrir("tangram.bmp")
#diffuser5=DiffusionLineaire(ims,5,0.2)
#diffuser10=DiffusionLineaire(ims,10,0.2)
#diffuser15=DiffusionLineaire(ims,15,0.2)
#diffuser30=DiffusionLineaire(ims,30,0.2)
##diffuser5=DiffusionLineaire(ims,5,0.9)
##diffuser10=DiffusionLineaire(ims,10,0.9)
##diffuser15=DiffusionLineaire(ims,15,0.9)
##diffuser30=DiffusionLineaire(ims,30,0.9)
##diffuserNon5=IterDiffusionNonLineaire(ims,100,300)
####diffuserNon10=DiffusionNonLineaire(ims,10,50,0.15)
####diffuserNon15=DiffusionNonLineaire(ims,15,50,0.15)
####diffuserNon30=DiffusionNonLineaire(ims,30,0.15)
###affiche(diffuserNon30)
##affiche(diffuserNon5)
    
