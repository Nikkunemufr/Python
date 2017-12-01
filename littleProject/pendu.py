#partie A
def ajout(l,motATrouver,motEnCours):
    newch=""
    for x in range(len(motATrouver)):
        if l==motATrouver[x]:#si la lettre appartient au mot a trouver alors on affiche la lettre a sa place 
            newch+=l
        elif motEnCours[x]==motATrouver[x]:#si la lettre du mot en cours appartient au mot a trouver on remet la lettres
            newch+=motEnCours[x]
        else:#sinon ( c-a-d si la lettre n'appartient pas au mot a trouver on affiche "_"
            newch+="_"
    return newch


#partie B
from random import randrange
mots = ("Bulbizarre", "Herbizarre", "Florizarre", "Salamèche", "Reptincel", "Dracaufeu", "Carapuce", "Carabaffe", "Tortank", "Chenipan", "Chrysacier", "Papilusion", "Aspicot", "Coconfort", "Dardargnan", "Roucool", "Roucoups", "Roucarnage", "Rattata", "Rattatac", "Piafabec", "Rapasdepic", "Abo", "Arbok", "Pikachu", "Raichu", "Sabelette", "Sablaireau", "Nidoran", "Nidorina", "Nidoqueen", "Nidoran", "Nidorino", "Nidoking", "Mélofée", "Mélodelfe", "Goupix", "Feunnard", "Rondoudou", "Grodoudou", "Nosferapti", "Nosferalto", "Mystherbe", "Ortide", "Rafflesia", "Paras", "Parasect", "Mimitoss", "Aéromite", "Taupiqueur", "Triopikeur", "Miaouss", "Persian", "Psykokwak","Akwakwak", "Férosinge", "Colossinge", "Caninos", "Arcanin", "Ptitard", "Tétarte", "Tartard","Abra", "Kadabra", "Alakazam", "Machoc", "Machopeur", "Mackogneur", "Chétiflor", "Boustiflor", "Empiflor", "Tentacool", "Tentacruel", "Racaillou", "Gravalanch", "Grolem", "Ponyta" ," Galopa", "Ramoloss", "Flagadoss", "Magneti" , "Magneton", "Canarticho", "Doduo", "Dodrio", "Otaria", "Lamantine", "Tadmorv", "Grotadmorv", "Kokiyas", "Crustabri", "Fantominus", "Spectrum", "Ectoplasma", "Onix", "Soporifik", "Hypnomade", "Krabby", "Krabboss", "Voltorbe", "Electrode", "Noeunoeuf", "Noadkoko", "Osselait", "Ossatueur", "Kicklee", "Tygnon", "Excelangue", "Smogo", "Smogogo","Rhinocorne", "Rhinoféros", "Leveinard", "Saquedeneu", "Kangourex", "Hypotrempe", "Hypocéan", "Poissirène", "Poissoroy", "Stari", "Staross", "M. Mime", "Insécateur", "Lippoutou", "Elektek","Magmar", "Scarabrute", "Tauros", "Magicarpe", "Léviator", "Lokhlass", "Métamorph", "Evoli", "Aquali", "Voltali", "Pyroli", "Porygon", "Amonita", "Amonistar", "Kabuto", "Kabutops", "Ptéra", "Ronflex", "Artikodin", "Electhor", "Sulfura", "Minidraco", "Draco", "Dracolosse", "Mewtwo", "Mew")
maxErreurs = 9

def lire_lettre(propositions):

    while True:
        lettre = input("Entrez une lettre : ")
        lettre=lettre.upper()

        if lettre in propositions:
            print("T'as deja dit cette lettre abrutie")
        else:
            break;

    propositions.append(lettre)
    return lettre

def mot_avec_tirets(mot, propositions):
    m = " "
    for lettre in mot:
        if lettre in propositions:
            m = m + lettre
        else:
            m = m + "_ "
    return m

def partie():
    erreurs = 0
    mot = mots[randrange(len(mots))]
    mot = mot.upper()
    propositions = []
    
    print("erreurs : ", erreurs)

    while True:
        print("Lettres déjà proposées :", propositions)
        print("Réponse actuelle :", mot_avec_tirets(mot, propositions))

        lettre = lire_lettre(propositions)

        if lettre in mot:
            if mot_avec_tirets(mot, propositions) == mot:
                print("Bravo, tu as gagné. Le mot était : ", mot)
                print("Nombre d'erreurs :", erreurs)
                return True
        else:
            erreurs = erreurs + 1
            print("erreurs : ", erreurs)
            if erreurs >= maxErreurs:
                print("Tu es pendu, le mot était :", mot)
                return False

parties = 0
victoires = 0


while True:
    parties = parties + 1
    if partie():
        victoires = victoires + 1

    while True:
        jeu = input("start pour jouer, stop pour arrêter : ")
        if jeu == "start" or jeu == "stop":
            break;

    if jeu == "stop":
        break;
if partie>1:
    print("Vous avez joué", parties, "partie")
else:
    print("Vous avez joué", parties, "parties")
    
print("Vous en avez gagné", victoires)
