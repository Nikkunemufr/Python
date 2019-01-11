#####################################################################
#               TP Sécurité et Aide à la décision                   #
#                                                                   #
#                   Cryptographie : 10 avril 2018                   #
#                                                                   #
#           ---------------------------------------------           #
#                                                                   #
#                           Exercice 1                              #
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
#   1) fonction chiffreCesar(s, k)                                  #
#                                                                   #
#####                                                           #####

def chiffreCesar(s, k):
    res = ""
    for ch in s:
        res += chr(ord("a") + (ord(ch) - ord("a") + k) % 26)
    return res

print("1)")
print("Message transmit :")
print()
print("abcdefghijklmnopqrstuvwxyz")
print()

m = "abcdefghijklmnopqrstuvwxyz"
cesar = 4
mChiffre = chiffreCesar(m, cesar)

print("Cesar : ", cesar)
print("Message chiffré : " , mChiffre)
print()

#####                                                           #####
#                                                                   #
#   2) fonction dechiffreCesar(s, k)                                #
#                                                                   #
#####                                                           #####

def dechiffreCesar(c, k):
    return chiffreCesar(c, -k)

mDechiffre = dechiffreCesar(mChiffre, 4)

print("2)")
print()
print("Message déchiffré : ", mDechiffre)
print()

#####                                                           #####
#                                                                   #
#   3) test chiffrement et déchiffrement                            #
#                                                                   #
#####                                                           #####

print("3)")
print()
print("Est ce que le message est bien déchiffré ?", mDechiffre == m)
print()

#####                                                           #####
#                                                                   #
#   4) fonction CalculOccurencesLettres(c)                          #
#                                                                   #
#####                                                           #####

def calculOccurencesLettres(c):
    nbOccur = [0]*26
    i = 0
    
    while i < len(c):
        nbOccur[int(ord(c[i]) - 97)] = (nbOccur[int(ord(c[i]) - 97)] + 1)
        i += 1
    
    return nbOccur

#
#   BONUS : Favorise la compréhension de l'affichage de la fonction
#   calculOccurencesLettres
#

def printListeOccurences(liste):
    l = [0]*26
    
    for i in range(26):
        print(chr(i + 97), liste[i])


m = "abbcccdefghijklmnopqrstttttuvwxyz"

print("4)")
print()
print("Version demandé :")
print()
print(calculOccurencesLettres(m))
print()
print("Version amélioré :")
print()
printListeOccurences(calculOccurencesLettres(m))
print()

#####                                                           #####
#                                                                   #
#   5) fonction CalculOccurencesBigrammes(c)                        #
#                                                                   #
#####                                                           #####

def calculOccurencesBigrammes(c):
    res = {}
    for ch in range(len(c) - 1):
        successors = c[ch] + c[ch + 1]
        if successors in res:
            res[successors] += 1
        else:
            res[successors] = 1
    return res

m = "bonjourlemessageestbon"

print("5)")
print()
print("Message : ", m)
print()
print(calculOccurencesBigrammes(m))
print()

#####                                                           #####
#                                                                   #
#   6) fonction decode(c)                                           #
#                                                                   #
#####                                                           #####

def decode(c):
    alphabet = ""
    for x in range(26):
        alphabet += chr(ord("a") + x)

    res = calculOccurencesLettres(c)
    indiceMax =alphabet[res.index(max(res))]
    clef = ord(indiceMax) - ord("e")
    return clef

mADechiffre = "qtslyjruxojrjxznxhtzhmjijgtssjmjzwjufwktnxfujnsjrfgtzlnjjyjnsyjrjxdjzcxjkjwrfnjsyxnanyjvzjojsfafnxufxqjyjruxijrjinwjojrjstwxjyzsjijrnmjzwjfuwjxqfujsxjjvznqjyfnyyjruxijhmjwhmjwqjxtrrjnqrjajnqqfnyojatzqfnxutxjwqjatqzrjvzjojhwtdfnxfatnwifsxqjxrfnsxjyxtzkkqjwrfqzrnjwj"

clef = decode(mADechiffre)

print("6)")
print()
print("Message décodé :")
print(dechiffreCesar(mADechiffre, clef))
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
print("Partie 1/2")
print()