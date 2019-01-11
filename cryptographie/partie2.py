#####################################################################
#               TP Sécurité et Aide à la décision                   #
#                                                                   #
#                   Cryptographie : 10 avril 2018                   #
#                                                                   #
#           ---------------------------------------------           #
#                                                                   #
#                           Exercice 2                              #
#                                                                   #
#                                   DE MENEZES VINCENT 21601489     #
#                                   MORTELIER ALEXIS 21605783       #
#                                                                   #
#                                   Licence 2   :   informatique    #
#                                       Groupe  :   2.B             #
#                                                                   #
#####################################################################

#####                                                           #####
#                                                                   #
#   1) Calculer la suite du LFSR suivant                            #
#                                                                   #
#   clé         : k = k9 k8 ... k0 = 1001001001                     #
#   polynome    : X10 + X9 + X7 + X6 + X3 + 1                       #
#                                                                   #
#####                                                           #####

polynome = "1011001001"
cle = "1001001001"

print("1)")
print("a)")
print()
print("Polynome : ", polynome)
print("Clé      : ", cle)
print()
print("Suite produite par le LFSR :")
print()
print("Cycle : 1")
print()
print("     ", polynome)
print("AND")
print("     ", cle)
print("-----------------")
print("      1001001001")
print()
print("1 XOR 0 XOR 0 XOR 1 XOR 0 XOR 0 XOR 1 XOR 0 XOR 0 XOR 1 = 0")
print()
print("chiffre entrant : 0")
print()
print("chiffre sortant : 1")
print()
print("Cycle : 2")
cle = "0100100100"
print()
print("     ", polynome)
print("AND")
print("     ", cle)
print("-----------------")
print("      0000000000")
print()
print("0 XOR 0 XOR 0 XOR 0 XOR 0 XOR 0 XOR 0 XOR 0 XOR 0 XOR 0 = 0")
print()
print("chiffre entrant : 0")
print()
print("chiffre sortant : 0")
print()
print("Cycle : 3")
cle = "0010010010"
print()
print("     ", polynome)
print("AND")
print("     ", cle)
print("-----------------")
print("      0010000000")
print()
print("0 XOR 0 XOR 1 XOR 0 XOR 0 XOR 0 XOR 0 XOR 0 XOR 0 XOR 0 = 1")
print()
print("chiffre entrant : 1")
print()
print("chiffre sortant : 0")
print()
cle = "1001001001"
print("Clé      : ", cle)
print()
print("On remarque qu'en 3 cycles on obtient la clé de départ")
print()

#####                                                           #####
#                                                                   #
#   2) Calculer la suite du LFSR suivant                            #
#                                                                   #
#   clé         : k = 001						                    #
#   polynome    : X3 + 1	                       					#
#                                                                   #
#####                                                           #####

polynome = "001"
cle = "001"

print("b)")
print()
print("Polynome : ", polynome)
print("Clé      : ", cle)
print()
print("Suite produite par le LFSR :")
print()
print("Cycle : 1")
print()
print("     ", polynome)
print("AND")
print("     ", cle)
print("----------")
print("      001")
print()
print("0 XOR 0 XOR 1 = 1")
print()
print("chiffre entrant : 1")
print()
print("chiffre sortant : 1")
print()
print("Cycle : 2")
cle = "100"
print()
print("     ", polynome)
print("AND")
print("     ", cle)
print("----------")
print("      000")
print()
print("0 XOR 0 XOR 0 = 0")
print()
print("chiffre entrant : 0")
print()
print("chiffre sortant : 0")
print()
print("Cycle : 3")
cle = "010"
print()
print("     ", polynome)
print("AND")
print("     ", cle)
print("----------")
print("      000")
print()
print("0 XOR 0 XOR 0 = 0")
print()
print("chiffre entrant : 0")
print()
print("chiffre sortant : 0")
print()
cle = "001"
print("Clé      : ", cle)
print()

#####                                                           #####
#                                                                   #
#   1) Ecrire une procédure de chiffrement                         	#
#                                                                   #
#####                                                           #####

#
#   BONUS : Convertis l'alphabet en binaire
#

