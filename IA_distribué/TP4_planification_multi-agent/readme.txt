Une grille est déjà généré pour que le programme puisse être lancer tel quel.
Pour initialiser une grille il faut le faire de cette façon :

game = alea_grid(taille de la grille, nombre d'obstacle, nombre de robot)
par défault le nombre de robot est fixé à 1

La variable game retournera donc un dictionnaire. L'element grid, corrrespond à la grille de jeu.
l'element length a la taille de la grille.
l'element robot aux positions des robots
l'element target aux positions des cibles

Pour initialiser planification_mixte qui retournera un plan de résolution:
plan = planification_mixte(grille de jeu, plan mixte-> liste d'etat associé à un coup -> (coordonnée de la case, action), plan vide->[])

Pour initialiser planification_jointe qui retournera un plan de résolution :
plan = planification_jointe(grille de jeu, plan vide-> [])