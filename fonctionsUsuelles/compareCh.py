"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
def compare (chaine1,chaine2):
    """
		Compare deux cha�nes de caract�res minuscules non accentu�s et
		retourne -1, 0 ou +1 selon que
		la premiére est inférieure, égale ou supérieure à la seconde dans l'ordre
		alphabétique.
	"""
    for i in range(0,min(len(chaine1),len(chaine2))):
        if chaine1[i]<chaine2[i]:
            return -1
        elif chaine1[i]>chaine2[i]:
            return +1
    return 0