def alphaToBin(message):
    tbl = []

    for e in message:
        nbr = ord(e) - ord("a") + 1
        for c in [4,3,2,1,0]:
            tbl.append(nbr // 2**c)
            nbr = nbr % 2**c
    
    return tbl

#
#   BONUS : Convertis un message binaire en lettre
#

def binToAlpha(message):
    string = ""

    if len(message) % 5 == 0 and len(message) > 0:
        limite = len(message) // 5
        tbl = [0] * limite
        
        for i in range(5):
            nbr = 0
            for j in range(limite):
                c = 4 - i
                nbr = tbl[j] + (message[i + j * 5] * 2**c)
                tbl[j] = nbr
        
        tbl = [chr(c + ord("a") - 1)  for c in tbl]
        return tbl
    else:
        return "Erreur de longueur vérfiez la taille de votre message binaire"

def getkey(a, k, n):
    s = []

    for index in range(n):
        counter = 0
        taille = len(k) - 1
        
        for i in range(len(a)):    
            if a[i] == 1 and k[i] == 1:
                counter += 1
        
        if counter % 2 == 1:
            k.insert(0, 1)
        else:
            k.insert(0, 0)

    k.reverse()
    return k

def chiffrement(a, k, m):
    c = []

    if len(k) < len(m):
        s = getkey(a, k, len(m)-len(k))
    
    for i in range(len(m)):
        c.append((m[i] + s[i]) % 2)

    return c
    
#####                                                           #####
#                                                                   #
#   2) Ecrire une procédure de dechiffrement                        #
#                                                                   #
#####                                                           #####

def dechiffrement(a, k, c):
    m = []

    if len(k) < len(c):
        s = getkey(a, k, len(c) - len(k))
    
    for i in range(len(c)):
        m.append((c[i] + s[i]) % 2)

    return m

m = alphaToBin("ax")
c = chiffrement([0,0,1,1], [1,1,0,1], m)
r = binToAlpha(dechiffrement([0,0,1,1], [1,1,0,1], c))
print("2) Test des fonctions chiffrement et déchiffrement avec le message ax")
print("a)")
print()
print("Message d'origine : ax")
print("Message convertit en binaire : ", m)
print("Message crypté : ", c)
print()
print("b)")
print()
print("Message trouvé : ",r)
print("Est ce que les fonctions chiffrement et déchiffrement sont correcte ?", binToAlpha(m) == r)
print()

print("3)")
print("a)")
print()
print("Le message est composé de 3 lettres car la longueur du message est de 15 chiffres binaire et une lettre est de longueur 5.")
print()
polynome = "0011"
cle = "1101"

print("b)")
print()
print("Polynome : ", polynome)
print("Clé      : ", cle)
print()
print("Pour des raisons de lisibilité, nous allons juste afficher le résultat de la suite à chaque cycle :")
print()
print("la valeur de clé est à chaque cycle : ")
print("1- 1011 valeur entrant : 0")
print("2- 0101 valeur entrant : 1")
print("3- 1010 valeur entrant : 1")
print("4- 1101 valeur entrant : 1")
print("5- 1110 valeur entrant : 1")
print("6- 1111 valeur entrant : 0")
print("7- 0111 valeur entrant : 0")
print("8- 0011 valeur entrant : 0")
print("9- 0001 valeur entrant : 1")
print("10- 1000 valeur entrant : 0")
print("11- 0100 valeur entrant : 0")
print("12- 0010 valeur entrant : 1")
print("13- 1001 valeur entrant : 1")
print("14- 1100 valeur entrant : 0")
print("15- 0110 valeur entrant : 1")
print("16- 1011")
print()

print("3)")
print()
c = [0,0,0,0,0,1,1,1,1,0,0,1,0,0,0]
print("Déduire le message :", c)
print()
m = binToAlpha(dechiffrement([0,0,1,1], [1,1,0,1], c))
print("Le message déchiffré est : ", m)
print()

#####                                                           #####
#                                                                   #
#                       INFORMATION SUR LE DEVOIR                   #
#                                                                   #
#####                                                           #####

print("Devoir réalisé par :")
print()
print("DE MENEZES VINCENT 21601489")
print()
print("MORTELIER ALEXIS 21605783")
print()
print("Partie 2/2")
print()