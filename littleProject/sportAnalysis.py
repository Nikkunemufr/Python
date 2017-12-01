fich=["J1.txt","J2.txt","J3.txt"]
ligue1= ['Bordeaux', 'Marseille', 'Lille', 'Lyon', 'Lorient', 'Nantes', 'Auxerre', 'Monaco','Valenciennes', 'Montpellier', 'Toulouse', 'Sochaux', 'Boulogne', 'Nancy', 'Paris', 'Nice']

#======================Partie1======================
def buts(fichier="J1.txt"):
  b=open(fichier,"r")
  res=0
  for l in b:
    x=l.split()
    res+=int(x[2])+int(x[3])
  b.close()
  return res

def matchNul(fichier="J1.txt"):
  b=open(fichier,"r")
  res=0
  for l in b:
    x=l.split()
    if int(x[2])==int(x[3]):
      res+=1
  b.close()
  return res

def monEquipe(equipe,fichier="J1.txt"):
  b=open(fichier,"r")
  for l in b:
    x=l.split()
    if equipe==x[0] or equipe==x[1]:
      print(l,end="")

def affichage(equipe,lesjournees=fich):
  for x in range(len(lesjournees)):
    monEquipe(equipe,lesjournees[x])


#======================Partie2======================
#--------------------------------------------PartieA--------------------------------------------
def creeDico(liste=ligue1):
  return {x:0 for x in liste}

def score(dico,p):
  res=[]
  for x in dico:
    if dico[x]>=p:
      res+=[x]
    return res

def premiers(dico):
  p,res=0,[]
  for x in dico:
    if dico[x]>p:
      p=dico[x]
      res=[x]
    elif dico[x]==p:
      res+=[x]
  return res,p

#--------------------------------------------PartieB--------------------------------------------
def ajoute(dico,fichier):
  b=open(fichier,"r")
  for l in b:
    x=l.split()
    if x[2]>x[3]:
      dico[x[0]]+=3
    elif x[2]==x[3]:
      dico[x[0]]+=0
      dico[x[1]]+=1
    elif x[2]<x[3]:
      dico[x[1]]+=3
  b.close()
  return dico

#======================Partie3======================
