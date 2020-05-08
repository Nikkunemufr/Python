Un arbre est déjà prechargé pour que le programme puisse être lancer tel quel.
Pour initialiser un arbre il faut l'architecturer de cette façon:

arbre = {
	Noeud:[Pere,[fils1,fils2,fils3,...., filsn]],
	....
	}
Si le noeud n'a pas de pere car c'est la racine, Pere = None

Pour lancer minmax il faut l'appeler de telle façon :
minmax (profondeur de l'arbre, arbre, noeud racine, Maximiser=True, Minimiser=False)

Pour lancer alphabeta il faut l'appeler de telle façon :
alphabeta(profondeur de l'arbre, arbre, noeud racine, Maximiser=True, Minimiser=False)

Les deux fonctions retournerons un tuple, l'element 0 du tuple corrrespond au meilleur score, l'element 1 au meilleur move.