"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
    Jeu du latroncules réalisé en python dans le cadre du projet Methodologie
"""
from tkinter import*
from time import *
from random import *

#####################################Sauvegarde#####################################
def chargePartie():
  """
      Cette fonction charge la grille et le tour prealablement enregistré puis lance le jeu
      :param n: numero de la sauvegarde
      :type n: entier
  """
  global grille
  global tour
  global intervalleChrono
  global gameMode
  nbSav=n.get()
  grille=refaitGrille(load(nbSav)[0][:-1])#Reassemble la grille de la sauvegarde
  tour=int(load(nbSav)[1][:-1])#Indique le tour de la sauvegarde
  gameMode=int(load(nbSav)[2][:-1])
  affGrille()
  affPion()
  intervalleChrono = 0
  affChrono.configure(text='')
  chrono()
  if victoire(grille)==False:
    can.bind("<Button-1>", prevDep)
  else:
    info.set("Victoire du joueur"+" "+victoire(grille))
    intervalleChrono=2
    gameMode=0
    can.unbind("<Button-1>")

def save():
  """
      Cette fonction sauvegarde la grille et le tour de la partie actuelle dans un fichier texte
      :param n: numero de la sauvegarde
      :type n: entier
  """
  nbSav=n.get()
  transforme=eclateGrille(grille)#Eclate la grille
  fichier = open("save"+nbSav+".txt", "w")#Ecris le fichier de sauvegarde
  fichier.write(transforme+"\n"+str(tour)+"\n"+str(gameMode)+"\n")#Ecris dans le fichier les elements de la grille, saute une ligne, et écris le tour
  fichier.close()

def load(n):
  """
      Cette fonction lis chaque ligne du fichier texte contenant la sauvegarde
      :param n: numero de la sauvegarde
      :type n: entier
  """
  fichier = open("save"+str(n)+".txt", "r")#Lis le fichier de sauvegarde
  sauvegarde = fichier.readlines()#Lis chaque ligne du fichier
  fichier.close()
  return sauvegarde

def refaitGrille(grille):
  """
      Cette fonction refait la grille qui a été prélablement eclaté par la fonction eclatGrille
      :param grille: ligne d'un fichier texte
      :type grille:string
  """
  res=[]
  lettre=""
  comptage=0
  ligne=[]
  for x in range(len(grille)):#Parcours toutes les caractères
    lettre+=grille[x]
    comptage+= 1
    if comptage%3==0:#Tout les 3 caractères
      ligne+=[list(lettre)]#Ajoute le caractère dans la liste intervalle
      lettre=""#reinitialiste les caractères
    if comptage%(3*8)==0:#Lorsqu'on atteint 24 on obtient une ligne entière du plateau
      res+=[list(ligne)]#J'ajoute donc une ligne du plateau au résultat
      lettre=""#reinitialiste les caractères
      ligne=[]#reinitialiste la ligne du plateau
  return res

def eclateGrille(grille):
  """
      Cette fonction eclate la grille et la transforme en string en ne gardant que la couleur de la case, le type du pion, le joueur, ainsi que les cases vides représentés par des espaces
      :param grille: grille du jeu
      :type grille:liste
  """
  res=""
  for ligne in grille:#Pour chaque ligne dans la grille
    for case in ligne:#Pour chaque case de la ligne
      for element in range(len(case)):#Pour chaque élement de la case
        res+=str(case[element])#Chaine de caractere comportant les elements
  return res
#####################################Initialisation du plateau de jeu#####################################

def creerGrille(n=8):
  """
      Cette fonction créer la grille de jeu du latroncules
      :param n: indique la taille de la grille (n*n)
      :type n: entier
  """
  grille=[0]*n
  for x in range(n):
    grille[x]= [0]*n
    for y in range(n):
      grille[x][y]=[" "," "," "]
  placerCases(grille)#place les cases
  placerPions(grille)#places les pions et indique a quels joueurs ils appartiennent
  return grille

def placerCases(grille):
  """
      Cette fonction place les cases en faisant un damier de case noir et blanche
      :param grille: grille vierge du jeu
      :type grille: liste
  """
  for x in range(len(grille)):
    for y in range(len(grille)):
      if (x+y)%2==0:#Si la case est paire
        grille[x][y][0]="B"#Case blanche
      else:#Si la case est impaire
        grille[x][y][0]="N"#Case noir
  return grille

def placerPions(grille):
  """
      Cette fonction place les pions ainsi que les joueurs auxquels appartiennent les pions sur la grille en respectant les regles du latroncules
      :param grille: grille vierge du jeu
      :type grille: liste
  """
  n=len(grille)
  for x in range(len(grille)):
    if x%2==0:#Place les fantassins et les cavaliers des colonnes paire
      grille[0][x][1]="F"
      grille[1][x][1]="C"
      grille[n-2][x][1]="F"
      grille[n-1][x][1]="C"
    else:#Place les fantassins et les cavaliers des colonnes impaire
      grille[0][x][1]="C"
      grille[1][x][1]="F"
      grille[n-2][x][1]="C"
      grille[n-1][x][1]="F"
    #Indique a quel joueur appartiennent les pièces.
    grille[0][x][2]="1"
    grille[1][x][2]="1"
    grille[n-2][x][2]="2"
    grille[n-1][x][2]="2"
  return grille



#####################################Deplacements#####################################

def depFantassins(grille,x,y):
  """
      Cette fonction renvoie le tuple de deplacement possible pour un fantassin par rapport à sa position dans la grille en respectant les régles du latroncules
      :param grille: grille de jeu
      :type grille: liste
      :param x: ligne du pion
      :type x: entier
      :param y: colonne du pion de départ
      :type y: entier
  """
  res=()
  joueur=grille[x][y][2]

  bas=[x-1,y]
  haut=[x+1,y]
  if joueur=="1" and haut[0]>=0 and haut[1]>=0 and haut[0]<=len(grille)-1 and haut[1]<=len(grille)-1 and grille[haut[0]][haut[1]][1:]==[" "," "] and not caseCapturable(grille,haut[0],haut[1],joueur) :#Retourne la coordonné possible pour avancer un fantassin du joueur 1:
    res+=(haut,)
  elif joueur=="2" and bas[0]>=0 and bas[1]>=0 and bas[0]<=len(grille)-1 and bas[1]<=len(grille)-1 and grille[bas[0]][bas[1]][1:]==[" "," "] and not caseCapturable(grille,bas[0],bas[1],joueur) :#Retourne la coordonné possible pour avancer un fantassin du joueur 2:
    res+=(bas,)
  else:
    return ()
  return res

def depCavaliers(grille,x,y):
  """
      Cette fonction renvoie le tuple de deplacement possible pour un cavalier par rapport à sa position dans la grille en respectant les régles du latroncules
      :param grille: grille de jeu
      :type grille: liste
      :param x: ligne du pion de départ
      :type x: entier
      :param y: colonne du pion de départ
      :type y: entier
  """
  res=()
  joueur=grille[x][y][2]

  gauche=[x,y-1]
  droite=[x,y+1]
  bas=[x-1,y]
  haut=[x+1,y]
  basDroite=[x-1,y+1]
  hautGauche=[x+1,y-1]
  basGauche=[x-1,y-1]
  hautDroite=[x+1,y+1]

  gaucheSaut=[x,y-2]
  droiteSaut=[x,y+2]
  basSaut=[x-2,y]
  hautSaut=[x+2,y]
  basDroiteSaut=[x-2,y+2]
  hautGaucheSaut=[x+2,y-2]
  basGaucheSaut=[x-2,y-2]
  hautDroiteSaut=[x+2,y+2]

  if grille[x][y][0]=="B":#Si le cavalier est sur une case blanche :
    #Si la coordonée gauche est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    if gauche[0]>=0 and gauche[1]>=0 and gauche[0]<=len(grille)-1 and gauche[1]<=len(grille)-1 and grille[gauche[0]][gauche[1]][2]==" " and not caseCapturable(grille,gauche[0],gauche[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(gauche,)
    #Si le mouvement normal gauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    elif gaucheSaut[0]>=0 and gaucheSaut[1]>=0 and gaucheSaut[0]<=len(grille)-1 and gaucheSaut[1]<=len(grille)-1 and grille[gauche[0]][gauche[1]][2]==adversaire(joueur) and grille[gaucheSaut[0]][gaucheSaut[1]][2]==" " and not caseCapturable(grille,gaucheSaut[0],gaucheSaut[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(gaucheSaut,)
    #Si la coordonée droite est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    if droite[0]>=0 and droite[1]>=0 and droite[0]<=len(grille)-1 and droite[1]<=len(grille)-1 and grille[droite[0]][droite[1]][2]==" " and not caseCapturable(grille,droite[0],droite[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(droite,)
    #Si le mouvement normal droite n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    elif droiteSaut[0]>=0 and droiteSaut[1]>=0 and droiteSaut[0]<=len(grille)-1 and droiteSaut[1]<=len(grille)-1 and grille[droite[0]][droite[1]][2]==adversaire(joueur) and grille[droiteSaut[0]][droiteSaut[1]][2]==" " and not caseCapturable(grille,droiteSaut[0],droiteSaut[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(droiteSaut,)
    #Si la coordonée bas est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    if bas[0]>=0 and bas[1]>=0 and bas[0]<=len(grille)-1 and bas[1]<=len(grille)-1 and grille[bas[0]][bas[1]][2]==" " and not caseCapturable(grille,bas[0],bas[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(bas,)
    #Si le mouvement normal bas n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    elif basSaut[0]>=0 and basSaut[1]>=0 and basSaut[0]<=len(grille)-1 and basSaut[1]<=len(grille)-1 and grille[bas[0]][bas[1]][2]==adversaire(joueur) and grille[basSaut[0]][basSaut[1]][2]==" " and not caseCapturable(grille,basSaut[0],basSaut[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(basSaut,)
    #Si la coordonée haut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    if haut[0]>=0 and haut[1]>=0 and haut[0]<=len(grille)-1 and haut[1]<=len(grille)-1 and grille[haut[0]][haut[1]][2]==" " and not caseCapturable(grille,haut[0],haut[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(haut,)
    #Si le mouvement normal haut n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    elif hautSaut[0]>=0 and hautSaut[1]>=0 and hautSaut[0]<=len(grille)-1 and hautSaut[1]<=len(grille)-1 and grille[haut[0]][haut[1]][2]==adversaire(joueur) and grille[hautSaut[0]][hautSaut[1]][2]==" " and not caseCapturable(grille,hautSaut[0],hautSaut[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(hautSaut,)
    #Si la coordonée basDroite est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    if basDroite[0]>=0 and basDroite[1]>=0 and basDroite[0]<=len(grille)-1 and basDroite[1]<=len(grille)-1 and grille[basDroite[0]][basDroite[1]][2]==" " and not caseCapturable(grille,basDroite[0],basDroite[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(basDroite,)
    #Si le mouvement basDroite gauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    elif basDroiteSaut[0]>=0 and basDroiteSaut[1]>=0 and basDroiteSaut[0]<=len(grille)-1 and basDroiteSaut[1]<=len(grille)-1 and grille[basDroite[0]][basDroite[1]][2]==adversaire(joueur) and grille[basDroiteSaut[0]][basDroiteSaut[1]][2]==" " and not caseCapturable(grille,basDroiteSaut[0],basDroiteSaut[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(basDroiteSaut,)
    #Si la coordonée hautGauche est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    if hautGauche[0]>=0 and hautGauche[1]>=0 and hautGauche[0]<=len(grille)-1 and hautGauche[1]<=len(grille)-1 and grille[hautGauche[0]][hautGauche[1]][2]==" " and not caseCapturable(grille,hautGauche[0],hautGauche[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(hautGauche,)
    #Si le mouvement normal hautGauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    elif hautGaucheSaut[0]>=0 and hautGaucheSaut[1]>=0 and hautGaucheSaut[0]<=len(grille)-1 and hautGaucheSaut[1]<=len(grille)-1 and grille[hautGauche[0]][hautGauche[1]][2]==adversaire(joueur) and grille[hautGaucheSaut[0]][hautGaucheSaut[1]][2]==" " and not caseCapturable(grille,hautGaucheSaut[0],hautGaucheSaut[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(hautGaucheSaut,)
    #Si la coordonée basGauche est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    if basGauche[0]>=0 and basGauche[1]>=0 and basGauche[0]<=len(grille)-1 and basGauche[1]<=len(grille)-1 and grille[basGauche[0]][basGauche[1]][2]==" " and not caseCapturable(grille,basGauche[0],basGauche[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(basGauche,)
    #Si le mouvement normal basGauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    elif basGaucheSaut[0]>=0 and basGaucheSaut[1]>=0 and basGaucheSaut[0]<=len(grille)-1 and basGaucheSaut[1]<=len(grille)-1 and grille[basGauche[0]][basGauche[1]][2]==adversaire(joueur) and grille[basGaucheSaut[0]][basGaucheSaut[1]][2]==" " and not caseCapturable(grille,basGaucheSaut[0],basGaucheSaut[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(basGaucheSaut,)
    #Si la coordonée hautDroite est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    if hautDroite[0]>=0 and hautDroite[1]>=0 and hautDroite[0]<=len(grille)-1 and hautDroite[1]<=len(grille)-1 and grille[hautDroite[0]][hautDroite[1]][2]==" " and not caseCapturable(grille,hautDroite[0],hautDroite[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(hautDroite,)
    #Si le mouvement normal hautDroite n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
    elif hautDroiteSaut[0]>=0 and hautDroiteSaut[1]>=0 and hautDroiteSaut[0]<=len(grille)-1 and hautDroiteSaut[1]<=len(grille)-1 and grille[hautDroite[0]][hautDroite[1]][2]==adversaire(joueur) and grille[hautDroiteSaut[0]][hautDroiteSaut[1]][2]==" " and not caseCapturable(grille,hautDroiteSaut[0],hautDroiteSaut[1],joueur):
      #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
      res+=(hautDroiteSaut,)
  elif grille[x][y][0]=="N":#Si le cavalier est sur une case noire :
    if x==0 or x==1 or x==6 or x==7:#2premieres et 2 dernieres lignes
      #Si la coordonée basDroite est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
      if basDroite[0]>=0 and basDroite[1]>=0 and basDroite[0]<=len(grille)-1 and basDroite[1]<=len(grille)-1 and grille[basDroite[0]][basDroite[1]][2]==" " and not caseCapturable(grille,basDroite[0],basDroite[1],joueur):
        #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
        res+=(basDroite,)
      #Si le mouvement normal basDroite n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
      elif basDroiteSaut[0]>=0 and basDroiteSaut[1]>=0 and basDroiteSaut[0]<=len(grille)-1 and basDroiteSaut[1]<=len(grille)-1 and grille[basDroite[0]][basDroite[1]][2]==adversaire(joueur) and grille[basDroiteSaut[0]][basDroiteSaut[1]][2]==" " and not caseCapturable(grille,basDroiteSaut[0],basDroiteSaut[1],joueur):
        #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
        res+=(basDroiteSaut,)
      #Si la coordonée hautGauche est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
      if hautGauche[0]>=0 and hautGauche[1]>=0 and hautGauche[0]<=len(grille)-1 and hautGauche[1]<=len(grille)-1 and grille[hautGauche[0]][hautGauche[1]][2]==" " and not caseCapturable(grille,hautGauche[0],hautGauche[1],joueur):
        #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
        res+=(hautGauche,)
      #Si le mouvement normal hautGauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
      elif hautGaucheSaut[0]>=0 and hautGaucheSaut[1]>=0 and hautGaucheSaut[0]<=len(grille)-1 and hautGaucheSaut[1]<=len(grille)-1 and grille[hautGauche[0]][hautGauche[1]][2]==adversaire(joueur) and grille[hautGaucheSaut[0]][hautGaucheSaut[1]][2]==" " and not caseCapturable(grille,hautGaucheSaut[0],hautGaucheSaut[1],joueur):
        #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
        res+=(hautGaucheSaut,)
      #Si la coordonée basGauche est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
      if basGauche[0]>=0 and basGauche[1]>=0 and basGauche[0]<=len(grille)-1 and basGauche[1]<=len(grille)-1 and grille[basGauche[0]][basGauche[1]][2]==" " and not caseCapturable(grille,basGauche[0],basGauche[1],joueur):
        #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
        res+=(basGauche,)
      #Si le mouvement normal basGauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
      elif basGaucheSaut[0]>=0 and basGaucheSaut[1]>=0 and basGaucheSaut[0]<=len(grille)-1 and basGaucheSaut[1]<=len(grille)-1 and grille[basGauche[0]][basGauche[1]][2]==adversaire(joueur) and grille[basGaucheSaut[0]][basGaucheSaut[1]][2]==" " and not caseCapturable(grille,basGaucheSaut[0],basGaucheSaut[1],joueur):
        #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
        res+=(basGaucheSaut,)#Ajout de la coordonnée au tuple comportant toute les coordonées possibles
      #Si la coordonée hautDroite est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
      if hautDroite[0]>=0 and hautDroite[1]>=0 and hautDroite[0]<=len(grille)-1 and hautDroite[1]<=len(grille)-1 and grille[hautDroite[0]][hautDroite[1]][2]==" " and not caseCapturable(grille,hautDroite[0],hautDroite[1],joueur):
        #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
        res+=(hautDroite,)
      #Si le mouvement normal hautDroite n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
      elif hautDroiteSaut[0]>=0 and hautDroiteSaut[1]>=0 and hautDroiteSaut[0]<=len(grille)-1 and hautDroiteSaut[1]<=len(grille)-1 and grille[hautDroite[0]][hautDroite[1]][2]==adversaire(joueur) and grille[hautDroiteSaut[0]][hautDroiteSaut[1]][2]==" " and not caseCapturable(grille,hautDroiteSaut[0],hautDroiteSaut[1],joueur):
        #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
        res+=(hautDroiteSaut,)
    elif x==2 or x==5:#3eme et 6 eme lignes
      if y==5 or y==7 or y==0 or y==2:#6 eme 8 eme 1er et 3eme colonne
        #Si la coordonée gauche est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if gauche[0]>=0 and gauche[1]>=0 and gauche[0]<=len(grille)-1 and gauche[1]<=len(grille)-1 and grille[gauche[0]][gauche[1]][2]==" " and not caseCapturable(grille,gauche[0],gauche[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(gauche,)
        #Si le mouvement normal gauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif gaucheSaut[0]>=0 and gaucheSaut[1]>=0 and gaucheSaut[0]<=len(grille)-1 and gaucheSaut[1]<=len(grille)-1 and grille[gauche[0]][gauche[1]][2]==adversaire(joueur) and grille[gaucheSaut[0]][gaucheSaut[1]][2]==" " and not caseCapturable(grille,gaucheSaut[0],gaucheSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(gaucheSaut,)
        #Si la coordonée droite est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if droite[0]>=0 and droite[1]>=0 and droite[0]<=len(grille)-1 and droite[1]<=len(grille)-1 and grille[droite[0]][droite[1]][2]==" " and not caseCapturable(grille,droite[0],droite[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(droite,)
        #Si le mouvement normal droite n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif droiteSaut[0]>=0 and droiteSaut[1]>=0 and droiteSaut[0]<=len(grille)-1 and droiteSaut[1]<=len(grille)-1 and grille[droite[0]][droite[1]][2]==adversaire(joueur) and grille[droiteSaut[0]][droiteSaut[1]][2]==" " and not caseCapturable(grille,droiteSaut[0],droiteSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(droiteSaut,)
        #Si la coordonée basGauche est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if basGauche[0]>=0 and basGauche[1]>=0 and basGauche[0]<=len(grille)-1 and basGauche[1]<=len(grille)-1 and grille[basGauche[0]][basGauche[1]][2]==" " and not caseCapturable(grille,basGauche[0],basGauche[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(basGauche,)
        #Si le mouvement normal basGauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif basGaucheSaut[0]>=0 and basGaucheSaut[1]>=0 and basGaucheSaut[0]<=len(grille)-1 and basGaucheSaut[1]<=len(grille)-1 and grille[basGauche[0]][basGauche[1]][2]==adversaire(joueur) and grille[basGaucheSaut[0]][basGaucheSaut[1]][2]==" " and not caseCapturable(grille,basGaucheSaut[0],basGaucheSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(basGaucheSaut,)
        #Si la coordonée hautDroite est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if hautDroite[0]>=0 and hautDroite[1]>=0 and hautDroite[0]<=len(grille)-1 and hautDroite[1]<=len(grille)-1 and grille[hautDroite[0]][hautDroite[1]][2]==" " and not caseCapturable(grille,hautDroite[0],hautDroite[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(hautDroite,)
          #Si le mouvement normal hautDroite n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif hautDroiteSaut[0]>=0 and hautDroiteSaut[1]>=0 and hautDroiteSaut[0]<=len(grille)-1 and hautDroiteSaut[1]<=len(grille)-1 and grille[hautDroite[0]][hautDroite[1]][2]==adversaire(joueur) and grille[hautDroiteSaut[0]][hautDroiteSaut[1]][2]==" " and not caseCapturable(grille,hautDroiteSaut[0],hautDroiteSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(hautDroiteSaut,)
      elif y==1 or y==3 or y==6 or y==4:#2 eme 4 eme 7 eme et 5eme colonne
        #Si la coordonée gauche est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if gauche[0]>=0 and gauche[1]>=0 and gauche[0]<=len(grille)-1 and gauche[1]<=len(grille)-1 and grille[gauche[0]][gauche[1]][2]==" " and not caseCapturable(grille,gauche[0],gauche[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(gauche,)
        #Si le mouvement normal gauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif gaucheSaut[0]>=0 and gaucheSaut[1]>=0 and gaucheSaut[0]<=len(grille)-1 and gaucheSaut[1]<=len(grille)-1 and grille[gauche[0]][gauche[1]][2]==adversaire(joueur) and grille[gaucheSaut[0]][gaucheSaut[1]][2]==" " and not caseCapturable(grille,gaucheSaut[0],gaucheSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(gaucheSaut,)
        #Si la coordonée droite est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if droite[0]>=0 and droite[1]>=0 and droite[0]<=len(grille)-1 and droite[1]<=len(grille)-1 and grille[droite[0]][droite[1]][2]==" " and not caseCapturable(grille,droite[0],droite[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(droite,)
        #Si le mouvement normal droite n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif droiteSaut[0]>=0 and droiteSaut[1]>=0 and droiteSaut[0]<=len(grille)-1 and droiteSaut[1]<=len(grille)-1 and grille[droite[0]][droite[1]][2]==adversaire(joueur) and grille[droiteSaut[0]][droiteSaut[1]][2]==" " and not caseCapturable(grille,droiteSaut[0],droiteSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(droiteSaut,)
        #Si la coordonée basDroite est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if basDroite[0]>=0 and basDroite[1]>=0 and basDroite[0]<=len(grille)-1 and basDroite[1]<=len(grille)-1 and grille[basDroite[0]][basDroite[1]][2]==" " and not caseCapturable(grille,basDroite[0],basDroite[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(basDroite,)
        #Si le mouvement normal basDroite n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif basDroiteSaut[0]>=0 and basDroiteSaut[1]>=0 and basDroiteSaut[0]<=len(grille)-1 and basDroiteSaut[1]<=len(grille)-1 and grille[basDroite[0]][basDroite[1]][2]==adversaire(joueur) and grille[basDroiteSaut[0]][basDroiteSaut[1]][2]==" " and not caseCapturable(grille,basDroiteSaut[0],basDroiteSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(basDroiteSaut,)
        #Si la coordonée hautGauche est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if hautGauche[0]>=0 and hautGauche[1]>=0 and hautGauche[0]<=len(grille)-1 and hautGauche[1]<=len(grille)-1 and grille[hautGauche[0]][hautGauche[1]][2]==" " and not caseCapturable(grille,hautGauche[0],hautGauche[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(hautGauche,)
        #Si le mouvement normal hautGauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif hautGaucheSaut[0]>=0 and hautGaucheSaut[1]>=0 and hautGaucheSaut[0]<=len(grille)-1 and hautGaucheSaut[1]<=len(grille)-1 and grille[hautGauche[0]][hautGauche[1]][2]==adversaire(joueur) and grille[hautGaucheSaut[0]][hautGaucheSaut[1]][2]==" " and not caseCapturable(grille,hautGaucheSaut[0],hautGaucheSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(hautGaucheSaut,)
    elif x==3 or x==4:#4eme et 5 eme lignes
      if y==1 or y== 3 or y==4 or y==6:#2eme 4eme 5eme et 7eme colonne
        #Si la coordonée bas est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if bas[0]>=0 and bas[1]>=0 and bas[0]<=len(grille)-1 and bas[1]<=len(grille)-1 and grille[bas[0]][bas[1]][2]==" " and not caseCapturable(grille,bas[0],bas[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(bas,)
        #Si le mouvement normal bas n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif basSaut[0]>=0 and basSaut[1]>=0 and basSaut[0]<=len(grille)-1 and basSaut[1]<=len(grille)-1 and grille[bas[0]][bas[1]][2]==adversaire(joueur) and grille[basSaut[0]][basSaut[1]][2]==" " and not caseCapturable(grille,basSaut[0],basSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(basSaut,)
        #Si la coordonée haut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if haut[0]>=0 and haut[1]>=0 and haut[0]<=len(grille)-1 and haut[1]<=len(grille)-1 and grille[haut[0]][haut[1]][2]==" " and not caseCapturable(grille,haut[0],haut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(haut,)
        #Si le mouvement normal haut n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif hautSaut[0]>=0 and hautSaut[1]>=0 and hautSaut[0]<=len(grille)-1 and hautSaut[1]<=len(grille)-1 and grille[haut[0]][haut[1]][2]==adversaire(joueur) and grille[hautSaut[0]][hautSaut[1]][2]==" " and not caseCapturable(grille,hautSaut[0],hautSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(hautSaut,)
        #Si la coordonée basDroite est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if basDroite[0]>=0 and basDroite[1]>=0 and basDroite[0]<=len(grille)-1 and basDroite[1]<=len(grille)-1 and grille[basDroite[0]][basDroite[1]][2]==" " and not caseCapturable(grille,basDroite[0],basDroite[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(basDroite,)
        #Si le mouvement normal basDroite n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif basDroiteSaut[0]>=0 and basDroiteSaut[1]>=0 and basDroiteSaut[0]<=len(grille)-1 and basDroiteSaut[1]<=len(grille)-1 and grille[basDroite[0]][basDroite[1]][2]==adversaire(joueur) and grille[basDroiteSaut[0]][basDroiteSaut[1]][2]==" " and not caseCapturable(grille,basDroiteSaut[0],basDroiteSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(basDroiteSaut,)
        #Si la coordonée hautGauche est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if hautGauche[0]>=0 and hautGauche[1]>=0 and hautGauche[0]<=len(grille)-1 and hautGauche[1]<=len(grille)-1 and grille[hautGauche[0]][hautGauche[1]][2]==" " and not caseCapturable(grille,hautGauche[0],hautGauche[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(hautGauche,)
        #Si le mouvement normal hautGauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif hautGaucheSaut[0]>=0 and hautGaucheSaut[1]>=0 and hautGaucheSaut[0]<=len(grille)-1 and hautGaucheSaut[1]<=len(grille)-1 and grille[hautGauche[0]][hautGauche[1]][2]==adversaire(joueur) and grille[hautGaucheSaut[0]][hautGaucheSaut[1]][2]==" " and not caseCapturable(grille,hautGaucheSaut[0],hautGaucheSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(hautGaucheSaut,)
      elif y==0 or y==2 or y==5 or y==7:#1er 3eme 6eme et 8eme colonne
        #Si la coordonée bas est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if bas[0]>=0 and bas[1]>=0 and bas[0]<=len(grille)-1 and bas[1]<=len(grille)-1 and grille[bas[0]][bas[1]][2]==" " and not caseCapturable(grille,bas[0],bas[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(bas,)
        #Si le mouvement normal bas n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif basSaut[0]>=0 and basSaut[1]>=0 and basSaut[0]<=len(grille)-1 and basSaut[1]<=len(grille)-1 and grille[bas[0]][bas[1]][2]==adversaire(joueur) and grille[basSaut[0]][basSaut[1]][2]==" " and not caseCapturable(grille,basSaut[0],basSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(basSaut,)
        #Si la coordonée haut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if haut[0]>=0 and haut[1]>=0 and haut[0]<=len(grille)-1 and haut[1]<=len(grille)-1 and grille[haut[0]][haut[1]][2]==" " and not caseCapturable(grille,haut[0],haut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(haut,)
        #Si le mouvement normal haut n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif hautSaut[0]>=0 and hautSaut[1]>=0 and hautSaut[0]<=len(grille)-1 and hautSaut[1]<=len(grille)-1 and grille[haut[0]][haut[1]][2]==adversaire(joueur) and grille[hautSaut[0]][hautSaut[1]][2]==" " and not caseCapturable(grille,hautSaut[0],hautSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(hautSaut,)
        #Si la coordonée basGauche est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if basGauche[0]>=0 and basGauche[1]>=0 and basGauche[0]<=len(grille)-1 and basGauche[1]<=len(grille)-1 and grille[basGauche[0]][basGauche[1]][2]==" " and not caseCapturable(grille,basGauche[0],basGauche[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(basGauche,)
        #Si le mouvement normal basGauche n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif basGaucheSaut[0]>=0 and basGaucheSaut[1]>=0 and basGaucheSaut[0]<=len(grille)-1 and basGaucheSaut[1]<=len(grille)-1 and grille[basGauche[0]][basGauche[1]][2]==adversaire(joueur) and grille[basGaucheSaut[0]][basGaucheSaut[1]][2]==" " and not caseCapturable(grille,basGaucheSaut[0],basGaucheSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(basGaucheSaut,)#Ajout de la coordonnée au tuple comportant toute les coordonées possibles
        #Si la coordonée hautDroite est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        if hautDroite[0]>=0 and hautDroite[1]>=0 and hautDroite[0]<=len(grille)-1 and hautDroite[1]<=len(grille)-1 and grille[hautDroite[0]][hautDroite[1]][2]==" " and not caseCapturable(grille,hautDroite[0],hautDroite[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(hautDroite,)
        #Si le mouvement normal hautDroite n'est pas possible et que le saut est autorisé et que la coordonnée du saut est dans la grille et que la case d'arrivée est libre et que le pion n'entre pas en position de capture alors:
        elif hautDroiteSaut[0]>=0 and hautDroiteSaut[1]>=0 and hautDroiteSaut[0]<=len(grille)-1 and hautDroiteSaut[1]<=len(grille)-1 and grille[hautDroite[0]][hautDroite[1]][2]==adversaire(joueur) and grille[hautDroiteSaut[0]][hautDroiteSaut[1]][2]==" " and not caseCapturable(grille,hautDroiteSaut[0],hautDroiteSaut[1],joueur):
          #Ajout de la coordonnée au tuple comportant toutes les coordonées possibles
          res+=(hautDroiteSaut,)
    else:
      return ()
  return res#Retourne le tuple contenant toutes les coordonnées possibles

def deplacement(grille,x,y):
  """
      Cette fonction appelle la fonction depFantassins ou depCavaliers en fonction de la nature du pion à bouger
      :param grille: grille de jeu
      :type grille: liste
      :param x: ligne du pion
      :type x: entier
      :param y: colonne du pion
      :type y: entier
  """
  if grille[x][y][1]=="F":#S'il s'agit d'un fantassin
    return depFantassins(grille,x,y)
  elif grille[x][y][1]=="C":#S'il s'agit d'un cavalier
    return depCavaliers(grille,x,y)
  else:
    return False



#####################################Capture#####################################
def caseCapturable(grille,x,y,joueur):
  """
      Cette fonction retourne True si un joueur à capturée une case
      :param grille: grille de jeu
      :type grille: liste
      :param x: ligne du pion de départ
      :type x: entier
      :param y: colonne du pion de départ
      :type y: entier
      :param joueur: joueur
      :type joueur: string
  """
  n=len(grille)-1
  #Regarde qui est l'adversaire
  adv=adversaire(joueur)
  #Si la case est en position capturable retourne True
  if x==0 and y==0 and grille[1][0][2]==adv and grille[0][1][2]==adv:#Coin en haut a gauche
    return True
  elif x==0 and y==n and grille[1][n][2]==adv and grille[0][n-1][2]==adv:#Coin en haut à droite
    return True
  elif x==n and y==0 and grille[n-1][0][2]==adv and grille[n][1][2]==adv:#Coin en bas a gauche
    return True
  elif x==n and y==n and grille[n][n-1][2]==adv and grille[n-1][n][2]==adv:#Coin en bas à droite
    return True
  elif 1<=y<=len(grille)-2 and grille[x][y-1][2]==adv and grille[x][y+1][2]==adv:#Capture horizontale
    return True
  elif 1<=x<=len(grille)-2 and grille[x-1][y][2]==adv and grille[x+1][y][2]==adv:#Capture verticale
    return True
  elif 1<=y<=len(grille)-2 and 1<=x<=len(grille)-2 and grille[x+1][y-1][2]==adv and grille[x-1][y+1][2]==adv:#Capture diagonale SQ à ZD
    return True
  elif 1<=y<=len(grille)-2 and 1<=x<=len(grille)-2 and grille[x-1][y-1][2]==adv and grille[x+1][y+1][2]==adv:#Capture diagonale ZQ à SD
    return True
  #Sinon retourne False
  return False

def caseCapturee(grille,x,y):
  """
      Cette fonction retourne True si le pion est capturée
      :param grille: grille de jeu
      :type grille: liste
      :param x: ligne du pion de départ
      :type x: entier
      :param y: colonne du pion de départ
      :type y: entier
      :param joueur: joueur
      :type joueur: string
  """
  n=len(grille)-1
  joueur=grille[x][y][2]
  #Regarde qui est l'adversaire
  adv=adversaire(joueur)
  #Si la pièce est en position capturable retourne True
  if x==0 and y==0 and grille[1][0][2]==adv and grille[0][1][2]==adv:#Coin en haut a gauche
    return True
  elif x==0 and y==n and grille[1][n][2]==adv and grille[0][n-1][2]==adv:#Coin en haut à droite
    return True
  elif x==n and y==0 and grille[n-1][0][2]==adv and grille[n][1][2]==adv:#Coin en bas a gauche
    return True
  elif x==n and y==n and grille[n][n-1][2]==adv and grille[n-1][n][2]==adv:#Coin en bas à droite
    return True
  elif 1<=y<=len(grille)-2 and grille[x][y-1][2]==adv and grille[x][y+1][2]==adv:#Capture horizontale
    return True
  elif 1<=x<=len(grille)-2 and grille[x-1][y][2]==adv and grille[x+1][y][2]==adv:#Capture verticale
    return True
  elif 1<=y<=len(grille)-2 and 1<=x<=len(grille)-2 and grille[x+1][y-1][2]==adv and grille[x-1][y+1][2]==adv:#Capture diagonale SQ à ZD
    return True
  elif 1<=y<=len(grille)-2 and 1<=x<=len(grille)-2 and grille[x-1][y-1][2]==adv and grille[x+1][y+1][2]==adv:#Capture diagonale ZQ à SD
    return True
  #Sinon retourne False
  return False

def pionCapturer(grille):#Si le pion est capturer efface le pion de la grille
  """
      Cette fonction efface de la grille les pions capturer
      :param grille: grille de jeu
      :type grille: liste
  """
  for x in range(len(grille)):
    for y in range(len(grille)):
      if caseCapturee(grille,x,y):
        grille[x][y][1:]=[" "," "]

#####################################Partie#####################################
def tourJoueur(grille,x,y):
  """
      Cette fonction vérifie que c'est bien au tour du joueur qui veux jouer
      :param grille: grille de jeu
      :type grille: liste
      :param x: ligne du pion de départ
      :type x: entier
      :param y: colonne du pion de départ
      :type y: entier
  """
  global tour
  if grille[x][y][2]=="1" and tour%2==0 or grille[x][y][2]=="2" and tour%2!=0:#Verifie le tour de jeu
    return True
  return False

def adversaire(joueur):
  """
      Cette fonction renvoie l'adversaire du joueur
      :param joueur: joueur auquel appartient le pion
      :type joueur: string
      :param return: adversaire du joueur
      :type return: string
  """
  if joueur=="1":#S'il s'agit du joueur 1
    return "2"#L'adversaire est le joueur 2
  elif joueur=="2":#S'il s'agit du joueur 2
    return "1"#L'adversaire est le joueur 1

def cavJ1(grille):
  res=0
  for x in range(len(grille)):
    for y in range(len(grille)):
      if grille[x][y][1:]==["C","1"]:
        res+=1
  return res

def cavJ2(grille):
  res=0
  for x in range(len(grille)):
    for y in range(len(grille)):
      if grille[x][y][1:]==["C","2"]:
        res+=1
  return res

def upgradeJ1(grille):
  """
      Cette fonction retourne un tuple de coordonnées de tout les fantassins pouvant être transformer en cavaliers pour le joueur 1
      :param grille: grille de jeu
      :type grille: liste
  """
  n=len(grille)
  resj1=()
  for y in range(len(grille)):
    if grille[n-1][y][1:]==["F","1"]:
      resj1+=([n-1,y],)
  return resj1

def upgradeJ2(grille):
  """
      Cette fonction retourne un tuple de coordonnées de tout les fantassins pouvant être transformer en cavaliers pour le joueur 2
      :param grille: grille de jeu
      :type grille: liste
  """
  n=len(grille)
  resj2=()

  for y in range(len(grille)):
    if grille[0][y][1:]==["F","2"]:
      resj2+=([0,y],)
  return resj2

def upgrade(grille):
  """
      Cette fonction appelle les fonctions d'upgrade d'un fantassin en fonction du tour actuelle et en vérifiant que celle ci ne soit pas vide
      :param grille: grille de jeu
      :type grille: liste
  """
  global tour
  if tour%2==0 and upgradeJ1(grille)!=() and cavJ1(grille)<8:
    return upgradeJ1(grille)
  elif tour%2!=0 and upgradeJ2(grille)!=() and cavJ2(grille)<8:
    return upgradeJ2(grille)
  else:
    return False

def coupPossible1(grille):#Calcul le nombre de coups possible pour le joueur 1
  """
      Cette fonction indique combien il y a de coups possible pour le joueur 1
      :param grille: grille de jeu
      :type grille: liste
  """
  j=0
  for x in range(len(grille)):
    for y in range(len(grille)):
      if grille[x][y][2]=="1" and deplacement(grille,x,y)!=():
        j+=1
  return j

def coupPossible2(grille):#Calcul le nombre de coups possible pour le joueur 2
  """
      Cette fonction indique combien il y a de coups possible pour le joueur 2
      :param grille: grille de jeu
      :type grille: liste
  """
  j=0
  for x in range(len(grille)):
    for y in range(len(grille)):
      if grille[x][y][2]=="2" and deplacement(grille,x,y)!=():
        j+=1
  return j

def nbPiece(grille,joueur):#Calcul le nombre de piece totale
  """
      Cette fonction regarde combien il reste de pion pour un joueur
      :param grille: grille de jeu
      :type grille: liste
      :param joueur: joueur
      :type joueur: string
  """
  j=0
  for x in range(len(grille)):
    for y in range(len(grille)):
      if grille[x][y][2]==joueur:
        j+=1
  return j

def victoire(grille):
  """
      Cette fonction définie les conditions de victoire et indique quelle joueur gagne
      :param grille: grille de jeu
      :type grille: liste
  """
  for x in range(len(grille)):
    for y in range(len(grille)):
      if coupPossible1(grille)==0 or nbPiece(grille,"1")<=1:#Si il ne reste plus qu'une piece au joueur 1 ou qu'il ne peut plus se deplacer alors victoire du joueur 2
        return "2"
      elif coupPossible2(grille)==0 or nbPiece(grille,"2")<=1:#Si il ne reste plus qu'une piece au joueur 2 ou qu'il ne peut plus se deplacer alors victoire du joueur 1
        return "1"
  return False

def coupValide (grille,x,y,xx,yy):
  """
      Cette fonction effectue le déplacement demander si il est valide et incremente le tour si le deplacement est effectué
      :param grille: grille de jeu
      :type grille: liste
      :param x: ligne du pion de départ
      :type x: entier
      :param y: colonne du pion de départ
      :type y: entier
      :param xx: ligne du pion d'arrivée
      :type xx: entier
      :param yy: colonne du pion d'arrivée
      :type yy: entier
  """
  global tour
  if [xx,yy] in deplacement(grille,x,y) and tourJoueur(grille,x,y):#Si les coordonnées d'arrivées sont dans le tuple des coordonnées autorisé alors
    #Avance le pion
    grille[xx][yy][1]=grille[x][y][1]
    grille[xx][yy][2]=grille[x][y][2]
    #Efface l'ancienne position du pion
    grille[x][y][1]=" "
    grille[x][y][2]=" "
    tour+=1#Incremente pour le changement de tour
    pionCapturer(grille)#Efface les pions capturés
  return grille

#####################################IA#####################################


def depIA():
  """
      Cette fonction effectue un déplacement aléatoire en fonction du pion lui aussi chosis aléatoirement
  """
  global info
  global gameMode
  global intervalleChrono
  i=[]
  j=[]
  for x in range(len(grille)):
    for y in range(len(grille)):
      if gameMode==0:
        break
      if gameMode==1:
        if grille[x][y][2]=="2" and deplacement(grille,x,y)!=() and victoire(grille)==False:
          i+=[x]
          j+=[y]
      if gameMode==2:
        if tour%2!=0 and grille[x][y][2]=="2" and deplacement(grille,x,y)!=() and victoire(grille)==False:
          i+=[x]
          j+=[y]
        elif tour%2==0 and grille[x][y][2]=="1" and deplacement(grille,x,y)!=() and victoire(grille)==False:
          i+=[x]
          j+=[y]
  if upgrade(grille)!=False:
    up=upgrade(grille)
    rand=randint(0,len(up)-1)
    grille[up[rand][1]][up[rand][0]][1]="C"
  alea=randint(0, len(i)-1)
  res=deplacement(grille,i[alea],j[alea])
  alea2=randint(0,len(res)-1)
  coupValide(grille,i[alea],j[alea],res[alea2][0],res[alea2][1])

#####################################Affichage#####################################

def afficheGrille(grille):
  for l in grille:#pour chaque ligne dans la grille
    for x in l:#pour chaque valeur dans la ligne
      print("{:^20}".format(str(x)),end="")#affiche x avec espace mais pas retour a la ligne
    print ()#retour a la ligne

def choixUpgrade(event):
  """
      Cette fonction effectue l'évolution du fantassin en cavalier par rapport au coordonnées donnée
      :param event: coordonnés du clic souris
      :type event: coordonnés
  """
  xx=event.y//t
  yy=event.x//t
  can.delete(ALL)
  affGrille()
  grille[xx][yy][1]="C"
  affPion()
  can.bind("<Button-1>", prevDep)

def affDep(event):
  """
      Cette fonction gére l'affichage qui découle du déplacement demander
      :param event: coordoonnés du clic souris
      :type event: coordoonnés
  """
  global X
  global Y
  global info
  global gameMode
  global intervalleChrono
  if gameMode==0:
    xx=event.y//t
    yy=event.x//t
    can.delete(ALL)
    affGrille()
    coupValide(grille,X,Y,xx,yy)
  if gameMode==1:
    xx=event.y//t
    yy=event.x//t
    can.delete(ALL)
    affGrille()
    coupValide(grille,X,Y,xx,yy)
    depIA()
  affPion()
  if victoire(grille)==False:
    can.bind("<Button-1>", prevDep)
  else:
    info.set("Victoire du joueur"+" "+victoire(grille))
    intervalleChrono=2
    gameMode=0
    can.unbind("<Button-1>")

def prevDep(event):
  """
      Cette fonction gére l'affichage de la prévisualisation des coups possible en fonction du pion cliqué
      :param event: coordoonnés du clic souris
      :type event: coordoonnés
  """
  global X
  global Y
  X=event.y//t
  Y=event.x//t
  can.delete(ALL)
  affGrille()
  affPion()
  dep=deplacement(grille,X,Y)
  if 0<= X<=len(grille)-1 and 0<=Y<=len(grille)-1:
    if upgrade(grille)!=False:
      info.set("Vous pouvez transformer un fantassin en cavalier")
      can.bind("<Button-1>", choixUpgrade)
      up=upgrade(grille)
      for i in range(len(up)):
        can.create_rectangle(t*up[i][1],up[i][0]*t,t*(up[i][1]+1),(up[i][0]+1)*t, outline=previup, width=8)#Prévisualisation des fantassins à transformer
    elif tourJoueur(grille,X,Y):
      can.bind("<Button-1>", affDep)
      for i in range(len(dep)):
        can.create_rectangle(t*dep[i][1],dep[i][0]*t,t*(dep[i][1]+1),(dep[i][0]+1)*t, outline=previ, width=8)#Prévisualisation des coups possibles

def affPion():
  """
      Cette fonction dessine les pions sur l'interface graphique
  """
  if tour%2==0:
    info.set("C'est au tour des blancs de joué")
  elif tour%2!=0:
    info.set("C'est au tour des noirs de joué")
  for x in range(len(grille)):
    for y in range(len(grille)):
      if grille[x][y][1:]==["F","1"]:
        can.create_image(t*((y+1/2)),t*((x+1/2)),image=pionB)
      elif grille[x][y][1:]==["F","2"]:
        can.create_image(t*((y+1/2)),t*((x+1/2)),image=pionN)
      if grille[x][y][1:]==["C","1"]:
        can.create_image(t*((y+1/2)),t*((x+1/2)),image=cavalierB)
      elif grille[x][y][1:]==["C","2"]:
        can.create_image(t*((y+1/2)),t*((x+1/2)),image=cavalierN)
  can.update()

def affGrille():
  """
      Cette fonction dessine le plateau de jeu sur l'interface graphique
  """
  for x in range(8):
    for y in range(8):
      if (x+y)%2==0:#Si la case est paire
        can.create_rectangle(t*x, t*y,t*(x+1),(y+1)*t, fill=case1)
      else:#Si la case est impaire
        can.create_rectangle(t*x, y*t,(x+1)*t,(y+1)*t, fill=case2)
        if y==0 or y==1 or y==6 or y==7:#2premieres et 2 dernieres lignes
          can.create_line(t*x, t*y,t*(x+1),(y+1)*t, fill="black",width=4)
          can.create_line(t*(x+1), t*y,t*x,(y+1)*t, fill="black",width=4)
        elif y==2 or y==5:#3eme et 6 eme lignes
          can.create_line(t*x,y*t+t/2,t*(x+1),y*t+t/2, fill="black",width=4)
          if x==1 or x==3 or x==6 or x==4:#2 eme 4 eme 7 eme et 5eme colonne
            can.create_line(t*(x+1), t*y,t*x,(y+1)*t, fill="black",width=4)
          elif x==5 or x==7 or x==0 or x==2:#6 eme 8 eme 1er et 3eme colonne
            can.create_line(t*x, t*y,t*(x+1),(y+1)*t, fill="black",width=4)
        elif y==3 or y==4:#4eme et 5 eme lignes
          can.create_line(t*x+t/2,t*y,t*x+t/2,t*(y+1), fill="black",width=4)
          if x==0 or x==2 or x==5 or x==7:#1er 3eme 6eme et 8eme colonne
            can.create_line(t*x, t*y,t*(x+1),(y+1)*t, fill="black",width=4)
          elif x==1 or x== 3 or x==4 or x==6:#2eme 4eme 5eme et 7eme colonne
            can.create_line(t*(x+1), t*y,t*x,(y+1)*t, fill="black",width=4)

def affSave():
  """
      Cette fonction affiche une fenetre qui permet de gérer une sauvegarde
  """
  global n
  fen=Toplevel(plateau)
  Label(fen,text="Numéro de la sauvegarde").pack()
  n=Entry(fen)
  n.pack()
  Button(fen,text="Sauvegarder",command=save).pack()
  Button(fen,text="Quitter",command=fen.destroy).pack()
  fen.mainloop()

def affLoad():
  """
      Cette fonction affiche une fenetre qui permet de gérer un chargement
  """
  global n
  fen=Toplevel(plateau)
  Label(fen,text="Numéro de la sauvegarde").pack()
  n=Entry(fen)
  n.pack()
  Button(fen,text="Charger",command=chargePartie).pack()
  Button(fen,text="Quitter",command=fen.destroy).pack()
  fen.mainloop()

def affJvJ():
  """
      Cette fonction permet de lancer une partie en joueur contre joueur
  """
  global intervalleChrono
  global grille
  global tour
  global gameMode
  gameMode=0
  intervalleChrono = 0
  affChrono.configure(text='')
  chrono()
  grille=creerGrille()
  tour=0
  affGrille()
  affPion()
  can.bind("<Button-1>", prevDep)

def affJvIA():
  """
      Cette fonction permet de lancer une partie en joueur contre IA
  """
  global intervalleChrono
  global grille
  global tour
  global gameMode
  gameMode=1
  intervalleChrono = 0
  affChrono.configure(text='')
  chrono()
  grille=creerGrille()
  tour=0
  affGrille()
  affPion()
  can.bind("<Button-1>", prevDep)

def affIAvIA():
  """
      Cette fonction permet de lancer une partie en IA contre IA
  """
  global intervalleChrono
  global grille
  global tour
  global gameMode
  gameMode=2
  intervalleChrono = 0
  affChrono.configure(text='')
  chrono()
  grille=creerGrille()
  tour=0
  while victoire(grille)==False:
    depIA()
    affPion()
    affGrille()
  
  


def affSurrend():
  """
      Cette fonction permet d'arrêter la partie sur une égalité
  """
  global intervalleChrono
  global gameMode
  intervalleChrono=2
  gameMode=0
  info.set("Egalité sur un accord commun")
  can.unbind("<Button-1>")

def affLight():
  """
      Cette fonction permet d'afficher le thême light
  """
  global case1
  global case2
  global previ
  global previup
  case1="medium turquoise"
  case2="lawn green"
  previ="darkcyan"
  previup="indigo"
  bJvJ=Button(plateau,text="Joueur VS Joueur",command=affJvJ,background=case1).grid(row=0,column=0)
  bJvIA=Button(plateau,text="Joueur VS IA",command=affJvIA,background=case2).grid(row=0,column=1)
  bIAvIA=Button(plateau,text="IA VS IA",command=affIAvIA,background=case1).grid(row=0,column=2)
  bSurr=Button(plateau,text="Surrender",command=affSurrend,background=case2).grid(row=3,column=2)
  affGrille()
  affPion()
def affDark():
  """
      Cette fonction permet d'afficher le thême dark
  """
  global case1
  global case2
  global previ
  global previup
  case1="gray64"
  case2="gray26"
  previ="black"
  previup="snow"
  bJvJ=Button(plateau,text="Joueur VS Joueur",command=affJvJ,background=case1).grid(row=0,column=0)
  bJvIA=Button(plateau,text="Joueur VS IA",command=affJvIA,background=case2).grid(row=0,column=1)
  bIAvIA=Button(plateau,text="IA VS IA",command=affIAvIA,background=case1).grid(row=0,column=2)
  bSurr=Button(plateau,text="Surrender",command=affSurrend,background=case2).grid(row=3,column=2)
  affGrille()
  affPion()
def affClass():
  """
      Cette fonction permet d'afficher le thême classique
  """
  global case1
  global case2
  global previ
  global previup
  case1="NavajoWhite2"
  case2="darkred"
  previ="goldenrod1"
  previup="red"
  bJvJ=Button(plateau,text="Joueur VS Joueur",command=affJvJ,background=case1).grid(row=0,column=0)
  bJvIA=Button(plateau,text="Joueur VS IA",command=affJvIA,background=case2).grid(row=0,column=1)
  bIAvIA=Button(plateau,text="IA VS IA",command=affIAvIA,background=case1).grid(row=0,column=2)
  bSurr=Button(plateau,text="Surrender",command=affSurrend,background=case2).grid(row=3,column=2)
  affGrille()
  affPion()

def affRules():
  """
      Cette fonction permet d'afficher les régles du jeu
  """
  fen=Toplevel(plateau)
  t=Text(fen)
  t.pack()
  t.insert(INSERT,"Le plateau de jeu comporte 64 cases (8 X 8).Les mouvements des pièces les plus mobiles, que l’on appelle « cavaliers » ou tout simplement « latroncules » variaient en fonction de leur situation sur le plateau.Ces possibilités de déplacement sont symbolisées sur notre jeu par de petits traits à l’intérieur des cases \n")
  t.insert(INSERT,"\nLes pions (calculi) : \n")
  t.insert(INSERT,"Les plus petits sont des fantassins, et les plus grands des cavaliers. Ils sont de deux couleurs distinctes. 8 fantassins blancs, 8 fantassins noirs, 8 cavaliers blancs, 8 cavaliers noirs.")
  t.insert(INSERT,"\nPréparation du jeu : \n")
  t.insert(INSERT,"Placer la tabula (le plateau de jeu) entre les deux joueurs de telle sorte que la case d’angle à la droite de chaque joueur soit blanche. Chaque joueur prend 8 fantassins et 8 cavaliers de même couleur et les dispose sur les deux premières lignes de jeu, les cavaliers sur les cases sombres et les fantassins sur les cases claires \n")
  t.insert(INSERT,"\nDéroulement de la partie :\n")
  t.insert(INSERT,"Les joueurs effectuent un seul coup à la fois, à tour de rôle. Le joueur qui a les pions blancs commence.")
  t.insert(INSERT,"\nDéplacement des pions : \n")
  t.insert(INSERT,"Les pions ne peuvent déplacés que vers une case vide. Une même case ne peut être occupée que par un pion à la fois.\n")
  t.insert(INSERT,"\n -Les cavaliers : \n")
  t.insert(INSERT,"*Un cavalier qui se trouve sur une case blanche peut aller dans n’importe laquelle des cases qui touchent la sienne par un côté ou par un angle \n")
  t.insert(INSERT,"*Un cavalier qui se trouve dans une case sombre ne peut se déplacer que dans les directions indiquées sur ces cases. Il doit impérativement respecter ces indications \n")
  t.insert(INSERT,"*le cavalier se déplace d’un case à la fois, sauf lorsqu’il saute par dessus un pion adverse. un cavalier peut sauter un pion adverse (cavalier ou fantassin) situé dans une case voisine de la sienne à condition qu’il y ait une case libre de l’autre côté de ce pion. Le cavalier ne peut pas sauter par dessus un pion de son propre camp, et il ne peut sauter qu’un pion adverse à la fois. Un pion sauté n’est pas capturé\n")
  t.insert(INSERT,"\n -Les fantassins : \n")
  t.insert(INSERT,"Ils ne se déplacent que d’une case à la fois, et uniquement dans la case située devant eux. Ils ne peuvent ni reculer, ni aller vers la droite, ni aller vers la gauche, ni avancer ou reculer en diagonale. Ils ne tiennent pas compte des marques tracées sur les cases sombres et ils ne peuvent pas sauter par dessus un pion adverse.\n")
  t.insert(INSERT,"\nPrise des pions : \n")
  t.insert(INSERT,"Un pion (cavalier ou fantassin) est capturé lorsqu’il se trouve entre deux pions adverses (deux cavaliers, deux fantassins ou un cavalier et un fantassin). Un pion capturé est retiré du jeu.Dans un angle, le pion est capturé en occupant les deux cases latérales.\n")
  t.config(state=DISABLED)
  fen.mainloop()

def aff_Chrono() :
  """
      Cette fonction permet d'afficher le chrono et de l'actualiser
  """
  global heureChrono
  global minuteChrono
  global secChrono
  dateheure=localtime()
  heure=dateheure[3]
  minute=dateheure[4]
  sec=dateheure[5]
  if heure >12 :
    heure=heure-12
  if intervalleChrono==1 :
    t1=(dateheure[3]*3600)+(dateheure[4]*60)+dateheure[5]
    tempsChrono=t1-t0
    heureChrono=int(tempsChrono/3600)
    minuteChrono=int((tempsChrono-(heureChrono*3600))/60)
    secChrono=tempsChrono-(heureChrono*3600)-(minuteChrono*60)
    affChrono.configure(text="%d" %heureChrono+".%02d"%minuteChrono+".%02d"%secChrono)
  can.after(1,aff_Chrono)

def chrono() :
  """
      Cette fonction permet d'initialiser le chrono
  """
  global intervalleChrono
  global t0
  if intervalleChrono==0 :
    intervalleChrono=1
    dateheure=localtime()
    t0=(dateheure[3]*3600)+(dateheure[4]*60)+dateheure[5]

plateau=Tk()
plateau.title("Latroncules")
tour=0
grille=[]
gameMode=0

intervalleChrono=0
t0=0
heureChrono=0
minuteChrono=0
secChrono=0
n=""

X=0
Y=0
t=100#Taille des cases

info=StringVar()
case1="NavajoWhite2"
case2="darkred"
previ="goldenrod1"
previup="red"

pionB=PhotoImage(file="pionB.png")
pionN=PhotoImage(file="pionN.png")
cavalierB=PhotoImage(file="cavalierB.png")
cavalierN=PhotoImage(file="cavalierN.png")
bJvJ=Button(plateau,text="Joueur VS Joueur",command=affJvJ,background=case1).grid(row=0,column=0)
bJvIA=Button(plateau,text="Joueur VS IA",command=affJvIA,background=case2).grid(row=0,column=1)
bIAvIA=Button(plateau,text="IA VS IA",command=affIAvIA,background=case1).grid(row=0,column=2)
can= Canvas(plateau,height=800,width=800)
can.grid(row=1,columnspan=3)
Label(plateau,textvariable=info).grid(row=2,column=1)
affChrono = Label(plateau,text="")
affChrono.grid(row=3,column=1)
bSurr=Button(plateau,text="Surrender",command=affSurrend,background=case2).grid(row=3,column=2)
aff_Chrono()
affGrille()
menubar = Menu(plateau)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Sauvegarder", command=affSave)
menu1.add_command(label="Charger", command=affLoad)
menu1.add_command(label="Quitter", command=plateau.destroy)
menubar.add_cascade(label="Jeu", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Light", command=affLight)
menu2.add_command(label="Dark", command=affDark)
menu2.add_command(label="Classique", command=affClass)
menubar.add_cascade(label="Themes", menu=menu2)

menubar.add_command(label="Regle du jeu", command=affRules)

plateau.config(menu=menubar)

plateau.mainloop()
