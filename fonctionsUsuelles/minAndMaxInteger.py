"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
def plusPetitEntier (l):
    """
		Retourne le plus petit entier d'une liste d'entiers.
		Jette une exception si la liste est vide.
	"""
    minCourant=l[0]
    for x in l[1:]:
        if x<minCourant:
            minCourant=x
    return minCourant

def plusGrandEntier (l):
    """
		Retourne l'élément maximal d'une liste d'entiers non vide.
		Jette une exception si la liste est vide.
	"""
    if len(l)==0:
        raise Exception("Impossible de calculer le maximum d'une liste vide")
    maxCourant=0
    for x in l:
        if x>maxCourant:
            maxCourant=x
    return maxCourant